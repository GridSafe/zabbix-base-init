#!/usr/bin/python2
#

import subprocess

import json

args="lscpu | grep 'CPU(s):' | head -1 | awk '{print $NF}'"

num=subprocess.Popen(args,shell=True,stdout=subprocess.PIPE).communicate()[0].split('\n')[0]

cpus=[]

for cpu in range(0,int(num)):

    cpus.append({'{#COREID}':cpu})

print json.dumps({'data':cpus},indent=4,separators=(',',':'))
