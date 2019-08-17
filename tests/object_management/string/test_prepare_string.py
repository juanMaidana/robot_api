import unittest
from object_management.string.prepare_string import prepare_string


class TestPrepareString(unittest.TestCase):

    def test_replace_one(self):
        string = "$R(0)_project"
        string = prepare_string(string, "vipre")
        self.assertEqual('vipre_project', string)

    def test_replace_two(self):
        string = "$R(0)_project_$R(1)"
        string = prepare_string(string, "vipre", "current_date")
        self.assertEqual('vipre_project_current_date', string)

    def test_replace_three(self):
        string = "$R(0)_project_$R(1)_workspace_$R(2)"
        string = prepare_string(string, "vipre", "date", "time")
        self.assertEqual('vipre_project_date_workspace_time', string)
