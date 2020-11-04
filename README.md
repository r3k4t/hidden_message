[![MIT](https://img.shields.io/packagist/l/doctrine/orm.svg)](https://github.com/r3k4t//blob/master/LICENSE) 
![python](https://img.shields.io/badge/python-3.9.0-brightgreen.svg)](https://www.python.org/downloads/release/python-390/)
[![OS](https://img.shields.io/badge/Tested%20On-Linux-yellowgreen.svg)](https://en.wikipedia.org/wiki/Linux/)

<h2>Hidden Message</h2>

<h4>Author : RKT</h4>

### Description ###

![Screenshot at 2020-11-04 11-58-15](https://user-images.githubusercontent.com/69615463/98142496-e00d9100-1eed-11eb-9a32-8ebef3a06885.png)

This program can hide your secret message.Its name is hidden_message.It builds on python.A hidden_message has two programs.There are message encrypt or message decrypt programs.Anyone  can not see or spy  your message from social media or any sms sender site.You can hide government secret message or information.At first,you can clone hidden_message github in your linux terminal and enter a message.In the time,a hidden_message program can encrypt your message.You can send encrypt message your friend and he can open his lnux terminal.He can select a message decrypt option and enter a message hash.In this time, a hidden_message program can decrypt your message.He can see your message.A secret communication system.


### Message  Encryption (conecpt) ###

>>> import cryptography
>>> from fernet import Fernet
>>> key = Fernet.generate_key()
>>> print (key) 
b'f2oJOLBrYq0EnfxkkrmIwR4gO-guHF9riQ5W61ukp4s='

### key.key file ###

>>> import cryptography
>>> from fernet import Fernet
>>> key = Fernet.generate_key()
>>> print(key)
>>> file = open('key.key','wb')
>>>>file.write(key) 
>>>>file.close()

#### Tested On ###
                                       
<ul>
<li>Ubuntu</li>
<li>Kali Linux</li>
<li>Linuxmint</li>
<li>Parrot Os</li>
</ul>

### Installation ###

We need to install cryptography and fernet on our linux .Open a terminal type and type the following command:

<ul>
<li>sudo apt install python3-cryptography<li>
<li>sudo apt install python3-fernet
</ul>

### Terminal Command ###

<ul>
<li>git clone https://github.com/r3k4t/hidden_message.git</li>
<li>cd hidden_message   </li>
<li>python3 hidden_message.py </li>
</ul>


### Example ###

![Screenshot at 2020-11-04 12-00-50](https://user-images.githubusercontent.com/69615463/98142775-3e3a7400-1eee-11eb-85f6-fb399dd9ef95.png)

Next

![Screenshot at 2020-11-04 12-01-45](https://user-images.githubusercontent.com/69615463/98142816-4e525380-1eee-11eb-9ccc-bb625b414e0c.png)
