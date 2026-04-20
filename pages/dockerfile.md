---
layout: page
title: Dockerfile Creation Guide
nav_order: 4
---

# 🐳 Dockerfile Creation Guide

A **Dockerfile** is a sequential text document containing all the commands needed to assemble a Docker image. It acts as an automated blueprint for setting up the environment, installing dependencies, and configuring how an application should run.

## 🛠️ Basic Dockerfile Commands

Before diving into a complete example, here are the core instructions used to construct a Docker image:

| Instruction | Purpose | Description |
| :--- | :--- | :--- |
| **`FROM`** | **Base Image** | Initializes a new build stage and sets the foundational operating system or runtime environment. It must be the first valid instruction. |
| **`WORKDIR`** | **Working Directory** | Sets the default directory inside the container. Any subsequent `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, and `ADD` instructions will be executed here. |
| **`COPY`** | **File Transfer** | Copies files or directories from the host machine's build context into the container's filesystem. |
| **`RUN`** | **Execute Command** | Executes shell commands inside the container *during the build process*. Commonly used to install software packages or create directories. |
| **`USER`** | **Set User** | Sets the user name (or UID) and optionally the user group (or GID) to use when running the image and for any subsequent `RUN`, `CMD`, and `ENTRYPOINT` instructions. |
| **`EXPOSE`** | **Network Ports** | Functions as a type of documentation between the person who builds the image and the person who runs the container, indicating which ports are intended to be published. |
| **`CMD`** | **Default Execution** | Provides default arguments or the main executable for an executing container. There can only be one `CMD` instruction in a Dockerfile. |

---

## 🏗️ Step-by-Step Breakdown of a Node.js Dockerfile

Below is an annotated example of a Dockerfile for a Node.js application. This specific configuration prioritizes security by utilizing the built-in, non-root `node` user.

```dockerfile
# 1. Base Image: Start from a lightweight Node.js image based on Alpine Linux
FROM node:20-alpine

# 2. Directory Setup: Create the app directory and node_modules, then assign ownership to the 'node' user
RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

# 3. Working Directory: Set the default directory inside the container for all subsequent commands
WORKDIR /home/node/app

# 4. Dependency Files: Copy package.json and package-lock.json (if available) to the working directory
COPY package*.json ./

# 5. Ownership Adjustment: Ensure the 'node' user owns the newly copied package files
RUN chown -R node:node /home/node/app

# 6. User Context: Switch from the default 'root' user to the unprivileged 'node' user
USER node

# 7. Install Dependencies: Execute npm install securely as the 'node' user
RUN npm i

# 8. Copy Application Code: Copy the rest of the application files and assign ownership in a single step
COPY --chown=node:node . .

# 9. Port Documentation: Indicate which port the container will listen on at runtime
EXPOSE 3000

# 10. Execution Command: Define the default command to start the application when a container runs
CMD [ "node", "app.js" ]
```
