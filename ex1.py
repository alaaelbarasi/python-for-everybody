def count (numbers):
    count=0
    for number in numbers:
        count+=1
    return count
def total (numbers):
    total=0
    for number in numbers:
        total+=number
    return total
def average (count, total):
    avg=total/count
    return avg 
def print_n (count, total, avr):
    print("Count:"+str(count))
    print("total : "+str(total))
    print("Average : "+str(avr))
def math(numbers):
    c=int(count(numbers))
    t=int(total(numbers))
    avr=float(average(c,t))
    print_n(c,t,avr)
def inp ():
    numbers=[]
    while True:
        try:
         inp=input("> ")
         if inp =="Done":
             break 
         number=int(inp)
         numbers.append(number)
        except:
            print("numercal numbers only!!!")
            continue
    math(numbers)

inp()

