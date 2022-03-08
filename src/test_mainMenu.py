from logging import captureWarnings
import unittest, io, sys, gameMenu, highscore, mainMenu, player, playerMenu, rules


class testMainMenu(unittest.TestCase):
    '''Tests for module mainMenu.py'''

    # Test constructor
    def test_init_with_deafult_args(self):
        '''Test initialisation with default args'''
        test_mainMenu = mainMenu.MainMenu()
        self.assertIsInstance(test_mainMenu, mainMenu.MainMenu)
        self.assertEqual(test_mainMenu.test_cmd, "")
        self.assertEqual(test_mainMenu.setup, ("pvc", "com"))
        self.assertIsNone(test_mainMenu.player_1)
        self.assertIsNone(test_mainMenu.player_2)
        self.assertFalse(test_mainMenu.test_mode)

    def test_init_with_changed_args(self):
        '''Test initialisation with arguments'''
        test_player_1 = player.Player("test_1")
        test_player_2 = player.Player("test_2")
        test_mainMenu = mainMenu.MainMenu(player_1=test_player_1, player_2=test_player_2,
            setup=("pvc", "test_2"), test_mode=True, test_cmd="end")
        self.assertIsInstance(test_mainMenu, mainMenu.MainMenu)
        self.assertEqual(test_mainMenu.test_cmd, "end")
        self.assertEqual(test_mainMenu.setup, ("pvc", "test_2"))
        self.assertEqual(test_mainMenu.player_1.player_id, "test_1")
        self.assertEqual(test_mainMenu.player_2.player_id, "test_2")
        self.assertTrue(test_mainMenu.test_mode)


    # Test cmdloop
    def test_cmdloop_in_test_mode_without_test_cmd_terminates(self):
        '''Test if cmdloop terminates if no test_cmd is given'''
        test_mainMenu = mainMenu.MainMenu(test_mode=True)
        test_mainMenu.cmdloop()
        self.assertTrue(True)

    def test_cmdloop_in_test_mode_with_test_cmd_terminates(self):
        '''Test if cmdloop terminates if command is given'''
        test_player_1 = player.Player("test_1")
        test_mainMenu = mainMenu.MainMenu(player_1=test_player_1, test_mode=True, test_cmd="rules")
        test_mainMenu.cmdloop()
        self.assertTrue(True)

    def test_cmdloop_in_test_mode_with_test_cmd_player(self):
        '''Test if input player activates respective option'''
        test_mainMenu = mainMenu.MainMenu(test_mode=True, test_cmd="player")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_mainMenu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "Player menu entered\nEnding\n")

    def test_cmdloop_in_test_mode_with_test_cmd_game(self):
        '''Test if input game activates respective option'''
        test_mainMenu = mainMenu.MainMenu(test_mode=True, test_cmd="game")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_mainMenu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "Game menu entered\nEnding\n")

    def test_cmdloop_in_test_mode_with_test_cmd_highscore(self):
        '''Test if input highscore activates respective option'''
        test_mainMenu = mainMenu.MainMenu(test_mode=True, test_cmd="highscore")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_mainMenu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "Highscore entered\nEnding\n")

    def test_cmdloop_in_test_mode_with_test_cmd_rules(self):
        '''Test if input rules activates respective option'''
        test_mainMenu = mainMenu.MainMenu(test_mode=True, test_cmd="rules")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_mainMenu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, rules.game_rules + "\nEnding\n")

    def test_cmdloop_in_test_mode_with_test_cmd_current(self):
        '''Test if input current activates respective option'''
        test_mainMenu = mainMenu.MainMenu(test_mode=True, test_cmd="current")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_mainMenu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "\nCurrent player: None\nEnding\n")

    def test_cmdloop_in_test_mode_with_test_cmd_menu(self):
        '''Test if input menu activates respective option'''
        test_mainMenu = mainMenu.MainMenu(test_mode=True, test_cmd="menu")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_mainMenu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, test_mainMenu.menu_message + "\nEnding\n")

    def test_cmdloop_in_test_mode_with_test_cmd_end(self):
        '''Test if input end activates respective option'''
        test_mainMenu = mainMenu.MainMenu(test_mode=True, test_cmd="end")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_mainMenu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "Ending\nEnding\n")


    # Test precmd
    def test_precmd_with_uppercase_input(self):
        '''Assert if input is converted to lowercase'''
        test_mainMenu = mainMenu.MainMenu()
        res = test_mainMenu.precmd("UPPER")
        exp = "upper"
        self.assertEqual(res, exp)

    def test_precmd_with_lowercase_input(self):
        '''Assert if input is unchanged'''
        test_mainMenu = mainMenu.MainMenu()
        res = test_mainMenu.precmd("lower")
        exp = "lower"
        self.assertEqual(res, exp)


    # Test preloop()
    def test_preloop_prints_menu(self):
        '''Assert if preloop() prints menu_message'''
        test_mainMenu = mainMenu.MainMenu()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_mainMenu.preloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, test_mainMenu.menu_message + "\n")

    
    # Test do_player
    # Opens player menu -> Functionality of player menu is tested in another file
    def test_do_player_in_test_mode(self):
        '''Check if call to do_player returns an instance of PlayerMenu'''
        test_mainMenu = mainMenu.MainMenu(test_mode=True)
        res = test_mainMenu.do_player("")
        self.assertIsInstance(res, playerMenu.PlayerMenu)

    
    # Test do_game
    # Opens game menu -> Functionality of game menu is tested in another file
    def test_do_game_in_test_mode(self):
        '''Check if call to do_game returns an instance of GameMenu'''
        test_player = player.Player("test_player")
        test_mainMenu = mainMenu.MainMenu(player_1=test_player, test_mode=True)
        res = test_mainMenu.do_game("")
        self.assertIsInstance(res, gameMenu.GameMenu)

    
    # Test do_highscore
    # Opens highscore -> Functionality of highscore is tested in another file
    def test_do_highscore_in_test_mode(self):
        '''Check if call to do_highscore returns an instance of Highscroe'''
        test_mainMenu = mainMenu.MainMenu(test_mode=True)
        res = test_mainMenu.do_highscore("")
        self.assertIsInstance(res, highscore.Highscore)

    # Test do_rules 
    def test_do_rules(self):
        '''Check if do_rules correctly displays the game rules'''
        test_mainMenu = mainMenu.MainMenu()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_mainMenu.do_rules("")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, rules.game_rules + "\n")


    # Test do_current
    def test_do_current_with_player_1(self):
        '''Check if current player is displayed correctly with chosen player'''
        test_player = player.Player("test_player")
        test_mainMenu = mainMenu.MainMenu(player_1=test_player)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_mainMenu.do_current("")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "\nCurrent player: test_player\n")

    def test_do_current_without_player(self):
        '''Check if current player is displayed correctly without chosen player'''
        test_mainMenu = mainMenu.MainMenu()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_mainMenu.do_current("")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "\nCurrent player: None\n")

    
    # Test do_menu()
    def test_do_menu(self):
        '''Assert if menu is printed correctly'''
        test_mainMenu = mainMenu.MainMenu()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_mainMenu.do_menu("")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, test_mainMenu.menu_message + "\n")

    
    # Test do_end
    def test_do_end(self):
        '''Check if do_exit returns True'''
        test_mainMenu = mainMenu.MainMenu()
        res = test_mainMenu.do_end("")
        self.assertTrue(res)

    
if __name__ == "__main__":
    unittest.main()