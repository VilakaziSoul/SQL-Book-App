# SQL Project README

## Project Overview

This project is a simple SQL-based application for managing a bookstore's inventory.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Available Options](#available-options)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## Features

1. **Inventory Management**
   - Add books to the database.
   - Update book information (title, author, quantity).
   - Delete books from the database.
   - Search for books by title or author.


## Getting Started

### Prerequisites

- Python 3.x
- SQLite (for the database)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/sql-bookstore-project.git
2. Navigate to the project directory:
   cd sql-bookstore-project
3. Create a virtual environment (optional):
   python -m venv venv
4. Activate the virtual environment:
  ```Windows
   venv\Scripts\activate
  ```macOS and Linux
   source venv/bin/activate
5. Install the required Python packages:
   pip install -r requirements.txt

### Usage

## Running the Application
###### To run the application, execute the following command from the project directory:
       python main.py

## Database Schema
The database schema includes a single table named books with the following columns:

id (INTEGER, PRIMARY KEY): Unique identifier for each book.
title (TEXT, NOT NULL): Title of the book.
author (TEXT, NOT NULL): Author of the book.
qty (INTEGER, NOT NULL): Quantity of the book in stock.

## Contributing 
Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: git checkout -b feature-name.
3. Make your changes and commit them: git commit -m "Add your feature".
4. Push your changes to your fork: git push origin feature-name.
5. Create a pull request.

### License 
This project is licensed under the MIT License.


