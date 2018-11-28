""" cryptanalytic.py
	A cryptanalytic toolkit in Python to analyze the statistical properties of files.
	
	- Determine the frequency distribution of characters in the file.
	- Print/display the selected distribution
	- Determine the Bigram, Trigram or higher distribution of symbols in a file.
	- The additional analysis techniques should facilitate the breaking of poly-alphabetic ciphers.
	- A tool that fully 'cracks' cipher text from a classic cipher

	Copyright @2018 Meiling Liu

"""
import click, re
from ngram_score import ngram_score
from itertools import permutations, starmap, cycle
# from pycipher import Vigenere


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@click.pass_context     # ctx
def cli(ctx):
    """ A cryptanalytic toolkit in Python to analyze the statistical properties of files. """
    pass


class Distribution(object):
	""" Base class for analysis routines for symbol distributions.
		Results are dictionary objects with human readable keys.
	"""
	def to_readable(self):
		""" Convert dictionary of symbols to readable text """
		pp = []
		for nary in sorted(self.result):		
			pp.append( "{}: {}\n".format( nary, self.result[nary]))
		return ''.join(pp)

	def to_dictionary(self):
		return self.result

class Ngraph(Distribution):
	""" Looking 'n' symbols at a time, create a dictionary
		of the occurrences of the n-ary string of symbols.
		Default is n=4, a quadgram.
	"""
	def __init__(self, n=4):
		self.n = n

	def analyze(self, text):
		n = self.n
		self.result = {} # results are stored as a dictionary
		
		text = text.upper()
		def letters(input):
			""" Clean cipher_text
			"""
			return ''.join(filter(str.isalpha, input))

		text = letters(text)

		for i in range( len(text) - n - 1 ):
			nary = text[ i:i+n ]
			if nary in self.result:
				self.result[nary] += 1
			else:
				self.result[nary] = 1
			
		return self.result


class Monograph(Distribution):
    def analyze(self, text): self.result = Ngraph( n=1 ).analyze(text)

class Digraph(Distribution):
    def analyze(self, text): self.result = Ngraph( n=2 ).analyze(text)

class Trigraph(Distribution):
    def analyze(self, text): self.result = Ngraph( n=3 ).analyze(text)

# collect all distribution routines for cli usage
dist_dict = {'mono':Monograph, 'di':Digraph, 'tri':Trigraph, 'ng':Ngraph}
dist_name_list =[ key for key in dist_dict]


@cli.command()
def list():
	""" List of available distributions
	"""
	click.echo( "The following {} distributions are supported:".format( len(dist_dict)))
	for key,value in dist_dict.items():
		click.echo("{} - {}".format(key, value.__name__))


@cli.command()
@click.option('--dtype', '-d', 'dist_name', type=click.Choice( dist_name_list ) )
@click.argument('input_file', type=click.File('r'))
@click.argument('output_file', type=click.File('w'))
def Dist(dist_name, input_file, output_file):
	""" Calculate frequency distributions of symbols in files.
	"""
	D = dist_dict[dist_name] # instantiate class from dictionary
	dist = D()
	text = input_file.read()

	dist.analyze(text)

	output_file.write( dist.to_readable() )


@cli.command()
@click.option('--dtype', '-d', 'dist_name', type=click.Choice( dist_name_list ) )
@click.argument('input_file', type=click.File('r'))
@click.argument('output_file', type=click.File('w'))
def caesar_frequency(dist_name, input_file, output_file):
	""" to break by calculating frequency of 'E'
	"""
	plain_text = input_file.read()

	D = dist_dict[dist_name] # instantiate class from dictionary
	dist = D()
	dist.analyze(plain_text)

	for k in sorted(dist.to_dictionary()):
		value = dist.to_dictionary()[k]

		freq = value / float(len(plain_text))
		if freq >= .1:
			print("Finding possible key: E=" + k + ". Attempting decryption...")
			# shift and decrypt key
			key = 0 - (ord(k) - ord('E'))
	output_file.write(caesar_cipher(plain_text, key))

	print("Check out your output file.")


@cli.command()
@click.argument('input_file', type=click.File('r'))
@click.argument('output_file', type=click.File('w'))
def caesar_ngram(input_file,output_file):
	""" to break by using quadgram statistics
		Quadgrams statistics determine how similar text is to English.

		For example several books worth of text, 
		and count each of the quadgrams that occur in them. 
		We then divide these counts by the total number of quadgrams 
		encountered to find the probability of each.

		Sources from:
		http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/#a-python-implementation
		https://github.com/jameslyons/python_cryptanalysis/blob/master/break_caesar.py
	"""
	ctext = input_file.read()
	original_text = ctext

	fitness = ngram_score('quadgrams.txt') # load our quadgram statistics

	# make sure ciphertext has all spacing/punc removed and is uppercase
	ctext = re.sub('[^A-Z]','',ctext.upper())
	# try all possible keys, return the one with the highest fitness
	scores = []
	for i in range(26):
		scores.append((fitness.score(caesar_cipher(ctext,i)),i))

	max_key = max(scores)
	print("The most possible key = " + str(max_key[1]))
	print("Check out your output file.")
	output_file.write(caesar_cipher(original_text, int(max_key[1])))


@cli.command()
@click.argument('input_file', type=click.File('r'))
def vigenere_ngram(input_file):
	""" to break by using quadgram statistics
		Quadgrams statistics determine how similar text is to English.

		For example several books worth of text, 
		and count each of the quadgrams that occur in them. 
		We then divide these counts by the total number of quadgrams 
		encountered to find the probability of each.

		Wrapping up:
		Statistical techniques can give you wrong answers. 
		To get around this 
		you may have to try decrypting the ciphertext 
		with each of several likely candidates to find the true key.

		Sources from:
		http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-vigenere-cipher/
		https://github.com/jameslyons/python_cryptanalysis/blob/master/break_vigenere.py
	"""
	ctext = input_file.read()
	original_text = ctext
	qgram = ngram_score('quadgrams.txt')
	trigram = ngram_score('trigrams.txt')

	# make sure ciphertext has all spacing/punc removed and is uppercase
	ctext = re.sub('[^A-Z]','',ctext.upper())
	
	print("It might take few minutes to finish the process.")
	print("Please wait for that...")
	
	#init
	N=100
	for KLEN in range(3,20):
		rec = nbest(N)

		for i in permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZ',3):
			key = ''.join(i) + 'A'*(KLEN-len(i))
			# pt = Vigenere(key).decipher(ctext)
			pt = vigenere_decrypt(original_text, key)
			pt = re.sub('[^A-Z]','',pt.upper())

			score = 0
			for j in range(0,len(ctext),KLEN):
				score += trigram.score(pt[j:j+3])
			rec.add((score,''.join(i),pt[:30]))

		next_rec = nbest(N)
		for i in range(0,KLEN-3):
			for k in range(N):
				for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
					key = rec[k][1] + c
					fullkey = key + 'A'*(KLEN-len(key))
					# pt = Vigenere(fullkey).decipher(ctext)
					pt = vigenere_decrypt(original_text, fullkey)
					pt = re.sub('[^A-Z]','',pt.upper())
			
					score = 0
					for j in range(0,len(ctext),KLEN):
						score += qgram.score(pt[j:j+len(key)])
					next_rec.add((score,key,pt[:30]))
			rec = next_rec
			next_rec = nbest(N)
		bestkey = rec[0][1]
		# pt = Vigenere(bestkey).decipher(ctext)
		pt = vigenere_decrypt(original_text, bestkey)
		pt = re.sub('[^A-Z]','',pt.upper())

		bestscore = qgram.score(pt)
		for i in range(N):
			# pt = Vigenere(rec[i][1]).decipher(ctext)
			pt = vigenere_decrypt(original_text, rec[i][1])
			score = qgram.score(pt)
			if score > bestscore:
				bestkey = rec[i][1]
				bestscore = score       
			
		print(bestscore,'Vigenere, klen',KLEN,':"'+bestkey+'",',vigenere_decrypt(original_text, bestkey))

# keep a list of the N best things we have seen, discard anything else
class nbest(object):
	def __init__(self,N=1000):
		self.store = []
		self.N = N

	def add(self,item):
		self.store.append(item)
		self.store.sort(reverse=True)
		self.store = self.store[:self.N]

	def __getitem__(self,k):
		return self.store[k]

	def __len__(self):
		return len(self.store)

def caesar_cipher(plain_text, key):
	""" Decrypte Caesar cipher.
		In Caesar cipher, each letter of the text is replaced by the letter 
		which stands a certain number of places before or after it in the alphabet. 

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

if __name__ == "__main__":
	cli()