# Cumulative points per heat with lap and time tie break
This is a [RotorHazard](https://github.com/RotorHazard/RotorHazard) leaderboard plugin   

Pilots are ranked in the following order:
1. Heats
2. Points  
3. Laps  
4. Total laptime (from race start)  

This is the format typically used in the UK for triple finals  

# Installation
You can also paste the below command into your command line to instal the plugin (your timer will need an internet connection)  

```
cd ~
wget https://github.com/Aaronsss/cumulative-points-per-heat-RH-plugin/archive/refs/heads/main.zip
unzip ./main.zip
mv ~/cumulative-points-per-heat-RH-plugin-main/cumulative_points_per_heat/ ~/RotorHazard/src/server/plugins/
rm -R ./cumulative-points-per-heat-RH-plugin-main/
rm ./main.zip
sudo systemctl restart rotorhazard.service
```

You can also instal by simply pasting the cumulative_points_per_heat folder into your rotorhazard plugin folder (/RotorHazard/src/server/plugins) and start / restart your RotorHazard server  
