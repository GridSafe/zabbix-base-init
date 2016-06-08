#!/usr/bin/python2
#

import subprocess

import json

args="grep -o '\<[s,h,v]d[a-z]\>' /proc/diskstats | sort | uniq 2>/dev/null"

t=subprocess.Popen(args,shell=True,stdout=subprocess.PIPE).communicate()[0]

disks=[]

for disk in t.split('\n'):

    if len(disk) != 0:

      disks.append({'{#DISK_NAME}':disk})

print json.dumps({'data':disks},indent=4,separators=(',',':'))
