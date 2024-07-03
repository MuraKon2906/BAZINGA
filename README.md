﻿# 📝 BAZINGA

BAZINGA is a simple note-taking application built with FastAPI, MongoDB, and Jinja2 for templating. It allows users to create, view, and manage notes through a web interface. ✨

## DEMO 🎥

https://github.com/MuraKon2906/BAZINGA/assets/158759753/88d77d21-fd15-4073-a0cb-85af0020814b


## Features 🌟
- 📝 Create and store notes in a MongoDB database.
- 🖥️ View all notes rendered as HTML pages using Jinja2 templates.
- 🔌 A RESTful API for managing notes programmatically.

## Getting Started 🚀

### Prerequisites ✅
Ensure you have Python installed on your system. The recommended version is Python 3.8 or newer. 🐍

### Installation 💾
1. Clone the repository to your local machine. 💻
2. Navigate to the project directory. 📂
3. Install the required dependencies: 📦
    ```bash
    pip install fastapi uvicorn python-multipart jinja2
    ```
4. Ensure MongoDB is running and accessible. The connection string is defined in `config/db.py`. ⚙️

### Running the Application ▶️
To start the application, run the following command in your terminal:

```bash
fastapi dev index.py
```
This command starts a local development server. By default, the server runs on port 8000. Access the application by navigating to [http://localhost:8000](http://localhost:8000) in your web browser. 🌐

## Usage 📖

### Creating a Note ✍️
To create a new note, send a POST request to `/notes/` with the note's title and description in the request body. 📨

### Viewing Notes 👀
Accessing the root endpoint ([http://localhost:8000](http://localhost:8000)) displays all notes in a paginated format. 📄

