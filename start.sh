#!/bin/bash
export LD_PRELOAD=/usr/lib/`cd /usr/lib && find -name v4l1compat.so`
data_time=`date +'%Y-%m-%d'` && nohup python main.py >>./log/all_run_info-$data_time.log &
#data_time=`date +'%Y-%m-%d'` && nohup python main.py 1>./log/run_info-$data_time.log 2>./log/run_error-$data_time.log &

