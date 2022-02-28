import unittest
import io
import sys
import mainMenu


class testMainMenu(unittest.TestCase):

    def test_do_end(self):
        res = mainMenu.MainMenu().do_end(line="exit")
        self.assertTrue(res)

    def test_do_exit_terminates_menu(self):
        menu = mainMenu.MainMenu()
        menu.cmdloop()
        res = menu.onecmd("end")
        self.assertTrue(res)

if __name__ == "__main__":
    unittest.main()