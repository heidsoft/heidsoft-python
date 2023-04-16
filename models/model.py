# -*- coding: utf-8 -*-
"""
导入工具模块
"""
import gevent

if __name__=='__main__':

	def f(n):
		for i in range(n):
			print(gevent.getcurrent(), i)
		g1 = gevent.spawn(f, 5)
		g2 = gevent.spawn(f, 5)
		g3 = gevent.spawn(f, 5)
		g1.join()
		g2.join()
		g3.join()