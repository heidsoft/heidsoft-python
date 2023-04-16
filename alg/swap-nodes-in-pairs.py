# https://leetcode.com/problems/swap-nodes-in-pairs/description/
from typing import Optional


class LinkedList:
    """定义一个链表结构
    """

    def __init__(self):
        self.head = None

    def __repr__(self):
        """
        s1 = "-"
        s2 = ""
        seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
        print (s1.join( seq ))
        print (s2.join( seq ))
        r-u-n-o-o-b
        runoob
        Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
        """
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """返回对象的字符串表达形式，相对__str__更加贴近对象实际数据类型
        https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#section-8
        https://www.digitalocean.com/community/tutorials/python-str-repr-functions
        :return:
        返回该节点的值
        """
        return self.val


class Solution:
    """
    链表交换相邻元素
    """
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

mylist = LinkedList()
print(mylist)
# 定义链表节点
node1 = ListNode("a")
node2 = ListNode("b")
node3 = ListNode("c")
node4 = ListNode("d")
node1.next = node2
node2.next = node3
node3.next = node4
mylist.head = node1
print(mylist)
help = Solution()
new_swap_pairs_head = help.swapPairs(mylist.head)
new_swap_pairs_mylist = LinkedList()
new_swap_pairs_mylist.head = new_swap_pairs_head
print(new_swap_pairs_mylist)
# None
# a->b->c->d->None
# b->a->d->c->None