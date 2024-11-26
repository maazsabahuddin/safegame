Safe Game - Microservice Architecture

Overview
This project is built using a microservices architecture to ensure modularity, scalability, and maintainability. Each microservice focuses on a specific functionality and communicates with other services when needed. The platform leverages Docker and docker-compose for orchestration and includes shared utilities for common functionality.

Architecture
The project consists of the following components:

Services:

user_auth_service: Manages user authentication and authorization. Includes endpoints for user registration, login, and token management.
library_service: Handles functionality related to managing a library system, such as books, categories, and user interactions.
Shared Utilities:

Shared reusable code (e.g., helper functions, constants) resides in the shared directory and is accessed by multiple services.
Reverse Proxy:

NGINX: Serves as the reverse proxy to route requests to the appropriate services.
Environment Management:

.env File: Contains environment variables for configuration, such as database credentials, service ports, and secret keys.
Orchestration:

Docker Compose: Used to run all services, the reverse proxy, and databases in containers.