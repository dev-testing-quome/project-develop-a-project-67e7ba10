# Developer Setup Guide - project-develop-a-project

This guide helps you set up your development environment for "project-develop-a-project," a project management application.  We recommend using Docker for a consistent and simplified development experience.

## Prerequisites

* **Required Software Versions:**
    * Docker Desktop (>= 20.10.0)
    * Docker Compose (>= 1.29.0)  (Usually included with Docker Desktop)
    * Node.js (>= 16.0.0) (For Option 2: Native Development)
    * Python (>= 3.9) (For Option 2: Native Development)
    * Git (>= 2.30.0)
* **Development Tools:**
    * Text editor or IDE (VS Code recommended)
    * Git client (e.g., GitKraken, Sourcetree, or command line)
    * Postman or similar API testing tool (optional, but recommended)
* **IDE Recommendations and Configurations:**
    * **VS Code:** Install the following extensions:
        * Python extension (for Python backend)
        * ESLint (for JavaScript/TypeScript linting)
        * Prettier (for code formatting)


## Local Development Setup

### Option 1: Docker Development (Recommended)

1. **Clone Repository:**
   ```bash
   git clone <repository_url>
   cd project-develop-a-project
   ```

2. **Docker Setup Commands:**  Ensure Docker and Docker Compose are installed and running.

3. **Development `docker-compose.yml` Configuration:**  (Assume a `docker-compose.yml` file exists in the root directory)  This file will define your services (database, backend, frontend).  Example:

   ```yaml
   version: "3.9"
   services:
     db:
       image: postgres:14
       environment:
         - POSTGRES_USER=project_user
         - POSTGRES_PASSWORD=project_password
         - POSTGRES_DB=project_db
       ports:
         - "5432:5432"
     backend:
       build: ./backend
       ports:
         - "8000:8000"
       depends_on:
         - db
       environment:
         - DATABASE_URL=postgres://project_user:project_password@db:5432/project_db
         - SECRET_KEY=your_secret_key  # Replace with a strong secret key
     frontend:
       build: ./frontend
       ports:
         - "3000:3000"
       depends_on:
         - backend
   ```

4. **Hot Reload Setup:**  This will depend on your frontend framework (e.g., React, Vue, Angular).  Most frameworks have built-in hot reloading capabilities.  Ensure that your frontend build process is configured for hot reloading.


### Option 2: Native Development

1. **Backend Setup:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r backend/requirements.txt
   ```

2. **Frontend Setup:**
   ```bash
   cd frontend
   npm install
   ```

3. **Database Setup:**  Install PostgreSQL (or your chosen database) and create a database named `project_db` with a user `project_user` and password `project_password`. Update the connection string in your backend configuration accordingly.


## Environment Configuration

* **Required Environment Variables:**
    * `DATABASE_URL`:  Database connection string.
    * `SECRET_KEY`:  A strong, randomly generated secret key for security.
    * `GITHUB_CLIENT_ID` & `GITHUB_CLIENT_SECRET` (for GitHub integration)
    * ...other environment variables specific to your application's features.

* **Local Development `.env` File Setup:** Create a `.env` file in the root directory (or in a designated config directory) and populate it with your environment variables:

   ```
   DATABASE_URL=postgres://project_user:project_password@localhost:5432/project_db
   SECRET_KEY=your_secret_key
   GITHUB_CLIENT_ID=your_github_client_id
   GITHUB_CLIENT_SECRET=your_github_client_secret
   ```

* **Configuration for Different Environments:** Use environment variables to configure different settings for development, staging, and production environments.  Consider using a configuration management tool like `dotenv` (Python) or similar tools for other languages.


## Running the Application

* **Start Commands for Development:**
    * **Docker:** `docker-compose up -d`
    * **Native:**  Start the backend server (e.g., `python manage.py runserver` if using Django) and then start the frontend development server (e.g., `npm start`).

* **How to Access Frontend and Backend:** The frontend will typically be accessible at `http://localhost:3000` and the backend API at `http://localhost:8000`.

* **API Documentation Access:** If you're using tools like Swagger or OpenAPI, access the documentation through the specified URL (usually a path on your backend).


## Development Workflow

* **Git Workflow and Branching Strategy:** Use Gitflow or a similar branching strategy (e.g., feature branches, pull requests).

* **Code Formatting and Linting Setup:** Use Prettier and ESLint (or equivalent tools for your languages) to ensure consistent code style.  Configure your IDE to automatically format code on save.

* **Testing Procedures:**  Write unit and integration tests for both frontend and backend.  Use a testing framework like pytest (Python) or Jest (JavaScript).

* **Debugging Setup:** Use your IDE's debugging tools or command-line debuggers (e.g., `pdb` for Python, `node inspect` for Node.js).


## Database Management

* **Running Migrations:**  Use database migration tools (e.g., Alembic for SQLAlchemy) to manage database schema changes.

* **Seeding Development Data:** Create scripts to seed your database with sample data for testing.

* **Database Reset Procedures:** Create scripts to easily reset your database to a clean state.


## Testing

* **Running Unit Tests:**  Use your testing framework's commands (e.g., `pytest` or `jest`).

* **Running Integration Tests:**  These tests should cover interactions between different parts of your application.

* **Test Coverage Reports:**  Generate test coverage reports to track the percentage of your code covered by tests.


## Common Development Tasks

* **Adding New API Endpoints:** Follow the established API design guidelines. Write tests for the new endpoint.

* **Adding New Frontend Components:** Use your framework's component architecture.  Ensure the component is styled consistently and integrates well with the existing UI.

* **Database Schema Changes:**  Use migrations to manage changes. Update your models and run the migrations.

* **Adding Dependencies:**  Use your package manager (pip, npm) to add dependencies. Update the relevant `requirements.txt` or `package.json` file.


## Troubleshooting

* **Common Setup Issues:** Refer to the documentation of the tools and frameworks used in the project.

* **Port Conflicts Resolution:**  Change the ports used by your services in the `docker-compose.yml` file or your configuration files.

* **Dependency Issues:**  Check your `requirements.txt` or `package.json` for conflicting dependencies.  Use tools like `pip-tools` (Python) to manage dependency versions.

* **Environment Variable Problems:** Double-check the spelling and values of your environment variables in the `.env` file and your application's configuration.


## Contributing

* **Code Style Guidelines:** Adhere to the project's coding style guide (if one exists).

* **Pull Request Process:**  Create feature branches, write tests, and submit pull requests with clear descriptions and explanations.

* **Issue Reporting:**  Use the project's issue tracker to report bugs or request new features.  Provide detailed descriptions and steps to reproduce issues.


This guide provides a solid foundation for setting up your development environment. Remember to consult the project's specific documentation and guidelines for more detailed instructions. Remember to replace placeholders like `<repository_url>` and `your_secret_key` with your actual values.
