import csv
import os
import time
from dotenv import load_dotenv
from ai import add_message, create_thread, run_assistant
from csv_functions import load_titles, load_already_done
from file_checker import check_files
load_dotenv()

# Constants for rate limiting
RATE_LIMIT = 120  # Number of requests per minute
TIME_INTERVAL = 60  # Time interval in seconds

def main():
    api_key = os.getenv('OPENAI_API_KEY')
    assistant_id = os.getenv('OPENAI_ASSISTANT_ID')
    if not api_key:
        raise ValueError('Missing OpenAI API Key')
    if not assistant_id:
        raise ValueError('Missing OpenAI Assistant ID')
    try:
        check_files()
    except Exception as e:
        print(str(e))
        return
    already_done = load_already_done('data/runs.csv')
    titles = load_titles('data/titles.csv', already_done)

    for title in titles:
        if title in already_done:
            continue
        threadId = create_thread()
        add_message(title, threadId)
        runId = run_assistant(threadId)
        if not None in [threadId, runId]:
            with open('data/runs.csv', 'a', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([title, threadId, runId])
            time.sleep(TIME_INTERVAL / RATE_LIMIT)  # Rate limiting
        else:
            break


if __name__ == "__main__":
    main()
