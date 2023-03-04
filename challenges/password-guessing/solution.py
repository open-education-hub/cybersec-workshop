#!/usr/bin/python3

from pwn import *
import sys
import itertools
import random
import string

HOST = '141.85.224.104'
PORT = 20100
PASSWORD_LEN = 3

def is_right_guess(io, guess):
    io.sendline(guess)

    return io.recvline() != b'Try Again!\n'

def get_secret(io):
    return io.recv()

def break_password():
    io = remote(HOST, PORT)

    io.recvuntil(b'Start playing!\n')

    isGuessed = False
    #TODO: stop when isGuessed is True
    #TODO: use itertools.product() to generate all possible combinations
    #TODO: use the is_right_guess() function to check each and every guess

    #TODO: once is_right_guess() returns true, use get_secret(io) to get the secret
    print(get_secret(io))

def main():
    break_password()

if __name__ == '__main__':
    main()
