# Task Manager

This ReadMe file will provide you with essential information about setting up, configuring, and running this project. Please read through the instructions carefully to ensure a smooth experience.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Setup](#setup)
3. [Configuration](#configuration)
   - [Environment Variables](#environment-variables)
   - [Database Configuration](#database-configuration)
4. [Running the Project](#running-the-project)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

## Project Overview

This Django project is designed to manage a list of tasks. The user should be able to create, update, and delete tasks. They can als view them on a dashboard.

## Installation

### Prerequisites

Before you begin, ensure that you have the following software installed:

- Python 3.8
- Django 4.2.2

### Setup

1. Clone this repository to your local machine:

   ```
   git clone "https://github.com/GituMbugua/to-do-list.git"
   ```

2. Navigate to the project directory:

   ```
   cd /to-do-list
   ```

3. Create a virtual environment to isolate project dependencies:

   ```
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

   - On Windows:

     ```
     venv\Scripts\activate
     ```

5. Install project dependencies:

   ```
   pip install -r requirements.txt
   ```

## Configuration

### Database Configuration

Our project uses SQLite. Update the database settings in the `settings.py` file according to your database configuration.

## Running the Project

Run the following command to apply migrations and start the development server:

```
python manage.py migrate
python manage.py runserver
```

The development server will start at `http://127.0.0.1:8000/`.

## Contributing

We welcome contributions to our project! If you'd like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request detailing your changes.

## License
[LICENSE](./LICENSE)

---
Happy coding!