#!/bin/bash
#

case $1 in
ESTAB)
result=`ss -s | grep estab | awk -F" |,"  '{print $6}'`
echo $result
;;
TIMEWAIT)
result=`ss -ant | awk '{++s[$1]} END {for(k in s) print k,s[k]}' | grep 'TIME-WAIT' | awk '{print $2}'`
echo $result
;;
FINWAIT1)
result=`ss -ant | awk '{++s[$1]} END {for(k in s) print k,s[k]}' | grep 'FIN-WAIT-1' | awk '{print $2}'`
echo $result
;;
FINWAIT2)
result=`ss -ant | awk '{++s[$1]} END {for(k in s) print k,s[k]}' | grep 'FIN-WAIT-2' | awk '{print $2}'`
echo $result
;;
LASTACK)
result=`ss -ant | awk '{++s[$1]} END {for(k in s) print k,s[k]}' | grep 'LAST-ACK' | awk '{print $2}'`
echo $result
;;
LISTEN)
result=`ss -ant | awk '{++s[$1]} END {for(k in s) print k,s[k]}' | grep 'LISTEN' | awk '{print $2}'`
echo $result
;;
*)
echo "Usage: $0 (ESTAB|TIMEWAIT|FINWAIT1|FINWAIT2|LASTACK|LISTEN)"
;;
esac
