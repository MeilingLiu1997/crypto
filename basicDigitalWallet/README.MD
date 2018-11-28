# Preliminary Design - Digital Wallet
A design/preliminary implementation of hardware wallet

## Getting Started
This program uses the version of Python 3

### How to set up
This program import pyqrcode & png. Please install packages by following below:
```
pip3 install pyqrcode
```
```
pip3 install pypng
```

## Design
Hardware wallet stores the user's private keys in a secure hardware device. This program will generate random public key pair, and store into QR code. Users don't need to memorize or backup seed/phrase.

### Advantages
* private keys are often stored in a protected area of a microcontroller, and cannot be transferred out of the device in plaintext
* immune to computer viruses that steal from software wallets
* can be used securely and interactively, private keys never need to touch potentially-vulnerable software
* much of the time, the software is open source, allowing a user to validate the entire operation of the device

### Why choose QR code?
A QR code can easily represent this amount of data in a machine-readable manner and do so reliably. The QR code can contain other information as well -- such as an amount and a message and other fields as well.

So with a mobile, a convenient way to pass that data is for the payment recipient (e.g., a merchant) to display a QR code with the Bitcoin address for the transaction, and then for the person paying to scan that QR code to obtain the bitcoin address.

Detailed see [Barcode scanner](https://play.google.com/store/apps/details?id=com.google.zxing.client.android) from ZXing

* Try online [bitcoin qr code generator](https://www.bitcoinqrcodegenerator.win/bitcoin-wallet-generator/index.php)

### Generate Key Pair
```
from Crypto.PublicKey import RSA

new_key = RSA.generate(length)
public_key = new_key.publickey().exportKey("PEM")
private_key = new_key.exportKey("PEM")
```

### SHA 256 Hash Function (hash key-pair)
```
import hashlib, binascii

hash_object = hashlib.sha256(publickey)
print(hash_object.hexdigest())
hash_object1 = hashlib.sha256(privatekey)
print(hash_object1.hexdigest())
```

### Create QR Code
```
import pyqrcode, png

qr = pyqrcode.create(hash_object.hexdigest())
qr.png('pubk.png', scale=5)
new_qr = pyqrcode.create(hash_object1.hexdigest())
new_qr.png('prik.png', scale=5)
```

### Wallet Code Reference
* https://github.com/goodhamgupta/Digital-Wallet/blob/master/wallet/views.py
* https://github.com/CityOfZion/neo-python/blob/master/neo/Wallets/Wallet.py

## Author
* **Meiling Liu** [@Github](https://github.com/MeilingLiu1997)


## Acknowledgments
* This program includes some reference codes from internet, detailed will be found in reference link.

## References
* [Types of hardware wallet](https://en.bitcoin.it/wiki/Hardware_wallet)
* [QR code usage in real transaction](https://bitcoin.stackexchange.com/questions/8111/what-are-qr-codes-and-how-do-you-use-them-as-request-payment-from-wallet)
* [NEWS store private keys with encrypted QR codes](https://www.coindesk.com/crypto-wallet-to-replace-private-keys-with-encrypted-qr-codes/)
* [blockchain-bitcoin](http://adilmoujahid.com/posts/2018/03/intro-blockchain-bitcoin-python/)
* [public-key Vs. public address](https://www.reddit.com/r/Bitcoin/comments/3filud/whats_the_difference_between_public_key_and/)