# FastAPI + MongoDB on OpenShift

This project demonstrates how to deploy a simple **FastAPI service** connected to a **MongoDB database** on OpenShift.  
The system uses two pods:

- **MongoDB Pod** – Stores all data.  
- **FastAPI Pod** – Runs the API server and connects to MongoDB.

---

## Features

The FastAPI pod provides a REST API with basic CRUD operations:

- **POST /items** → Insert new data  
- **GET /items** → Retrieve all documents  
- **PUT /items/{id}** → Update a document by ID  
- **DELETE /items/{id}** → Delete a document by ID

---

## Project Structure

project_root/
│
├── infrastructure/
│ └── k8s/ # YAML files for MongoDB and FastAPI
│
├── main.py # FastAPI main code
├── requirements.txt # Required Python libraries
└── commands.bat # Command file to deploy



---

## How it Works

1. **MongoDB Pod** runs the database.  
2. **FastAPI Pod** runs the Python code and connects to MongoDB through an internal Service in OpenShift.  
3. **Route** in OpenShift exposes the FastAPI service externally.

---

## Usage

### 1. Deployment on OpenShift
- All YAML files are located in:  
infrastructure/k8s/

- To deploy everything easily, run the command file from the project root:
```bat
commands.bat