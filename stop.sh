#!/bin/bash
ps -ef | grep main.py | grep -v grep | awk '{print $2}' | xargs kill -9
