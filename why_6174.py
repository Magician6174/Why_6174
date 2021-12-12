"""
SOURCE: https://en.wikipedia.org/wiki/6174_(number)

6174 is known as Kaprekar's constant after the Indian mathematician D. R. Kaprekar.
   
   1. Take any four-digit number, using at least two different digits (leading zeros are allowed).
   2. Arrange the digits in descending and then in ascending order to get two four-digit numbers,
      adding leading zeros if necessary.
   3. Subtract the smaller number from the bigger number.
   4. Go back to step 2 and repeat.
The above process, known as Kaprekar's routine, will always reach its fixed point, 6174, 
in at most 7 iterations.Once 6174 is reached, the process will continue yielding 7641 - 1467 = 6174.

Other Interesting Properties of 6174:

1. 6174 is a Harshad number, since it is divisible by the sum of its digits.
2. 6174 is a 7-smooth number, i.e. none of its prime factors are greater than 7.
3. 6174 can be written as the sum of the first three degrees of 18:

    18^3 + 18^2 + 18^1 = 5832 + 324 + 18 = 6174.
4. The sum of squares of the prime factors of 6174 is a square:

    2^2 + 3^2 + 3^2 + 7^2 + 7^2 + 7^2 = 4 + 9 + 9 + 49 + 49 + 49 = 169 = 13^2
"""

def list_to_num(l):
    """
    Concatenate list of numbers & returns the number.
    """
    s=''
    for i in range(len(l)):
        s+=l[i]
    return int(s)

def check_num(number_):
    """
    Checks if the number is valid or not if valid then returns the number.
    """
    try:
        if number_ == 'Q':
                exit()
        int(number_)
        if len(number_) > 4 or len(number_) < 4:
            print("Please check length of digits you entered: ")
            number = input()
            number = check_num(number)
            return number  
        else:
            return number_
    except ValueError:
        print("Please Enter Correct four digit number but not all same:")
        print("or To exit press Q")
        number_ = input()
        number = check_num(number_)
        return number

if __name__ == "__main__":
    print("Enter four digit number but not all same:")
    number = input()
    number = check_num(number)

    while True:
        num = [n for n in number]
        ascending_sort = sorted(num)
        descending_sort = sorted(num,reverse=True)
        large_num = list_to_num(descending_sort) # number arranged in descending order
        small_num = list_to_num(ascending_sort) # number arranged in ascending order
        if large_num == small_num:
            print("Please Enter a valid 4 digit number, not all digits same:")
            print("Or To get a list of all invalid numbers run <python show_incorrect_number.py> in seprate terminal...")
            number = input()
            number = check_num(number)
            continue

        difference = large_num - small_num
        print("Taking the difference of sorted digits...")
        print(f"{large_num} - {small_num} = {difference}")
        number = str(difference)
        if difference == 6174:
            print("The series always converges to 6174!!")
            print("Hence 6174! Have a nice day!! ;)")
            print("--------------------")
            print("To exit press Q")
            print("Or Try a new Number")
            number = input()
            number = check_num(number)

        

