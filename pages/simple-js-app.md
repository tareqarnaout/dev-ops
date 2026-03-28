---
layout: page
title: 3.2 Simple JavaScript MongoDB App
description: Copy-ready Node.js project to test MongoDB Docker connectivity.
permalink: /simple-js-app/
parent: 3. Projects
nav_order: 2
---

# Node.js MongoDB Connection Test Project

This project contains the files needed to test your local MongoDB Docker container setup.

## Project Structure

```text
docker-test-app/
  package.json
  server.js
  index.html
```

## 1. package.json

```json
{
  "name": "docker-test-app",
  "version": "1.0.0",
  "description": "Simple Node.js app to test MongoDB connection",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.18.2",
    "mongodb": "^6.3.0"
  }
}
```

## 2. server.js

```javascript
const express = require('express');
const { MongoClient } = require('mongodb');
const path = require('path');

const app = express();
const port = 3000;

const url = "mongodb://admin:password@localhost:27017";
const dbName = "user-account";
const collectionName = "users";

app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.post('/add-user', async (req, res) => {
    const client = new MongoClient(url);
    try {
        await client.connect();
        console.log("Successfully connected to MongoDB server");

        const db = client.db(dbName);
        const collection = db.collection(collectionName);

        const newUser = {
            name: req.body.name,
            timestamp: new Date()
        };

        const result = await collection.insertOne(newUser);
        res.send(`<h3>Success!</h3><p>User added to MongoDB with ID: ${result.insertedId}</p><a href="/">Go back</a>`);

    } catch (err) {
        console.error("Database connection failed:", err);
        res.status(500).send("Error connecting to the database. Is the Docker container running?");
    } finally {
        await client.close();
    }
});

app.listen(port, () => {
    console.log(`App listening at http://localhost:${port}`);
});
```

## 3. index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Docker Node Test</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f4f4f9;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        input, button {
            padding: 10px;
            margin-top: 10px;
            font-size: 16px;
        }
        button {
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>MongoDB Connection Test</h2>
        <p>Ensure your MongoDB Docker container is running, then submit a name below.</p>
        <form action="/add-user" method="POST">
            <input type="text" name="name" placeholder="Enter a test name" required>
            <button type="submit">Test Write Operation</button>
        </form>
    </div>
</body>
</html>
```

## 4. Execution Instructions

1. Save the three files above in a single directory.
2. Open your terminal and navigate to that directory.
3. Run `npm install` to download dependencies.
4. Run `npm start` to launch the server.
5. Open `http://localhost:3000` in your web browser.

## Optional Quick Setup (Copy/Paste)

```bash
mkdir docker-test-app && cd docker-test-app
```

Create `package.json`, `server.js`, and `index.html` with the exact content above, then run:

```bash
npm install
npm start
```
