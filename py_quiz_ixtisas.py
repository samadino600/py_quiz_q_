#1

"""
start_num = int ( input ( "Diapazonun baslangic qiymetini daxil edin: " ) )
end_num = int ( input ( "Diapazonun son qiymetini daxil edin: " ) )
perfect_number_count = 0
for num in range ( start_num , end_num ):
    sum_of_divisors , divisors = 0 , " "
    for divisor in range ( 1 , num ):
        if num % divisor == 0 :
            sum_of_divisors += divisor
            divisors += str(divisor) + " "
    if sum_of_divisors == num :
        print ( f"Perfect number found: {num}" )
        print ( f"Divisors: {divisors}" )
        perfect_number_count += 1
print ( f"Total number found: {perfect_number_count}" )
"""

#2

"""
number = int ( input ( "Enter a number (N>0): " ) )
step_count = 0
while number > 1 :
    num_01 , sum_of_digs  = number , 0
    while num_01 > 0 :
        dig = num_01 % 10
        num_01 //= 10
        sum_of_digs += dig
    if number % sum_of_digs == 0 :
        step_count += 1
        print ( f"Step {step_count} : {number} / {sum_of_digs} = {number // sum_of_digs}" )
        number = number // sum_of_digs
print ( f"Total chain length: {step_count}" )
"""

#3

"""
number = int ( input ( "Enter a number (N>0): " ) )
num_01 , one_count , max_dig = number , 0 ,0
while num_01 > 0 :
    dig = num_01 % 10
    num_01 //= 10
    if dig > max_dig :
        max_dig = dig
print ( f"Max digit: {max_dig}" )
while number > 0 :
    binary_dig = number % 2
    number //= 2
    if binary_dig == 1:
        one_count += 1
print ( f"Binary ones count: {one_count}" )
if one_count == max_dig :
    print ( f"Result: True. It is a Dominant Trip number." )
else :
    print ( f"Result: False. It is not a Dominant Trip number." )
"""

#4

"""
number = int(input("Enter a number (N>0): "))
num_01 , num_02 = number , number
num_rotated = 0
one_count = 0
sum_of_divisors = 0
digits = len(str(number))
first = number // (10 ** (digits - 1))
rest = number % (10 ** (digits - 1))
num_rotated = rest * 10 + first
while num_02 > 0:
    binary_dig = num_02 % 2
    num_02 //= 2
    if binary_dig == 1:
        one_count += 1
if one_count == 0:
    one_count = 0
elif one_count % 2 == 0:
    one_count = 2
else:
    one_count = 1
lamp = 1
for divisor in range(2, number):
    if number % divisor == 0:
        lamp = 0
        break
lamp_rot = 1
for divisor in range(2, num_rotated):
    if num_rotated % divisor == 0:
        lamp_rot = 0
        break
print(f"Original: {number}")
print(f"Rotated: {num_rotated}")
print(f"Binary Weight Type: {one_count}")
if lamp == 1 and lamp_rot == 1:
    print("Result: Category A")
elif lamp == 0 and one_count == 2:
    print("Result: Category B (Composite with Even Binary Weight)")
else:
    for divisor_0 in range(1, number):
        if number % divisor_0 == 0:
            sum_of_divisors += divisor_0
    if sum_of_divisors == number:
        print("Result: Category C")
    else:
        print("Heç bir xüsusiyyət tapılmadı")

"""

#5

"""
def get_factorial_sum(number):
    factorial_sum = 0
    temp_number = number
    while temp_number > 0:
        digit = temp_number % 10
        temp_number //= 10
        factorial = 1
        for i in range(1, digit + 1):
            factorial *= i
        factorial_sum += factorial
    return factorial_sum 
def is_happy(number):
    seen_numbers = set()
    while number != 1 and number not in seen_numbers:
        seen_numbers.add(number)
        next_number = 0
        temp_number = number
        while temp_number > 0:
            digit = temp_number % 10
            temp_number //= 10
            next_number += digit ** 2
        number = next_number
    return number == 1
n = int(input("N natural ədədini daxil edin: "))
factorial_sum_result = get_factorial_sum(n)
happy_status = is_happy(factorial_sum_result)
print(f"Faktoriyal Cəmi (int): {factorial_sum_result}")
print(f"Xoşbəxtdirmi? (bool): {happy_status}")
"""






































    
