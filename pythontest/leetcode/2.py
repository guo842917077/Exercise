# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""
leetcode 第二题两个数的和
思路 每个列表取一位进行相加
1。记得进位
2。最后计算后还有进位，记得保留
3。判断非空
"""

class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None



class Solution:
    def __init__(self):
       self.l1=ListNode(0)
       self.l2=ListNode(0)

    def save(self):
        a = [1, 2, 3]
        b = [4, 5, 6]
        t1=self.l1
        t2=self.l2
        for x in a:
            t1.val=x
            t1.next=ListNode(0)
            t1=t1.next
        for x in b:
            t2.val=x
            t2.next = ListNode(0)
            t2=t2.next


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 存储每次计算的进位
        carry = 0
        # x=l1,y=l2，resultNode最后的结果 用来存储链表
        resultNode = ListNode(0)
        p = l1
        q = l2
        curr = resultNode
        while p is not None and q is not None :
        # 取出当前的值赋值给临时变量
           x = p.val if (p.val != 0) else None
           y = q.val if (q.val != 0) else None
           # 每次计算带上进位
           if x is None or y is None:
               break
           sum = x + y + carry
           # 重新计算进位 除10后剩下的就是进位
           carry = sum / 10
           # 将结果赋值给节点，结果为除以10的余数
           curr.next = ListNode(int(sum % 10))
           # 取出当前链表的next，进行上述赋值操作
           curr = curr.next
           # 判断给定链表是否还有值
           if p.next is not None:
            p = p.next
           if q.next is not None:
            q = q.next
           if carry > 0:
            curr.next = ListNode(carry)
        return resultNode.next


sol = Solution()
sol.save()
result=sol.addTwoNumbers(sol.l1,sol.l2)
r1=result
while r1.next is not None:
    print(r1.val)
    r1=r1.next