# Peas in a Pod

You have on you our hands an `authorized_keys` file that will get you access via SSH to the remote system `141.84.224.104` on port `34622` with the user `ctf`.
Get the flag and submit it on the [CTF platform](https://workshop-ctf.security.cs.pub.ro/challenges).

## Walkthrough

The `authorized_keys` file consists of a series of public SSH keys.
The keys are generated using the [RSA algorithm](https://en.wikipedia.org/wiki/RSA_(cryptosystem)).

Individually, these public keys are virtually impossible to break.
But we have information that two keys are using the same prime number `p` as part of their generation;
this is something uncommon and frowned upon in the crypto community;
but we can abuse it.

So our idea is to walk through all public keys and compute the greatest common divisor (GCD) for all possible pairs of two keys.
If the GCD is greater than one, then that GCD is the prime number `p` for both keys in the pair.

With `p` compute we can compute the pairing prime number `q` for one of the keys.
We do that by dividing `n` (part of the public key) to `p`, since `n = p * q`.
With `p` and `q` now computed, we can compute the other numbers `e` (exponent) and `d` (the multiplicative inverse).
And, with all them together we can now compute the private SSH key.

With the private SSH key generated we can login to the remote system and get the flag:

```console
$ ssh -i sol_key ctf@141.85.224.104 -p 34622

ctf@6c6a1d2011c1:~$ cat /home/ctf/flag
CTF{AbItOfMaThDoEsNoThUrT}
```

The program to generate the private key is in `src/sol/compute_private_key.py`.

You can quickly call it, and get the flag, by using the `solution.sh` script in the `src/sol/` directory:

```console
$ ./solution.sh
CTF{AbItOfMaThDoEsNoThUrT}
```
