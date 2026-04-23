---
layout: page
title: "4.2 The Resilient Blog (WordPress + MySQL)"
description: Deploy WordPress with MySQL using Docker volumes for persistence and test recovery.
permalink: /second-project/
parent: "8. Projects"
nav_order: 2
---

# Project Guide: The Resilient Blog (WordPress + MySQL)

## The Objective
To master Docker Volumes and container networking. By default, everything created inside a container is temporary; its writable layer is ephemeral. If a container crashes or is deleted, the internal filesystem is wiped clean, and data is lost forever. To run stateful applications like a database, data must be anchored safely outside the container's lifecycle. 

In this project, you will deploy a WordPress blog connected to a MySQL database and test your volume configuration by "destroying" the database container without losing your blog posts.

---

## Step-by-Step Implementation

### Step 1: Create an Isolated Network
Containers are completely isolated by default. For WordPress to securely communicate with MySQL behind the scenes, we need to create a dedicated Docker bridge network.

    docker network create blog-network


### Step 2: Create a Docker Volume
Instead of a Bind Mount (which relies on your host machine's directory structure), we will use a Docker Volume. Volumes are fully managed by the Docker CLI/API and are the best practice for databases.

    docker volume create db-data


### Step 3: Boot the MySQL Database
We will use the `docker container run` command to boot a new instance of the official MySQL image. We'll use modifier flags to attach our network, mount our volume, and inject necessary configuration settings.

    docker container run -d \
      --name mysql-db \
      --network blog-network \
      -v db-data:/var/lib/mysql \
      -e MYSQL_ROOT_PASSWORD=secret \
      -e MYSQL_DATABASE=wordpress \
      mysql:latest

What is happening here?
* -d: Runs the container in "detached mode" in the background.
* --name: Assigns a human-readable name (mysql-db) instead of a random hash.
* --network: Connects this container to the blog-network we created.
* -v db-data:/var/lib/mysql: The persistence matrix. This maps our persistent Docker Volume (db-data) to the exact path where MySQL stores its data inside the container (/var/lib/mysql).
* -e: Injects environment variables into the live container to configure the database credentials.


### Step 4: Boot the WordPress App
Next, we spin up the WordPress container. It needs to be on the same network, and we must configure port mapping to expose the internal traffic to your host machine.

    docker container run -d \
      --name my-wp \
      --network blog-network \
      -p 8080:80 \
      -e WORDPRESS_DB_HOST=mysql-db \
      -e WORDPRESS_DB_USER=root \
      -e WORDPRESS_DB_PASSWORD=secret \
      -e WORDPRESS_DB_NAME=wordpress \
      wordpress:latest

What is happening here?
* -p 8080:80: Port mapping. This bridges the internal network boundary, mapping your Host's Port 8080 to the Container's internal Port 80.
* WORDPRESS_DB_HOST=mysql-db: Notice how we use the container name of the database as the host address. Docker's internal DNS automatically resolves container names on the same network.

---

## The Midterm Test

### 1. Generate the Data
1. Open your web browser and navigate to http://localhost:8080.
2. Follow the quick 1-minute WordPress setup.
3. Create a new blog post titled "Hello, DevOps!" and publish it.

### 2. Simulate a Disaster
You are now going to intentionally destroy your active database container. You cannot remove a running container unless you use the -f (force) flag. Always stop it first, or force it.

    docker container rm -f mysql-db

If you refresh your WordPress site now, you will see an "Error establishing a database connection." Your database is gone!

### 3. The Recovery
Because we mapped our database container to a Docker Volume (db-data), our data is safely anchored outside the deleted container's lifecycle. Re-run the exact same MySQL command from Step 3 to boot a fresh container attached to the same volume:

    docker container run -d \
      --name mysql-db \
      --network blog-network \
      -v db-data:/var/lib/mysql \
      -e MYSQL_ROOT_PASSWORD=secret \
      -e MYSQL_DATABASE=wordpress \
      mysql:latest


### 4. Verify the Persistence
Refresh your browser at http://localhost:8080. Your WordPress site will be back online, and your "Hello, DevOps!" post will still be there. You have successfully bypassed the ephemeral storage trap!

---

## Cleanup Procedures
To keep your host system clean, remove the resources when you are finished. 

    # Force-remove both containers
    docker container rm -f my-wp mysql-db

    # Remove the isolated network
    docker network rm blog-network

    # Remove the persistent volume (This wipes your data permanently!)
    docker volume rm db-data