#!/bin/bash
#

echo -e "{"
echo -e  "  \"data\":["

netcard=`ip l | grep UP | grep -Ev '(lo|@NONE|tap|NO-CARRIER|tun|vn)' | awk  '{print $2}' | tr -d ':' | sed '/^$/d'`

internal=
external=
tmp=0

for i in $netcard;do
	ip a s dev $i | grep '\<inet\>' &> /dev/null
	if [ $? -eq 0 ];then
		interface[k++]=$i
	fi
done
	
for j in ${interface[@]};do
	ip a s dev $j | grep '\<inet\>' | awk -F'/| ' '{print $6}' | grep -Ev '(^192.168.)|^172.16.|^10.' &> /dev/null
	if [ $? -eq 0 ];then
		external[n++]=$j
	else
		internal[m++]=$j
		tmp=1
	fi
done

if [ ${#external[@]} -ne 0 ];then
	for k in ${external[@]};do
		
	echo -e "\t{"
	echo -e "\t    \"{#EXTERNAL}\":\"$k\""
	if [ $tmp -eq 0 ] ;then
		echo -e "\t}"
	else
		echo -e "\t},"
	fi

	done
fi

if [ ${#internal[@]} -ne 0 ];then
	for l in ${internal[@]};do
		
	echo -e "\t{"
	echo -e "\t    \"{#INTERNAL}\":\"$l\""
	if [ "${internal[${#internal[*]}-1]}" == "$l" ];then
		echo -e "\t}"
	else
		echo -e "\t},"
	fi

	done
fi

echo -e "  ]"
echo -e "}"

