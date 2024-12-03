# ft_transcendence

**ft_transcendence** is a full-stack web application built as part of the **42 Network** Common Core curriculum. This project aims to create a social gaming platform where users can participate in tournaments, chat in real-time, and track their gaming statistics. The application is built using a **vanilla JavaScript** frontend and a **Django** backend with a **PostgreSQL** database, all containerized using **Docker** for easy deployment and scalability.

The project integrates advanced features such as **real-time chat**, **user authentication with JWT**, **two-factor authentication (2FA)**, **microservices architecture**, and **game customization options**.

## Features

- **User Authentication**: Secure user sign-up and login with JWT and support for two-factor authentication (2FA).
- **Real-Time Chat**: Live messaging feature for players to communicate during and after games.
- **Matchmaking System**: Users can join or create tournaments, with matchmaking based on user history and ranking.
- **User Dashboards**: Players can view their stats, games played, and progress in various tournaments.
- **Game Customization**: Customize game settings to enhance user experience.
- **Microservices Architecture**: Backend is designed using Django and structured as microservices for scalability.
- **Remote Authentication**: Supports remote authentication, allowing users to securely log in from different devices.
- **Containerized Application**: Full setup provided with **Docker** and **docker-compose** for seamless local development and deployment.

## Technologies Used

### Frontend:
- **Vanilla JavaScript** (No frameworks, plain JavaScript)
- **HTML5**
- **CSS3**
- **WebSockets** (for real-time chat)
- **Nginx** (used to serve the frontend as well as reverse proxy requests to backend services)

### Backend:
- **Django** (Backend Framework)
- **PostgreSQL** (Database for storing user and game data)
- **JWT** (JSON Web Tokens for Authentication)
- **Two-Factor Authentication (2FA)**
- **Redis** (Used for real-time data caching and chat functionality)
- **Etcd** (Distributed key-value store, used for configuration management and coordination between services)
- **Python** (Backend services implemented in Python, running in containers)

### DevOps & Infrastructure:
- **Docker** (For containerization)
- **docker-compose** (For managing multi-container applications)
- **Apache APISIX** (API Gateway for routing requests to different backend services)
- **Redis** (Caching, session storage, and real-time communication management)
- **PostgreSQL** (Database for storing application data)
- **Etcd** (Distributed key-value store for managing service configuration)
- **pgAdmin** (Database management tool for PostgreSQL)

### Microservices:
- **Authentication Service**: Handles user sign-up, login, JWT authentication, and 2FA.
- **User Management Service**: Manages user data, profiles, and game history.
- **Chat Service**: Handles real-time communication between users using WebSockets.
- **Game Service**: Manages tournament and game-related functionalities, including matchmaking.
- **API Gateway**: **Apache APISIX** serves as the API Gateway to route incoming requests to the appropriate backend services.

## Installation and Setup

### Prerequisites

- Docker
- Docker Compose

Make sure you have **Docker** and **Docker Compose** installed on your machine. You can download Docker from [here](https://www.docker.com/get-started).

### Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/ft_transcendence.git
   cd ft_transcendence
   ```

    Build and run the Docker container:

    To set up the application, simply run:
   ```bash
   docker-compose up -d
   ```

This will:

  Build and run the Docker containers for each service
  Start the backend services (Django, Redis, PostgreSQL, etc.)
  Start the frontend and reverse proxy through Nginx
  Set up the PostgreSQL database

Access the Application:

Once everything is up and running, you can access the application via https://localhost:9443.

  Authentication Setup:
        JWT Authentication: Use your credentials to log in. JWT tokens will be used for session management.
        Two-Factor Authentication (2FA): Enable 2FA during login for added security.

Architecture and Services
Microservices Overview

The ft_transcendence application follows a microservices architecture. The backend is split into several services, each responsible for different aspects of the application:

  Authentication Service (auth): Handles authentication, JWT management, and two-factor authentication.
  User Management Service (management): Manages user profiles, statistics, and game history.
  Chat Service (chat): Manages real-time communication between users using WebSockets and Redis.
  Game Service (games): Handles game logic, matchmaking, and tournament creation.
  API Gateway (apisix): Routes API requests to appropriate backend services via Apache APISIX.

Dependencies and Container Services

  PostgreSQL: The relational database that stores user and game-related data.
  Redis: Used for caching, real-time communication, and managing user sessions.
  Etcd: Distributed key-value store for configuration and coordination between services.
  API Gateway: Apache APISIX is used to manage and route API traffic to the correct backend services.
  pgAdmin: A web-based tool for managing PostgreSQL databases, used for administrative tasks.



This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

  42 Network for providing the opportunity and project specifications.
  Django and PostgreSQL for providing great backend frameworks.
  Docker and docker-compose for simplifying deployment.
  Apache APISIX for providing an easy-to-use API Gateway solution.
  Redis and Etcd for enhancing system performance and coordination.
