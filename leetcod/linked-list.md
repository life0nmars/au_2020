
# Linked-List

+[Reverse Linked List](#reverse-linked-list)

##Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
 def reverseList(self, head: ListNode) -> ListNode:
        
        if head == None or head.next == None:
            
            return head
        
        else:
            prev = None
            while head != None:
                
                a = head.next
                head.next = prev
                prev = head
                head = a
        
            return prev
                
```
# Linked-List

+[Middle of the Linked List](#middle-of-the-linked-list)

##Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
 def middleNode(self, head: ListNode) -> ListNode:
        dict = {}
        
        i = 0
        while head:            
            dict[i] = head
            head = head.next 
            i += 1
            
        
        m = i // 2
        
        return dict[m]
        
        
```
# Linked-List

+[Palindrome Linked List](#palindrome-linked-list)

##Palindrome Linked List

 https://leetcode.com/problems/palindrome-linked-list/

```python
 def isPalindrome(self, head: ListNode) -> bool:
        a = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            a, a.next, slow = slow, a, slow.next
        if fast:
            slow = slow.next
        while a and a.val == slow.val:
            slow = slow.next
            a = a.next
        return not a
            
```
# Linked-List

+[Merge Two Sorted Lists](#merge-two-sorted-lists)

##Merge Two Sorted Lists

 https://leetcode.com/problems/merge-two-sorted-lists/

```python
 def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = cur = ListNode(0)
        while l1 and l2:
            cur.next = l1
            if l1.val < l2.val:
                l1 = l1.next
            else:
                tmp = l2.next
                cur.next = l2
                l2.next = l1
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return a.next 
```