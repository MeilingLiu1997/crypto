# Classic Ciphers

A command-line tool implimenting simple ciphers and basic frequency analysis tools.

## Getting Started

This program uses the version of Python 3

Libraries use for this program: 
```
argparse, math, starmap, cycle, chain, ascii_letters
```

* argparse - command line parsing
* math - for block transposition cipher
* starmap - for vigenere cipher
* cycle - for vigenere & fence (zigzag) cipher
* chain - for fence cipher
* ascii_letters - for simple substitution cipher


### A command line help
```
Usage: cipher.py [-h] [-i I] [-e] [-d] [-a A] [-o O]

	Optional arguments:
		-h, --help  show this help message and exit
		-i I        Input file
		-e          Encryption
		-d          Decryption
		-a A        Algorithm you choose = ['caesar', 'simple_substitution',
		          'vigenere', 'block_transposition', 'fence']
		-o O        Output file
```

Plain text:
```
Welcome to the cipher world!
This is only a test file for encryption or decryption.
Now,
Choose the algorithm that you want to encrypt or decrypt.
Please follow the instruction!
```

Encryption with simple_substitution:
```
Uqogliq sl sdq gmxdqv ulvoh!
Sdmt mt laoj n sqts kmoq klv qagvjxsmla lv hqgvjxsmla.
Alu,
Gdlltq sdq noclvmsdi sdns jlw unas sl qagvjxs lv hqgvjxs.
Xoqntq kloolu sdq matsvwgsmla!
```

## Running the tests

Open input_small.txt and encrypt it with caesar cipher (default algorithm ):
```
Welcome to the cipher world!
This is only a test file for encryption or decryption.
Now,
Choose the algorithm that you want to encrypt or decrypt.
Please follow the instruction!
>>> python3 cipher.py -e -i input_small.txt
Making an Encryption...

Check your results in output.txt file.
```

Get encrypted output.txt and decrypt it:
```
Zhofrph wr wkh flskhu zruog!
Wklv lv rqob d whvw iloh iru hqfubswlrq ru ghfubswlrq.
Qrz,
Fkrrvh wkh dojrulwkp wkdw brx zdqw wr hqfubsw ru ghfubsw.
Sohdvh iroorz wkh lqvwuxfwlrq!

>>> python3 cipher.py -d -i output.txt
Making a Decryption...

Check your results in output.txt file.
```

Then, we get decrypted output.txt:
```
Welcome to the cipher world!
This is only a test file for encryption or decryption.
Now,
Choose the algorithm that you want to encrypt or decrypt.
Please follow the instruction!
```


## Authors

* **Meiling Liu** [@Github](https://github.com/MeilingLiu1997)


## Acknowledgments

* This program includes some reference codes from internet, detailed will be found in reference link.

## References
* https://codereview.stackexchange.com/questions/166452/substitution-cipher-in-python-3
* https://rosettacode.org/wiki/Vigen%C3%A8re_cipher#Python
* https://inventwithpython.com/hacking/chapter8.html
* https://inventwithpython.com/hacking/chapter9.html
* https://github.com/exercism/python/blob/master/exercises/rail-fence-cipher/example.py

