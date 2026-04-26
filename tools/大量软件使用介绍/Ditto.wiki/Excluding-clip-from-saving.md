Clips can be excluded from saving in Ditto by going to options - general - advanced, scroll to the bottom and expand "Exclude clips by Regular Expressions"
If the copied text matches the Regex and the Process Name then the clip will not be saved.  Leave the Process Name name empty or * to match against any process.
~~~
Ex)
1 Rexeg: .*test.*
1 Process Name: 
~~~
This will not save any clip that is copied that contains the text "test" from any processes.
~~~
Ex)
1 Rexeg: .*test.*
1 Process Name: notepad.exe
~~~
This will not save any clip that is copied that contains the text "test" when copied from notepad.exe.
