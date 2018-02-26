#!/bin/bash
# author zhangjie
# date 2017-02-28
CUR_DIR=$(pwd)
cp $CUR_DIR"/kbot_profile.sh" /etc/profile.d/kbot_profile.sh
echo $CUR_DIR"/kbot_profile.sh"
sed -is "s#^cur_dir#cur_dir=${PWD}#" /etc/profile.d/kbot_profile.sh
rm -f /etc/profile.d/kbot_profile.shs
cp $CUR_DIR"/kbc.py" $CUR_DIR"/kbc"
chmod +x $CUR_DIR"/kbc"