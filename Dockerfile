FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir app
WORKDIR app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN ["chmod", "+x", "/app/docker-entrypoint.sh"]
CMD '/app/docker-entrypoint.sh'