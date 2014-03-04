#!/usr/bin/env python3
import sys
from pprint import pprint

try:
   import anyjson
except ImportError:
   print >>sys.stderr, "TIP: pip install anyjson"
   raise

def run(*args):
   if args:
       content = file(args[0]).read()
   else:
       content = sys.stdin.read()
   struct = anyjson.deserialize(content)
   pprint(struct)
   return 0

if __name__ == '__main__':
   sys.exit(run(*sys.argv[1:]))
