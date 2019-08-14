import unittest
import core.utils.json_reader as jreader
from os.path import join, realpath, dirname


class TestJsonReader(unittest.TestCase):

    def test_read_all_file(self):
        file_path = join(dirname(realpath(__file__)), '..', 'data', 'read_me.json')
        self.assertIsInstance(jreader.json_reader(file_path), dict)

    def test_read_attributes(self):
        file_path = join(dirname(realpath(__file__)), '..', 'data', 'read_me.json')
        self.assertEqual(jreader.json_reader(file_path)["name"], "Gabriel Valdez")
        self.assertEqual(jreader.json_reader(file_path)["id"], "7174304")
        self.assertEqual(jreader.json_reader(file_path)["age"], 24)
        self.assertEqual(jreader.json_reader(file_path)["password"], "himalaya")
        self.assertIsInstance(jreader.json_reader(file_path)["formation"], dict)
        formation = jreader.json_reader(file_path)["formation"]
        self.assertEqual(formation["school"], "San Bernardo de Tarija")
        self.assertEqual(formation["university"], "Universidad Privada Boliviana")
        self.assertEqual(formation["post-grade"], False)
