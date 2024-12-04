n=int(input("Enter number"))
if n %2:
    print("odd")
else:
    print("even")



for i in range (50):
    print(i)


numbers = [3, 7, 12, 25, 8, 15]
for num in numbers:
    if num > 10:
        print(num)



c=[1,2,3,4,5,6,7,8,9,10]
print(c[0]-c[9])
print(c[0]+c[9])
print(c[0]*c[9])


h=int(input("enter your number (0-4)"))
g=["Andria","mate","luka","Danieli","viqtoria"]
if h == 0:
    print(g[0])
elif h == 1:
    print(g[1])
elif h == 2:
    print(g[2])
elif h == 3:
    print(g[3])
elif h == 4:
    print(g[4])
else:
    print("wrong index")