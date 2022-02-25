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

    def test_do_exit(self):
        res = mainMenu.MainMenu().do_exit(line="exit")
        self.assertTrue(res)

    def test_do_exit_terminates(self):
        mainMenu.MainMenu().cmdloop()
        mainMenu.MainMenu().do_exit(line="exit")
        self.assertIsNone(None)

if __name__ == "__main__":
    unittest.main()