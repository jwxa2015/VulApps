#!/usr/bin/env bash

echo "docker build -t $1 $2/Dockerfile"

docker build -t $1 $2
docker save -o $3 $1
# scp -P 2200 $3 qgw@192.168.1.102:/home/qgw/work/code/Shujiang/deploy/Install/hosts/images/
# rm -rf $3