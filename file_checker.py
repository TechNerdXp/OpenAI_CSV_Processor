import os

def check_files():
    # Directory to check
    directory = 'data'

    # Check if directory exists
    if not os.path.exists(directory):
        # If not, create it
        os.makedirs(directory)
        print(f'Created {directory}')

    # List of files to check and create if not exist
    files_to_create = ['data/runs.csv', 'data/messages.csv']

    for file in files_to_create:
        # Check if file exists
        if not os.path.isfile(file):
            # If not, create it
            open(file, 'w').close()
            print(f'Created {file}')

    # File to check and raise exception if not exist
    file_to_check = 'data/titles.csv'

    # Check if file exists
    if not os.path.isfile(file_to_check):
        # If not, raise an exception
        raise FileNotFoundError(f'{file_to_check} does not exist. It must be provided by the user.')

if __name__ == "__main__":
    check_files()
