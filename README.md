# Cumulative points per heat with lap and time tie break
This is a [RotorHazard](https://github.com/RotorHazard/RotorHazard) leaderboard plugin   

Pilots are ranked in the following order:
1. Heats
2. Points  
3. Laps  
4. Total laptime (from race start)  

This is the format typically used in the UK for triple finals  

# Installation
There are 3 ways you can install this plugin  
1. Though RotorHazards community plugin manager on RotorHazard 4.3.0 or greater:  
   This can be found on your timer which must be connected to the internet by going to settings -> plugins -> Browse Community Plugins (online only) -> Class Rankings then install the Cumulative Points Per Heat plugin
   
2. Paste the following commands into your timers SSH terminal:  
  You can also paste the below command into your command line to instal the plugin (your timer will need an internet connection)    
  
  ```
  cd ~
  wget https://github.com/Aaronsss/cumulative-points-per-heat-RH-plugin/archive/refs/heads/main.zip
  unzip ./main.zip
  rm -R ~/RotorHazard/src/server/plugins/cumulative_points_per_heat/
  mv ~/cumulative-points-per-heat-RH-plugin-main/custom_plugins/cumulative_points_per_heat/ ~/RotorHazard/src/server/plugins/
  rm -R ./cumulative-points-per-heat-RH-plugin-main/
  rm ./main.zip
  sudo systemctl restart rotorhazard.service
  ```

3. Manually:  
   By simply pasting the custom_plugins/cumulative_points_per_heat folder into your rotorhazard plugin folder (/RotorHazard/src/server/plugins) and start / restart your RotorHazard server  
