def encode_password(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def decoder(encoded_password):
    encoded_password = list(str(encoded_password))

    for i in range(len(encoded_password)):
        if int(encoded_password[i]) > 2:
            encoded_password[i] = int(encoded_password[i]) - 3

        elif int(encoded_password[i]) == 2:
            encoded_password[i] = 9

        elif int(encoded_password[i]) == 1:
            encoded_password[i] = 8

        elif int(encoded_password[i]) == 0:
            encoded_password[i] = 7

    for i in range(len(encoded_password)):
        encoded_password[i] = str(encoded_password[i])

    return "".join(encoded_password)


