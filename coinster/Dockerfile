FROM ubuntu


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y python3 python3-pip cron nano

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000