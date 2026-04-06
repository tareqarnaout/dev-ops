---
layout: page
title: "3.1.3 Docker Compose"
description: Automating Multi-Container Setups with Docker Compose.
permalink: /docker-compose/
parent: "3.1 First Project: How to Deal with Images"
nav_order: 3
---

# Step-by-Step Guide: Automating Multi-Container Setups with Docker Compose

This guide extracts the workflow from the 1:29:00 to 1:42:00 timestamp of the tutorial. It demonstrates how to transition from tedious, manual `docker run` commands to an automated, structured deployment using Docker Compose.

## Phase 1: Understanding Docker Compose

Running multiple containers individually via the command line requires managing long strings of configuration flags, networks, and environment variables. 

Docker Compose solves this by mapping those command-line arguments into a structured YAML file. 

**Key Benefits Shown in the Video:**
* **Centralized Configuration:** All services (MongoDB and Mongo Express) are defined in one file.
* **Automated Networking:** Docker Compose automatically creates a shared network for the services defined in the file. You no longer need to manually execute `docker network create`.

## Phase 2: Creating the YAML File

Create a file to hold your configuration. In the tutorial, this file is named **`mongo.yaml`**. 

Populate it with the following structure, which directly translates the previous `docker run` commands into YAML syntax:

```yaml
version: '3'
services:
  mongodb:
    image: mongo
    ports:
      - 27017:27017
    environment:
      - MONGO_INITDB_ROOT_USERNAME=admin
      - MONGO_INITDB_ROOT_PASSWORD=password

  mongo-express:
    image: mongo-express
    ports:
      - 8080:8081
    environment:
      - ME_CONFIG_MONGODB_ADMINUSERNAME=admin
      - ME_CONFIG_MONGODB_ADMINPASSWORD=password
      - ME_CONFIG_MONGODB_SERVER=mongodb
```

**Configuration Breakdown:**
* **`version: '3'`**: Specifies the version of the Docker Compose file format.
* **`services:`**: The root level for defining the containers you want to run.
* **`image:`**: Replaces the standard image name argument from the CLI.
* **`ports:`**: Replaces the `-p` flag (HostPort:ContainerPort). Note that Mongo Express is mapped to port 8080 on the host and 8081 inside the container.
* **`environment:`**: Replaces the multiple `-e` flags used for credentials and configuration.

## Phase 3: Starting the Containers

Once the `mongo.yaml` file is saved, you can bring up the entire environment with a single command.

1. **Open Terminal**: Navigate to the directory where you saved `mongo.yaml`.
2. **Execute the Up Command**: 
   ```bash
   docker-compose -f mongo.yaml up
   ```

**What Happens Next:**
* Docker Compose automatically creates a default network (e.g., `directoryname_default`).
* It starts both the `mongodb` and `mongo-express` containers and attaches them to this network.
* The logs for both containers will stream together in your terminal, allowing you to see when MongoDB is ready to accept connections and when Mongo Express successfully connects to it.

*(Note: If you name your file `docker-compose.yml`, which is the standard convention, you can omit the `-f mongo.yaml` flag and simply run `docker-compose up`.)*

## Phase 4: Stopping and Cleaning Up

When you are done testing, Docker Compose makes it equally easy to tear down the environment.

1. **Execute the Down Command**:
   Open a new terminal window in the same directory (or stop the current process) and run:
   ```bash
   docker-compose -f mongo.yaml down
   ```

**What Happens Next:**
* Docker Compose gracefully stops all running containers defined in the file.
* It automatically removes the containers.
* It deletes the default network it created. 
* **Important Note from the Video:** Restarting containers this way results in data loss for the database. Data persistence requires Docker Volumes, which is covered in a later section of the tutorial.

## Phase 5: Networks

![Docker network drivers overview](/assets/images/docker_network_diagram.svg)

## Docker Networking

Docker networking allows containers to communicate with each other, the host, and the outside world.

---

### Network Drivers (Types)

#### 1. `bridge` (default)
- Default network for containers on a single host
- Containers get their own IP and can talk to each other by IP or name
- Isolated from the host network

```bash
docker run --network bridge nginx
```

#### 2. `host`
- Container shares the host's network stack directly
- No network isolation - container uses host IP/ports
- Best performance, but risky

```bash
docker run --network host nginx
```

#### 3. `none`
- No networking at all
- Fully isolated container

```bash
docker run --network none nginx
```

#### 4. `overlay`
- Spans multiple Docker hosts (used with **Docker Swarm**)
- Allows containers on different machines to talk to each other

#### 5. `macvlan`
- Assigns a real MAC address to the container
- Container appears as a physical device on the network
- Used for legacy apps that need direct LAN access

---

### How Containers Communicate

```
 [Container A] --┐
                 ├--> [bridge network] --> [Internet]
 [Container B] --┘
```

On a **custom bridge network**, containers can reach each other by **container name** (DNS resolution built-in):

```bash
# Create custom network
docker network create mynet

# Run containers on it
docker run --network mynet --name db postgres
docker run --network mynet --name app myapp

# Inside "app", you can reach "db" by name:
ping db
```

> On the **default** bridge network, name-based DNS does **not** work - you must use IPs.

---

### Key Commands

```bash
# List networks
docker network ls

# Inspect a network
docker network inspect mynet

# Create a network
docker network create mynet

# Connect a running container to a network
docker network connect mynet mycontainer

# Disconnect
docker network disconnect mynet mycontainer
```

---

### Real-world Example (docker-compose)

```yaml
services:
  app:
    image: myapp
    networks:
      - backend

  db:
    image: postgres
    networks:
      - backend

networks:
  backend:
    driver: bridge
```

Here, `app` can reach `db` just by using the hostname `db` - Docker handles the DNS automatically.

---

### Summary Table

| Driver | Scope | Use Case |
|---|---|---|
| `bridge` | Single host | Default, isolated containers |
| `host` | Single host | Max performance, no isolation |
| `none` | Single host | Fully isolated |
| `overlay` | Multi-host | Docker Swarm / clustering |
| `macvlan` | Single host | Legacy apps needing LAN access |

The most common setup you'll use day-to-day is a **custom bridge network** with docker-compose, where services discover each other by name automatically.
