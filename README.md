# Meteo Clip Merger
Scripts to download &amp; merge video clips from [meteo.physic.ut.ee archive](https://meteo.physic.ut.ee/webcam/uus/archive/).

## Usage

1. Run `wget_meteo.sh YEAR` to download the year you wish (make sure it's available).
2. Run `convert_meteo.sh YEAR MONTH` for every month to speed up and join all clips. 
3. Run `join_meteo.sh YEAR` to join all months into one ~3 hour long video at 48 FPS.

The first and second steps may take quite a while (2-8 hours), but the third one should be fast (under a minute).  I usually run 2-4 instances of the second step at a time, but the effectiveness of this may depend on your CPU.

Please be kind to the meteo.physic.ut.ee servers.
