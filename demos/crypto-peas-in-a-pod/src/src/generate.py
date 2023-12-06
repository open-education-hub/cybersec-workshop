#!/usr/bin/env python
# coding: utf-8

import rsa
import math
import random
import os

NUM_KEYS = 10
NUM_BITS = 2048
AUTHORIZED_KEYS = '../public/authorized_keys'

# Generate NUM_KEYS-1 keys

print('Generating keys...')

keys = []
for i in range(NUM_KEYS-1):
    print(f'Generating key {i+1}')
    key = rsa.newkeys(NUM_BITS)
    keys.append(key)


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


# Generate one key to match p factor with another key

old_twin_sk = keys[0][1]
while True:
    aux_sk = rsa.newkeys(NUM_BITS)[1]
    e = aux_sk.e
    p = old_twin_sk.p
    q = aux_sk.q
    n = p * q
    phi = (p-1) * (q-1)

    d = getModInverse(e, phi)

    if d is None:
        continue

    new_twin_pk = rsa.PublicKey(n, e)
    new_twin_sk = rsa.PrivateKey(n, e, d, p, q)
    new_twin_key = (new_twin_pk, new_twin_sk)
    break

keys.append(new_twin_key)

# Shuffle keys

random.shuffle(keys)

USERS = [
    b'peter@acs.upb.ro',
    b'james@acs.upb.ro',
    b'john@acs.upb.ro',
    b'matthew@acs.upb.ro',
    b'thomas@acs.upb.ro',
    b'andrew@acs.upb.ro',
    b'mary@acs.upb.ro',
    b'joanna@acs.upb.ro',
    b'martha@acs.upb.ro',
    b'lazarus@acs.upb.ro',
]

with open(AUTHORIZED_KEYS, 'wb') as f:
    i = 0
    for _, sk in keys:
        pem_sk = sk.save_pkcs1('PEM')

        # Open as cryptography sk
        from cryptography.hazmat.primitives import serialization
        from cryptography.hazmat.backends import default_backend

        private_key = serialization.load_pem_private_key(
            pem_sk,
            password=None,
            backend=default_backend()
        )

        # Compute pk ssh
        ssh_pk = private_key.public_key().public_bytes(
           encoding=serialization.Encoding.OpenSSH,
           format=serialization.PublicFormat.OpenSSH,
        )

        ssh_pk += b' ' + USERS[i]

        # Write pk to authorized_keys
        f.write(ssh_pk + b'\n')

        i += 1
