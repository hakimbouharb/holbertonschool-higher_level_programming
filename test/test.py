#!/usr/bin/python3
print("========================")
print("    $ DOCTOR WISE $")
print("========================")
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs.append((x,y))
            print(combs)

"""
cars = ['bmw', 'mercedes','volvo']
price = [200,250,300]
#cars.extend(price)
print(cars)
cars.extend(['nissan','porche'])
print(cars)
print("=====================================")
cars.append('polo')
print(cars)
print("=========================================")
phones = ['apple','saamsung','huawei']
phones.insert(0,'xiaomi')
print(phones)
"""
"""
name = 'hakim'
details ="i am {} and in november i will become {}. ".format(name,age)
print(details)

txt ="i have {an: .2f} Rupees!"
print(txt.format(an = 4))
"""