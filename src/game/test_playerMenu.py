import unittest
import io
import sys
import playerMenu
import player


class TestPlayerMenu(unittest.TestCase):
    '''Tests for module playerMenu.py'''

    # Test constructor:
    def test_initialisation_without_player(self):
        '''Assert instance and player instance variable equals None'''
        menu = playerMenu.PlayerMenu()
        self.assertIsInstance(menu, playerMenu.PlayerMenu)
        self.assertIsNone(menu.player)

    def test_initialisation_with_player(self):
        '''Assert instance and player instance variable equals to player argument'''
        test_player = player.Player("test")
        menu = playerMenu.PlayerMenu(player=test_player)
        self.assertIsInstance(menu, playerMenu.PlayerMenu)        
        self.assertEquals(menu.player, test_player)

    # Test cmdloop()
    def test_cmdloop_in_test_mode_without_test_cmd_terminates(self):
        '''Test if test mode terminates if no test_cmd is given'''
        menu = playerMenu.PlayerMenu(test_mode=True)
        menu.cmdloop()
        self.assertTrue(True)

    def test_cmdloop_in_test_mode_with_test_cmd_terminates(self):
        '''Test if test mode terminates if command is given'''
        menu = playerMenu.PlayerMenu(test_mode=True, test_cmd="current")
        menu.cmdloop()
        self.assertTrue(True)

    def test_cmdloop_with_input_choose(self):
        '''Test if input choose activates respective option'''
        menu = playerMenu.PlayerMenu(test_mode=True, test_cmd="choose")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, "Enter a player id to choose a player: choose <player_id>\n")

    def test_cmdloop_with_input_create(self):
        '''Test if input create activates respective option'''
        menu = playerMenu.PlayerMenu(test_mode=True, test_cmd="create")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, "Enter a player id to create a player: create <player_id>\n")

    def test_cmdloop_with_input_id(self):
        '''Test if input id activates respective option'''
        menu = playerMenu.PlayerMenu(test_mode=True, test_cmd="id")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, "Enter a player id to change the id of the current player: id <player_id>\n")

    def test_cmdloop_with_input_current(self):
        '''Test if input current activates respective option'''
        menu = playerMenu.PlayerMenu(test_mode=True, test_cmd="current")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, "\nNo player chosen\n")

    def test_cmdloop_with_input_menu(self):
        '''Test if input menu activates respective option'''
        menu = playerMenu.PlayerMenu(test_mode=True, test_cmd="menu")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, menu.menu_message + "\n")

    def test_cmdloop_with_input_exit(self):
        '''Test if input exit activates respective option'''
        menu = playerMenu.PlayerMenu(test_mode=True, test_cmd="exit")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, "\nChoose or create a player to continue\n")


    # Test precmd()
    def test_precmd_with_uppercase_input(self):
        '''Assert if input is converted to lowercase'''
        menu = playerMenu.PlayerMenu()
        res = menu.precmd("UPPER")
        exp = "upper"
        self.assertEqual(res, exp)

    def test_precmd_with_lowercase_input(self):
        '''Assert if input is unchanged'''
        menu = playerMenu.PlayerMenu()
        res = menu.precmd("lower")
        exp = "lower"
        self.assertEqual(res, exp)


    # Test preloop()
    def test_preloop_prints_menu(self):
        '''Assert if preloop() prints menu_message'''
        menu = playerMenu.PlayerMenu()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.preloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, menu.menu_message + "\n")


    # Test do_choose()
    def test_do_choose_without_arg_and_initialised_player(self):
        '''Assert correct print of error message and unchanged current player'''
        test_player = player.Player("test")
        menu = playerMenu.PlayerMenu(player=test_player)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_choose()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, "Enter a player id to choose a player: choose <player_id>\n")
        self.assertEquals(menu.player, test_player)

    def test_do_choose_with_non_existing_player_and_initialised_player(self):
        '''Assert correct print of error message and unchanged current player'''
        test_player = player.Player("test")
        menu = playerMenu.PlayerMenu(player=test_player)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_choose("non_existant")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, "The player with the id non_existant does not exist\n")
        self.assertEquals(menu.player, test_player)

    def test_do_choose_with_existing_player_and_initialised_player(self):
        '''Assert equality of initialised player and sucessfully chosen player'''
        test_player = player.Player("test")
        player_1 = player.choosePlayer("player_1")
        menu = playerMenu.PlayerMenu(player=test_player)
        menu.do_choose("player_1")
        self.assertEquals(menu.player, player_1)


    # Test do_create()
    def test_do_create_without_arg_and_initialised_player(self):
        '''Assert correct print of error message and unchanged current player'''
        test_player = player.Player("test")
        menu = playerMenu.PlayerMenu(player=test_player)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_create()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, "Enter a player id to create a player: create <player_id>\n")
        self.assertEquals(menu.player, test_player)

    def test_do_create_with_existing_player_and_initialised_player(self):
        '''Assert correct print of error message and unchanged current player'''
        test_player = player.Player("test")
        menu = playerMenu.PlayerMenu(player=test_player)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_create("player_1")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, "A player with the id player_1 already exists.\n")
        self.assertEquals(menu.player, test_player)

    def test_do_create_with_non_existing_player_and_initialised_player(self):
        '''Assert equality of current player and succesfully created player'''
        test_player = player.Player("test")
        non_existant = player.Player("non_existant")
        menu = playerMenu.PlayerMenu(player=test_player)
        menu.do_choose("non_existant")
        self.assertEquals(menu.player, non_existant)


    # Test do_id()
    def test_do_id_without_arg_and_initialised_player(self):
        '''Assert correct print of error message and unchanged current player'''
        test_player = player.Player("test")
        menu = playerMenu.PlayerMenu(player=test_player)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_id()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, "Enter a player id to change the id of the current player: id <player_id>\n")
        self.assertEquals(menu.player, test_player)

    def test_do_id_with_existing_player_as_arg_and_non_initialised_player(self):
        '''Assert correct print of error message and unchanged current player'''
        menu = playerMenu.PlayerMenu()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_id("player_1")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, "Choose or create a player before changing the id\n")
        self.assertIsNone(menu.player)

    def test_do_id_with_existing_player_as_arg_and_initialised_player(self):
        '''Assert correct print of error message and unchanged current player'''
        test_player = player.Player("test")
        menu = playerMenu.PlayerMenu(player=test_player)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_id("player_1")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, "A player with the id player_1 already exists\n")
        self.assertEquals(menu.player, test_player)

    def test_do_id_with_non_existing_player_as_arg_and_initialised_player(self):
        '''Assert successful change of id of current player'''
        test_player = player.Player("test")
        menu = playerMenu.PlayerMenu(player=test_player)
        menu.do_id("non_exisiting")
        test_player = player.change_player_id(test_player)
        self.assertEquals(menu.player, test_player)


    # Test do_current()
    def test_do_current_with_non_initialised_player(self):
        '''Assert correct print of error message'''
        menu = playerMenu.PlayerMenu()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_current()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, "\nNo player chosen\n")

    def test_do_current_with_initialised_player(self):
        '''Assert correct print if player is chosen'''
        test_player = player.Player("test")
        menu = playerMenu.PlayerMenu(player=test_player)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_current()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, "\nCurrent player: test\n")


    # Test do_menu()
    def test_do_menu(self):
        '''Assert if menu is printed correctly'''
        menu = playerMenu.PlayerMenu()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_menu()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, menu.menu_message + "\n")


    # Test do_exit()
    def test_do_exit_without_initialised_player(self):
        '''Assert if error message is printed correctly'''
        menu = playerMenu.PlayerMenu()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_exit()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEquals(printed_output, "\nChoose or create a player to continue\n")

    def test_do_exit_with_initialised_player(self):
        '''Assert correct return value'''
        test_player = player.Player("test")
        menu = playerMenu.PlayerMenu(player=test_player)
        res = menu.do_exit()
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()
    