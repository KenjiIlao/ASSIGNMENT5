Age= int(input("your age:"))

if Age > -1 and Age <= 12:
    print ("Kid")
elif Age >= 13 and Age <= 17:
    print ("Teen")
elif Age == 18:
    print ("Debut")
else:
    print("Adult")

#steps
# 1. ask your age,covert and store
# 2. test 0-12
# 3.test 12-17
# 4. test 18
# 5. test >=19
# then print            