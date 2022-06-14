# pull official base image
FROM python:3.8.3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup app
RUN useradd -m -g app app -p PASWORD
RUN usermod -aG app app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME



# install dependencies
RUN apt-get update && apt-get install -y netcat

# copy entrypoint.prod.sh
COPY ./entrypoint.sh .
RUN chmod +x  $APP_HOME/entrypoint.sh

# copy project
COPY . $APP_HOME

COPY ./requirements.txt $APP_HOME
RUN pip install --upgrade pip
RUN pip install -r /home/app/web/requirements.txt
RUN pip install psycopg2-binary

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.prod.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]