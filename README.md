# apex-squirrelscripts-linux
Updated Squirrel scripts for linux only!  
  
(Base -> https://www.unknowncheats.me/forum/apex-legends/569820-modify-squirrel-script-linux.html)  
  
  
[Features]  
  
(original -> https://www.unknowncheats.me/forum/apex-legends/505139-apex-squirrel-scripts.html)  

by default those features  are enabled:

fullmap radar  
minimap radar  
seer health ESP  
basic glow with outline

TriggerBot (Usage: On/Off = F4, Activation = Mouse 4)  ( enabled by default)

item icon ESP (Usage: Press F3 For On/Off)  ( disabled by default)

autoloot (Usage: Press F2 For On/Off)  ( disabled by default)
  
  
[implementation]  

Download "Titanfall_VPKTool3.4_Portable.zip" from https://noskill.gitbook.io/titanfall2/intro/duction/tools  
  
Open "englishclient_frontend.bsp.pak000_dir.vpk" in "...../Steam/steamapps/common/Apex Legends/vpk/" with the downloaded "Titalfall VPK Tool", extract all (delete the log file)  
  
Replace "sh_character_select_new.gnut" using the file in this repository 

sh_character_select_new is located at "$(extracted directory)"/scripts/Vscripts/

Repack with Tools -> Repack  
  
Rename the generated vpk file to "client_frontend.bsp.pak000_000.vpk" and the _dir.vpk file to "englishclient_frontend.bsp.pak000_dir.vpk"

[Usage]

Move the two generated files back to "...../Steam/steamapps/common/Apex Legends/vpk/" 

and delete those files after loading into the lobby ( because apex has implemented file check and it will force close if you didn't remove those files )

** auto moving **

you can use the provided script it will auto delete the files after loading into apex (not using timelimit but by using process detection)

to use the script you need to create directory and add the 2 vpk files with the python script and run the script by: python3 ./inject.py 

you need to modify the variable apexfolder: to the destination vpk folder (steam)
  
  
[Video]  
https://vimeo.com/795981518  
(From https://www.unknowncheats.me/forum/apex-legends/569820-modify-squirrel-script-linux.html)  
