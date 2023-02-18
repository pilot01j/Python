def add(*args):#*args semnifica ca met data poate primi mai multi argumenti
    print(args[0])#datele din args sunt un tuplu

    sum = 0
    for n in args:
        sum += n
    return sum
print(add(1, 2, 3, 4, 50))

def calculate(n, **kwargs):#kwaegs este un dictionar
    n += kwargs["add"]
    n *= kwargs["multipy"]
    print(n)
calculate(2, add=3, multipy=5)