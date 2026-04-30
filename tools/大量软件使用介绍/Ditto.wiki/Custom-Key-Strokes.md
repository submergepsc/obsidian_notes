Some applications to not accept the default key stroke to paste a clip, ctrl-v.  Starting in 3.15.1 custom key strokes can be set per application can be set to send the appropriate key stroke to paste the clip. 
<br>
Default key strokes for paste, copy and cut, these can be customized in Options - General - Advanced, "Default paste/copy/cut string:
~~~
    paste: ^v (ctrl-v)
    copy: ^c (ctrl-c)
    cut: ^x (ctrl-x)
~~~
 <br>
 Examples
~~~
    ^p  (sends ctrl-p)
    %e{DELAY 50}p  (sends Alt-e, delays 50 ms then sends p)
    ^c  (Sends ctrl-c)
    ^x  (Sends ctrl-x)
    {VKEY162}v (sends left control - v) (virtual key definitions, https://docs.microsoft.com/en-us/windows/desktop/inputdev/virtual-key-codes)
~~~
Key | Code 
---------- | ----------
WINKEY|@
SHIFT|+
CTRL|^
ALT|%
~~~
# How to set a custom key stroke
    1. Custom Paste Strings
        1. Installed Version
                1. Start - Run, enter regedit.
                2. Browse to "HKCU\Software\Ditto\PasteStrings"
                3. Add a string value of your application name, must be the full name, ex: notepad.exe
                4. Enter the key stroke to send 
           2. Portable Version
                1. Open Ditto.Settings in xcopy folder
                2. Add text to [PasteStrings] ini section
                3. example
                    1. [PasteStrings]
                    2. SomeApp.exe=^y
    2. Custom Copy Strings
        1. Installed Version
            2. Start - Run, enter regedit.
            3. Browse to "HKCU\Software\Ditto\CopyStrings"
            4. Add a string value of your application name, must be the full name, ex: notepad.exe
            5. Enter the key stroke to send 
        2. Portable Version
            1. Open Ditto.Settings in xcopy folder
            2. Add text to [CopyStrings] ini section
            3. example
                1. [CopyStrings]
                2. SomeApp.exe=^y
    3. Custom Cut Strings
        1. Installed Version
            1. Start - Run, enter regedit.
            2. Browse to "HKCU\Software\Ditto\CutStrings"
            3. Add a string value of your application name, must be the full name, ex: notepad.exe
            4. Enter the key stroke to send 
        2. Portable Version
            1. Open Ditto.Settings in xcopy folder
            2. Add text to [CutStrings] ini section
            3. Example
                1. [CopyStrings]
                2. SomeApp.exe=^y
~~~
Key | Code 
---------- | ----------
BACKSPACE|{BACKSPACE}, {BS}, or {BKSP}
BREAK|{BREAK}
CAPS LOCK|{CAPSLOCK}
DEL or DELETE|{DELETE} or {DEL}
DOWN ARROW|{DOWN}
END|{END}
ENTER|{ENTER} or ~
ESC|{ESC}
HELP|{HELP}
HOME|{HOME}
INS or INSERT|{INS}
LEFT ARROW|{LEFT}
NUM LOCK|{NUMLOCK}
PAGE DOWN|{PGDN}
PAGE UP|{PGUP}
PRINT SCREEN|{PRTSC} (reserved for future use)
RIGHT ARROW|{RIGHT}
SCROLL LOCK|{SCROLL}
TAB|{TAB}
UP ARROW|{UP}
F1|{F1}
F2|{F2}
F3|{F3}
F4|{F4}
F5|{F5}
F6|{F6}
F7|{F7}
F8|{F8}
F9|{F9}
F10|{F10}
F11|{F11}
F12|{F12}
F13|{F13}
F14|{F14}
F15|{F15}
F16|{F16}
Keypad add|{ADD}
Keypad subtract|{SUBTRACT}
Keypad multiply|{MULTIPLY}
Keypad divide|{DIVIDE}
Key | Code 
---------- | ----------
+|{PLUS}
@|{AT}
APPS|{APPS}
^|{CARET}
~|{TILDE}
{ }|{LEFTBRACE} {RIGHTBRACE}
( )|{LEFTPAREN} {RIGHTPAREN}
Left/Right WINKEY|{LWIN} {RWIN}
WINKEY|{WIN} equivalent to {LWIN}
Command Syntax | Action 
---------- | ----------
{VKEY X}|Sends the VKEY of value X.<br>Very useful if you don't want to recompile CSendKeys and add new Vkey to the hardcoded special keys table.<br>For example, {VKEY 13} is equivalent to VK_RETURN.
{BEEP X Y}}|Beeps with a frequency of X and a duration of Y milliseconds.
{DELAY X}|Delays sending the next key of X milliseconds. After the delaying the following key, the subsequent keys will not be further delayed unless there is a default delay value (see DELAY=X).<br>Example: {DELAY 1000} <-- delays subsequent key stroke for 1 second.
