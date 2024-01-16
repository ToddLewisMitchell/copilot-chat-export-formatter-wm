# Visual Studio Code Copilot Chat Export Formatter

This Python script takes the raw Visual Studio Code Github Copilot chat log and turns it into a more readable text file.

## Prerequisites

1. Make sure you have [Python](https://www.python.org/downloads/) installed.

## How to Use

1. Export a Copilot Chat session to a JSON file via `Ctrl+Shift+P | Chat: Export Session...` or by choosing `View > Command Palette | Chat: Export Session...`
2. Place this chat.json file in the same folder as the `format_chat_log.py` file.
3. Open command prompt in this folder and run `python format_chat_log.py`.
4. This gives you the formatted chat logs in a .md file in that same folder.

## Script Arguments

You can customize the output format and content with the following arguments:

- `-md`: Format the chat log in markdown instead of txt.
- `-html`: Format the chat log in html instead of txt.
- `-requests`: Only output requests, not responses.
- `-anon`: Omit requester and responder usernames.

For example, to format the chat log in HTML and only output requests, run `python format_chat_log.py -html -requests`.

## Functionality

The `format_chat_log` function formats a chat log into the specified format. It adds the requester and responder usernames at the beginning of the output if they exist and the `-anon` argument is not set. It formats each request and its responses according to the specified format. If the `-requests` argument is set, it only formats the requests.

The `main` function parses the command line arguments, reads the chat log file, calls `format_chat_log` to format the chat log, and writes the formatted chat log to a new file.
