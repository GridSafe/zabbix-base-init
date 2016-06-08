#!/bin/bash
#

echo -e "{"
echo -e  "  \"data\":["

netcard=`ip l | grep UP | grep -Ev '(lo|@NONE|tap|NO-CARRIER|tun|vn)' | awk  '{print $2}' | tr -d ':' | sed '/^$/d'`
disk=`mount  | grep -o '/dev/sd[a-z]' | sort | uniq | awk -F/ '{print $NF}'`


for i in $disk;do
	let n++;
done


for l in $disk;do
	
let tmp++
echo -e "\t{"
echo -e "\t    \"{#DISK_NAME}\":\"$l\""

if [ $tmp -eq $n ];then
	echo -e "\t}"
else
	echo -e "\t},"
fi

done

echo -e "  ]"
echo -e "}"

