from tests import TEST_OWL

import unittest

from oaklib.selector import get_resource_from_shorthand
from oaklib.implementations import implementation_resolver
from {{cookiecutter.__project_slug}}.{{cookiecutter.implementation_name}} import {{cookiecutter.implementation}}

class Test{{cookiecutter.implementation}}(unittest.TestCase):
    """Test {{cookiecutter.implementation}}."""
        
    def test_plugin(self):
        """tests plugins are discovered"""
        resolved = implementation_resolver.lookup("FOO")
        self.assertEqual(resolved, {{cookiecutter.implementation}})

        slug = f"{{cookiecutter.scheme}}:{TEST_OWL}"
        r = get_resource_from_shorthand(slug)
        self.assertEqual(r.implementation_class, {{cookiecutter.implementation}})
