Two config settings can be restricted 
1.  Remove friends tab
    1. Starting in version 3.24.187.0, this can be configured in options - general advanced - Disable friends
    2. "AllowFriends"=dword:00000000
2.  Remove the ability to change remove clip settings,  Maximum Number of Saved Copies and Paste Entries Expire After (they show up disabled)
    3.  "DisableExpireClipsConfig"=dword:00000001
Add the settings to Computer\HKEY_CURRENT_USER\Software\Ditto or the Ditto.settings ini file if you are using the portable or store version
