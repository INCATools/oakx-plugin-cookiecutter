"""{{cookiecutter.__project_slug}} package."""
from importlib import metadata

__version__ = metadata.version(__name__)

from {{cookiecutter.__project_slug}} import {{cookiecutter.implementation}}

schemes = {
    '{{cookiecutter.scheme}}': {{cookiecutter.implementation}}
}
