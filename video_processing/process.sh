#!/bin/bash

# find all mkv files and generate folder names for their output
# this is specific to the way I've LEGALLY OBTAINED the evangelion videos 
# NOTE: We're encoding to BMP for speed, will encode later for storage
rate=0.25
echo "getting matching videos with a frame rate of $rate per second"

for input_file in *.mkv
do
    echo "processing $input_file"
    dir_out=$(echo "$input_file" | cut -d'.' -f1 | cut -d'-' -f2- | cut -d'[' -f1 | cut -d' ' -f2-)
    mkdir -p "output/$dir_out"
    ffmpeg -i "$input_file" -r $rate "output/$dir_out/%02d.bmp"
done
