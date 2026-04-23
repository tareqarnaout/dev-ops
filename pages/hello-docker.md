---
layout: page
title: "4.3 Hello Docker - Single Container Project"
description: A hands-on Flask project to build and run a single-container Docker app from scratch.
permalink: /hello-docker/
parent: "8. Projects"
nav_order: 3
---

# Hello Docker - Single Container Project

A hands-on Docker project for students who already know the basics of images and containers. We will containerize a real Flask web app from scratch.

---

## Project Structure

```text
hello-docker/
├── app.py
├── requirements.txt
└── Dockerfile
```

---

## The Files

### `app.py`

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Docker!</h1><p>This app is running inside a container.</p>"

@app.route("/about")
def about():
    return "<h1>About</h1><p>A simple Flask app containerized with Docker.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

> **Why `host="0.0.0.0"`?** By default Flask binds to `127.0.0.1` - localhost inside the container - which is unreachable from outside. Binding to `0.0.0.0` means "accept connections on all interfaces", making the app accessible through port mapping.

### `requirements.txt`

```txt
flask==3.0.0
```

### `Dockerfile`

```dockerfile
# 1. Base image - what OS/runtime we start from
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy dependencies file first (layer caching optimization)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the app code
COPY . .

# 6. Tell Docker which port the app listens on (documentation only)
EXPOSE 5000

# 7. The command to run when the container starts
CMD ["python", "app.py"]
```

---

## Commands - Step by Step

```bash
# Step 1 - Build the image
docker build -t hello-docker .

# Step 2 - Run a container from the image
docker run -d -p 5000:5000 --name my-app hello-docker

# Step 3 - Open in browser
# Visit: http://localhost:5000

# Step 4 - Check running containers
docker ps

# Step 5 - View logs
docker logs my-app

# Step 6 - Stop and remove
docker stop my-app
docker rm my-app
```

---

## Key Concept: The `.` in `COPY`

When you write:

```dockerfile
COPY requirements.txt .
```

The `.` means **"copy into the current working directory inside the container"**. Since `WORKDIR /app` was set earlier, this is equivalent to:

```dockerfile
COPY requirements.txt /app/requirements.txt
```

Think of `WORKDIR` like doing `cd /app` in a terminal. After that, any `.` you use refers to `/app`.

---

## Key Concept: Layer Caching Optimization

Docker builds images layer by layer - one layer per instruction. If a layer has not changed since the last build, Docker reuses the cached version and skips re-running it.

### Why order matters

```dockerfile
# Without optimization - slower rebuilds
COPY . .
RUN pip install -r requirements.txt

# With optimization - dependency install can stay cached
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

### What happens on each build

| Layer | Instruction | Build #1 | Build #2 (edited `app.py`) |
| :--- | :--- | :---: | :---: |
| 1 | `FROM python:3.11-slim` | run | cached |
| 2 | `WORKDIR /app` | run | cached |
| 3 | `COPY requirements.txt .` | run | cached |
| 4 | `RUN pip install ...` | run (~30s) | cached |
| 5 | `COPY . .` | run | run |

> **The rule:** Put things that change rarely at the top, and things that change often at the bottom. Dependencies change far less than your code, so they go first.

---

## Key Concepts Summary

- **Image**: Read-only blueprint. Like a class in OOP.
- **Container**: Running instance of an image. Like an object.
- **Port mapping**: Connects a host port to a container port.
- **Layer cache**: Unchanged layers are reused to speed up builds.

---

## Student Exercise

1. Add a new route `/time` that returns the current server time.
2. Rebuild the image and run a new container.
3. Try running without stopping the old container first and observe the port conflict error.
4. Stop and remove the old container, then run again.

This reinforces the image vs container distinction and gets you comfortable with the build-run cycle.
