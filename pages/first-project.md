---
layout: page
title: 3. First Project: How to Deal with Images
description: Run a local Node.js app with MongoDB and Mongo Express using Docker images and networking.
permalink: /first-project/
has_children: true
nav_order: 3
---

# First Project: How to Deal with Images

This guide follows the workflow from the tutorial segment (1:10:00 to 1:29:00). It shows how to run a local JavaScript/Node.js app and connect it to MongoDB and Mongo Express containers on a shared Docker network.

## Phase 1: Pull Required Images

Pull the official images from Docker Hub:

```bash
docker pull mongo
docker pull mongo-express
```

## Phase 2: Create a Docker Network

Create a network so containers can communicate using container names.

```bash
docker network create mongo-network
```

Optional verification:

```bash
docker network ls
```

## Phase 3: Start MongoDB Container

Run MongoDB, attach it to the network, and configure root credentials.

```bash
docker run -d \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=password \
  --name mongodb \
  --net mongo-network \
  mongo
```

Meaning of main flags:

- `-d`: Run in background (detached mode).
- `-p 27017:27017`: Expose MongoDB on local port 27017.
- `-e`: Set environment variables for credentials.
- `--name mongodb`: Assign a container name.
- `--net mongo-network`: Connect the container to the custom network.

## Phase 4: Start Mongo Express Container

Run Mongo Express and connect it to MongoDB by container name.

```bash
docker run -d \
  -p 8081:8081 \
  -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
  -e ME_CONFIG_MONGODB_ADMINPASSWORD=password \
  -e ME_CONFIG_MONGODB_SERVER=mongodb \
  --name mongo-express \
  --net mongo-network \
  mongo-express
```

Important part:

- `ME_CONFIG_MONGODB_SERVER=mongodb` uses the MongoDB container name on the same network.

## Phase 5: Configure Database in UI

1. Open `http://localhost:8081`.
2. Create database: `user-account`.
3. Create collection inside it: `users`.

## Phase 6: Connect Local Node.js App

Because your Node.js app runs on your host machine (outside Docker network), use `localhost`.

```javascript
const url = "mongodb://admin:password@localhost:27017";
const dbName = "user-account";
const collectionName = "users";
```

After this configuration, start your Node.js app and it will connect to MongoDB running in Docker.

## Quick Check Commands

```bash
docker ps
docker logs mongodb
docker logs mongo-express
```
