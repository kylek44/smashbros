#!/bin/bash


#sed  's/\n/ /g' ./matches/parsed$1 > ./matches/lbr_parsed$2

tr '\n' ' ' < ./matches/parsed$1 > ./matches/lbr_parsed$2



