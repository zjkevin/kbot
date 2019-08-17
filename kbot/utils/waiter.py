#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#author zhangjie

#侍者模块，提供一些支线功能
import yaml
#from fabric.colors import *
from kevin_utils.strlib import newline
from utils import colorwords

#打印帮助目录
def print_help_menu(file):
    with open(file, 'rb') as f:
        d = yaml.load(f)
        for i in d["helps"]:
            colorwords.tDarkGray(i["kind"].center(120,"*"))
            if "cmds" in i:
                for x in i["cmds"]:
                    colorwords.tDarkWhite(newline.str_newline(x["cmd"] + "  " + x["content"].strip(),80,4))
            if "flows" in i:
                for x in i["flows"]:
                    content = ""
                    print(newline.str_newline(x["title"], 80, 4))
                    for i,c in enumerate(x["content"].split("|")):
                        if i == len(x["content"].split("|")) - 1:
                            content = content + c
                        else:
                            content = content + c + " " + "-->" + " "
                    print(" "*4 + content)
            print("\n")

#获取帮助命令
def get_cmds_list(file):
    cmds_list = []
    with open(file, 'rb') as f:
        d = yaml.load(f)
        for i in d["helps"]:
            if "cmds" in i:
                for x in i["cmds"]:
                    cmds_list.append(x["cmd"])
    return cmds_list  