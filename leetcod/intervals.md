+ [Non-overlapping Intervals](#non-overlapping-intervals)
+ [Merge Intervals](#merge-intervals)
+ [Insert Interval](#insert-interval)
<!-----solution----->

## Insert Interval

https://leetcode.com/problems/insert-interval/

```python
    if len(intervals) == 0:
.        
.        return newInterval#Я не могу понять, почему эта часть кода не работает.
.    
.    else:
.        
.        a = []
.        merged = []
.        
.        for interval in intervals:
.        
.            if interval[1] < newInterval[0] or interval[0] > newInterval[1] :
.            
.                a.append(interval)
.            
.            else:
.                
.                if not merged:
.                    
.                    merged.append(interval)
.                    merged[-1][1] = max(newInterval[1], interval[1])
.                    
.                else:
.                    
.                    merged[-1][1] = max(newInterval[1], interval[1])
.                
.        f = merged + a
.        f.sort(key = lambda x:x[1])
.        return f
```

## Merge Intervals

https://leetcode.com/problems/merge-intervals/

```python
    a = []
.    for interval in intervals:
.        
.        if not a or a[-1][1] < interval[0]:
.            a.append(interval)
.            
.        else:
.            
.            a[-1][1] = max(a[-1][1], interval[1])
.
.    return a
```

## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

```python
    if intervals == []:
.        
.        return '0'
.    
.    else:
.        
.          intervals.sort(key=lambda x: x[1])
.          count = 0
.          i = 0
.          j = 1
.
.    while i < len(intervals) and j < len(intervals): 
.        if intervals[i][1] <= intervals[j][0]:
.            
.            count += 1
.            i = j
.            j += 1
.        
.        else:
.            j += 1
.            
.    return count
```