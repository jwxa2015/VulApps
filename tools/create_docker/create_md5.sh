#!/bin/bash

for tar_file in `ls *.tar`
do
	echo $tar_file
	md5=`md5sum $tar_file`
	echo $md5 | tee $tar_file.md5
done

