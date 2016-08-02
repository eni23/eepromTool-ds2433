#!/usr/bin/env python

from pprint import pprint
import argparse, subprocess, sys, os, binascii, time
from termcolor import colored, cprint

parser = argparse.ArgumentParser()

parser.add_argument("-1", "--one", type=str, required=True)
parser.add_argument("-2", "--two", type=str, required=True)
parser.add_argument("-l", "--length", type=int, required=False)


args = parser.parse_args()
if not args.length:
    args.length=128

f1 = open(args.one, 'rb')
f2 = open(args.two, 'rb')
ba1 = bytearray(f1.read())
ba2 = bytearray(f2.read())

ch=0
for i in range(0,args.length):

    one = colored("{0} ".format(str(ba1[i]).rjust(3)), "red")
    two = colored("{0} ".format(str(ba2[i]).rjust(3)), "green")
    num = str(i).rjust(3)
    chs=""
    if ba1[i] != ba2[i]:
        chs = colored("changed", "yellow")
        ch+=1

    print("{0}: {1} {2} {3}".format(num, one, two, chs))


print("\n total changed: {0}".format(ch))
