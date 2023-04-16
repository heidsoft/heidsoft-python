import asyncio
import time

from sanic import Sanic
from sanic.response import json

app = Sanic()

iid = 1
async def next_id():
    global iid
    res = iid
    iid += 1
    return res

@app.route('/')
async def test(request):
    size = app.queue.qsize()
    print("app size "+str(size));
    res = await next_id()
    await app.queue.put("请求第"+str(res)+"次   " + time.ctime())
    return json({'hello': 'world'})


async def task_func(info):
    print('in task_func '+str(info))
    return 'the result'


async def work(queue):
    while True:
        print("loop queue start ");
        info = await queue.get()
        size = queue.qsize()
        print("info "+str(info)+" size: "+str(size))
        await asyncio.sleep(1)

@app.listener('before_server_start')
async def setup_db(app, loop):
    print("setup_db....")
    queue = asyncio.Queue(maxsize=1000)
    app.queue = queue
    app.add_task(work(queue))

@app.listener('after_server_start')
async def notify_server_started(app, loop):
    print("notify_server_started");
    # app.add_task(loop.create_task(work(app.queue)))

@app.listener('before_server_stop')
async def notify_server_stopping(app, loop):
    print('Server shutting down!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,return_asyncio_server=True)