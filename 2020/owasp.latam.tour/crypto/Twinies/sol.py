#!/usr/bin/env python
import gmpy2

from Crypto.Util.number import inverse

n=45720209399092609060247331423255424241170055107973953458271640392869624838766054503760852992288576521459387170172458092315240096664794016740408557086906358265155516315638078606022954058972155136137833601211955426365850509613205091618083103329097606562425277795518890808709538832775026622416017913127626991363

# flag
c=934823870401720571770940536983827532541532264110792247976024985418244412743604407358056591962343648521552797131852437614792653820972434515432463101685789655216201772510885631474758640722277871266200955144742110309904509837117246309842896817669466689311205214308586595637513364406852974847184166150381601183

e=65537

def fermat_factor(n):
	assert n % 2 != 0

	a = gmpy2.isqrt(n)
	b2 = gmpy2.square(a) - n

	while not gmpy2.is_square(b2):
	    a += 1
	    b2 = gmpy2.square(a) - n

	p = a + gmpy2.isqrt(b2)
	q = a - gmpy2.isqrt(b2)

	return int(p), int(q)

if __name__ == "__main__":
	(p, q) = fermat_factor(n)

	print("p = {}".format(p))
	print("q = {}".format(q))

	phi = (p-1)*(q-1)
	d = inverse (e, phi)
	m = pow (c, d, n)

	print(m)
	print(hex(m))

	hex_string = str(hex(m))[2:]
	bytes_object = bytes.fromhex(hex_string)
	ascii_string = bytes_object.decode("ASCII")

	print(ascii_string)