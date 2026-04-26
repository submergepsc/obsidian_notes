The following command line options are available in Ditto.  The path to Ditto.exe must be the same instance that is running.
1) **Ditto.exe /Disconnect**
        <br>- Disconnects Ditto from the clipboard, Ditto will not save any clipboard changes to its database when it's disconnected.
2) **Ditto.exe /Connect**
        <br>- Reconnects Ditto to the clipboard.
3) **Ditto.exe /Open**
        <br>- Opens Ditto's window
4) **Ditto.exe /Close**
        <br>- Closes Ditto's window
5) **Ditto.exe /PlainTextPaste**
        <br>- Pastes current clipboard data as plain text
        <br>- (as of version 3.21.238.0)
6) **Ditto.exe /Edit:(clip id)**
        <br>- Opens the clip editor for a clip by the id, clip id can be found in the window title of the clip properties
        <br>- You can also post a message to Ditto window ::PostMessage(hWnd, 1258, (clip id), 0)
        <br>- (as of version 3.24.180.0)
7) **Ditto.exe /Paste:(clip id)** 
        <br>- Pastes the clip by the id, clip id can be found in the window title of the clip properties
        <br>- You can also post a message to Ditto window ::PostMessage(hWnd, 1257, (clip id), 0)
        <br>- (as of version 3.24.180.0)
8) **Ditto.exe /Exit** (added in version 3.24.229 1-20-2022)
        <br>- Closes Ditto's window
