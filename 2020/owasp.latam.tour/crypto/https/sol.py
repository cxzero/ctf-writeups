#!/usr/bin/env python
import gmpy2

from Crypto.Util.number import inverse
from Crypto.PublicKey import RSA
import math

# Read certificates

#1
with open("cert1.der", "rb") as f1:
	key1 = RSA.importKey(f1.read())
	n1 = key1.n
	e1 = key1.e
	print("key1",key1)
	print("n1=",n1)
	print("e1=",e1)

#2
with open("cert2.der", "rb") as f2:
	key2 = RSA.importKey(f2.read())
	n2 = key2.n
	e2 = key2.e
	print("key2",key2)
	print("n2=",n2)
	print("e2=",e2)

# private key will be d1
# private key will be d2
gcd = math.gcd(n1,n2)
print("gcd=",gcd)

# integer division
# n = p*q
q1 = n1 // gcd
print("q1=",q1)

q2 = n2 // gcd
print("q2=",q2)

# inverse multiplication 
# phi = (p-1)*(q-1), where p = gcd
phi1 = (gcd-1)*(q1-1)
d1 = inverse (e1, phi1)
print("d1=",hex(d1))

phi2 = (gcd-1)*(q2-1)
d2 = inverse (e2, phi2)
print("d2=",hex(d2))

# export public keys to file to PEM format
with open("publicKey1.pem", "wb") as f3:
	f3.write(key1.publickey().exportKey('PEM'))

with open("publicKey2.pem", "wb") as f3:
	f3.write(key2.publickey().exportKey('PEM'))

# https://www.dlitz.net/software/pycrypto/api/current/Crypto.PublicKey.RSA-module.html
privateKey1=RSA.construct([n1, e1, d1, gcd, q1])
print(privateKey1)
with open("privateKey1.pem", "wb") as f3:
	f3.write(privateKey1.exportKey('PEM'))

privateKey2=RSA.construct([n2, e2, d2, gcd, q2])
print(privateKey2)
with open("privateKey2.pem", "wb") as f4:
	f4.write(privateKey2.exportKey('PEM'))

# export public keys to file to DER format (from just created private keys to verify)
with open("publicKey1.der", "wb") as f3:
	f3.write(privateKey1.publickey().exportKey('DER'))

with open("publicKey2.der", "wb") as f4:
	f4.write(privateKey2.publickey().exportKey('DER'))
