#1
"""
import math
x = int ( input ( "x'i daxil edin: " ) )
y = int ( input ( "y'i daxil edin: " ) )
if y >= -3 and x >= -5 and y >= 2*x - 3 and y <= math.sin ( x ) and x**2 + y**2 <= 30 :
    print ( "daxildir" )
elif y <= 2*x - 3 and y >= math.sin ( x ) and x**2 + y**2 <= 30 :
    print ( "daxildir" )
else:
    print( "daxil deyil" )
"""

#2
"""
num_count = int ( input ( "Nece eded daxil edeceksiniz? " ) )
sum_of_prime_numbers = 0
for i in range ( 1, num_count + 1) :
    num = int ( input ( f"{i}-ci ededi daxil edin: " ) )
    lamp = 0
    for n in range ( 2, num ) :
        if num % n == 0:
            lamp = 1
    if lamp == 1 :
        print ( f"({num} sade deyil! Proses dayandirilir.)" )
        break
    else:
        print ( f"({num} sadedir, ceme elave olundu.)" )
        sum_of_prime_numbers += num
print ( f"Yekun cem: {sum_of_prime_numbers}" )
"""

#3

"""
num = int ( input ( "Analiz ucun ede daxil edin: " ) )
step_count = 1
while num >= 10 :
    num_02, sum_of_digs = num, 0
    while num > 0 :
        dig = num % 10
        num //= 10
        sum_of_digs += dig
    print ( f"Addim {step_count}: {num_02} reqemleri cemi = {sum_of_digs}" )
    step_count, num = step_count + 1, sum_of_digs
print ( f"Yekun Redem Koku: {sum_of_digs}" )
print ( f"Addim sayi: {step_count-1}" )
"""

#4

"""
start_num = int ( input ( "Diapazonun baslangic qiymetini daxil edin: " ) )
end_num = int ( input ( "Diapazonun son qiymetini daxil edin: " ) )
armstrong_count = 0
for num in range ( start_num , end_num + 1 ):
    num_01 , num_02 , sum_of_cube_nums , dig_count = num , num , 0 , 0
    while num_01 > 0 :
        dig = num_01 % 10
        num_01 //= 10
        dig_count += 1
    while num_02 > 0 :
        dig = num_02 % 10
        num_02 //= 10
        sum_of_cube_nums += dig ** dig_count
    if sum_of_cube_nums == num :
        print ( f"Tapildi: {num} (Reqem saysi: {dig_count})" )
        armstrong_count += 1
print ( f"Cemi {armstrong_count} eded tapildi." )
"""

#5

"""
num_decimal = int ( input ( "Analiz ucun eded daxil edin: " ) )
binary_analysis , octal_analysis , one_count , dig_count = num_decimal , num_decimal ,0 ,0
while binary_analysis > 0 :
    number = binary_analysis % 2
    binary_analysis //= 2
    if number == 0 :
        one_count += 1
while octal_analysis > 0 :
    num = octal_analysis % 8
    octal_analysis //= 8
    dig_count += num
print ( f"Daxil edilen eded (Onluq): {num_decimal}" )
print ( f"Sekkizlik reqemlerin cemi: {dig_count}" )
print ( f"Ikilik '1'-lerin sayi: {one_count}" )
if one_count == dig_count:
    print ( f"Netice: True (Eded BALANSLIDIR)" )
"""
