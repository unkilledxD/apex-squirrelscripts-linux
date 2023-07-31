import os, shutil, time, getpass, psutil
 
username = getpass.getuser()
cheat = str(os.getcwd())+'/'
 
apexfolder = f'/home/abdo/.steam/debian-installation/steamapps/common/Apex legends/vpk/'
 
# Fetching the list of all the files
files = os.listdir(cheat)
     
def wait_for_process(process_name):
    while True:
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == process_name:
                print('Game Started!')
                return proc.info['pid']
        # Wait for .5 second before checking again
        time.sleep(0.5)
     
files_moved = []
for file_name in files:
    if file_name.endswith('.vpk'):
    	shutil.copy(cheat+file_name, apexfolder+file_name)
    	files_moved.append(file_name)

apex_pid = None
while apex_pid is None:
    print('Please Start Game.')
    apex_pid = wait_for_process("R5Apex.exe")
    os.system('clear')
     
time.sleep(8)
     
for delete_files in files_moved:
    os.remove(apexfolder+delete_files)
     
print('Files Cleared!')
