#!/bin/bash

# find all mkv files and generate folder names for their output
# this is specific to the way I've LEGALLY OBTAINED the evangelion videos 
rate=0.25
echo "getting matching videos with a frame rate of $rate per second"

for input_file in *.mp4
do
    echo "processing $input_file"
    dir_out=$(echo $input_file | cut -d'.' -f1)
    mkdir -p "output/$dir_out"
    ffmpeg -i "$input_file" -r $rate -vf scale=480:360 "output/$dir_out/%02d.png"
done
