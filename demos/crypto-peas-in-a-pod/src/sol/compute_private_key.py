#!/usr/bin/env python
# coding: utf-8

import rsa
import math
from Crypto.PublicKey import RSA
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

AUTHORIZED_KEYS = '../public/authorized_keys'


def getModInverse(a, m):
    if math.gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


with open(AUTHORIZED_KEYS, 'rb') as f:
    public_keys_ssh = f.read().split(b'\n')[:-1]

Ns = []
for pk_ssh in public_keys_ssh:
    try:
        pk_ssh = b' '.join(pk_ssh.split(b' '))

        pk = RSA.importKey(pk_ssh)
        Ns.append(pk.n)
    except Exception:
        pass

for i in range(len(Ns)):
    for j in range(i+1, len(Ns)):
        if i == j:
            continue
        gcd = math.gcd(Ns[i], Ns[j])
        if gcd > 1:
            # print('Eureka!', i, j, gcd)
            n = Ns[i]
            p = gcd
            q = n // p
            e = pk.e
            phi = (p-1) * (q-1)
            d = getModInverse(e, phi)

sk = rsa.PrivateKey(n, e, d, p, q)

pem_sk = sk.save_pkcs1('PEM')

# Open as cryptography sk
private_key = serialization.load_pem_private_key(
    pem_sk,
    password=None,
    backend=default_backend()
)

# Write sk
with open('sol_key', 'wb') as g:
    g.write(pem_sk)

# Compute pk ssh
ssh_pk = private_key.public_key().public_bytes(
   encoding=serialization.Encoding.OpenSSH,
   format=serialization.PublicFormat.OpenSSH,
)

# Write pk
with open('sol_key.pub', 'wb') as g:
    g.write(ssh_pk)
