# -*- coding: utf8 -*-
#!/usr/bin/python
__author__ = 'hadoop'

seq = ["one","two","three"]

print(seq)

if __name__=='__main__':
    """
    列表推导
    """
    for i,element in enumerate(seq):
        seq[i] = '%d: %s' % (i, seq[i])

    print(seq)

    def _treatment(pos,element):
        return '%d: %s' % (pos,element)

    [_treatment(i,el) for i,el in enumerate(seq)]