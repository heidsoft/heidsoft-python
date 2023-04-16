#!/usr/bin/python
# -*- coding:utf8 -*-

import asyncio

def hello_world(loop):
    print('Hello World')
    loop.stop()


if (__name__=='__main__'):
	loop = asyncio.get_event_loop()
	loop.call_soon(hello_world, loop)
	loop.run_forever()
	loop.close()



