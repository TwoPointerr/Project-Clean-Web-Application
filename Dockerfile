FROM python:3.9.13

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /code

WORKDIR /code

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh","/entrypoint.sh" ]