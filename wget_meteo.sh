#!/bin/bash

year=$1
url="https://meteo.physic.ut.ee/webcam/uus/archive/${year}/"

wget -np --limit-rate=450k --random-wait -e robots=off -r -A webm "${url}"
