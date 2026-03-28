# Step-by-Step Guide: Running a Local App with MongoDB & Mongo Express Containers

This guide extracts the exact workflow from the 1:10:00 to 1:29:00 timestamp of the tutorial. It demonstrates how to run a local JavaScript/Node.js application and connect it to MongoDB and Mongo Express UI containers running on a shared Docker network.

## Phase 1: Pulling Required Images

First, pull the necessary official images from Docker Hub to your local machine.

1. **Pull MongoDB**:
   ```bash
   docker pull mongo
   ```

2. **Pull Mongo Express** (Web-based MongoDB admin interface):
   ```bash
   docker pull mongo-express
   ```

## Phase 2: Creating a Docker Network

Containers need to communicate with each other. By placing them on the same Docker network, they can resolve each other using their container names rather than IP addresses.

**Create the Network**:
```bash
docker network create mongo-network
```
*(You can verify creation by running `docker network ls`)*

## Phase 3: Starting the MongoDB Container

Run the MongoDB container, attach it to the network, and set up the root authentication credentials using environment variables.

**Run Command**:
```bash
docker run -d \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=password \
  --name mongodb \
  --net mongo-network \
  mongo
```

**Breakdown of Flags**:
* `-d`: Runs the container in detached mode (in the background).
* `-p 27017:27017`: Maps the host machine port to the container port.
* `-e`: Sets environment variables for the root username and password.
* `--name mongodb`: Assigns a specific name to the container.
* `--net mongo-network`: Attaches the container to the network created in Phase 2.

## Phase 4: Starting the Mongo Express Container

Run the Mongo Express UI. It needs to connect to the MongoDB container, which is possible because they share the same network.

**Run Command**:
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

**Breakdown of Specific Flags**:
* `-e ME_CONFIG_MONGODB_SERVER=mongodb`: Tells Mongo Express to connect to the database container using its exact name (`mongodb`). This works exclusively because they are on the same `mongo-network`.
* `-p 8081:8081`: Exposes the Mongo Express UI on port 8081.

## Phase 5: Database Configuration via UI

With both containers running, use the UI to prep the database for the application.

1. **Access the UI**: Open your web browser and navigate to `http://localhost:8081`.
2. **Create Database**: Create a new database named **`user-account`**.
3. **Create Collection**: Inside the `user-account` database, create a new collection named **`users`**.

## Phase 6: Connecting the Local Node.js Application

The final step is updating your local Node.js backend code to communicate with the running MongoDB container.

1. **Set Connection String**: Because your Node.js app runs directly on your local machine (outside of the Docker network), it must connect via `localhost`.
2. **Implement in Code**: Update your MongoDB connection logic (e.g., using `MongoClient`) to point to the local port and include the credentials you configured.

**Connection URI Example**:
```javascript
const url = "mongodb://admin:password@localhost:27017";
// Database Name
const dbName = "user-account";
// Collection Name
const collectionName = "users";
```

Once configured, starting your local Node.js application will successfully route data into your isolated MongoDB Docker container.