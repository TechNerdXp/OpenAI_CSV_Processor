import json
import csv
import os
import time
from dotenv import load_dotenv
from ai import check_run_status, get_thread_messages
from csv_functions import load_already_done, save_message

load_dotenv()

# Constants for rate limiting
RATE_LIMIT = 60  # Number of requests per minute
TIME_INTERVAL = 60  # Time interval in seconds

def main():
    api_key = os.getenv('OPENAI_API_KEY')
    assistant_id = os.getenv('OPENAI_ASSISTANT_ID')
    if not api_key:
        raise ValueError('Missing OpenAI API Key')
    if not assistant_id:
        raise ValueError('Missing OpenAI Assistant ID')
    

    already_done = load_already_done('data/messages.csv')
    
    for title, threadId, runId in csv.reader(open('data/runs.csv', 'r', encoding='utf-8')):
        if title in already_done:
            continue
        status = check_run_status(threadId, runId)
        while status != 'completed':
            print(f'status: {status}')
            time.sleep(5)
            status = check_run_status(threadId, runId)
            if(status == 'expired' or status == 'failed'):
                break
        print(title)
        if status == 'completed':
            try:
                messages = get_thread_messages(threadId)
                message = messages.data[0].content[0].text.value
                message  = json.loads(message)
                row = [title, message['part_name'], message['compatible_models'], message['specs'], status] # ADJUST THIS LINE ACCORDING TO YOUR NEEDS
            except:
                row = [title, None, None, None, status]
        else:
            row = [title, None, None, None, status]
        save_message('data/messages.csv', row)
        time.sleep(TIME_INTERVAL / RATE_LIMIT)  # Rate limiting
        

if __name__ == "__main__":
    main()
