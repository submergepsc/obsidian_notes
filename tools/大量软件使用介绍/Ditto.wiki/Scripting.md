**Scripting in Ditto uses ChaiScript (http://chaiscript.com/) to process the script. Scripts can be called either on copy or on paste.**
1. There is a built-in variable called "clip" that is used to access the current clip.
2. Each script must return true/false. Return true to cancel the copy or to cancel the paste.
3. Scripts are accesssed from Options - Advanced - On Copy Scripts / On Paste Scripts
4. Only ascii text is supported, limitation of chaiscript.
4. Each script has access to the clip being copied or pasted the interface is.
~~~
std::string GetAsciiString();
void SetAsciiString(std::string stringVal);
std::string GetClipMD5(std::string clipboardFormat);
SIZE_T GetClipSize(std::string clipboardFormat);
std::string GetActiveApp();
std::string GetActiveAppTitle() { return m_activeAppTitle; }
- Starting in version 3.21.247.0
BOOL FormatExists(std::string clipboardFormat);
BOOL RemoveFormat(std::string clipboardFormat);
BOOL SetParentId(int parentId);
BOOL AsciiTextMatchesRegex(std::string regex);
void AsciiTextReplaceRegex(std::string regex, std::string replaceWith);
-- Starting in version 3.22.21.0
std::string GetActiveAppTitle();
void SetMakeTopSticky();
void SetMakeLastSticky();
void SetReplaceTopSticky();
-- global function (not accessed through clip like all others)
std::string FormatCurrentTime(std::string format);
-- Starting in version 3.23
BOOL DescriptionMatchesRegex(std::string regex);
void DescriptionReplaceRegex(std::string regex, std::string replaceWith)
~~~
<br>
**Examples**
1) Somebody out there was continually having an image and some HTML copied to the clipboard when he accessed webex. This flooded Ditto with the same image over and over. The HTML data was always different so it was never seen as the same clip. The copy came from the browser so we couldn't exclude the browser from saving copies. The following gets the image md5 value that was just copied and compares it against the md5 value for the image that was always being copied, returning true if the copied image matches the known md5 value found in the previous copied properties window.
Copy Script
~~~
var md5 = clip.GetClipMD5("CF_DIB")
return md5 == "9764313F508B852BB66AA0ACAA5F4F0A" || md5 == "14D5CDB06BEF471E72F1EDA6E5EEA124"
~~~
<br>
2) Another request was made to paste the selected clip but remove some known bad characters. Also removing the first character if it was an empty space or line feed.
Paste Script
~~~
//add to the following list for characters to be excluded from the paste
var bad = "!&";
var newString = "";
var removeLineFeed_r = true;
var removeLineFeed_n = true;
var removeSpace = true;
var oldString = clip.GetAsciiString();
for (var i = 0; i < oldString.size(); ++i)
{
    var add = false;
    if (removeSpace == true &&
        oldString[i] == ' ')
    {
        removeSpace = false;
        add = false;
    }
    else if (removeLineFeed_r == true &&
        oldString[i] == '\r')
    {
        removeSpace = false;
        removeLineFeed_r = false;
    }
    else if (removeLineFeed_n == true &&
                oldString[i] == '\n')
    {
        removeSpace = false;
        removeLineFeed_n = false;
        removeLineFeed_r = false;
    }
    else
    {
        if (bad.find(oldString[i], 0) == -1)
        {
            removeSpace = false;
            removeLineFeed_n == false;
            removeLineFeed_r = false;
            add = true;
        }
    }
    if (add)
    {
        newString += oldString[i];
    }
}
clip.SetAsciiString(newString);
return false;
~~~
<br>
3) Auto move clips that contain email addresses to a folder.  First open the group properties, in the window title will be the clip id of that group, use this for what group to set the clip.
used a variation of the regex available here,  https://www.wired.com/2008/08/four-regular-expressions-to-check-email-addresses/
~~~
if(clip.AsciiTextMatchesRegex(".*.+\\@.+\\.(com|net|edu|gov).*") == 1)
{
    clip.SetParentId(<insert group id>);
}
return false;
~~~
<br>
4) Had a friend that always copied a daily corporate password and always wanted it as the top clip.  He always copied it from chrome, it was 4 characters and needed the text to be reversed.  The following checks if the copy was from chrome.exe, the copied app title contains password.aspx, copied text is 4 characters, if so it will reverse the text, set it to be the top sticky clip.
~~~
if(clip.GetActiveApp() == "chrome.exe")
{
	if(clip.GetActiveAppTitle().find("password.aspx") >= 0)
	{
		auto text = clip.GetAsciiString();
		if(text.size() == 4)
		{
			text.reverse();
			clip.SetReplaceTopSticky();
			clip.SetAsciiString(text);
		}
	}	
}
return false;
~~~
<br>
5) Replace image description with an empty string, they didn't like seeing CF_DIB. This could be used to replace any text in the description, replace  CF_DIB with Image or really anything
~~~
if(clip.DescriptionMatchesRegex("CF_DIB") == 1)
{
	clip.DescriptionReplaceRegex(".*", "");
}
return false;
~~~
<br>
6) Remove invalid file name characters \/:"*?<>|
~~~
clip.AsciiTextReplaceRegex("[\\\\/:\"*?<>|]+", "_");
return false
~~~
