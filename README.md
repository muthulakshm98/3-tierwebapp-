# 3-tierwebapp

🚀 3-Tier Web Application on AWS

This repository demonstrates a 3-tier web application architecture deployed on AWS, following industry best practices for scalability, maintainability, and separation of concerns.

📌 Overview

The application is divided into three core layers:

Frontend Layer
Handles user interface and client-side interactions.
Backend Layer
Implements business logic using Python and manages communication between frontend and database.
Database Layer
Stores and retrieves application data using a lightweight database.

🏗️ Architecture

This project follows a standard 3-tier architecture:

User → Frontend → Backend → Database

The application is deployed on AWS using cloud services such as EC2, and can be extended with S3 and CloudFront for static hosting and content delivery.

⚙️ Tech Stack
Frontend: HTML, CSS (Templates)
Backend: Python (Flask)
Database: SQLite
Cloud Platform: AWS (EC2)
CI/CD: GitHub Actions

📂 Project Structure
3-tierwebapp/
│── .github/workflows/   # CI/CD pipelines
│── templates/           # Frontend templates
│── app.py               # Backend application (Flask)
│── database.db          # SQLite database
│── README.md            # Project documentation

🚀 Features
Simple and clean 3-tier architecture
Beginner-friendly AWS deployment setup
Integrated CI/CD pipeline using GitHub Actions

![Stars](https://img.shields.io/github/stars/muthulakshm98/3-tierwebapp-?style=social)
![Forks](https://img.shields.io/github/forks/muthulakshm98/3-tierwebapp-?style=social)
![Issues](https://img.shields.io/github/issues/muthulakshm98/3-tierwebapp-)
![Last Commit](https://img.shields.io/github/last-commit/muthulakshm98/3-tierwebapp-)
