# if elif else  statement
 
# show ticket pricing
# 1 to 3  (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

age = int(input("input your age : "))

if 0< age <=3 :
    print("Ticket is free")
elif 3< age <=10:
    print("price is 150 ")
elif 10< age <=60 :
    print("price is 250")
else:
    print("above 60 is 200")