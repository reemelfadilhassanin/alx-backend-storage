# MySQL Advanced Project

## Overview

This project involves advanced SQL concepts using MySQL. The primary objective is to create and manipulate database tables while implementing best practices for data integrity and optimization.

## Learning Objectives

By the end of this project, you should be able to:
- Create tables with constraints.
- Optimize queries by adding indexes.
- Implement stored procedures and functions in MySQL.
- Create and use views in MySQL.
- Implement triggers in MySQL.

## Project Structure

The project consists of several SQL scripts located in the `0x00-MySQL_Advanced` directory. Each script corresponds to specific tasks outlined below.

### Tasks

1. **We are all unique!**
   - **File:** `0-uniq_users.sql`
   - **Description:** Creates a `users` table with a unique email constraint.

2. **In and not out**
   - **File:** `1-country_users.sql`
   - **Description:** Extends the `users` table to include a `country` field with specified enumerations.

3. **Best band ever!**
   - **File:** `2-fans.sql`
   - **Description:** Ranks country origins of bands based on the number of fans.

## Requirements

- All SQL scripts must be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30).
- All files should end with a new line.
- SQL queries should be prefixed with comments describing their purpose.
- All SQL keywords should be in uppercase.

## How to Run

1. Start the MySQL service in your container:
   ```bash
   service mysql start
