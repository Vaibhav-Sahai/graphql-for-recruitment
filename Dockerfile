FROM python:3.7

WORKDIR /graphql-recruitment-api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./applicant ./applicant

CMD ["python", "applicant/main.py"]