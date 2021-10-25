#!/bin/bash

year=$1
out="${year}.mp4"

for fn in *.mp4; do
  echo "file $fn" >> join-list.txt
done

ffmpeg -f concat -i join-list.txt -c copy "${out}"

rm join-list.txt
