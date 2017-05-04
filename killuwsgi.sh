#!/bin/bash
if [ $1 = start ];then
  psid=`ps aux|grep "uwsgi"|grep -v "grep"|wc -l`
  if [ $psid -gt 2 ];then
    echo "uwsgi is running!"
    exit 0
  else
    uwsgi -s /tmp/uwsgi.sock -w wsgi_handler -p 10 -M -t 120 -T -H
/home/uliweb/python -C -d /home/uliweb/project/logs/uwsgi.log
  fi
  echo "Start uwsgi service [OK]"
elif [ $1 = stop ];then
  killall -9 uwsgi
  echo "Stop uwsgi service [OK]"
elif [ $1 = restart ];then
  killall -9 uwsgi
  uwsgi -s /tmp/uwsgi.sock -w wsgi_handler -p 10 -M -t 120 -T -H
/home/uliweb/python -C -d /home/uliweb/project/logs/uwsgi.log
  echo "Restart uwsgi service [OK]"
else
  echo "Usages: sh start.sh [start|stop|restart]"
fi