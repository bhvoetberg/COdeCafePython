import logging
import os

logging.basicConfig(
    level=logging.WARNING,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='logging_examples1.log',
    filemode='a'  # append mode to file, create if not exists
)

def create_directory(directory_path):
    try:
        logging.info(f'Creating directory: {directory_path}')
        os.makedirs(directory_path, exist_ok=True)
        logging.info(f'Directory created successfully: {directory_path}')
        return True
    except Exception as e:
        logging.error(f'Error creating directory: {directory_path}, error: {str(e)}')
        return False
    finally:
        logging.info(f'Exiting function: create_directory')



if __name__ == "__main__":
    directory_path = '/path/to/your/directory'
    result = create_directory(directory_path)
    print(f'Directory creation result: {result}')
