while True:
    ask = input("Do you want to convert 'yes' or 'no' =")

    if ask == 'yes':
        curr = int(input("which currency do you have?" "\n"
                         "options: '1' Euro , '2' Dollar, '3' PKR, '4' INR,  '5' yen" "\n" "Choose by no." "\n"))
        if curr == 1:
            to_curr = int(input("to which currency you want to convert" "\n"
                                "options:, '1' Dollar, '2' PKR, '3' INR,  '4' yen" "\n" "Choose by no." "\n"))

            # Euro to other currencies
            if to_curr == 1:
                am = float(input("please tell amount"))
                print("you can get your", am * 1.1045000646, "$", "\n" "Thanks! for  using our program")

            elif to_curr == 2:
                am = float(input("please tell amount"))
                print("you can get your", am * 204.0957270206, "PKR", "\n" "Thanks! for  using our program")

            elif to_curr == 3:
                am = float(input("please tell amount"))
                print("you can get your", am * 83.7363, "INR", "\n" "Thanks! for  using our program")

            elif to_curr == 4:
                am = float(input("please tell amount"))
                print("you can get your", am * 135.39, "YEN", "\n" "Thanks! for  using our program")
            else:
                pass

            # Euro to other currencies

        if curr == 2:
            to_curr = int(input("to which currency you want to convert" "\n"
                                "options:, '1' Euro, '2' PKR, '3' INR,  '4' yen" "\n" "Choose by no." "\n"))

            # dollar to other currencies
            if to_curr == 1:
                am = float(input("please tell amount"))
                print("you can get your", am * 0.90, "€", "\n" "Thanks! for  using our program")

            elif to_curr == 2:
                am = float(input("please tell amount"))
                print("you can get your", am * 183.90, "PKR", "\n" "Thanks! for  using our program")

            elif to_curr == 3:
                am = float(input("please tell amount"))
                print("you can get your", am * 75.97, "INR", "\n" "Thanks! for  using our program")

            elif to_curr == 4:
                am = float(input("please tell amount"))
                print("you can get your", am * 122.49, "YEN", "\n" "Thanks! for  using our program")
            else:
                pass

            # dollar to other currencies

        if curr == 3:
            to_curr = int(input("to which currency you want to convert" "\n"
                                "options:, '1' Euro, '2' Dollar, '3' INR,  '4' yen" "\n" "Choose by no." "\n"))

            # PKR to other currencies
            if to_curr == 1:
                am = float(input("please tell amount"))
                print("you can get your", am * 0.0049, "€", "\n" "Thanks! for  using our program")

            elif to_curr == 2:
                am = float(input("please tell amount"))
                print("you can get your", am * 0.0054, "$", "\n" "Thanks! for  using our program")

            elif to_curr == 3:
                am = float(input("please tell amount"))
                print("you can get your", am * 0.41, "INR", "\n" "Thanks! for  using our program")

            elif to_curr == 4:
                am = float(input("please tell amount"))
                print("you can get your", am * 0.66, "YEN", "\n" "Thanks! for  using our program")
            else:
                pass

            # PKR to other currencies

        if curr == 4:
            to_curr = int(input("to which currency you want to convert" "\n"
                                "options:, '1' Euro, '2' Dollar, '3' PKR,  '4' yen" "\n" "Choose by no." "\n"))

            # INR to other currencies
            if to_curr == 1:
                am = float(input("please tell amount"))
                print("you can get your", am * 0.012, "€", "\n" "Thanks! for  using our program")

            elif to_curr == 2:
                am = float(input("please tell amount"))
                print("you can get your", am * 0.013, "$", "\n" "Thanks! for  using our program")

            elif to_curr == 3:
                am = float(input("please tell amount"))
                print("you can get your", am * 2.42, "PKR", "\n" "Thanks! for  using our program")

            elif to_curr == 4:
                am = float(input("please tell amount"))
                print("you can get your", am * 1.61, "YEN", "\n" "Thanks! for  using our program")
            else:
                pass

            # INR to other currencies

        if curr == 5:
            to_curr = int(input("to which currency you want to convert" "\n"
                                "options:, '1' Euro, '2' Dollar, '3' PKR,  '4' INR" "\n" "Choose by no." "\n"))

            # Yen to other currencies
            if to_curr == 1:
                am = float(input("please tell amount"))
                print("you can get your", am * 0.0074, "€", "\n" "Thanks! for  using our program")

            elif to_curr == 2:
                am = float(input("please tell amount"))
                print("you can get your", am * 0.0082, "$", "\n" "Thanks! for  using our program")

            elif to_curr == 3:
                am = float(input("please tell amount"))
                print("you can get your", am * 1.51, "PKR", "\n" "Thanks! for  using our program")

            elif to_curr == 4:
                am = float(input("please tell amount"))
                print("you can get your", am * 0.62, "INR", "\n" "Thanks! for  using our program")
            else:
                pass

            # Yen to other currencies

        else:
            pass

    else:
        break
