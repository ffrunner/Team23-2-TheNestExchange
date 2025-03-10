# The Nest Exchange

The Nest Exchange is an e-commerce web platform designed for the KSU community, enabling users to exchange free goods. This document outlines how to download, set up, and run the project locally, as well as information about the technologies used. 

## Table of Contents

-[Features](#features)
-[Prerequisites](#prerequisites)
-[Installation](#installation)
-[Frontend Setup with React](#frontend-setup-with-react)
-[Backend Setup](#backend-setup)
-[Usage](#usage)
-[Technologies Used](#technologies-used)
-[Contributing](#contributing)
-[License](#license)
-[Contact](#contact)

#Features

- User registration and authentication
- Role-based access for Listers, Claimers, and Admins
- Item posting and claiming functionality
- Admin dashboard for managing items and users
- Redis caching for performance optimization

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Git**: Installed version control ([Download Git](https://git-scm.com/downloads ))
- **Python**: Version 3.6 or higher installed ([Download](https://www.python.org/downloads/))
- **PostgreSQL**: Installed and running ([Download PostgreSQL](https://www.postgresql.org/download/))
- **Redis**: Installed and running ([Download Redis](https://redis.io/download))
- **Node.js**: Installed for frontend development ([Download Node.js](https://nodejs.org/en/download/))

## Installation

Follow these steps to set up The Nest Exchange:

### Frontend Setup with React

1. **Clone the repository**:
    Open the terminal and run the following command: 
    ```bash
    git clone https://github.com/ffrunner/Team23-2-TheNestExchange.git

2. **Navigate to the project directory**: 
    ```bash
    cd TheNestExchange

3. **Install React dependicies**:
    npm install

4. **Start the react application**:
    npm start

### Backend Setup

1. **Create a Python virtual environment**:
    ```bash
    python -m venv venv

2. **Activate the virtual environment**:
- On windows:
    ```bash
    venv\Scripts\activate

- On macOS/Linux:
    ```bash
    source venv/bin/activate

3. **Install Python dependencies**:
    pip install -r requirements.txt

4.