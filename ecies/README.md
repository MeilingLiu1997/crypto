#  Elliptic Curve Integrated Encryption Scheme

Optimizate the source code from [Elliptic Curve Integrated Encryption Scheme (ECIES) with AES](https://asecuritysite.com/encryption/ecc3);
A Python command line program that encrypts and decrypts files based on public key cryptography.

## Getting Started

This program uses the version of Python 3


Libraries use for this program:
```
import click
from Crypto.Cipher import AES
```
Please be sure to install following libraries: 
```
pip3 install click
pip3 install pycrypto
```


### A command line help
```
Usage: ecies.py [OPTIONS] COMMAND [ARGS]...

  A Python command line program that encrypts and decrypts files based on
  public key cryptography

Options:
  -h, --help  Show this message and exit.

Commands:
  do
```


## Running the tests

### User input encrypt message
```
$ python3 ecies.py do
Input a file? (y or Y): n
Please implement a valid string: (type message you want to encrypt)
```

### Sample of running a string
```
Input a file? (y or Y): n
Please implement a valid string: hello
Starting...........
Private key: 0xa489fe78d1faf53f3337c8b8f2ff9932427ea31451cea3c9ab2ec13178e5d03b
Public key: (0x9ff6772068a4a77d8c4e0d485a86a95bf1003b929c4c3ce589dc98096ded79c9, 0xf92f3c8848d6dd9f50749c83f3348416a4e72b0ad81352ac7e626ac64402707c)
=========================
(72353209484228612889458701756661237974992391870728740094387090151531030084041, 112709358888282344562054911603150002840148630236744181213793523998441611620476)
======Symmetric key========
Encryption key: 113887443815071927596158937582263509045102954688550469455026652489897764117327
Encrypted:	 b'334d4f3646656d394b39352f746457453443473134513d3d'
Decrypted:	 hello
```

### Sample of running a file
```
Input a file? (y or Y): y
Please enter your file: input.txt
Starting...........
Private key: 0x2cc891c1fdedee88a613cebfcb06fd2b7bf8eecc6aad3efa9351d1b440663cad
Public key: (0x91a10db8bcb9fb7ce0947a0d55a5b661d663d2761f3eeab534b7c9ef31723947, 0x856b112f7ae64fdb015a3336ae0677d1fbdd2759beaa1023fc51f9349746ef6c)
=========================
(65869920125210860769023139336243536349417733730108875423232614508359935211847, 60346780107253949991015864889909713799000686113194560842583543753141427564396)
======Symmetric key========
Encryption key: 38942489765680430609503473906338768495118910629036302535714884160361459021820
Encrypted:	 b'62415370574a317877354a483030426d5a56546866413d3d'
Decrypted:	 Hello World!
```

## Authors

* **Meiling Liu** [@Github](https://github.com/MeilingLiu1997)


## Acknowledgments

* This program includes some reference codes from internet, detailed will be found in reference link.

## References
* [Elliptic Curve Integrated Encryption Scheme (ECIES) with AES](https://asecuritysite.com/encryption/ecc3)
* [Source Code](https://github.com/andreacorbellini/ecc/blob/master/scripts/ecdhe.py)