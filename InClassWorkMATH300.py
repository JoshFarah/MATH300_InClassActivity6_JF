#Grade Calculator
score = 83

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")    
elif score >= 70:
    print("Grade: C") 
elif score >= 60:
    print("Grade: D") 
else:
    print("Grade: F") 

#Check prime number  
number = 6217
if number <= 1:
    print("Number isn't prime")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("Prime")
    else:
        print("Number isn't prime")

#Check leap year
year = 2018
if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Non Leap-year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Non Leap-year")