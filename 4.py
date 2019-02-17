def zero(st=10):
    if st==10:
        return 0 
    else:
        cont=0
        number=int(st[0])
        calculation=st[1]
        print(mathact(cont, calculation, number))
def one(st=10):
    if st==10:
        return 1
    else:
        cont=1
        number=int(st[0])
        calculation=st[1]
        print(mathact(cont, calculation, number))
def two(st=10):
    if st==10:
        return 2
    else:
        cont=2
        number=int(st[0])
        calculation=st[1]
        print(mathact(cont, calculation, number))
def three(st=10):
    if st==10:
        return 3
    else:
        cont=3
        number=int(st[0])
        calculation=st[1]
        print(mathact(cont, calculation, number))
def four(st=10):
    if st==10:
        return 4
    else:
        cont=4
        number=int(st[0])
        calculation=st[1]
        print(mathact(cont, calculation, number))
def five(st=10):
    if st==10:
        return 5
    else:
        cont=5
        number=int(st[0])
        calculation=st[1]
        print(mathact(cont, calculation, number))
def six(st=10):
    if st==10:
        return 6
    else:
        cont=6
        number=int(st[0])
        calculation=st[1]
        print(mathact(cont, calculation, number))
def seven(st=10):
    if st==10:
        return 7
    else:
        cont=7
        number=int(st[0])
        calculation=st[1]
        print(mathact(cont, calculation, number))
def eight(st=10):
    if st==10:
        return 8
    else:
        cont=8
        number=int(st[0])
        calculation=st[1]
        print(mathact(cont, calculation, number))
def nine(st=10):
    if st==10:
        return 9
    else:
        cont=9
        number=int(st[0])
        calculation=st[1]
        print(mathact(cont, calculation, number))
def times(st):
    st=str(st)+"*"
    return st
def minus(st):
    st=str(st)+"-"
    return st
def plus(st):
    st=str(st)+"+"
    return st
def mathact(cont, calculation, number):
    if calculation=="*":
        return number*cont
    elif calculation=="-":
        return cont-number
    elif calculation=="+":
        return number+cont
