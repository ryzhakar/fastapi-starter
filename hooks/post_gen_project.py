"""This module is called after project is created.

It does the following:
1. Generates and saves random secret key
2. Prints further instructions

A portion of this code was adopted from Django's standard crypto functions and
utilities, specifically:
https://github.com/django/django/blob/master/django/utils/crypto.py
"""
import os
import secrets
import shutil
import string
import subprocess

# CHANGEME mark
CHANGEME = '__CHANGEME__'

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

# Messages
PROJECT_SUCCESS = """
Your project {0} is created.
Now you can start working on it:

    cd {0}
"""


def init_git():
    """Initialize a git repository."""
    subprocess.run(
        ['git', 'init', '--initial-branch=main'],
        check=True,
    )
    subprocess.run(
        ['git', 'add', '.'],
        check=True,
    )
    subprocess.run(
        [
            'git',
            'commit',
            '-m',
            'feat: copy the template',
            '-m',
            'Check out the github.com/ryzhakar/fastapi-starter to learn more.',
        ],
        check=True,
    )


def _get_random_string(length=50):
    """Returns a securely generated random string.

    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits

    >>> secret = _get_random_string()
    >>> len(secret)
    50
    """
    punctuation = string.punctuation.replace(
        '"', '',
    ).replace(
        "'", '',
    ).replace(
        '\\', '',
    ).replace(
        '$', '',  # see issue-271
    )

    chars = string.digits + string.ascii_letters + punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))


def _create_secret_key(config_path):
    # Generate a SECRET_KEY that matches the Django standard
    secret_key = _get_random_string()

    with open(config_path, 'r+') as config_file:
        # Replace CHANGEME with SECRET_KEY
        file_contents = config_file.read().replace(CHANGEME, secret_key, 1)

        # Write the results to the file:
        config_file.seek(0)
        config_file.write(file_contents)
        config_file.truncate()


def print_futher_instuctions():
    """Shows user what to do next after project creation."""
    print(PROJECT_SUCCESS.format(PROJECT_DIRECTORY))  # noqa: WPS421


def set_dotenv():
    """Handler to copy local configuration."""
    secret_template = os.path.join(
        PROJECT_DIRECTORY, '.env.example',
    )
    secret_config = os.path.join(
        PROJECT_DIRECTORY, '.env',
    )
    shutil.copyfile(secret_template, secret_config)
    _create_secret_key(secret_config)


set_dotenv()
init_git()
print_futher_instuctions()
