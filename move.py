"""Moves revision-controlled files interactively in an editor."""

__version__ = '0.1.3'


import subprocess


REVISION_CONTROL = (
    (['git', 'rev-parse'], ['git', 'mv']),
    (['svn', 'info'],      ['svn', 'mv']),
    (['hg',  'summary'],   ['hg',  'mv']),
    (None,                 ['mv'])
)


def check_command_status(arguments):
    """Return True if command returns 0."""
    try:
        return subprocess.call(
            arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0
    except OSError:
        return False


def revision_control_move(arguments):
    """Move file under revision control."""
    for check, move in REVISION_CONTROL:
        if not check or check_command_status(check):
            result = subprocess.call(move + arguments,
                                     stdout=subprocess.PIPE)

            if result == 0:
                break


def interactive_move(arguments):
    """Run qmv."""
    subprocess.call(['qmv', '--command=qmv-move-helper'] + arguments)
