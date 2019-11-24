def fibonacci(n):
    series = [0, 1]
    for i in range(n):
        series.append(series[-1] + series[-2])
    
    s = [str(num) for num in series]
    print(s)
    
    n = []
    for num in s:
        for digit in num:
            n.append(digit)
    return n

