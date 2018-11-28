""" digital_wallet.py

    Generating a key-pair, associate with RSA algorithm.
    
    References:
      HAC - "Handbook of Applied Cryptography",Menezes, van Oorschot, Vanstone; 1996
      Professor Paul A. Lambert's source code: 
        https://github.com/CryptoUSF/Course-Material/blob/master/code/prime.py
	
	Author: Meiling Liu
"""

import pyqrcode, png, os, random, sympy
# from Crypto.PublicKey import RSA 
from prime import new_random_prime


def xgcd(a,b):
    """Extended GCD:
    Returns (gcd, x, y) where gcd is the greatest common divisor of a and b
    with the sign of b if b is nonzero, and with the sign of a if b is 0.
    The numbers x,y are such that gcd = ax+by.
	
	Reference from: https://anh.cs.luc.edu/331/code/xgcd.py
    """
    prevx, x = 1, 0;  prevy, y = 0, 1
    while b:
        q, r = divmod(a,b)
        x, prevx = prevx - q*x, x  
        y, prevy = prevy - q*y, y
        a, b = b, r
    # return a, prevx, prevy
    return prevx

if __name__ == '__main__':
	print("Generating new address...")

	message_length = 2
	p = new_random_prime(message_length, False)
	q = new_random_prime(message_length, False)

	n = p*q

	phi = (p-1)*(q-1)

	# primes = [i for i in range(1, phi-1) if sympy.isprime(i)]
	primes = [i for i in range(1, 20) if sympy.isprime(i)]
	e = random.choice(primes)

	# e * d ≡ 1 mod φ(n)
	d = xgcd(e, phi)

	publickey = "your public key is (e=" + str(e) + ", n=" + str(n) + ")"

	privatekey = "your private key is (p=" + str(p) + ", q=" + str(q) + ", d=" + str(d) + ")"

	qr = pyqrcode.create(publickey)
	qr.png('pubk.png', scale=5)

	new_qr = pyqrcode.create(privatekey)
	new_qr.png('prik.png', scale=5)

	print("Finished...Please check qr code.")

	""" 
	  Apply RSA Library to generate key-pair

	"""

	# key = RSA.generate(2048)
	# print(key)
	# privatekey = key.exportKey()
	# publickey = key.publickey().exportKey()
	# print(publickey)
	# print(privatekey)

	# hash_object = hashlib.sha256(publickey)
	# print(hash_object.hexdigest())

	# qr = pyqrcode.create(hash_object.hexdigest())
	# qr.png('pubk.png', scale=5)

	# hash_object1 = hashlib.sha256(privatekey)
	# print(hash_object1.hexdigest())
	# new_qr = pyqrcode.create(hash_object1.hexdigest())
	# new_qr.png('prik.png', scale=5)



