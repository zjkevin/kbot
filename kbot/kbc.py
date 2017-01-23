from fabric.colors import *

if __name__=="__main__":
    print yellow("current config file: no set")
    #sbc_context.set_sbt_env(synbot_env.get_synbot_ini())
    #cmds_list = synbot_waiter.get_cmds_list()
    #if len(sys.argv) == 1 or (len(sys.argv) > 1 and sys.argv[1] in ("--help","-h")):
    #  synbot_waiter.print_help_menu()
    #  sys.exit(0)
    #elif len(sys.argv) > 1 and (sys.argv[1] in cmds_list or "-hide" in sys.argv):
    #  def calf(type,**arg):
    #    result = {"-i":lambda:synbot_clusterinstall.install_cluster(**arg),
    #            "-i-all":lambda:synbot_clusterinstall.install_all_cluster(**arg),
    #            "-rebuild":lambda:synbot_clusterinstall.rebuild_cluster(**arg),
    #            "-rebuild-all":lambda:synbot_clusterinstall.rebuild_all_cluster(**arg),
    #            "-restart":lambda:synbot_clusterstartstop.restart_cluster(**arg),
    #            "-start":lambda:synbot_clusterstartstop.start_cluster(**arg),
    #            "-stop":lambda:synbot_clusterstartstop.stop_cluster(**arg),
    #            "-d":lambda:synbot_clusterconf.define_cluster_config(**arg),
    #            "-p":lambda:synbot_clusterconf.set_config_file_path(**arg),
    #            "-e":lambda:synbot_clusterconf.edit_config_file(**arg),
    #            "-s":lambda:synbot_info.check_sources(**arg),
    #            "-cn":lambda:synbot_info.get_cn_info(**arg),
    #            "-parse":lambda:synbot_clusterconf.parse_cluster_config(**arg),
    #            "-img":lambda:synbot_hv.update_img_for_hv(**arg),
    #            "-hv":lambda:synbot_hv.hv_init(**arg),
    #            "-scanpv":lambda:__scan_pv(**arg),
    #            "-scandisk":lambda:synbot_disk.scan_disk(**arg),
    #            "-ssh":lambda:synbot_network.ssh_dispense(**arg),
    #            "-ping":lambda:synbot_network.ping_host(**arg),
    #            "-socket":lambda:synbot_network.socket_host(**arg),
    #            "-createhosts":lambda:synbot_network.create_hosts(**arg),
    #            "-sendhosts":lambda:synbot_network.send_hosts(**arg),
    #            "-en":lambda:synbot_network.edit_network_config_file(**arg),
    #            "-vmclear":lambda:synbot_vm.vm_clear(**arg),
    #            #"-debiansource":lambda:__debian_source(**arg),
    #            #"-pipsource":lambda:__pip_source(**arg),
    #            "-scanmem":lambda:synbot_mem.scan_mem(**arg),
    #            #"-zk":lambda:synbot_zk.zk_install(**arg),
    #            "-hvmode":lambda:synbot_setting.change_mode("hv"),
    #            "-vmmode":lambda:synbot_setting.change_mode("vm"),
    #            "-diskformat":lambda:synbot_disk.format_disk(**arg),
    #            "-diskmount":lambda:synbot_disk.mount_disk(**arg)
    #            }
    #    result[type]()
    #  sbcenv = sbc_context.get_sbt_env()
    #  sbcenv.cluster_username = 'hadoop'
    #  sbc_context.set_sbt_env(sbcenv)
    #  print yellow("synbot base information start".center(80,"-"))
    #  print yellow("mode:%s" % sbcenv.base)
    #  if sbcenv.cluster_config_path == "" and sbcenv.cluster_config_file == "":
    #    print yellow("current config file: no set")
    #  else:
    #    print yellow("current config file:%s" % synbot_tools.path_join(sbcenv.cluster_config_path,sbcenv.base,sbcenv.cluster_config_file))
    #  if sbcenv.base == "vm":
    #    print yellow("network config file:%s" % synbot_tools.path_join(os.path.abspath("."),"conf/network_conf_vm.yml"))
    #  else:
    #    print yellow("network config file:%s" % synbot_tools.path_join(os.path.abspath("."),"conf/network_conf_hv.yml"))
    #  print yellow("synbot base information end".center(80,"-"))
    #  args_list = sys.argv
    #  if "-hide" in args_list:
    #    args_list.remove("-hide")
    #  calf(args_list[1],args=args_list[2:])                
    #else:
    #  print("Try `sbc --help' for more information.")
    #  sys.exit(0)