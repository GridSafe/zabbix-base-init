#!/usr/bin/python2
#

import subprocess

import json

args="ip l | grep UP | grep -Ev '(lo|@NONE|tap|NO-CARRIER|tun)' | awk  '{print $2}' | tr -d ':' | sed '/^$/d'"

netcard=subprocess.Popen(args,shell=True,stdout=subprocess.PIPE).communicate()[0].split('\n')

nets=[]

for net in netcard:
    if net == "":
	continue
    nets.append({'{#NETCARD}':net})

print json.dumps({'data':nets},indent=4,separators=(',',':'))
