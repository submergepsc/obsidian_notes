Starting in version 3.21.196.0 the database path can contain environment variables wrapped in %.  This allows the path the be dynamic based on the machine name or current user.
Examples
~~~
D:\Dropbox\AppData\Ditto\%computername%.db
D:\Dropbox\AppData\Ditto\%username%.db
~~~
1. A list of common environment variables can be found here, https://en.wikipedia.org/wiki/Environment_variable#Default_values
2. The hyper link to this path below the database path text box will display the resolved path if it sees a % in the database path
3. Custom environment varialbes are supported, in windows go to system properties - advanced - Environment Variables to define.  After creating environment variables i was see Ditto need to be restarted before it would see the new value.
