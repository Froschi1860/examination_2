import unittest, gameMenu, player, game, io, sys


class TestGameMenu(unittest.TestCase):
    '''Tests for module gameMenu.py'''

    # Test constructor
    def test_init_without_player_2(self):
        '''Test initialisation with one player and default setup'''
        test_player_1 = player.Player(player_id="test")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1)
        self.assertIsInstance(test_gameMenu, gameMenu.GameMenu)
        self.assertEqual(test_gameMenu.player_1.player_id, "test")
        self.assertEqual(test_gameMenu.player_2.player_id, "com")
        self.assertEqual(test_gameMenu.setup, ("pvc", "com"))

    def test_init_with_player_2_and_changed_setup(self):
        '''Test initialisation with two players and changes setup'''
        test_player_1 = player.Player("test_1")
        test_player_2 = player.Player("test_2")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, player_2=test_player_2, setup=("pvp", "test_2"))
        self.assertEqual(test_gameMenu.player_1.player_id, "test_1")
        self.assertEqual(test_gameMenu.player_2.player_id, "test_2")
        self.assertEqual(test_gameMenu.setup, ("pvp", "test_2"))


    # Test cmdloop
    def test_cmdloop_in_test_mode_without_test_cmd_terminates(self):
        '''Test if test mode terminates if no test_cmd is given'''
        test_player_1 = player.Player("test_1")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, test_mode=True)
        test_gameMenu.cmdloop()
        self.assertTrue(True)

    def test_cmdloop_in_test_mode_with_test_cmd_terminates(self):
        '''Test if test mode terminates if command is given'''
        test_player_1 = player.Player("test_1")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, test_mode=True, test_cmd="current")
        test_gameMenu.cmdloop()
        self.assertTrue(True)

    def test_cmdloop_with_input_start(self):
        '''Test if input start activates respective option'''
        test_player_1 = player.Player("test_1")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        gameMenu.GameMenu(player_1=test_player_1, test_mode=True, test_cmd="start").cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "Game started\nExiting\n")
        
    def test_cmdloop_with_input_setup(self):
        '''Test if input setup activates respective option'''
        test_player_1 = player.Player("test_1")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        gameMenu.GameMenu(player_1=test_player_1, test_mode=True, test_cmd="setup invalid").cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "\nThe inputs of arguments was invalid. " +
            "Type help setup for instructions.\nExiting\n")

    def test_cmdloop_with_input_current(self):
        '''Test if current setup activates respective option'''
        test_player_1 = player.Player("test_1")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        gameMenu.GameMenu(player_1=test_player_1, test_mode=True, test_cmd="current").cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "Current setup: Game mode player vs computer -> " +
            "test_1 plays against com\nExiting\n")

    def test_cmdloop_with_input_menu(self):
        '''Test if current menu activates respective option'''
        test_player_1 = player.Player("test_1")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, test_mode=True, test_cmd="menu")
        test_gameMenu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, test_gameMenu.menu_message + "\nExiting\n")
    
    def test_cmdloop_with_input_exit(self):
        '''Test if current exit activates respective option'''
        test_player_1 = player.Player("test_1")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, test_mode=True, test_cmd="exit")
        test_gameMenu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "Exiting\nExiting\n")


    # Test precmd
    def test_precmd_with_uppercase_input(self):
        '''Assert if input is converted to lowercase'''
        test_player_1 = player.Player("test_1")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1)
        res = test_gameMenu.precmd("UPPER")
        exp = "upper"
        self.assertEqual(res, exp)

    def test_precmd_with_lowercase_input(self):
        '''Assert if input is unchanged'''
        test_player_1 = player.Player("test_1")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1)
        res = test_gameMenu.precmd("lower")
        exp = "lower"
        self.assertEqual(res, exp)


    # Test preloop()
    def test_preloop_prints_menu(self):
        '''Assert if preloop() prints menu_message'''
        test_player_1 = player.Player("test_1")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_gameMenu.preloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, test_gameMenu.menu_message + "\n")

    
    # Test do_start
    def test_do_start_one_player_default_setup(self):
        '''Check if game is started correctly with one player'''
        test_player_1 = player.Player("test_1")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, test_mode=True)
        res = test_gameMenu.onecmd("start")
        self.assertIsInstance(res, game.Game)
        self.assertEqual(res.player_1.player_id, "test_1")
        self.assertEqual(res.player_2.player_id, "com")

    def test_do_start_two_player_changed_setup(self):
        '''Check if game is started correctly with two players and changes setup'''
        test_player_1 = player.Player("test_1")
        test_player_2 = player.Player("test_2")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, player_2=test_player_2, test_mode=True,
                setup=("pvp", "test_2"))
        res = test_gameMenu.onecmd("start")
        self.assertEqual(res.player_1.player_id, "test_1")
        self.assertEqual(res.player_2.player_id, "test_2")


    # Test do_setup
    def test_do_setup_with_only_arg_pvc_and_two_players(self):
        '''Check if setup is correctly changed for mode pvc'''
        com = player.Player("com")
        player.add_player("com")
        test_player_1 = player.Player("test_1")
        test_player_2 = player.Player("test_2")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, player_2=test_player_2, test_mode=True,
                setup=("pvp", "test_2"))
        test_gameMenu.onecmd("setup pvc")
        self.assertEqual(test_gameMenu.player_2.player_id, "com")
        self.assertEqual(test_gameMenu.setup, ("pvc", "com"))

    def test_do_setup_with_args_pvc_and_extra_arg_and_one_player(self):
        '''Check if setup is correctly changed for mode pvc with wrong additional input'''
        com = player.Player("com")
        player.add_player("com")
        test_player_1 = player.Player("test_1")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, test_mode=True)
        test_gameMenu.onecmd("setup pvc invalid")
        self.assertEqual(test_gameMenu.player_2.player_id, "com")
        self.assertEqual(test_gameMenu.setup, ("pvc", "com"))

    def test_do_setup_with_args_pvp_and_existing_player(self):
        '''Check if setup and player 2 are correctly changed for mode pvp and existing player 2'''
        test_player_1 = player.Player("test_player_1")
        existing_test_player = player.Player("existing_test_player")
        player.add_player("existing_test_player")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, test_mode=True)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_gameMenu.do_setup("pvp existing_test_player")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(test_gameMenu.player_2.player_id, "existing_test_player")
        self.assertEqual(printed_output, "Player 2 was set to existing_test_player\n")
        self.assertEqual(test_gameMenu.setup, ("pvp", "existing_test_player"))

    def test_do_setup_with_args_pvp_and_non_existing_player_plus_invalid(self):
        '''Check if setup and player 2 are correctly changed for mode pvp and existing player 2'''
        test_player_1 = player.Player("test_player_1")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, test_mode=True)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_gameMenu.do_setup("pvp non_existing_test_player invalid")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(test_gameMenu.player_2.player_id, "non_existing_test_player")
        self.assertEqual(printed_output, "Player non_existing_test_player was created and set to player 2\n")
        self.assertEqual(test_gameMenu.setup, ("pvp", "non_existing_test_player"))

    def test_do_setup_with_no_arg(self):
        '''Check if correct error message is printed for no given arg'''
        test_player_1 = player.Player("test_player_1")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, test_mode=True)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_gameMenu.do_setup("")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "\nThe inputs of arguments was invalid. Type help setup for instructions.\n")

    def test_do_setup_with_invalid_arg(self):
        '''Check if correct error message is printed for invalid arg'''
        test_player_1 = player.Player("test_player_1")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, test_mode=True)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_gameMenu.do_setup("invalid")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "\nThe inputs of arguments was invalid. Type help setup for instructions.\n")

    
    # Test do_current
    def test_do_current_with_default_setup(self):
        '''Check if current setup is displayed correctly for player vs computer'''
        test_player_1 = player.Player("test_player_1")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, test_mode=True)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_gameMenu.do_current("")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "Current setup: Game mode player vs computer " + 
            "-> test_player_1 plays against com\n")

    def test_do_current_with_setup_pvp_and_test_player_2(self):
        '''Check if current setup is displayed correctly for player vs player'''
        test_player_1 = player.Player("test_player_1")
        test_player_2 = player.Player("test_player_2")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, player_2=test_player_2,
            setup=("pvp", "test_player_2"), test_mode=True)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_gameMenu.do_current("")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "Current setup: Game mode player vs player " + 
        "-> test_player_1 plays against test_player_2\n")

    
    # test do_menu
    def test_do_menu(self):
        '''Assert if menu is printed correctly'''
        test_player_1 = player.Player("test_player_1")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, test_mode=True)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_gameMenu.do_menu("")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, test_gameMenu.menu_message + "\n")


    # Test do_exit
    def test_do_exit(self):
        '''Check if do_exit returns True'''
        test_player_1 = player.Player("test_player_1")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, test_mode=True)
        res = test_gameMenu.do_exit("")
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()
