"""{{cookiecutter.implementation}} test."""

from tests import TEST_OWL
from tests import NUCLEUS

import unittest

class Test{{cookiecutter.implementation}}(unittest.TestCase):
    """Test {{implementation}}."""

    def setUp(self) -> None:
        self.oi = get_implementation_from_shorthand(f"{{cookiecutter.scheme}}:{TEST_OWL}")
        
    def test_plugin(self):
        """tests plugins are discovered"""
        plugins = discovered_plugins
        self.assertIn('{{cookiecutter.__project_slug}}', plugins)
        slug = f"{{cookiecutter.scheme}}:{TEST_OWL}"
        r = get_resource_from_shorthand(slug)
        self.assertEqual(r.implementation_class, {{cookiecutter.implementation}})

     def test_all_entities(self):
        """
        Test basic functionality
        """
        curies = list(self.oi.all_entity_curies())
        self.assertIn(NUCLEUS, curies)

