# The price of electricity
# 0-100 units:  $3
#101-200 units: $5
#201-300 units: $6.5
#301-500 units: $8
# 501+ units. : $10
units = float(input("Enter the units consumed: "))
if 100>units:
    cost = units*3
elif 200>units:
    cost = (3 * 100) + (units-100)*5
elif 300>units:
    cost = (3 * 100)+ (100*5) + (units-200)*6.5
elif 500>=units:
    cost = (3 * 100)+ (100*5)+ (100 * 6.5) + (units-300)*8
elif units>500:
    cost = (3 * 100)+ (100*5)+ (100 * 6.5) + (200 * 8) + (units-500)*10
print("$", cost)