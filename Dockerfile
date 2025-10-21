FROM python:3.13-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir -p /i8o8i-wakatime-stats/assets

ADD requirements.txt /i8o8i-wakatime-stats/requirements.txt
RUN apk add --no-cache g++ jpeg-dev zlib-dev libjpeg make git && pip3 install -r /i8o8i-wakatime-stats/requirements.txt

RUN git config --global user.name "Readme-Bot"
RUN git config --global user.email "i8o8iworkstation@outlook.com"

ADD Sources/* /i8o8i-wakatime-stats/
ENTRYPOINT cd /i8o8i-wakatime-stats/ && python3 Main.py