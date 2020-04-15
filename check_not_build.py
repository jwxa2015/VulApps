#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file     : createvul
# @date     : 2020/1/15
# @author   : q
# @email    : qiuguowei@jingweixinan.com
# @project  : 'PyCharm'
# @copyright: (c)LalonSec Co., Ltd.
# @url      : https://www.jingweixinan.com

__author__ = 'q'

import json
import os, subprocess

JSON_CFG = 'lalon_vulhub.json'


def check_vulapp():
    with open(JSON_CFG, 'r') as j:
        str = j.read()
        vul_json = json.loads(str)
    vul_path = []
    for vul in vul_json:
        # print(vul)
        vul_path.append(os.path.join(vul_json[vul]['vul_path'],'Dockerfile'))

    cur_dir = "./"

    print("exists:{}".format(len(vul_path)))
    print(vul_path)

    print("==================================")
    print("not exists")

    for root, dirs, files in os.walk(cur_dir):
        for f in files:
            if f == "Dockerfile":
                path = os.path.join(root,f)
                path = path.lstrip(cur_dir)
                if path not in vul_path:
                    print(path)


if __name__ == '__main__':
    check_vulapp()
