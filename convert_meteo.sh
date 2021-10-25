#!/bin/bash

year=$1
month=$2
out="${year}-${month}.mp4"

for fn in $year/$month/*.webm; do
  echo "file $fn" >> concat-list.txt
done

ffmpeg -f concat -i concat-list.txt -r 48 -filter:v "setpts=0.5*PTS" "${out}"

rm concat-list.txt
