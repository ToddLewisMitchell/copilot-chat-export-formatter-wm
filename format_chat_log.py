from datetime import datetime
import json
import argparse
import html

def format_chat_log(chat_log, format='txt', requests_only=False, anon=False):
	formatted_chat_log = ""
	requests = chat_log['requests']
	if not anon:
		requester_username = chat_log.get('requesterUsername', '')
		responder_username = chat_log.get('responderUsername', '')
		if format == 'html':
			formatted_chat_log += f"<p>Coder: {html.escape(requester_username)}</p>\n<p>AI: {html.escape(responder_username)}</p>\n<hr>\n"
		else:
			formatted_chat_log += f"Coder: {requester_username}\nAI: {responder_username}\n\n"
	if requests_only and format == 'html':
		formatted_chat_log += "<ul>\n"
	for request in requests:
		request_text = request['message'].get('text') if format == 'txt' else "> " + html.escape(request['message'].get('text'))
		if not requests_only:
			responses = request['response']
			response_text = ""
			for response in responses:
				response_value = response.get('value')
				if response_value:
					response_text += (response_value if format == 'txt' else html.escape(response_value)) + "\n"
			if format == 'md':
				formatted_chat_log += f"> {request_text}\n\n {response_text}\n\n---\n"
			elif format == 'html':
				formatted_chat_log += f"<p>{request_text}</p>\n<p>{response_text}</p>\n<hr>\n"
			else:
				formatted_chat_log += f"> {request_text}\n\n{response_text}\n"
		else:
			if format == 'md':
				formatted_chat_log += f"> {request_text}\n\n---\n"
			elif format == 'html':
				formatted_chat_log += f"<li>{request_text}</li>\n"
			else:
				formatted_chat_log += f"> {request_text}\n"
	if requests_only and format == 'html':
		formatted_chat_log += "</ul>\n"
	return formatted_chat_log

def main():
	parser = argparse.ArgumentParser(description='Format a chat log.')
	parser.add_argument('file_path', metavar='F', type=str, nargs='?', default='chat.json',
						help='the path to the chat log file')
	parser.add_argument('-md', action='store_true',
						help='format the chat log in markdown instead of txt')
	parser.add_argument('-html', action='store_true',
						help='format the chat log in html instead of txt')
	parser.add_argument('-requests', action='store_true',
						help='only output requests, not responses')
	parser.add_argument('-anon', action='store_true',
						help='omit requester and responder usernames')
	args = parser.parse_args()

	file_path = args.file_path
	format = 'md' if args.md else 'html' if args.html else 'txt'
	requests_only = args.requests
	anon = args.anon

	output_file_path = (
		f'formatted_chat_log-{datetime.now().strftime("%Y%m%d_%H%M%S")}.{format}'
	)

	with open(file_path, 'r') as file:
		raw_data = file.read()

	chat_log = json.loads(raw_data)

	formatted_chat_log = format_chat_log(chat_log, format, requests_only, anon)

	with open(output_file_path, 'w') as file:
		file.write(formatted_chat_log)

if __name__ == '__main__':
	main()
