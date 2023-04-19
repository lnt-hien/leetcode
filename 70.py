# Fibonacci
def climbStairs(self, n: int) -> int:
    if n <= 2:
        return n
    
    x, y = 1, 2
    for i in range(2, n):
        x, y = y, x +  y

    return y