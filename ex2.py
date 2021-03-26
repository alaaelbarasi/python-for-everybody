def x(numbers):
    x=None
    for number in numbers:
        if x== None or x<number:
            x=number
    return x
def min(numbers):
    min=None
    for number in numbers:
        if min== None or min>number:
            min=number
    return min
def inp():
    numbers=[]
    while True:
        number=input(">")
        if number == "done":
         break
        try:
            number=int(number)
            numbers.append(number)
        except:
            print("numrcal value only")
            continue
    
    print("min: "+str(min(numbers)))
    print("max: "+str(x(numbers)))
inp()

