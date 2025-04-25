FROM python:3.10-alpine3.21

WORKDIR /note-taking

COPY requirements.txt   requirements.txt  

RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python", "app.py"]