# -*- coding: utf8 -*-

from celery import Celery

#amqp://guest@localhost//
app = Celery('hello', broker='redis://127.0.0.1:6379/0')



@app.task
def hello():
    return 'hello world'

# if __name__=='__main__':
#     print "执行hello 任务"
#     hello