#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#author zhangjie
import platform

#当前控制机状态

def info():
    sysstr = platform.system()
    platformstr = platform.platform()
    architecturestr = platform.architecture()
    python_version = platform.python_version()
    return "sys:{system} platform:{platform} architecture:{architecture} python_version:{python_version}".format(system=sysstr,platform=platformstr,architecture=architecturestr,python_version=python_version)

if __name__ == "__main__":
    print(info())