FROM python:3.7-stretch

RUN mkdir app

COPY . /app

RUN pip install -r /app/requirements.txt

EXPOSE 8080

CMD ["python","/app/app/helloworld.py"]