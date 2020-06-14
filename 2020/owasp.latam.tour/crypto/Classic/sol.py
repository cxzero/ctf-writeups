#!/usr/bin/env python
import hashlib, binascii, base64

def base64_coding(flag):
    return base64.b64encode(bytes([m % 251 for m in flag]))

def encrypt(flag, a, b):
    return base64.b64encode(bytes([(m*a + b) % 251 for m in flag]))

# Brute force a and b
def discover_a_b(cflag):
	start=b'owasp{'
	listS=list(start)

	for i in range(0,250):
		for j in range(0,250):
			partial = encrypt(listS, i, j)
			if cflag.startswith(partial.decode("utf-8")[:5]):
				print("Got it!")
				print("a = {0}; b = {1}".format(i,j))
				return i, j

#Python program for Extended Euclidean algorithm
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		gcd, x, y = egcd(b % a, a)
		return (gcd, y - (b//a) * x, x)

def decrypt(cflag, a, b):
    t=base64.b64decode(cflag)
    #print(list(t))
    M = egcd(a,-251)[1]
    return [((n-b)*M) % 251 for n in list(t)]

if __name__ == "__main__":
	c="G1etOaB1yzm+y57LOZ68GwwbnsuCnlUbr0aeVa2CvBuRnss5nkiRnryCrTnpvBuElA=="

	(a, b) = discover_a_b(c)

	message = decrypt(c, a, b)
	print(bytes(message))
