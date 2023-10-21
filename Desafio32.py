
list = list(range(1,7))
res = []

quad = lambda x: x**2

for i in list:
    res.append(quad(i))
    
print(res)