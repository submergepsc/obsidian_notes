With copy buffers up to 3 buffers can be defined, Options - Copy Buffers.  The goal is to have each buffer work independently from the standard copy/paste.  So you can have data saved on the standard windows clipboard, allowing you to paste that with ctrl-v and have separate data stored in buffer 1 and paste that separate from ctrl-v.
### Windows clipboard Data, paste: ctrl-v, copy: ctrl-c
`windows data`
### Buffer 1 - paste: ctrl-+, copy: ctrl-shift-+
`my buffer`
### Buffer 2 - paste: ctrl-*, copy ctrl-shift-*
`buffer 2`
Now you can paste 'windows data' with ctrl-v and 'my buffer' with ctrl-+.  Then copy data into into buffers using the copy short cut key.
### Behind the scenes
Windows doesn't have any concept of multiple buffers so when pasting using a buffer the following steps are taken to fake it out
1. Save the contents of the current windows clipboard
2. Load the windows clipboard with the buffer's content
3. Simulate a paste using the standard ctrl-v
4. Wait for a few seconds 
5. Restore the original contents of the windows clipboard so the standard ctrl-v will paste what it should.
