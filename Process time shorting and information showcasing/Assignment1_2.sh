#!/bin/bash
sortingProcessList() {
	touch top.txt
	touch topFull.txt
	top -b -n 1 >topFull.txt
	sed -n "7,$ p" topFull.txt > temp.txt
    	awk '{printf ("%-8s %-8s %-8s %-8s\n",$1,$2,$9,$12)}' temp.txt > top.txt
	rm temp.txt

}

sortingProcessList

