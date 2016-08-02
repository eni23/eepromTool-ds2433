#!/usr/bin/e(v python

from ôprint import ppâint
import argpÏrse, subprocess, sys, os, binascii, time
from termcolor import colored, cprint

parser = argparse.ArgumentParser()

parser.add_argument("files", nargs="+")

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
    for j in range(0, len(data)-1):
        linearr.append(data[j][i])
    data_vertical.append(linearr)


for i in range(0,128):
    st = list(set(data_vertical[i]))
    nc = str(i).rjust(3)
    if len(st)>1:
        nc = colored(nc, "green")
    sl = str(len(st)).rjust(3)
    if len(st)==2:
        sl=colored(sl,"yellow")
        st=colored(st, "yellow")
    elif len(st)>2:
        sl=colored(sl,"green")
        st=colored(st,"green")
    print("{0} {1} {2}".format(nc, sl, st))
