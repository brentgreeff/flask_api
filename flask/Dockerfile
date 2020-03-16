FROM python:3.7.7-stretch

LABEL maintainer="email@brentgreeff.com"

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["uwsgi", "app.ini"]
# CMD ["strace", "-f", "uwsgi", "--ini", "app.ini"]
