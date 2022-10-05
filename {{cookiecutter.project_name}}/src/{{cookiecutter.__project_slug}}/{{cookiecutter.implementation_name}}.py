import logging
from abc import ABC
from dataclasses import dataclass
from oaklib.interfaces import BasicOntologyInterface
from typing import Any, Iterable, Optional

@dataclass
class {{cookiecutter.implementation}}(BasicOntologyInterface):

    def __post_init__(self):
        pass

