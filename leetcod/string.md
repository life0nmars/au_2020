+ [Valid Anagram](#valid-anagram)
+ [Reverse String](#reverse-string)
+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)
+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)
+ [To Lower Case](#to-lower-case)
<!-----solution----->

## To Lower Case

https://leetcode.com/problems/to-lower-case/

```python
def toLowerCase(self, str: str) -> str:
.    return "".join([chr(ord(i)+32) if ord(i)<92 and ord(i)>64 else i for i in str])
```

## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
def reverseWords(self, s: str) -> str:
.    s_1 = []
.    a = []
.    s_1 = s.split()
.    for i in s_1:
.        reversed_str = i[::-1]
.        a.append(reversed_str)
.    return ' '.join(a)
```

## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
def reverseVowels(self, s: str) -> str:
.    vowels = []
.    result = ''
.    for i in s:
.        if i in "aeiouAEIOU":
.            vowels.append(i)
.    for i in s:
.        if i in "aeiouAEIOU":
.            result += vowels.pop()
.        else:
.            result += i
.    return result
```

## Reverse String

https://leetcode.com/problems/reverse-string/

```python
def reverseString(self, s: List[str]) -> None:
.    """
.    Do not return anything, modify s in-place instead.
.    """
.    i = 0
.    j = len(s) - 1
.    while i < j:
.        s[i], s[j] = s[j], s[i]
.        i += 1
.        j -= 1
.    return s
```

## Valid Anagram

https://leetcode.com/problems/valid-anagram/

```python
def isAnagram(self, s: str, t: str) -> bool:
.    return sorted(s) == sorted(t)
```