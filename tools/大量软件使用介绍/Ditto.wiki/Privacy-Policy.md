# Ditto Privacy Policy
# What data does Ditto collect from client machines
Absolutly nothing, there is no tracking of any kind built into Ditto.  All data Ditto saves (settings and saved clipboard copies) are stored locally on your machine.
# Where is the local data stored
**Standard Installed Version**
1. Settings - Registry folder: HKEY_CURRENT_USER\Software\Ditto
2. Saved Clips - sqlite database saved in the folder: c:\Users\<user>\AppData\Roaming\Ditto\
**Store Version**
1. Settings - ditto.settings ini file in the Ditto store app data folder C:\Users\<user>\AppData\Local\Packages\<ditto_app_folder>\LocalCache\Local\Ditto_WindowsApp
2. Saved Clips - sqlite database in the Ditto store app data folder C:\Users\<user>\AppData\Local\Packages\<ditto_app_folder>\LocalCache\Local\Ditto_WindowsApp
**Portable Version**
1. Settings - ditto.settings ini file in the folder Ditto is ran from
2. Saved Clips - sqlite database in the folder Ditto is ran from
# Why does Ditto open a network port
Options - Friends allows you to define other machines you can send clips to.  This port is only used to to send clips on your local network and only what you define. Option - Friends - Disable Recieving Clips to disable/enable recieving clips.
