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

    return encoded_password
