def fibonacci(n):
    a,b = 0,1
    fib = []
    while a< n:
        fib.append(a)
        a,b = b, a+b
    return fib

def classer(classeur, nombre):
    if nombre >0:
        classeur['positif'].append(nombre)
    else:
        classeur['negatif'].append(nombre)

    return classeur