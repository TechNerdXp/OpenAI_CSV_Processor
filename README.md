# CSV to OpenAI Processor

This program processes strings from a CSV column through the OpenAI API.

## Setup

1. Clone the repository.
2. Install the required dependencies. `pip install -r requirements.txt`

## OpenAI assitant

Create an OpenAI assistant by providing a prompt and other settings. 

## Environment Variables

Create a `.env` file in the root directory of the project and add the following environment variables:

OPENAI_API_KEY=your_openai_api_key
OPENAI_ASSISTANT_ID=your_openai_assistant_id

Replace `your_openai_api_key` and `your_openai_assistant_id` with your actual OpenAI API key and Assistant ID.

## Input data

Make sure there is a single coumn CSV file named titles.csv in data directory to be used as input.

## Code Changes for Response Extraction

Update the line *#42* 

`row = [title, message['part_name'], message['compatible_models'], message['specs'], status] # ADJUST THIS LINE ACCORDING TO YOUR NEEDS` on `get.py` 

according to your assitant response

## Running the Program

1. Run `run.py` to start accumulating run IDs and thread IDs.
2. After some time gap, run `get.py` to start fetching processed data into the CSV.
