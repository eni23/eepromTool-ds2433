#!/usr/bin/env python

from pprint import pprint
import argparse, subprocess, sys, os, binascii, time, subprocess
from termcolor import colored, cprint

parser = argparse.ArgumentParser()
parser.add_argument("-i","--infile", type=str, required=True)
parser.add_argument("-o","--outfile", type=str, required=True)
parser.add_argument("-u","--upper", type=str, required=False, default="1")
parser.add_argument("-l","--lower", type=str, required=False, default="1")
parser.add_argument("-m","--middle", type=str, required=False, default="1")
parser.add_argument("-f","--flash", action="store_true")

args = parser.parse_args()

bf = open(args.infile, 'rb')
ba = bytearray(bf.read())

## upper
#variant 1
ba[15]=234
ba[31]=41
ba[47]=161
# variant 2
if (args.upper=="2"):
    ba[15]=87
    ba[31]=150
    ba[47]=14
## middle
# variant 1
ba[63]=0
# variant 2
if (args.middle=="2"):
    ba[63]=109

#lower
ba[120]=238
ba[121]=144
ba[122]=30
if (args.lower=="2"):
    ba[120]=98
    ba[121]=43
    ba[122]=38

of  = open(args.outfile, 'wb')
of.write(ba)
of.close()
bf.close()

# dbg
l=0
for i in range(0,128):
    s = str(ba[i]).rjust(3)

    if i == 63: s = colored(s, "red")
    if i in [15,31,47]: s = colored(s,"green")
    if i in [120,121,122]: s = colored(s,"yellow")

    print("{0} ".format(s), end="");
    l+=1
    if (l==16):
        l=0
        print("")


if (args.flash):
    subprocess.check_call([
        "./tool.py",
        "-l",
        "-f",
        args.outfile
    ])
