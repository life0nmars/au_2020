+ [K Closest Points to Origin](#k-closest-points-to-origin)
<!-----solution----->

## K Closest Points to Origin

https://leetcode.com/problems/k-closest-points-to-origin/

```python
def kClosest(self, points, k):
    return sorted(points, key=lambda(x,y): ((x**2)+ (y**2))**0.5)[:k]
```
