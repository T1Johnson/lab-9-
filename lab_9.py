def encode(password):
    password = " "
    for num in password:
        num = int(num)
        num += 3
        password += str(num)
    return password

print(encoder("23456677"))