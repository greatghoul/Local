#!/bin/bash

sockfile=/tmp/uwsgi-local.sock
projectdir=/home/greatghoul/Projects/Local
logfile=/var/log/uwsgi-local.log
key=Local

case "$1" in
    start)
        psid=`ps aux|grep "uwsgi"|grep $key|grep -v "grep"|wc -l`
        if [ $psid -gt 2 ];then
            echo "uwsgi is running!"
            exit 0
        else
            uwsgi -s $sockfile --chdir $projectdir -w wsgi_handler:application -p 10 -M -t 120 -T -C -d $logfile
        fi
        echo "Start uwsgi service [OK]"
        ;;

    stop)
        ps -ef|grep uwsgi|grep $key|grep -v grep|awk '{kill -9 $2}'
        echo "Stop uwsgi service [OK]"
        ;;

    restart)
        ps -ef|grep uwsgi|grep $key|grep -v grep|awk '{kill -9 $2}'
        uwsgi -s $sockfile --chdir $projectdir -w wsgi_handler:application -p 10 -M -t 120 -T -C -d $logfile
        echo "Restart uwsgi service [OK]"
        ;;

    *)
        echo "Usages: sh start.sh [start|stop|restart]"
        ;;
esac
