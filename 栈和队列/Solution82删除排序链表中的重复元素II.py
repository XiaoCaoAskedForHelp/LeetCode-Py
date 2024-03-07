# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    # 双指针
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个新的头节点
        res = ListNode(1000)
        res.next = head
        pre = res
        while head:
            flag = False
            # 碰到前一个和后一个的重复的就跳过
            while head.next and head.val == head.next.val:
                head = head.next
                flag = True
            if flag:
                # 处理重叠的最后一个
                head = head.next
                pre.next = head
            else:
                pre = head
                head = head.next

        return res.next

    # 如果当前cur.next与cur.next.next对应的元素相同，那么我们就需要将cur.next以及所有后面拥有相同元素值的链表节点全部删除
    def deleteDuplicates1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


head = [1, 2, 3, 3, 4, 4, 5]
listNode = ListNode()
pre = listNode
for h in head:
    node = ListNode(h)
    pre.next = node
    pre = node
Solution().deleteDuplicates(listNode.next)
