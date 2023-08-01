import unittest
from utils.dicts import get_val


class TestDicts(unittest.TestCase):


    def test_get(self):
        data = {"vcs": "mercurial"}
        self.assertEqual(get_val(data, "vcs"), "mercurial")
        self.assertEqual(get_val(data, "vcs", "git"), "mercurial")
        data = {}
        self.assertEqual(get_val(data, "vcs", "git"), "git")
        self.assertEqual(get_val({}, "vcs", "bazaar"), "bazaar")
