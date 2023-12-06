# Peas in a Pod

Login via SSH `141.85.224.104` on port `34622` using the `ctf` user.

## Hints

1. Two public keys have the same P.
1. Follow the RSA algorithm.

## Scenario

Two authorized keys have a common prime, so it's easy to factorize N by computing gcd for each pair of two keys.
Once N is factorized, one can compute the secret key to access the computer as a privileged user and read the flag.

## Solution

Generate the private key and then use it to login to the remote user.

Use the scripts in the `sol/` folder.
Run:

```console
$ ./solution.sh
CTF{AbItOfMaThDoEsNoThUrT}
```

## Deploy

You need to have [Docker](https://docs.docker.com/engine/) installed on the system.

Enter the `deploy` directory and then build and run the Docker container:

```
$ cd deploy/

$ make

$ make run
```
