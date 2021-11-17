def TatlongNumero():
    una = int(input("FIRST NUMBER:"))
    pangalawa = int(input("SECOND NUMBER:"))
    pangatlo = int(input("THIRD NUMBER:"))
    return una, pangalawa, pangatlo

def  ThreeNumbers(first,second,third):
    if first < second and first < third:
        result = first

    elif second < first and second > third:
        result = second  

    elif third< first and third < second:
         result = third
    
    return result 

first, second, third = TatlongNumero()
result = ThreeNumbers(first,second,third)
print(f'The lowest term of the 3 numbers {first}, {second}, {third} is {result}')


