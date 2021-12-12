"""
The below code prints all the invalid numbers in range [1000,9999].
"""

def list_to_num(l):
    """
    Concatenate list of numbers & returns the number.
    """
    s=''
    for i in range(len(l)):
        s+=l[i]
    return int(s)

for i in range(1000  ,10000):
    number = str(i)

    while True:
        
        num = [n for n in number]
        ascending_sort = sorted(num)
        descending_sort = sorted(num,reverse=True)
        large_num = list_to_num(descending_sort)
        small_num = list_to_num(ascending_sort)
        
        if large_num == small_num:
            print("Not a valid Number: ",i)
            break   
        
        difference = large_num - small_num
        number = str(difference).zfill(4) # padding with zeros to make 4 digit number
        
        if difference == 6174:
            break
        