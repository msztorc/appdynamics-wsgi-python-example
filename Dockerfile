FROM python:3.6 

RUN mkdir /app
WORKDIR /app

COPY app/ /app
RUN pip install -r requirements.txt

EXPOSE 8080

CMD pyagent run -c appd.cfg -- python wsgisam.py