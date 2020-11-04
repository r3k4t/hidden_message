


import os
import sys
import cryptography
from fernet import Fernet

os.system("clear")



print (chr(27)+"[31m")

 

import pyfiglet
banner = pyfiglet.figlet_format("Hidden Message ",font = "standard")
print (banner)

print (chr(27)+"[33m"+"                  Author : Rahat Khan Tusar(RKT)")
print (chr(27)+"[33m"+"                 Github : https://github.com/r3k4t")

print (chr(27)+"[35m")

resp = input("""\n Please, select your favourite option :
                               1. Message Encrypt
                               2. Message Decrypt\n""")
print ("you have selected your option : ",resp)


if resp == '1' :


  print (chr(27)+"[32m")

  os.system("clear")
  banner2 = pyfiglet.figlet_format("Encrypt",font="standard")
  print (banner2)
  
  file = open('key.key','rb')
  key = file.read() 
  file.close()

  message = input("Enter your private message : ")

  print (chr(27)+"[37m")

  encoded = message.encode()


  f = Fernet(key)
  encrypted = f.encrypt(encoded)
  print (encrypted)


elif resp == '2':
  
  print (chr(27)+"[34m")

  os.system("clear")
  banner3 = pyfiglet.figlet_format("Decrypt",font="standard")
  print (banner3)

  file = open('key.key','rb')
  key2 = file.read() 
  file.close()

  message = input("Enter your hash message : ")
  print (chr(27)+"[37m")
  encoded = message.encode()

  f2= Fernet(key2)
  decrypted = f2.decrypt(encoded)
  print (decrypted)

