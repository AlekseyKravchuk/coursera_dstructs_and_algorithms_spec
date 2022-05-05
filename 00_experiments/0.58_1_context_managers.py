import contextlib
import os


@contextlib.contextmanager
def in_dir(directory):
    """
    Change current working directory to `directory`,
    allow the user to run some code, and change back.

    Args:
      directory (str): The path to a directory to work in.
    """
    current_dir = os.getcwd()
    os.chdir(directory)

    # Add code that lets you handle errors
    try:
        yield
    # Ensure the directory is reset,
    # whether there was an error or not
    finally:
        os.chdir(current_dir)


if __name__ == '__main__':
    print(f'current directory: {os.getcwd()}')
    # say, file we need is located at: '/home/kav/kinozal.tv'

    with in_dir('/home/kav'):
        with open('kinozal.tv', 'r') as f:
            data = f.read().strip()
    print(f'data: {data.split()}')
    print(f'current directory: {os.getcwd()}')

