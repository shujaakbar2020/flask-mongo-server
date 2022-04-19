# Test gunicorn

$ gunicorn app:app -b localhost:8000 &

# Setup Supervisor
Create a supervisor file in /etc/supervisor/conf.d/ and configure it according to your requirements.

[program:tracking_server]
directory=/home/ubuntu/tracking_server
command=/home/ubuntu/.env/bin/gunicorn app:api -b localhost:8000
autostart=true
autorestart=true
stderr_logfile=/var/log/tracking_server/tracking_server.err.log
stdout_logfile=/var/log/tracking_server/tracking_server.out.log

$ sudo supervisorctl reread
$ sudo service supervisor restart
$ sudo supervisorctl status


# Setup NGINX

Let’s define a server block for our flask app.

$ sudo vim /etc/nginx/conf.d/virtual.conf

server {
    listen       80;
    server_name  your_public_dnsname_here;

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}

$ sudo nginx -t
$ sudo service nginx restart

