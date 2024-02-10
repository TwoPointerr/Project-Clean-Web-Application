FROM python:3.9.13

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN apt-get update && apt-get install -y gnupg2 curl

# Import the Microsoft GPG key
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Add the Microsoft SQL Server package repository
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Install ODBC Driver
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Install additional dependencies
RUN apt-get install -y unixodbc unixodbc-dev

RUN pip install -r requirements.txt

COPY . /code

WORKDIR /code

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh","/entrypoint.sh" ]