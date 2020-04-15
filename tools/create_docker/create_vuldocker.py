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

JSON_CFG = '../../lalon_vulhub.json'
vul_base_path = '../../'

def build_vul_docker():
    with open(JSON_CFG, 'r') as j:
        str = j.read()
        vul_json = json.loads(str)
    
    error_image = []
    except_image = []
    if vul_json:
        for k in vul_json:
            # print k, vul_json[k]['vul_path']
            try:
                img_cfg = vul_json[k]
                rep_tag = img_cfg['image_repository'] + ":" + img_cfg['image_tag']
                vul_path = img_cfg['vul_path']
                image_tar = img_cfg['image_tar']
                cmd = './create_vuldocker.sh {} {} {}'.format(rep_tag, os.path.join(vul_base_path, vul_path), image_tar)
                # print(cmd)
                p = subprocess.call(cmd, shell=True)
                if p:
                    error_image.append(k)
                    print("create docker:{} faild".format(k))
            except Exception as ex:
                except_image.append(k)
                print("create docker {} Except".format(k))
    
    print("create docker error :{}".format(error_image))
    print("create docker except :{}".format(except_image))


if __name__ == '__main__':
    build_vul_docker()
