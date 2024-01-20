#Calculates the tax of monetary gifts in Holland

value = int(input("Value of gift:"))
if value < 5000: 
    tax = 0
if value >= 5000 <= 25000:
    extra = (value - 5000)
    tax = 100 + (extra * .08)
if value >= 25000 <= 55000:
    extra = (value - 25000)
    tax = 1700 + (extra * .10)
if value >= 55000 <= 200000:
    extra = (value - 55000)
    tax = 4700 + (extra * .12)
if value >= 200000 <= 1000000:
    extra = (value -200000 )
    tax = 22100 + (extra * .15)
if value >= 1000000:
    extra = (value - 1000000 )
    tax = 142100 + (extra * .17)
if tax > 0:
    print("Amount of tax:", tax)
else:
    print("No tax!")

#My solution. Honestly I think it's not too shabby