To make a translation in your language follow the following steps
[Download the latest version here.](http://ditto-cp.sourceforge.net/) 
* Navigate to the language directory under the installation path (usually, C:\Program files\Ditto)
* Make a copy of English.xml and name it appropriately (ex. Spanish.xml)
* Open the file in your favorite text editor. (http://notepad-plus-plus.org/)
* For each item place the translated text in the tag. You are translating the text in "English_Text". Do Not change the ID or English Text
* ex. <Item English_Text "Groups" ID "100">Replacement for "Groups" goes here</Item>
* Save the file in the language directory, then restart Ditto, and on the General Tab, there is a language combo. Select your language and hit ok. Now you should see your language when you view Ditto. You can still edit your file but you will need to restart Ditto to view your changes.
* For languages that require Unicode characters save the file as UTF-8
* When you're finished with a language file email the files to me (mailto:sabrogden@sourceforge.net) so I can include them in an upcoming release.
