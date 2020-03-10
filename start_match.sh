#!/bin/bash

num_players=$1
playerone_name=$2
playerone_port='/dev/ttyACM0'
playertwo_port='/dev/ttyACM1'

if [ $num_players -eq 1 ]
then
	python3 smash_bros_stuff.py $playerone_port $playerone_name
else
	playertwo_name=$3
	python3 smash_bros_stuff.py $playerone_port $playerone_name &
	python3 smash_bros_stuff.py $playertwo_port $playertwo_name &
fi
