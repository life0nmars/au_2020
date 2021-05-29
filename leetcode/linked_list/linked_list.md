+ [Merge k Sorted Lists](#merge-k-sorted-lists)
<!-----solution----->

## Merge k Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists/

```python
ass ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next
s Solution:
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    self.arr = []
    for lst in lists:
        while lst:
            self.arr.append(lst.val)
            lst = lst.next
    head = node = ListNode(0)
    for elem in sorted(self.arr):
        node.next = ListNode(elem)
        node = node.next
    return head.next
     
```
