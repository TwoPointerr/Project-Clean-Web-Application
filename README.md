# Grievance Registration Web Application

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

[Project-Clean-Android-Application ![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/be1cbe45-b0bc-41de-892e-2970a57ec720)](https://github.com/TwoPointerr/Project-Clean-Android-Application)

Download Android Application here: [Releases](https://github.com/TwoPointerr/Project-Clean-Android-Application/releases)

## Overview

In today's interconnected world, our Grievance Registration Android Application leverages technology to address modern issues related to grievance registration. The project modules are designed to streamline and simplify the overall grievance registration process, saving users valuable time.

Research Paper: https://www.irjet.net/archives/V9/i4/IRJET-V9I4373.pdf

## Features

- **Image Severity Analysis**: Users can capture images through the application, and a machine learning model assesses the severity of the issue, categorizing it as high, medium, or low.

- **Geospatial Location Registration**: The application records the spatial location of the user during the image-capturing process. This information is crucial for identifying the overall location of the reported issue.

- **Effortless Grievance Submission**: Users can submit captured images along with relevant descriptions. The submissions are then sent to a government body responsible for addressing grievances.

- **Public Grievance Posts**: A grievance post is generated for each submission, visible to fellow citizens. Users can view and upvote these posts, creating a transparent system that encourages civic engagement.

## Working
![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/c445a3d3-1988-4028-ae5e-bcc0fe04f761)


## Installation using docker

<details>

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

</details>


## Installation on Local

<details>

Environment: Python 3 (3.9.5 recommended)

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
</details>

-----

### WEB App Screenshots

![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/3d21c7b2-cb84-4bc5-b301-e09a53e1e6ad)

<details>
  
<summary>More screenshots</summary>
  
![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/19e8079b-8d20-4930-9e62-ebddaab9ed16)

![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/3d21c7b2-cb84-4bc5-b301-e09a53e1e6ad)

![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/634f3f40-10d8-47c3-9038-257e7779e0e2)

![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/41d19e29-6ce9-4071-a85d-83f3903b7a82)

![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/089c94ec-bd8c-462d-9e98-93828ea7b476)

![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/6e900124-db2f-4f4e-970f-f9a4ff31124b)

![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/1134db73-f9ae-4164-b517-611f2b4372b3)

![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/258a4d30-acde-4bca-977a-1ef2e20c0a7d)

![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/39f77571-2b7b-4668-8a7d-d38a41e39df4)

![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/7c73ad86-50b6-41a5-806d-7795b17e942a)

</details>

-----

### Android App Screenshots

![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/2ba5fba7-8945-44b3-81c8-884a33437ac7)

<details>
<summary>More screenshots</summary>
  
![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/664c75ac-b7c2-4f7a-9c0f-497af4b99978)
![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/4ce96a36-f385-43fa-8870-d1d9a946d50c)
![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/2ba5fba7-8945-44b3-81c8-884a33437ac7)
![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/3c151d96-5c55-471d-9ede-6f50bdc64b58)
![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/c925923f-be56-45a3-8d9b-4d7d41fd59a2)
![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/1bd48cf9-b932-4dc4-a46b-59766c195d27)
![image](https://github.com/TwoPointerr/Project-Clean-Web-Application/assets/45624147/bdf6dac6-b1f5-4ae9-824d-97065cdf344b)
</details>
