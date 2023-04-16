# -*- coding: utf-8 -*-
g = lambda x:x+1

print(g(1))

print(g(2))

# Python 中 数组套字典的排序(用lambda实现)

dict = [
    {'id':'4','name':'b'},
    {'id':'6','name':'c'},
    {'id':'3','name':'a'},
    {'id':'1','name':'g'},
    {'id':'8','name':'f'}
]

#排序后：[{'id': '1', 'name': 'g'}, {'id': '3', 'name': 'a'}, {'id': '4', 'name': 'b'}, {'id': '6', 'name': 'c'}, {'id': '8', 'name': 'f'}]

print(sorted(dict))

#遍历列表
# for d in dict:
# 	#循环字段
# 	for w in sorted(d, key=d.get):
# 		print w, d[w]
# 		print type(w)

a = [5,2,1,9,6]

sorted(a)
sorted(a,reverse=False)
# myKey = lambda d:d['id']
test = ('id',)
print(sorted(dict,key=lambda d:d['id'],reverse=True))


