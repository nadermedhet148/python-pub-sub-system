FROM python:3.6-stretch
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python", "./server.py" ]