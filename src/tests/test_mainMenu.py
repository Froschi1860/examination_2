import unittest
import io
import sys
import mainMenu

class testMainMenu(unittest.TestCase):
    def test_preloop(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        mainMenu.MainMenu().preloop()
        sys.stdout = sys.__stdout__
        res = captured_output.getvalue()
        exp = "\n"
        self.assertEqual(exp, res)
        