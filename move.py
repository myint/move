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
    """Return diff from revision control system."""
    for check, move in REVISION_CONTROL:
        if not check or check_command_status(check):
            subprocess.call(move + arguments,
                            stdout=subprocess.PIPE)


def interactive_move(arguments):
    """Run qmv."""
    subprocess.call(['qmv', '--command=qmv-move-helper'] + arguments)