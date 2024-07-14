
# Project Name: Flask CRUD Application

## Overview

This project is a web application built using the Flask framework and MongoDB for database operations. The application demonstrates basic CRUD (Create, Read, Update, Delete) operations through a web interface. It includes routes for creating, reading, updating, and deleting records in a MongoDB collection. 

## Features

- **Create**: Add new records to the database.
- **Read**: Retrieve and display all records from the database.
- **Update**: Edit and update existing records.
- **Delete**: Remove records from the database.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Flask
- MongoDB
- pymongo

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/flask-crud-app.git
cd flask-crud-app
```

2. Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Ensure MongoDB is running on your local machine. If MongoDB is running on a different host or port, update the connection string in the code.

## Project Structure

```
flask-crud-app/
├── templates/
│   ├── form.html
│   ├── get.html
│   └── index.html
├── venv/
├── server.py
├── requirements.txt
└── README.md
```

## Running the Application

1. Start the Flask application:

```bash
python server.py
```

2. Open your web browser and navigate to `http://localhost:5000`.

## Routes

- `/` : Home page
- `/create` : Create a new record
- `/get` : Fetch and display all records
- `/delete/<id>` : Delete a record by ID
- `/edit/<id>` : Edit a record by ID

## Code Overview

### `server.py`

This file contains the main logic of the application.

- **MongoDB Connection**: Connects to the MongoDB database.
- **Home Route**: Renders the home page.
- **Create Route**: Handles both GET and POST requests for creating new records.
- **Fetch All Route**: Retrieves all records from the database and renders them.
- **Delete Route**: Deletes a record by its ID.
- **Edit Route**: Handles both GET and POST requests for editing existing records.

### `templates/`

This directory contains HTML templates used by the Flask application.

- **form.html**: Form for creating and editing records.
- **get.html**: Displays all records from the database.
- **index.html**: Home page of the application.

## Logging

The application uses Python's built-in `logging` module to log various events and errors. Logs are printed to the console for easy debugging.


## Contact

For any questions or suggestions, please contact **omkarane84@gmail.com**
