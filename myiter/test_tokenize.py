# -*- coding: utf8 -*-
#!/usr/bin/python

import tokenize

"""
遍历文件每一行
"""
if __name__=="__main__":
   reader = open("test_iter.py").next
   tokens = tokenize.generate_tokens(reader)
   print tokens.next()
   print tokens.next()
   print tokens.next()
   print tokens.next()
   print tokens.next()

