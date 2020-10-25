+ [Fizz Buzz](#fizz-buzz)
<!-----solution----->

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
def fizzBuzz(self, n: int) -> List[str]:
.    lst = []
.    for i in range(1, n + 1):
.        if i % 15 == 0:
.            i = 'FizzBuzz'
.        elif i % 5 == 0:
.            i = 'Buzz'
.        elif i % 3 == 0:
.            i = 'Fizz'
.        else: 
.            lst.append(str(i))
.            continue
.        lst.append(i)
.    return lst
```