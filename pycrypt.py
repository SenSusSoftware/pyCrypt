#########################################################################################
#PyCrypt is simple python script which uses know hashing algorithms to crypt string.    #
#Note: Any of this strings will not be uploaded to some kind of sites or hash databases #
#   If you don't trust me , look at the source code.                                    #
#   Thank you for using this script, there is a lot other thigs to do here              #
#                                                                      SenSus           #
#########################################################################################




import sys
import hashlib

print('::::::::: :::   ::: :::::::: ::::::::: :::   :::::::::::::::::::::::')
print(':+:    :+::+:   :+::+:    :+::+:    :+::+:   :+::+:    :+:   :+:    ')
print('+:+    +:+ +:+ +:+ +:+       +:+    +:+ +:+ +:+ +:+    +:+   +:+    ')
print('+#++:++#+   +#++:  +#+       +#++:++#:   +#++:  +#++:++#+    +#+    ')
print('+#+          +#+   +#+       +#+    +#+   +#+   +#+          +#+    ')
print('#+#          #+#   #+#    #+##+#    #+#   #+#   #+#          #+#    ')
print('###          ###    ######## ###    ###   ###   ###          ###    ')

print('+=========================================================================================+')
print('+ Pycrypt is simple python script which uses known hashing algorithms to crypt string.    +')
print('+ Note: Any of this strings will not be uploaded to some kind of sites or hash databases. +')
print('+    If you do not trust me look at the source code.                                      +')
print('+    Thank you for using this script, SenSus                                              +')
print('+=========================================================================================+')

def imporfile():
    ifile = raw_input('Enter txt file destination > ')
    file  = open(ifile,'r')
    for word in file.readlines():
           word = word.strip('\n')
           hash = hashlib.md5(word)

           print(hash.hexdigest())




def choice2():
    ask = raw_input('Do you want to encrypt only one string or file which contains more strings (more strings will be encrypt to MD5) ? [1 / 2] > ')
    if ask == '1':
        algorithms()
    elif ask == '2':
        imporfile()





def algorithms():

    text = raw_input('Please enter your string > ')

    print("+-----------------------+")
    print("+ [1] MD5     algorithm +")
    print("+ [2] SHA1    algorithm +")
    print("+ [3] SHA224  algorithm +")
    print("+ [4] SHA256  algorithm +")
    print("+ [5] SHA384  algorithm +")
    print("+ [6] SHA512  algorithm +")
    print("+-----------------------+")

    algr = raw_input("[+]Please choose your encryption > ")

    if algr == '1':
        hash1 = hashlib.md5(text)
        print(hash1.hexdigest())
        choice()


    elif algr == '2':
        hash2 = hashlib.sha1(text)
        print(hash2.hexdigest())
        choice()



    elif algr == '3':
        hash3 = hashlib.sha224(text)
        print(hash3.hexdigest())
        choice()


    elif algr == '4':
        hash4 = hashlib.sha256(text)
        print(hash4.hexdigest())
        choice()

    elif algr == '5':
        hash5 = hashlib.sha384(text)
        print(hash5.hexdigest())
        choice()

    elif algr == '6':
        hash6 = hashlib.sha512(text)
        print(hash6.hexdigest())
        choice()

def choice():
    chs = raw_input("Do you want to crypt more strings ? [ 1 / 0 ] >  ")
    if chs == '1':
        menu()
    elif chs == '0':
        sys.exit()





def menu():
    choice2()
    algorithms()
    choice()



menu()
