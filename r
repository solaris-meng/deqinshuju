pkill uwsgi;
uwsgi -s 127.0.0.1:8528 -w deqinshuju.wsgi --daemonize /var/log/uwsgi.log
