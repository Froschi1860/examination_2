"""This module contains tests for the module player_menu.py"""

import unittest
import io
import sys
import player_menu
import player


class TestPlayerMenu(unittest.TestCase):
    '''Tests for module playerMenu.py'''

    # Test constructor:
    def test_initialisation_without_player(self):
        '''Assert instance and player instance variable equals None'''
        menu = player_menu.PlayerMenu()
        self.assertIsInstance(menu, player_menu.PlayerMenu)
        self.assertIsNone(menu.player_1)

    def test_initialisation_with_player(self):
        '''Assert instance and player instance variable equals to player argument'''
        test_player = player.Player("test")
        menu = player_menu.PlayerMenu(player_1=test_player)
        self.assertIsInstance(menu, player_menu.PlayerMenu)
        self.assertEqual(menu.player_1, test_player)

    # Test cmdloop()
    def test_cmdloop_in_test_mode_without_test_cmd_terminates(self):
        '''Test if test mode terminates if no test_cmd is given'''
        menu = player_menu.PlayerMenu(test_mode=True)
        res = menu.cmdloop()
        self.assertIsNone(res)

    def test_cmdloop_in_test_mode_with_test_cmd_terminates(self):
        '''Test if test mode terminates if command is given'''
        menu = player_menu.PlayerMenu(test_mode=True, test_cmd="current")
        res = menu.cmdloop()
        self.assertIsNone(res)

    def test_cmdloop_with_input_choose(self):
        '''Test if input choose activates respective option'''
        menu = player_menu.PlayerMenu(test_mode=True, test_cmd="choose com")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "The computer can not be chosen as player\nExiting\n")

    def test_cmdloop_with_input_create(self):
        '''Test if input create activates respective option'''
        menu = player_menu.PlayerMenu(test_mode=True, test_cmd="create")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "Enter a player id to create a " +
            "player: create <player_id>\nExiting\n")

    def test_cmdloop_with_input_id(self):
        '''Test if input id activates respective option'''
        menu = player_menu.PlayerMenu(test_mode=True, test_cmd="id")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "Enter a player id to change the" +
            " id of the current player: id <player_id>\nExiting\n")

    def test_cmdloop_with_input_current(self):
        '''Test if input current activates respective option'''
        menu = player_menu.PlayerMenu(test_mode=True, test_cmd="current")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "\nNo player chosen\nExiting\n")

    def test_cmdloop_with_input_menu(self):
        '''Test if input menu activates respective option'''
        menu = player_menu.PlayerMenu(test_mode=True, test_cmd="menu")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, menu.menu_message + "\nExiting\n")

    def test_cmdloop_with_input_exit(self):
        '''Test if input exit activates respective option'''
        test_player = player.Player("test")
        menu = player_menu.PlayerMenu(player_1=test_player, test_mode=True, test_cmd="exit")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.cmdloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "Exiting\nExiting\n")


    # Test precmd()
    def test_precmd_with_uppercase_input(self):
        '''Assert if input is converted to lowercase'''
        menu = player_menu.PlayerMenu()
        res = menu.precmd("UPPER")
        exp = "upper"
        self.assertEqual(res, exp)

    def test_precmd_with_lowercase_input(self):
        '''Assert if input is unchanged'''
        menu = player_menu.PlayerMenu()
        res = menu.precmd("lower")
        exp = "lower"
        self.assertEqual(res, exp)


    # Test preloop()
    def test_preloop_without_chosen_player(self):
        '''Assert if preloop() prints primpt to choose player and menu_message'''
        menu = player_menu.PlayerMenu()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.preloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "\nPlease choose or create a player to start\n" +
            menu.menu_message + "\n")

    def test_preloop_with_chosen_player(self):
        '''Assert if preloop() prints only menu_message'''
        test_player = player.Player("test_player")
        menu = player_menu.PlayerMenu(player_1=test_player)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.preloop()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, menu.menu_message + "\n")


    # Test do_choose()
    def test_do_choose_without_arg_and_initialised_player(self):
        '''Assert correct print of error message and unchanged current player'''
        test_player = player.Player("test")
        menu = player_menu.PlayerMenu(player_1=test_player)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_choose("")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "Enter a player id to choose a " +
            "player: choose <player_id>\n")
        self.assertEqual(menu.player_1, test_player)

    def test_do_choose_with_arg_com_and_initialised_player(self):
        '''Assert correct print of error message and unchanged current player'''
        test_player = player.Player("test")
        menu = player_menu.PlayerMenu(player_1=test_player)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_choose("com")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "The computer can not be chosen as player\n")
        self.assertEqual(menu.player_1, test_player)

    def test_do_choose_with_non_existing_player_and_initialised_player(self):
        '''Assert correct print of error message and unchanged current player'''
        test_player = player.Player("test")
        menu = player_menu.PlayerMenu(player_1=test_player)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_choose("non_existant")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "The player with the id non_existant does not exist\n")
        self.assertEqual(menu.player_1, test_player)

    def test_do_choose_with_existing_player_and_initialised_player(self):
        '''Assert equality of initialised player and sucessfully chosen player'''
        test_player_1 = player.Player("test_player_1")
        test_player_2 = player.Player("test_player_2")
        player.add_player("test_player_2")
        menu = player_menu.PlayerMenu(player_1=test_player_1)
        menu.do_choose("test_player_2")
        self.assertEqual(menu.player_1.player_id, test_player_2.player_id)


    # Test do_create()
    def test_do_create_without_arg_and_initialised_player(self):
        '''Assert correct print of error message and unchanged current player'''
        test_player = player.Player("test")
        menu = player_menu.PlayerMenu(player_1=test_player)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_create("")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "Enter a player id to create a " +
            "player: create <player_id>\n")
        self.assertEqual(menu.player_1, test_player)

    def test_do_create_with_existing_player_and_initialised_player(self):
        '''Assert correct print of error message and unchanged current player'''
        test_player = player.Player("test_player")
        player.add_player("existing")
        menu = player_menu.PlayerMenu(player_1=test_player)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_create("existing")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "A player with the id existing already exists.\n")
        self.assertEqual(menu.player_1.player_id, "test_player")

    def test_do_create_with_non_existing_player_and_initialised_player(self):
        '''Assert equality of current player and succesfully created player'''
        test_player = player.Player("test_player")
        menu = player_menu.PlayerMenu(player_1=test_player)
        menu.do_create("non_existant")
        self.assertEqual(menu.player_1.player_id, "non_existant")


    # Test do_id()
    def test_do_id_without_arg_and_initialised_player(self):
        '''Assert correct print of error message and unchanged current player'''
        test_player = player.Player("test")
        menu = player_menu.PlayerMenu(player_1=test_player)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_id("")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "Enter a player id to change the " +
            "id of the current player: id <player_id>\n")
        self.assertEqual(menu.player_1, test_player)

    def test_do_id_with_existing_player_as_arg_and_non_initialised_player(self):
        '''Assert correct print of error message and unchanged current player'''
        menu = player_menu.PlayerMenu()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_id("player_1")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "Choose or create a player before changing the id\n")
        self.assertIsNone(menu.player_1)

    def test_do_id_with_existing_player_as_arg_and_initialised_player(self):
        '''Assert correct print of error message and unchanged current player'''
        test_player = player.Player("test_player")
        menu = player_menu.PlayerMenu(player_1=test_player)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_id("existing")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "A player with the id existing already exists\n")
        self.assertEqual(menu.player_1.player_id, "test_player")

    def test_do_id_with_non_existing_player_as_arg_and_initialised_player(self):
        '''Assert successful change of id of current player'''
        test_player = player.Player("test")
        menu = player_menu.PlayerMenu(player_1=test_player)
        player_object_before_change = menu.player_1
        menu.do_id("non_exisiting")
        self.assertEqual(menu.player_1, player_object_before_change)
        self.assertEqual(menu.player_1.player_id, "non_exisiting")


    # Test do_current()
    def test_do_current_with_non_initialised_player(self):
        '''Assert correct print of error message'''
        menu = player_menu.PlayerMenu()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_current("")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "\nNo player chosen\n")

    def test_do_current_with_initialised_player(self):
        '''Assert correct print if player is chosen'''
        test_player = player.Player("test")
        menu = player_menu.PlayerMenu(player_1=test_player)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_current("")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "\nCurrent player: test\n")


    # Test do_menu()
    def test_do_menu(self):
        '''Assert if menu is printed correctly'''
        menu = player_menu.PlayerMenu()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_menu("")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, menu.menu_message + "\n")


    # Test do_exit()
    def test_do_exit_without_initialised_player(self):
        '''Assert if error message is printed correctly'''
        menu = player_menu.PlayerMenu()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        menu.do_exit("")
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "\nChoose or create a player to continue\n")

    def test_do_exit_with_initialised_player(self):
        '''Assert correct return value'''
        test_player = player.Player("test")
        menu = player_menu.PlayerMenu(player_1=test_player)
        res = menu.do_exit("")
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()
