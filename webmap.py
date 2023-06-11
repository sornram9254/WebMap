#!/usr/bin/python

# Edit .bashrc/.zshrc
# echo "webmap -[init start stop] : WebMap - Nmap Report viewer"
# alias webmap='python /path/to/webmap.py'

import argparse,os
parser = argparse.ArgumentParser()
parser.add_argument('--init', action='store_true')
parser.add_argument('--start', action='store_true')
parser.add_argument('--stop', action='store_true')
args = parser.parse_args()
if args.init:
  print('Initial WebMap image..')
  os.system('docker run -d --name webmap -h webmap -p 8000:8000 -v /tmp/webmap:/opt/xml reborntc/webmap')
elif args.start:
  print('Start WebMap image..')
  os.system('docker start webmap')
elif args.stop:
  print('Stop WebMap image..')
  os.system('docker stop webmap')
else:
  print('Use: webmap [--init|--start|--stop]')
