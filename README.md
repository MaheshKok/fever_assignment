# FastAPI Events API

## Overview

This repository contains a high-performance FastAPI application designed for fetching, caching, and serving event data efficiently. It integrates Redis for caching to enhance response speeds and reduce load on the database backend during high-traffic periods. The application uses SQLAlchemy in its asynchronous mode to interact with a PostgreSQL database, ensuring non-blocking database operations suitable for high concurrency needs.

## Run Project
- it used postgresql as database, so run postgresql 
- create database fever
- It uses alembic for migration
- To apply migration ```alembic upgrade head```
- To run project ```python main.py```
- TO access API Endpoints - ```https://localhost:8000/docs```

## Key Features

- **Efficient Data Fetching**: Dynamically fetches events based on start and end times through RESTful endpoints.
- **Redis Caching**: Implements Redis for caching event data to speed up repeated requests.
- **Asynchronous Support**: Utilizes asynchronous programming paradigms across database and network operations to improve I/O efficiency.
- **Scalability**: Built to handle between 1,000 to 5,000 requests per minute, suitable for high-load environments.

## Technologies

- **[FastAPI](https://fastapi.tiangolo.com/)**: Modern, fast (high-performance), web framework for building APIs.
- **[SQLAlchemy AsyncIO](https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html)**: SQLAlchemy's support for asynchronous database access.
- **[Redis](https://redis.io/)**: An in-memory data structure store used as a distributed, in-memory key–value database, cache and message broker.
- **[aioredis](https://aioredis.readthedocs.io/en/latest/)**: Asynchronous Redis client that supports asyncio.
- **[HTTPX](https://www.python-httpx.org/)**: Fully featured HTTP client for Python 3, which provides synchronous and asynchronous APIs.

## Project Structure

```plaintext
/
├── app/
│ ├── database/
│ │ ├── schemas/ # Contains SQLAlchemy models.
│ │ └── session_manager/ # Manages database sessions.
│ ├── endpoints/
│ │ ├── dependency.py # Provides dependencies such as Redis client.
│ │ ├── utils.py # Utility functions for interacting with DB and Redis.
│ │ └── routes.py # Defines FastAPI routes for API endpoints.
│ ├── pydantic_models/ # Pydantic models for data validation.
│ └── core/
│ │ └── config.py # Manages configuration and environment variables.
├ └── main.py # Entry point of the FastAPI application.
├── cron/
│ └── scheduler.py # Contains the setup for scheduled tasks (cron jobs).
└── README.md



## Setup and Installation

### Prerequisites

- Python 3.8+
- Redis server (local or remote setup)

### Installation Steps

1. **Clone the repository**

    ```bash
    git clone https://github.com/swolfyguy/MarketplaceEventsAPI.git
    cd MarketplaceEventsAPI
    ```

2. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the environment**

    There are two toml files in cfg directory
        test.toml
        production.toml
    Set as per usage

4. **Run the application**

    ```bash
    uvicorn app.main:app --reload
    ```

    The `--reload` flag is ideal for development to automatically reload the server on code changes.

## Usage

Access the API through the endpoint:

- **API Documentation**: Navigate to `http://localhost:8000/docs` in your browser to view the Swagger UI which provides interactive documentation generated by FastAPI.

## Contributing

Contributions are welcome! Please fork the project and submit a pull request with your features or fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
