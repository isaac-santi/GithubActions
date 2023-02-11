FROM python:3.9.16-alpine3.16

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . .

EXPOSE 80

WORKDIR /app

COPY app.sh .

RUN chmod +x app.sh
#ENTRYPOINT ["python", "IsaacFlask/src/app.py"]
CMD ["./app.sh"]
# cmd arrancar gunicorn
#CMD ["gunicorn"," --bind=0.0.0.0:5000 app:app"]
