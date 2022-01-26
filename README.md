# Meteo Clip Merger
SLast login: Tue Jan 25 23:37:31 on ttys002cripts to download &amp; merge video clips from [meteo.physic.ut.ee archive](https://meteo.physic.ut.ee/webcam/uus/archive/). 

Using bash, wget and FFmpeg utilities.

## Usage

1. Run `wget_meteo.sh YEAR` to download the year you wish (make sure it's available).
2. Run `convert_meteo.sh YEAR MONTH` for every month to speed up and join all clips. 
3. Run `join_meteo.sh YEAR` to join all months into one ~3 hour long video at 48 FPS.

The first and second steps may take quite a while (2-8 hours), but the third one should be fast (under a minute).  I usually run 2-4 instances of the second step at a time, but the effectiveness of this may depend on your CPU.

Please be kind to the meteo.physic.ut.ee servers.

## Merged Clips

- [Tartu in 2021](https://www.youtube.com/watch?v=XiWUUGcrCzs)
- [Tartu in 2020](https://www.youtube.com/watch?v=9cNdEs1fOOQ)
- [Tartu in 2019](https://www.youtube.com/watch?v=q_ZRND_3uQY)
- [Tartu in 2018](https://www.youtube.com/watch?v=i3sxpB2TqvA)
