---
layout: page
title: "3. Docker Networking"
description: Docker network drivers, container communication, and common network commands.
permalink: /networking/
nav_order: 3
---

# Docker Networking

Docker networking allows containers to communicate with each other, the host, and the outside world.

![Docker network drivers overview]({{ '/assets/images/docker_network_diagram.svg' | relative_url }})

---

## Network Drivers (Types)

### 1. `bridge` (default)
- Default network for containers on a single host
- Containers get their own IP and can talk to each other by IP or name
- Isolated from the host network

```bash
docker run --network bridge nginx
```

### 2. `host`
- Container shares the host's network stack directly
- No network isolation - container uses host IP/ports
- Best performance, but risky

```bash
docker run --network host nginx
```

### 3. `none`
- No networking at all
- Fully isolated container

```bash
docker run --network none nginx
```

### 4. `overlay`
- Spans multiple Docker hosts (used with **Docker Swarm**)
- Allows containers on different machines to talk to each other

### 5. `macvlan`
- Assigns a real MAC address to the container
- Container appears as a physical device on the network
- Used for legacy apps that need direct LAN access

---

## How Containers Communicate

```
 [Container A] --┐
                 ├--> [bridge network] --> [Internet]
 [Container B] --┘
```

On a **custom bridge network**, containers can reach each other by **container name** (DNS resolution built-in).

### Step 1: Create the Custom Network

First, create a user-defined bridge network so the containers can resolve each other by name.

```bash
docker network create my-db-network
```

### Step 2: Start the Database Container

Run the official `postgres` image from Docker Hub. Attach it to your new network and give it a specific name (`my-postgres`).

```bash
docker run -d \
  --name my-postgres \
  --network my-db-network \
  -e POSTGRES_PASSWORD=mysecretpassword \
  postgres
```

### Step 3: Start the Web App Container

Run the official `adminer` image. Attach it to the same network and expose its web interface to your local machine on port `8080`.

```bash
docker run -d \
  --name my-adminer \
  --network my-db-network \
  -p 8080:8080 \
  adminer
```

### How the DNS Resolution Happens in Practice

If you open your web browser and go to `http://localhost:8080`, you will see the Adminer login screen.

When Adminer asks for the **Server** to connect to, you do not type an IP address. Instead, you simply type:

```text
my-postgres
```

> On the **default** bridge network, name-based DNS does **not** work - you must use IPs.

---

## Key Commands

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

## Real-world Example (docker-compose)

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

## Summary Table

| Driver | Scope | Use Case |
|---|---|---|
| `bridge` | Single host | Default, isolated containers |
| `host` | Single host | Max performance, no isolation |
| `none` | Single host | Fully isolated |
| `overlay` | Multi-host | Docker Swarm / clustering |
| `macvlan` | Single host | Legacy apps needing LAN access |

The most common setup you'll use day-to-day is a **custom bridge network** with docker-compose, where services discover each other by name automatically.
