import os.path


def get_path():
    """Return the path to this theme."""
    return os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
