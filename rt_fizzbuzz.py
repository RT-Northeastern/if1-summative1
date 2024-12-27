# defines our function rt_fizznumber where the fizz_number is either divisable by 6,2 or 3
def rt_fizznumber(fizz_number):

# if our fizz_number is divsable by 6 with 0 remainder it returns "Fizzbuzz"
    if (fizz_number) % 6 == 0:
        return ("Fizzbuzz")

 # if our fizz_number is divsable by 2 with 0 remainder it returns "Fizz"   
    elif (fizz_number) % 2 == 0: 
        return ("Fizz")
    
 # if our fizz_number is divsable by 3 with 0 remainder it returns "Buzz"   
    elif (fizz_number) % 3 == 0: 
        return ("Buzz") 
    
 # else return thr fizz_number in string format   
    else: 
        return str(fizz_number)