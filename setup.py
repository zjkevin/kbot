# coding:utf-8

from setuptools import setup

setup(
        name='kbot',     # 包名字
        version='0.1.0',   # 包版本
        description='This is a tools for operator',   # 简单描述
        author='zhangjie',  # 作者
        author_email='zhangjiesoft@163.com',  # 作者邮箱
        packages=['kbot'],                 # 包
        install_requires=['fabric','ansible==2.8.4']
)
