# Definition for singly-linked list.
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
    反转链表
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # cur 当前节点，prev上一个节点
        cur, prev = head, None
        while cur:
            # 反转逻辑
            # a->b->c   --->  c->b->a
            cur.next, prev, cur = prev, cur, cur.next
        return prev


mylist = LinkedList()
print(mylist)
# 定义链表节点
node1 = ListNode("a")
node2 = ListNode("b")
node3 = ListNode("c")
node1.next = node2
node2.next = node3
mylist.head = node1
print(mylist)
help = Solution()
new_mylist_head = help.reverseList(mylist.head)
# 定义新列表
new_mylist = LinkedList()
new_mylist.head = new_mylist_head
print(new_mylist)
