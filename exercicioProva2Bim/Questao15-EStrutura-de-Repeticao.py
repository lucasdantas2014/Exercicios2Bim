n=eval(input("Digite até que valor será a série de Fibonacci:"))
if(n >= 0):
    a = True
    x = 0
    y = 1
    while (a==True):
        if(n==0):
            print(x)
        elif(n > 0):
            print(x)
            print(y)
            x = x + y
            y = x + y
        if (x > n or y > n):
            a = False
        else:
             a = True
else:
    print("O valor não pode ser negativo")

