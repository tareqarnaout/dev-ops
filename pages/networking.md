---
layout: page
title: "3. Docker Networking"
description: Docker network drivers, container communication, and common network commands.
permalink: /networking/
nav_order: 3
---

# Docker Networking

Docker networking allows containers to communicate with each other, the host, and the outside world.

![Docker network drivers overview](/assets/images/docker_network_diagram.svg)

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
