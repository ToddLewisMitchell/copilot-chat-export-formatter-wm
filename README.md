# Visual Studio Code Copilot chat export formatter
this python script takes the raw Visual Studio Code Github Copilot chat log and turns it into a more readable text file

# how to use:
1. make sure you have [python](https://www.python.org/downloads/)  installed
2. export a Copilot Chat session to a JSON file via `Ctrl+Shift+P | Chat: Export Session...` or by choosing `View > Command Palette | Chat: Export Session...`
3. place this chat.json file in the same folder as the format_chat_log.py file
4. open command prompt in this folder and run `python format_chat_log`
5. this gives you the formatted chat logs in a .md file in that same folder.

