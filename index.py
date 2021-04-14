#!/bin/python3
# Copyright (c) Harvey298 2021
linux = "linux-zen"
import os, sys
from sys import argv
from subprocess import run, PIPE, STDOUT, Popen
home = os.environ['HOME']
workdir = home + '/kernel'
print('Welcome to Kernel Konstructor')
def clean():
    os.chdir(workdir)
    print('Removing Kernel Source!')
    os.system('rm -rf ' + linux)
    print('Done!')
    sys.exit(5)


def make():
    os.chdir(workdir)
    print('Making your Kernel')
    getk = run(["asp","update",linux], stdout=PIPE, stderr=STDOUT)
    getd = run(["asp","export",linux], stdout=PIPE, stderr=STDOUT)
    print(getk)
    print(getd)
    os.chdir(workdir + "/" + linux)
    os.system("nano PKGBUILD")
    os.system("makepkg -scif")
    print("Done!")
    sys.exit(5)

def help():
    helpmsg = """
    -m make
    -u update/make
    -c clean up (remove kernel source)
    -h this message!
    """
    print(helpmsg)

try:
    if argv[1] == '-m':
        make()
    elif argv[1] == '-u':
        print("You could of done -m!")
        make()
    elif argv[1] == '-c':
        clean()
    elif argv[1] == '-h':
        help()
except IndexError:
    print("Ooops! you haven't told me what todo! have you tried -h?")
