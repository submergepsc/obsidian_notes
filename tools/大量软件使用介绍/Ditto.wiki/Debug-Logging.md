Logging can be logged to two different locations.
- Standard output debug string and viewed with debug view (https://technet.microsoft.com/en-us/library/bb896647.aspx)
- To file ditto.log (c:\Users\<user>\AppData\Roaming\Ditto\ditto.log)
To enable only output debug string logging open Ditto and press (ctrl-D, ctrl-O). Press (ctrl-D, ctrl-O). again to turn logging off. These values can be viewed in real time using DebugView.exe (http://technet.microsoft.com/en-us/sysinternals/bb896647.aspx), Prior to version 3.22.12.0, the shortcut was F5.
To enable logging to file open Ditto and press (ctrl-D, ctrl-F).. Press (ctrl-D, ctrl-F). again to turn file logging off. Logging will now be logged to ditto.log in the directory c:\Users\<user>\AppData\Roaming\Ditto\. Prior to version 3.22.12.0, the shortcut was ctrl-F5.
Or enable logging in options - general - advanced - "Write debug to file" or "Write debug to OutputDebuString"
![image](https://user-images.githubusercontent.com/16867884/185279110-1e765aa0-7104-48c1-bb76-5d4a96784d07.png)
What is logged?
- What application and key strokes are sent to the active window to paste a clip
- Times to fill the main list
- When a system copy takes place
- General debugging information
