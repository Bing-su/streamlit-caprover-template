FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

ENV PORT 80

RUN sh setup.sh

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]