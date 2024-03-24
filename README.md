# Grievance Registration Web Application

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

[Project-Clean-Android-Application ![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/be1cbe45-b0bc-41de-892e-2970a57ec720)](https://github.com/TwoPointerr/Project-Clean-Android-Application)

## Overview

In today's interconnected world, our Grievance Registration Android Application leverages technology to address modern issues related to grievance registration. The project modules are designed to streamline and simplify the overall grievance registration process, saving users valuable time.

## Features

- **Image Severity Analysis**: Users can capture images through the application, and a machine learning model assesses the severity of the issue, categorizing it as high, medium, or low.

- **Geospatial Location Registration**: The application records the spatial location of the user during the image-capturing process. This information is crucial for identifying the overall location of the reported issue.

- **Effortless Grievance Submission**: Users can submit captured images along with relevant descriptions. The submissions are then sent to a government body responsible for addressing grievances.

- **Public Grievance Posts**: A grievance post is generated for each submission, visible to fellow citizens. Users can view and upvote these posts, creating a transparent system that encourages civic engagement.

## Installation using docker
### 1. Clone the Repository

```bash
git clone https://github.com/TwoPointerr/Project-Clean-Web-Application.git
cd ./Project-Clean-Web-Application
```

### 2. Configure Databse
configure database as per project_clean/settings.py or adjust project_clean/settings.py as per your database configuration
https://github.com/TwoPointerr/Project-Clean-Web-Application/blob/34f8d6bfbc10c6d324fcb6e35bda2201576aeef3/project_clean/settings.py#L107-L122

### 3. Spin up Containers
```bash
docker-compose up
```
- Make sure docker is running

## Installation on Local

### 1. Clone the Repository

```bash
git clone https://github.com/TwoPointerr/Project-Clean-Web-Application.git
cd ./Project-Clean-Web-Application
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
# Install virtualenv if not already installed
pip install virtualenv

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This command installs all the required Python packages specified in the `requirements.txt` file.

### 4. Configure Databse
configure database as per project_clean/settings.py or adjust project_clean/settings.py as per your database configuration
https://github.com/TwoPointerr/Project-Clean-Web-Application/blob/34f8d6bfbc10c6d324fcb6e35bda2201576aeef3/project_clean/settings.py#L107-L122


### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

This command applies any pending database migrations.

### 6. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

This command creates a superuser account for administrative access to the Django admin interface.

### 7. Run the Development Server

```bash
python manage.py runserver
```


