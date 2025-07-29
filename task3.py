import random
len= int(input("Enter password length: "))
a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
p = ""
for i in range(len):
    p += random.choice(a)
print("Generated Password:", p)
