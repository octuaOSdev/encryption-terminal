import shiftcrypt
enstr = ""
while True:
    command = input("> ")


    if command == "encrypt":
        string = input("string to encrypt:")
        shiftnumber = int(input("shift number:"))
        enstring = shiftcrypt.caesar_encrypt(string , shiftnumber)
        print(enstring)
        answer = input("save to variable?(Y/N)")
        if answer == "Y" or "y":
            enstr = enstring

















    if command == "decrypt":
        if enstr != "":
            deanswer = input("load from variable?(Y/N)")
            if deanswer == "Y" or "y":
                encryptedstr = enstr
        if enstr == "":
            encryptedstr = input("encrypted string:")
        sn = int(input("enter the number the string was shifted by:"))
        destr = shiftcrypt.caesar_decrypt(encryptedstr, sn)
        print(destr)
        













            
            


        

