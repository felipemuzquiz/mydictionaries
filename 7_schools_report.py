"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $60,000



"""

import json

with open('school_data.json', 'r') as outfile:
    schools = json.load(outfile)

NCAA_NAIA = [372, 108, 107, 130]

print("Schools that are part of the ACC, Big 12, Big Ten and SEC divisons")
print()
for school in schools:
    name = school.get("instnm", "Unknown School")
    
    ncaa_info = school.get("NCAA", {})
    
    conf_id = ncaa_info.get("NAIA conference number football (IC2020)", 0)
    
    if conf_id in NCAA_NAIA:
        print(name)
        print()

input()
print()
print()


print("Universities that have a graduation rate for Women over 75%")
print()
for school in schools:
    name = school.get("instnm", "Unknown School")
    
    grad_rate = school.get("Graduation rate  women (DRVGR2020)")
    
    if grad_rate is not None and grad_rate > 75:
        print(f"{name}\n Graduation rate for women: {grad_rate}%")
        print()

input() 
print()
print()


print("Universities that have a total price for in-state students living off campus over $60,000")
print()
for school in schools:
    name = school.get("instnm", "Unknown School")
    
    price = school.get("Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)")
    
    if price is not None and price > 60000:
        print(f"{name}\n Total Price for in-state students living off campus: ${price:,}")
        print()

        