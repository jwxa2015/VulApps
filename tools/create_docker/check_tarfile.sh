#!/bin/bash

for md5file in `ls *.tar.md5`
do
	md5sum -c $md5file
done
