If you need to open Ditto with key strokes that the standard hot keys control doesn't support in options - keyboard shortcuts, then AutoHotKey can be used, https://www.autohotkey.com.  
There are many limitations with using the built in hot keys with windows that Ditto uses.  All the default windows shortcut keys happen first so it's hard to use the windows key globally, or space key or any other already defined shortcut.  AutoHotKey gets around this, the keystrokes will be processed first by AutoHotKey so you can override any of those global shortcut keys.
1. Install AutoHotKey
2. Create a .ahk text file
3. Paste one of the example from below and modify it to your desire and save.
3. Double click on the .ahk file and it will run in auto hot key processing shortcut keys and opening Ditto through command line.
Examples (update file path to Ditto as needed)
Common keys
~~~
# is for Win key
^ is for Ctrl key
! is for Alt key
+ is for Shift key
~~~
**Open Ditto by double control key press**
~~~
Ctrl::
    KeyWait,Ctrl
    KeyWait,Ctrl,D T0.3
    If !ErrorLevel
        Run C:\program files\Ditto\Ditto.exe /Open
Return
~~~
**Open Ditto with Shift - space**
~~~
+Space::
  Run C:\Program Files\Ditto\Ditto.exe /Open
Return
~~~
**Open Ditto with windows - v**
~~~
#v::
  Run C:\Program Files\Ditto\Ditto.exe /Open
Return
~~~
**Open Ditto with windows - control - v**
~~~
#^v::
   Run C:\Program Files\Ditto\Ditto.exe /Open
Return
~~~
**Open Ditto with a shortcut and move the selection up and down**
~~~
https://sourceforge.net/p/ditto-cp/discussion/287511/thread/c191e6fd/#c4e0
~~~
