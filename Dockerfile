FROM python:3.9-buster

# install nginx
RUN apt-get update && apt-get install -y nginx
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

# install gettext
RUN apt-get update && apt-get install -y gettext

# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
#RUN mkdir -p /opt/app/DaniMundo
COPY requirements.txt start_server.sh /opt/app/
#COPY .pip_cache /opt/app/pip_cache/
ADD DaniMundo/ /opt/app/
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app

# start server
RUN chmod 755 /opt/app/start_server.sh
EXPOSE 80
STOPSIGNAL SIGTERM
#CMD ["/opt/app/start_server.sh"]
CMD /bin/bash
