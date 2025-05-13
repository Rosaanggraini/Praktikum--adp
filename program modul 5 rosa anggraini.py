nilai_x = [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]
f = []
print("| x   | f(x)       |")
print("|-----|------------|")
for x in nilai_x :
    if x > 0 :
        f.extend([x**3 - x])
    elif x < 0 :
        f.extend([round(1 /x**2, 4)])
    else:
        f.extend([1])
for i in range(len(nilai_x)):
    print(f'|{nilai_x[i]:4} | {f[i] : 10} |')


