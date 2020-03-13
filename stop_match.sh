#!/bin/bash

for pid in $(ps -ef | grep 'python3 smash_bros_stuff' | awk '{print $2}'); do kill -9 $pid; done
