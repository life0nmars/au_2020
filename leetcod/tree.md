+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Symmetric Tree](#symmetric-tree)
+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Invert Binary Tree](#invert-binary-tree)
+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
+ [Binary Search Tree Iterator](#binary-search-tree-iterator)
<!-----solution----->

## Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/

```python

def __init__(self, root: TreeNode):
    self.root = root
    self.sorted_roots = []
    self.index = -1    
    def traversal(self,root):
        if root:
            traversal(self,root.left)
            self.sorted_roots.append(root.val)
            traversal(self,root.right)
    traversal(self,root)      


def next(self) -> int:
    self.index += 1
    return self.sorted_roots[self.index]
    

def hasNext(self) -> bool:
    if self.index+1 < len(self.sorted_roots):
        return True
    return False
```

## Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

```python
def kthSmallest(self, root: TreeNode, k: int) -> int:
    res = []
    self.traverse(root, res)
    return res[k - 1]
    
def traverse(self, node, order):
    if node is None:
        return
    self.traverse(node.left, order)
    order.append(node.val)
    self.traverse(node.right, order)
```

## Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/

```python
def invertTree(self, root):
    return self.invert(root)
def invert(self, node):
    if node is None:
        return
    node.left, node.right = node.right, node.left
    self.invert(node.left)
    self.invert(node.right)
    return node
```

## Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

```python
def maxDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    leftN = self.maxDepth(root.left)
    rightN = self.maxDepth(root.right)
    return max(leftN, rightN) + 1
```

## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

```python
def inorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    self.traverse(root, res)
    return res
 def traverse(self, node, order):
    if node is None:
        return
    self.traverse(node.left, order)
    order.append(node.val)
    self.traverse(node.right, order)
```

## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

```python
    return self.valid(root, float('-inf'), float('inf'))
def valid(self, node, left, right):
    if not node: return True
    if left >= node.val or node.val >= right:
        return False
    else:
        return (self.valid(node.left, left, node.val) and self.valid(node.right, node.val, right))
```

## Symmetric Tree

https://leetcode.com/problems/symmetric-tree/

```python
def isSymmetric(self, root: TreeNode) -> bool:
    if root == None:
        return True
    def change(node):
        if node == None:
            return node
        elif node.left == None and node.right == None:
            return node
        else:
            tmp = node.right
            node.right = node.left
            node.left = tmp
            change(node.left)
            change(node.right)
    change(root.right)
    def identicalTrees(l, r): 
        if l is None and r is None: 
            return True 
        if l is not None and r is not None: 
            return ((l.val == r.val) and 
            identicalTrees(l.left, r.left)and
            identicalTrees(l.right, r.right)) 
        return False
    return identicalTrees(root.left, root.right)
```

## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

```python
    #def isValidBST(self, root: TreeNode) -> bool:
    #res = []
    #self.traverse(root, res)
    #if res == sorted(res):
        #return True
    #else:
        #return False
#def traverse(self, node, order):
    #if node is None:
        #return
    #self.traverse(node.left, order)
    #order.append(node.val)
    #self.traverse(node.right, order)
def isValidBST(self, root: TreeNode) -> bool:
    return self.valid(root, float('-inf'), float('inf'))
def valid(self, node, left, right):
    if not node: return True
    if left >= node.val or node.val >= right:
        return False
    else:
        return (self.valid(node.left, left, node.val) and self.valid(node.right, node.val, right))
```