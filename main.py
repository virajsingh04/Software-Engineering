from menu import Menu

if __name__ == "__main__":
    while True:
        Menu()
        menu_option = int(input("Please enter an option: "))

        if menu_option == 1:
            password_to_encode = int(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")

        if menu_option == 2:
            print(f"The encoded password is {your_encoding_output}, and the original password is {password_to_encode}.")

        if menu_option == 3:
            break
