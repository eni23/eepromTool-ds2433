#!/usr/bin/env python

from pprint import pprint
import argparse, subprocess, sys, os, binascii, time
from termcolor import colored, cprint

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--infile", type=str, required=True)
parser.add_argument("-1", "--one", type=int, required=True)
parser.add_argument("-2", "--two", type=int, required=True)
parser.add_argument("-3", "--three", type=int, required=True)
parser.add_argument("-4", "--four", type=int, required=True)

args = parser.parse_args()
f = open(args.infile, 'rb')
ba = bytearray(f.read())
f.close()

ba[12] = args.one
ba[28] = args.two
ba[44] = args.three
ba[60] = args.four

ff = open(args.infile, 'wb')
ff.write(ba)
ff.close()
