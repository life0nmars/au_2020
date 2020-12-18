+ [Fizz Buzz](#fizz-buzz)
+ [Sqrt(x)](#sqrtx)
+ [Fibonacci Number](#fibonacci-number)
+ [Reverse Integer](#reverse-integer)
+ [Palindrome Number](#palindrome-number)
+ [Base 7](#base-7)
+ [Largest Perimeter Triangle](#largest-perimeter-triangle)
<!-----solution----->

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

```python
def largestPerimeter(self, A: List[int]) -> int:
    A.sort()
    for i in range(len(A) - 3, -1, -1):
        if A[i] + A[i+1] > A[i+2]:
            return A[i] + A[i+1] + A[i+2]
    return 0
```

## Base 7

https://leetcode.com/problems/base-7/

```python
def convertToBase7(self, num: int) -> str:
    if num < 0:
        num = num * (-1)
        res = self.forPositive(num)
        res = res * (-1)
    else:
        res = self.forPositive(num)
    return str(res)
def forPositive(self, num):
    nums = []
    i = 0
    sum = 0
    while num != 0:
        res = num % 7
        num = num // 7
        nums.append(res)
    for elem in nums:
        sum = sum + elem*10**i
        i += 1
    return sum
```

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
def isPalindrome(self, x: int) -> bool:
    res = 0
    y = abs(x)
    while y != 0:
        last = y % 10
        a = res * 10 + last
        res = a
        y = y // 10
    if x < 0:
        return False
    else:
        if x == res:
            return True
        else:
            return False
```

## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
def reverse(self, x: int) -> int:
    res = 0
    y = abs(x)
    while y != 0:
        last = y % 10
        a = res * 10 + last
        res = a
        y = y // 10
    if x < 0:
        res = - res
    return res
```

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

```python
def fib(self, N: int) -> int:
    c = 0
    cur = 1
    prev = 0
    if N > 1:
        while c < N - 1:
            new = cur + prev
            prev = cur
            cur = new 
            c += 1
        return new
    elif N == 1:
        return cur
    elif N == 0:
        return prev
    else:
        return False
```

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

```python
def mySqrt(self, x: int) -> int:
    r = x
    while r*r > x:
        r = (r + x/r) / 2
    return int (r)
```

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
def fizzBuzz(self, n: int) -> List[str]:
    lst = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            i = 'FizzBuzz'
        elif i % 5 == 0:
            i = 'Buzz'
        elif i % 3 == 0:
            i = 'Fizz'
        else: 
            lst.append(str(i))
            continue
        lst.append(i)
    return lst
```
