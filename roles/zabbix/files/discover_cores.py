#!/usr/bin/python2
#

import subprocess

import json

args="lscpu | grep 'Core(s) per socket:' | awk '{print $NF}'"

num=subprocess.Popen(args,shell=True,stdout=subprocess.PIPE).communicate()[0].split('\n')[0]

cores=[]

for core in range(0,int(num)):

      cores.append({'{#COREID}':core})

print json.dumps({'data':cores},indent=4,separators=(',',':'))
