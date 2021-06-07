FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 80

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]