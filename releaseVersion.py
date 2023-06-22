#!/usr/bin/python3
import sys, os
from unittest import main as mainTest


def newVersion(level=2, message=''):
  """
  Create a new version

  Args:
    level (int): which number of the version to increase 0=mayor,1=minor,2=sub
    message (str): what is the name/message
  """
  os.system('git commit -a -m "'+message+'"')
  os.system('git tag -a v0.1 -m "Version 0.1"')
  os.system('git push')
  os.system('git push origin v0.1')
  return

if __name__=='__main__':
  #do update
  if len(sys.argv)==1:
    print("**Require more arguments for creating new version 'message' 'level (optionally)' ")
    level = None
  elif len(sys.argv)==2:
    level=2
  else:
    level = int(sys.argv[2])
  if level is not None:
    message = sys.argv[1]
    newVersion(level, message)
  print("\n==============================\nAlso publish extractors\n======================")
