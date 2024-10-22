# 0x01. NoSQL - MongoDB Project

## Project Overview

This project is focused on understanding and implementing NoSQL databases, specifically MongoDB. The main objective is to learn how to perform basic database operations, including listing databases, inserting, updating, and deleting data.

## Learning Objectives

By the end of this project, you should be able to explain:

- What NoSQL means
- The differences between SQL and NoSQL databases
- The ACID properties
- The concept of document storage
- Types of NoSQL databases
- Benefits of using a NoSQL database
- How to query information from a NoSQL database
- How to perform CRUD operations (Create, Read, Update, Delete) in MongoDB
- How to use MongoDB with Python

## Project Requirements

### MongoDB Command Files

- All files must be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2).
- Each file should end with a new line.
- The first line of all files should be a comment: `// my comment`.
- A `README.md` file is mandatory at the root of the project folder.

### Python Scripts

- All files must be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7) and PyMongo (version 3.10).
- Each file should end with a new line.
- The first line should be: `#!/usr/bin/env python3`.
- Code must follow the `pycodestyle` style (version 2.5.*).
- All modules and functions should have documentation.
- Code should not be executed when imported.

## Installation Instructions

1. **Install MongoDB 4.2 on Ubuntu 18.04:**

   ```bash
   $ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
   $ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
   $ sudo apt-get update
   $ sudo apt-get install -y mongodb-org
   ```
