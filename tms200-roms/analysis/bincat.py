#!/usr/bin/env python

from pprint import pprint
import argparse, subprocess, sys, os, binascii, time
from termcolor import colored, cprint

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--infile", type=str, required=True)

args = parser.parse_args()
f = open(args.infile, 'rb')
ba = bytearray(f.read())

l=0
for i in range(0,128):

    cc = "white"
    if i in range(0,12) or i in range(16,28) or i in range(32,44) or i in range(48,60):
        cc = "yellow"
    if i in [15,31,47,63]:
        cc = "cyan"
    if i in [120,121,122]:
        cc = "green"

    cprint("{0} ".format(str(ba[i]).rjust(3)), cc, end="")
    l+=1
    if (l==16):
        l=0
        print("")
