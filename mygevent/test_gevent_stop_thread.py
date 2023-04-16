# -*- coding: utf8 -*-
import gevent
import signal
import datetime


def run_forever():
    print "当前时间 %s" % datetime.datetime.now()

if __name__ == '__main__':
    print "启动线程"
    thread = gevent.spawn(run_forever)
    thread.join()