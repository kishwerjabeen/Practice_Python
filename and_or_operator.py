# check two conditions at same time 
# and , or

#and (when both condition is true then true otherwise false)
name = 'abc'
age = 19

if name == "abc" and age== 19:
    print("condition is true")
else:
    print("condition is false")

if name == "abcd" and age== 19:
    print("condition is true")
else:
    print("condition is false")

#or (when atlest one condition is true then true )

if name=='abcd' or age==23:
    print("condition True")
else:
    print("condition False")

if name =='abc' or age==13:
    print("condition True")
else:
    print("condition False")

