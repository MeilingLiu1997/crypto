# Cryptanalytic Toolkit

	A cryptanalytic toolkit in Python to analyze the statistical properties of files.

## Getting Started

This program uses the version of Python 2.7/3

Notify: Statistical techniques can give you wrong answers. In this program, these are mainly two techniques. The first technique is calculating the frequency of the English letters (to break Caeser Cipher). It has high possibility to decode and to get the exact same text (performing well in input_big_encrypted_in_caeser.txt); Second technique is n-gram (to break Vigenere Cipher), you may have to try decrypting the ciphertext with each of several likely candidates to find the true key. What plaintext/encryted_text (input_small_encrypted_in_vigenere.txt) I provide in here might fail of this technique. 


Libraries use for this program: 
```
click, re, ngram_score, permutations, starmap, cycle
```

* click - Command line parsing.
* re - For cleaning the cipher text.
* ngram_score - Quadgrams statistics of analysis techniques.
* permutations - For efficient looping when breaking of poly-alphabetic ciphers.
* starmap - For decrypting vigenere cipher.
* cycle - For decrypting vigenere cipher.


### A command line help
```
	Usage: cryptanalytic.py [OPTIONS] COMMAND [ARGS]...

		A cryptanalytic toolkit in Python to analyze the statistical properties of
		files.

	Options:
		-h, --help  Show this message and exit.

	Commands:
		caesar_frequency  to break by calculating frequency of 'E'
		caesar_ngram      to break by using quadgram statistics...
		dist              Calculate frequency distributions of symbols...
		list              List of available distributions
		vigenere_ngram    to break by using quadgram statistics...
```

Plain text choices:
* input_small.txt (recommand to test vigenere_ngram)
* input_small_encrypted_in_caeser.txt
* input_small_encrypted_in_vigenere.txt
* input_middle.txt
* input_middle_encrypted_in_caeser.txt
* input_middle_encrypted_in_vigenere.txt
* input_big.txt
* input_big_encrypted_in_caeser.txt
* input_big_encrypted_in_vigenere.txt


## Running the tests

### Calculate the frequency

Display available distributions: 
```
$ python3 cryptanalytic.py list

The following 4 distributions are supported:
mono - Monograph
ng - Ngraph
tri - Trigraph
di - Digraph
```

Print/display the selected distribution (example of choose Monograph):
```
$ python3 cryptanalytic.py dist -d mono input_middle.txt output.txt
```
*Note: Users have to enter input file and output file

```
$ cat output.txt
A: 5
C: 8
D: 3
E: 15
F: 3
G: 1
H: 8
I: 9
L: 8
M: 2
N: 8
O: 17
P: 6
R: 11
S: 6
T: 18
U: 2
W: 5
Y: 6
```

### Break Caeser by calculating frequency of 'E': (Recommand use big file, such as input_big_encrypted_in_caeser.txt)

Note: Users have to choose distribution type, input file, output file
Example gives that choose Monograph type, input input_big_encrypted_in_caeser.txt, output output.txt:
```
$ python3 cryptanalytic.py caesar_frequency -d mono input_big_encrypted_in_caeser.txt output.txt
Finding possible key: E=H. Attempting decryption...
Check out your output file.
```

### Break Caeser Cipher by using quadgram statistics:
```
$ python3 cryptanalytic.py caesar_ngram input_big_encrypted_in_caeser.txt output.txt
The most possible key = 23
Check out your output file.
```

### Break Vigenere Cipher by using quadgram statistics: (Recommand use input_small.txt)
```
$ python3 cryptanalytic.py vigenere_ngram input_small_encrypted_in_vigenere.txt
It might take few minutes to finish the process.
Please wait for that...
```

## Authors

* **Meiling Liu** [@Github](https://github.com/MeilingLiu1997)


## Acknowledgments

* This program includes some reference codes from internet, detailed will be found in reference link.

## References
* http://practicalcryptography.com/cryptanalysis/
* https://github.com/jameslyons/python_cryptanalysis