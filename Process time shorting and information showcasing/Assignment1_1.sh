#!/bin/bash
sortingProcessTime() {
	touch sorted.txt
	n=$(($1+7))
	printf "%-16s %-16s\n" "process id"  "execution time"
	top -b -n 1 | sed -n "8,$n p" > sorted.txt
	sort -r -k11 sorted.txt|awk '{printf ("%-16s %-16s\n", $1,$11 )}'
	
}
#Input from top
printf "Give the value of line n: "
read n
sortingProcessTime $n

