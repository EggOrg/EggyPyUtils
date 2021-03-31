'''OS Utilities (Limited NT Support)'''

import os,socket,getpass
from os import system

def clr():
  '''Clears the screen'''
  if osName == 'posix':
    system('clear')
  if osName == 'nt':
    system('cls')

def ls(args=None):
  '''Views current files in directory'''
  if osName == 'posix':
    if args == None:
      system('ls --color=auto')
    else:
      system('ls --color=auto '+args)
  if osName == 'nt':
    system('dir')
    
dir       = ls
cls       = clr
clear     = clr
osName    = os.name
userName  = getpass.getuser()
hostName  = socket.gethostname()
