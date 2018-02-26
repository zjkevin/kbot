#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#author zhangjie
import logging
import logging.config
import codecs
import yaml
import os
import sys
from fabric.colors import *

from utils import waiter

os.chdir(os.environ["SYNBOT_HOME"])

with codecs.open('./conf/logging.yaml', 'r', 'utf-8') as logging_file:
  logging.config.dictConfig(yaml.load(logging_file))
#日志级别
#CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
logger = logging.getLogger(__name__)

if __name__=="__main__":
    #print(yellow("current config file: no set"))
    #logger.info("info")
    #logger.debug("info")
    #print(green("current config file: no set"))
    #print(yellow("11111"))
    #arg_parser = argparse.ArgumentParser()
    #arg_parser = argparse.ArgumentParser()
    #arg_parser.add_argument('-n', '--nfs', required=True, help="nfs list string list this:192.168.110.187:/home/hadoop/nfstest,192.168.1.1:/home/hadoop/nfs1,192.168.1.2:/home/hadoop/nfs2,192.168.1.2:/home/hadoop/nfs3", type=str)
    #parser_args = arg_parser.parse_args()
    #nfs_mount_check(parser_args.nfs)
    #sbc_context.set_sbt_env(synbot_env.get_synbot_ini())
    cmds_list = waiter.get_cmds_list("./conf/help_menu.yaml")
    if len(sys.argv) == 1 or (len(sys.argv) > 1 and sys.argv[1] in ("--help","-h")):
      waiter.print_help_menu("./conf/help_menu.yaml")
      sys.exit(0)
    elif len(sys.argv) > 1 and (sys.argv[1] in cmds_list or "-hide" in sys.argv):
      def calf(type,**arg):
        result = {"-i":lambda:None,
                "-i-all":lambda:None,
                "-rebuild":lambda:None,
                "-rebuild-all":lambda:None,
                "-restart":lambda:None,
                "-start":lambda:None,
                "-stop":lambda:None,
                "-d":lambda:None,
                "-p":lambda:None,
                "-e":lambda:None,
                "-s":lambda:None,
                "-cn":lambda:None,
                "-parse":lambda:None,
                "-img":lambda:None,
                "-hv":lambda:None,
                "-scanpv":lambda:None,
                "-scandisk":lambda:None,
                "-ssh":lambda:None,
                "-ping":lambda:None,
                "-socket":lambda:None,
                "-createhosts":lambda:None,
                "-sendhosts":lambda:None,
                "-en":lambda:None,
                "-vmclear":lambda:None,
                #"-debiansource":lambda:__debian_source(**arg),
                #"-pipsource":lambda:__pip_source(**arg),
                "-scanmem":lambda:None,
                #"-zk":lambda:synbot_zk.zk_install(**arg),
                "-hvmode":lambda:None,
                "-vmmode":lambda:None,
                "-diskformat":lambda:None,
                "-diskmount":lambda:None
                }
        result[type]()
      #sbcenv = sbc_context.get_sbt_env()
      #sbcenv.cluster_username = 'hadoop'
      #sbc_context.set_sbt_env(sbcenv)
      #print yellow("synbot base information start".center(80,"-"))
      #print yellow("mode:%s" % sbcenv.base)
      #if sbcenv.cluster_config_path == "" and sbcenv.cluster_config_file == "":
      #  print yellow("current config file: no set")
      #else:
      #  print yellow("current config file:%s" % synbot_tools.path_join(sbcenv.cluster_config_path,sbcenv.base,sbcenv.cluster_config_file))
      #if sbcenv.base == "vm":
      #  print yellow("network config file:%s" % synbot_tools.path_join(os.path.abspath("."),"conf/network_conf_vm.yml"))
      #else:
      #  print yellow("network config file:%s" % synbot_tools.path_join(os.path.abspath("."),"conf/network_conf_hv.yml"))
      #print yellow("synbot base information end".center(80,"-"))
      args_list = sys.argv
      if "-hide" in args_list:
        args_list.remove("-hide")
      calf(args_list[1],args=args_list[2:])                
    else:
      print("Try `sbc --help' for more information.")
      sys.exit(0)