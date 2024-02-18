This is a [RotorHazard](https://github.com/RotorHazard/RotorHazard) leaderboard plugin   

Pilots are ranked in the following order:
1. Heat
2. points  
3. laps  
4. total laptime (from race start)  

This is the format typically used in the UK for triple finals  

To instal paste the cumulative_points_per_heat folder into your rotorhazard plugin folder (/RotorHazard/src/server/plugins) and start / restart your RotorHazard server  

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
