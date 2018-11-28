""" cipher.py

	A command-line tool implimenting simple ciphers and
    basic frequency analysis tools.

    Usage: cipher.py [-h] [-i I] [-e] [-d] [-a A] [-o O]

	Optional arguments:
		-h, --help  show this help message and exit
		-i I        Input file
		-e          Encryption
		-d          Decryption
		-a A        Algorithm you choose = ['caesar', 'simple_substitution',
		          'vigenere', 'block_transposition', 'fence']
		-o O        Output file

	Example usage:
		python3 cipher.py -e -i input_small.txt -o output.txt		# default algorithm - caesar cipher

		python3 cipher.py -a vigenere -i input_small.txt -d  		# default output file - output.txt

	Notes: 
	1. User has to enter mode of this program, either encryption (-e) or decryption (-d); 
		and has to enter input plaint text (-i plaint_text_filename.txt).
	2. When user enter algorithm that is not on the list ['caesar', 'simple_substitution',
		'vigenere', 'block_transposition', 'fence'], then will get help message.

	Copyright @2018 Meiling Liu

"""

import argparse, math
from itertools import starmap, cycle, chain
from string import ascii_letters


def getplain_text(input_file):
	""" Open Test file, and return plain text """
	file = open(input_file,'r')

	line = file.readline()
	plain_text = ""

	while line != '':
		plain_text+=line
		line = file.readline()
	file.close()

	return plain_text

def outputFile(text, output_file):
	""" Write output result to a new file """
	file = open(output_file, 'w')
	file.write(text)
	file.close()


def encrypt(plain_text, algorithm):
	""" Encrypts the given string using a chosen algorithm cipher and returns the result. 
	"""
	if algorithm == "caesar":
		return caesar(plain_text, 3)

	elif algorithm == "simple_substitution":
		cipher_letters = "nzghqkcdmyfoialxevtswrupjbNZGHQKCDMYFOIALXEVTSWRUPJB"
		return simple_substitution_encrypt(plain_text, cipher_letters)

	elif algorithm == "vigenere":
		key = "crypotograph"
		return vigenere_encrypt(plain_text, key)

	elif algorithm == "block_transposition":
		key = 8
		return block_transposition_encrypt(plain_text, key)

	elif algorithm == "fence":
		return fence_encrypt(plain_text, 5)


def decrypt(plain_text, algorithm):
	""" Decrypts a string that was previously encrypted using a chosen algorithm cipher and returns the result. """
	if algorithm == "caesar":
		return caesar(plain_text, -3)

	elif algorithm == "simple_substitution":
		cipher_letters = "nzghqkcdmyfoialxevtswrupjbNZGHQKCDMYFOIALXEVTSWRUPJB"
		return simple_substitution_decrypt(plain_text, cipher_letters)

	elif algorithm == "vigenere":
		key = "crypotograph"
		return vigenere_decrypt(plain_text, key)

	elif algorithm == "block_transposition":
		key = 8
		return block_transposition_decrypt(plain_text, key)

	elif algorithm == "fence":
		return fence_decrypt(plain_text, 5)


def caesar(plain_text, key):
	""" Caesar cipher.
		In Caesar cipher, each letter of the text is replaced by the letter 
		which stands a certain number of places before or after it in the alphabet. 
		In this program, set Shift symbols to right by 3. 

		From "Manual of Cryptography", 1911, page 28
	"""
	cipher_text = ""

	for c in plain_text:
		if (65 <= ord(c) <= 90):
			p = ord(c) - ord('A')
			c = (p + key)%26 + ord('A')
			cipher_text += chr(c)
		elif (97 <= ord(c) <= 122):
			p = ord(c) - ord('a')
			c = (p + key)%26 + ord('a')
			cipher_text += chr(c)
		else:
			cipher_text = cipher_text + c

	return cipher_text


def simple_substitution_encrypt(plain_text, cipher_letters):
	""" Simple substitution cipher.
		In letter substitution ciphers other letters are substituted 
		for the letters of the text either singly or in pairs.
		From "Manual of Cryptography", 1911, page 15
		
		Reference source code from: 
		https://codereview.stackexchange.com/questions/166452/substitution-cipher-in-python-3
	"""
	trans = str.maketrans(ascii_letters, cipher_letters)
	return plain_text.translate(trans)

def simple_substitution_decrypt(plain_text, cipher_letters):
	""" Simple substitution cipher.
		In letter substitution ciphers other letters are substituted 
		for the letters of the text either singly or in pairs.
		From "Manual of Cryptography", 1911, page 15
		
		Reference source code from: 
		https://codereview.stackexchange.com/questions/166452/substitution-cipher-in-python-3
	"""
	trans = str.maketrans(cipher_letters, ascii_letters)
	return plain_text.translate(trans)


def vigenere_encrypt(plaintext, key):
	""" Poly-alphabetic cipher -- vigenere cipher
		The vigenere cipher is a method of encrypting alphabetic text 
		by using a series of different Caesar ciphers based on the letters of a keyword. 
		It is a simple form of poly-alphabetic substitution. 
		(From: https://www.wattpad.com/368521846-book-of-codes-and-ciphers-8-vigenere-cipher)
		Reference source code from: https://rosettacode.org/wiki/Vigen%C3%A8re_cipher#Python 
	"""

	# single letter encrpytion.
	def enc(c,k): 
		# keep other characters that are not alpha
		if (c.isalpha()) == False:
			return c
		else:
			if c.isupper():
				return chr(((ord(k) + ord(c) - 2*ord('A')) % 26) + ord('A'))
			else:
				# encrypted lowercase characters
				return chr(((ord(k) + ord(c.upper()) - 2*ord('A')) % 26) + ord('A') + 32)


	return "".join(starmap(enc, zip(plaintext, cycle(key))))

def vigenere_decrypt(ciphertext, key):
	""" Poly-alphabetic cipher -- vigenere cipher
		The vigenere cipher is a method of encrypting alphabetic text 
		by using a series of different Caesar ciphers based on the letters of a keyword. 
		It is a simple form of poly-alphabetic substitution. 
		(From: https://www.wattpad.com/368521846-book-of-codes-and-ciphers-8-vigenere-cipher)
		Reference source code from: https://rosettacode.org/wiki/Vigen%C3%A8re_cipher#Python 
	"""

	# single letter decryption.
	def dec(c,k):
		# keep other characters that are not alpha
		if (c.isalpha()) == False:
			return c
		else:
			if c.isupper():
				return chr(((ord(c) - ord(k) - 2*ord('A')) % 26) + ord('A'))
			else:
				# decrypted lowercase characters
				return chr(((ord(c.upper()) - ord(k) - 2*ord('A')) % 26) + ord('A') + 32)
	return "".join(starmap(dec, zip(ciphertext, cycle(key))))

def block_transposition_encrypt(plaintext, key):
	""" Transposition cipher -- block-transposition cipher
		In transposition ciphers the letters or words of the text are not changed, 
		but their order is altered according to some prearranged plan.
		From "Manual of Cryptography", 1911, page 20

		Reference source code from: https://inventwithpython.com/hacking/chapter8.html
	"""
	# Each string in ciphertext represents a column in the grid.
	ciphertext = [''] * key

	# Loop through each column in ciphertext.
	for col in range(key):
		pointer = col
		# Keep looping until pointer goes past the length of the plaintext.
		while pointer < len(plaintext):
			# Place the character at pointer in plaintext at the end of the current column in the ciphertext list.
			ciphertext[col] += plaintext[pointer]
			# move pointer over
			pointer += key
	# Convert the ciphertext list into a single string value and return it.
	return ''.join(ciphertext)


def block_transposition_decrypt(ciphertext, key):
	""" Transposition cipher -- block-transposition cipher
		In transposition ciphers the letters or words of the text are not changed, 
		but their order is altered according to some prearranged plan.
		From "Manual of Cryptography", 1911, page 20

		Reference source code from: https://inventwithpython.com/hacking/chapter8.html
	"""

	# The number of "columns" in our transposition grid:
	numOfColumns = math.ceil(len(ciphertext) / key)
	# The number of "rows" in our grid will need:
	numOfRows = key
	# The number of "shaded boxes" in the last "column" of the grid:
	numOfShadedBoxes = (numOfColumns * numOfRows) - len(ciphertext)# Each string in plaintext represents a column in the grid.
	plaintext = [''] * numOfColumns
	# The col and row variables point to where in the grid the next

	# character in the encrypted ciphertext will go.
	col = 0
	row = 0
	for symbol in ciphertext:
		plaintext[col] += symbol
		col += 1 # point to next column
		# If there are no more columns OR we're at a shaded box, go back to the first column and the next row.
		if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
			col = 0
			row += 1
	return ''.join(plaintext)



def fence_pattern(rails, size):
	""" Help method for fence cipher """
	zig_zag = cycle(chain(range(rails), range(rails - 2, 0, -1)))
	return zip(zig_zag, range(size))


def fence_encrypt(msg, rails):
	""" Rail Fence Cipher
		In the Zigzag Transposition cipher, the letters are written up and down alternate columns, 
		beginning at the top or bottom of a certain column, 
		and the cryptogram is formed by reading off the lines of letters.
		From "Manual of Cryptography", 1911, page 21

		Reference source code from: https://github.com/exercism/python/blob/master/exercises/rail-fence-cipher/example.py
	"""
	fence = fence_pattern(rails, len(msg))
	return ''.join(msg[i] for _, i in sorted(fence))


def fence_decrypt(msg, rails):
	""" Rail Fence Cipher
		In the Zigzag Transposition cipher, the letters are written up and down alternate columns, 
		beginning at the top or bottom of a certain column, 
		and the cryptogram is formed by reading off the lines of letters.
		From "Manual of Cryptography", 1911, page 21

		Reference source code from: https://github.com/exercism/python/blob/master/exercises/rail-fence-cipher/example.py
	"""

	fence = fence_pattern(rails, len(msg))
	fence_msg = zip(msg, sorted(fence))
	return ''.join(
    	char for char, _ in sorted(fence_msg, key=lambda item: item[1][1]))


def main():
	parser = argparse.ArgumentParser(description="A Python command-line program to encrypt or decrypt a file.")

	#Option flags to select the algorithm to use for encryption or decryption
	parser.add_argument("-i", help='Input file', type=argparse.FileType('r'))
	parser.add_argument('-e', help="Encryption",action="store_true")
	parser.add_argument('-d', help="Decryption",action="store_true")
	parser.add_argument('-a', help="Algorithm you choose = ['caesar', 'simple_substitution', 'vigenere', 'block_transposition', 'fence']")
	parser.add_argument('-o', help='Output file', type=argparse.FileType('w'))

	args = parser.parse_args()

	result = ""

	# User have to enter input file; if not, print help plaintexts
	if args.i:
		input_file = args.i.name
	else:
		parser.print_help()

	# Set algorithm, if not, set caesar as a default
	algorithm = ""
	if args.a:
		algorithm = args.a
	else:
		algorithm = "caesar"

	if args.e:
	    print("Making an Encryption...")
	    print()
	    result += encrypt(getplain_text(input_file), algorithm)
	elif args.d:
	    print("Making a Decryption...")
	    print()
	    result += decrypt(getplain_text(input_file), algorithm)


	# Set output file; if not, set output.txt as a default output file
	output_file = ""
	if args.o:
		output_file = args.o.name
	else:
		output_file = "output.txt"

	outputFile(result, output_file)
	print("Check your results in {} file.".format(output_file))

main()