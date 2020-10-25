+ [Max Consecutive Ones](#max-consecutive-ones)
+ [Reshape the Matrix](#reshape-the-matrix)
+ [Flipping an Image](#flipping-an-image)
+ [Squares of a Sorted Array](#squares-of-a-sorted-array)
<!-----solution----->

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

```python
def sortedSquares(self, A: List[int]) -> List[int]:
.    squares = []
.    for i in A:
.        c = i * i
.        squares.append(c)
.    squares.sort()
.    return squares
```

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

```python
def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
.    B = []
.    for i in A:
.        i.reverse()
.        B.append(i)
.    for j in B:
.        i = 0
.        while i < len(j):
.            if j[i] == 1:
.                j[i] = 0
.            else:
.                j[i] = 1
.                  
.            i += 1
.    return B
.        
```

## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/

```python
def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
.    if len(nums) * len(nums[0]) != r * c:
.        return nums
.    else:
.        lst = []
.        a = []
.        new = []
.        for n in nums:
.            new.append(n[0])
.            new.append(n[1])
.        for i in range (0, len(new), c):
.            a = new[i:i+c]
.            lst.append(a)
.        return lst
```

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

```python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
.    c = 0
.    lst = []
.    for i in nums:
.        if i == 1:
.            c += 1
.        else:
.            lst.append(c)
.            c = 0
.    return max(lst)
```