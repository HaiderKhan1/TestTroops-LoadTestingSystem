# TestTroops-LoadTestingSystem
A simple REST API developed using Python + Flask for the purpose of learning load testing.

# Flask Math Operations API

This Flask application provides a simple REST API for performing basic arithmetic operations (add, subtract, multiply, divide) on two numbers.

## Setup and Installation

### Prerequisites

- Python (3.x is recommended)
- Flask

### Cloning the Repository

Clone the repository to your local machine:

```bash
git clone [URL_OF_YOUR_REPOSITORY]
```

Navigate into the project directory:
```bash
cd [NAME_OF_YOUR_PROJECT_DIRECTORY]
```

### Cloning the Repository
Ensure that Python is installed on your system:
```bash
python --version
```

If Python is not installed, download and install it from the official [Python website](https://www.python.org/downloads/).

Install Flask using pip:
```bash
pip install Flask
```

## Running the Server
Start the Flask server by running:


```bash
python app.py
```

This will start the server on http://localhost:5000.

## Making Requests
You can interact with the API using curl or any other HTTP client.

### Sample cURL request

```bash
curl "http://localhost:5000/multiply?x=5&y=3"
```

This request calls the /multiply endpoint with x=5 and y=3 as query parameters.

### Creating Your Own Requests
You can modify the curl command to interact with different endpoints and pass different values. The general format is:


```bash
curl "http://localhost:5000/[ENDPOINT]?x=[VALUE1]&y=[VALUE2]"
```

Replace [ENDPOINT] with add, subtract, multiply, or divide, and [VALUE1], [VALUE2] with the numbers you wish to operate on.

### API Endpoints
- /: Returns a simple message indicating the server is operational.
- /add: Adds two numbers. Pass x and y as query parameters.
- /subtract: Subtracts y from x. Pass x and y as query parameters.
- /multiply: Multiplies x and y. Pass x and y as query parameters.
- /divide: Divides x by y. Pass x and y as query parameters.