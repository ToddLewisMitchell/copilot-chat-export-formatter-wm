import json

def format_chat_log(chat_log):
    """
    Formats the chat log in markdown format. 
    Requests are prefixed with `> ` to format as block quotes.
    The formatted chat log is returned as a string.
    """
    formatted_chat_log = "# From chat.json\n\n---\n\n"  
    requests = chat_log['requests']
    for request in requests:
        request_text = request['message'].get('text')
        responses = request['response']
        response_text = ""
        for response in responses:
            response_value = response.get('value')
            if response_value:
                response_text += response_value + "\n"
        formatted_chat_log += f"> {request_text}\n\n {response_text}\n\n---\n"
    return formatted_chat_log

# Path to the JSON file
file_path = 'chat.json'

# Path to the output markdown file (newly created)
output_file_path = 'formatted_chat_log.md'

# Reading the JSON file
with open(file_path, 'r') as file:
    raw_data = file.read()

# Parsing the JSON data
chat_log = json.loads(raw_data)

# Formatting the chat log
formatted_chat_log = format_chat_log(chat_log)

# Creating and saving the formatted chat log to a new text file
with open(output_file_path, 'w') as file:
    file.write(formatted_chat_log)
