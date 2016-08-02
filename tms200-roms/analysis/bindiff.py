#!/usr/bin/env python

from pprint import pprint
import argparse, subprocess, sys, os, binascii, time
from termcolor import colored, cprint

parser = argparse.ArgumentParser()

parser.add_argument("files", nargs="+")
parser.add_argument("-n","--nomatching", action="store_true")

args = parser.parse_args()


data = []
ftable = []
i=0
for binfile in args.files:
    bf = open(binfile, 'rb')
    ba = bytearray(bf.read())
    dd = []
    for c in range(0,128):
        dd.append(ba[c])
    data.append(dd)
    ftable.append(binfile)
    i+=1

data_vertical = []
for i in range(0,128):
    linearr = []
    for j in range(0, len(data)):
        linearr.append(data[j][i])
    data_vertical.append(linearr)


for i in range(0,len(ftable)):
    print("{0}: {1}".format(i, ftable[i]));


for i in range(0,127):
    st = list(set(data_vertical[i]))
    nc = str(i).rjust(3)

    sl = str(len(st)).rjust(3)
    cc="white"
    if len(st)==2: cc="yellow"
    elif len(st)>2: cc="green"

    sl = colored(sl,cc)
    nc = colored(nc, cc)

    os="{0} {1}\t\t".format(nc, sl)
    st = list(set(data_vertical[i]))
    for j in range(0, len(ftable)):
        d=str(data_vertical[i][j]).rjust(3)
        cx=cc
        if (len(st)==2):
            if (st[1]==data_vertical[i][j]):
                cx="red"
        os+=colored("{0} ".format(d), cx)

    os+=colored("\t{0}".format(st), cc)

    if (args.nomatching):
        if (cc!="white"): print(os)
    else: print(os)
