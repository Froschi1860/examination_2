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

    # Test with existing player_id and player in contructor-> Check whether self.player is the same as a retreived player
    # + Test if call to current prints the correct player

    # Test with existing player_id and no player in contructor-> Check whether self.player is the same as a retreived player
    # + Test if call to current prints the correct player

    # Test with non-exisitng player and player in constructor -> Should print statement
    # + Test if self.player stays the same
    # + Test if call to current prints the correct player

    # Test with non-exisitng player and player in constructor -> Should print statement
    # + Test if self.player stays the same
    # + Test if call to current prints the correct player


    # Test do_create()
    # See above


    # Test do_id()
    # See above

    # Test do_current()
    # Create menu with player and assert if do_current() prints correct

    # Create menu without player and assert if do_current() prints correct


    # Test do_menu()
    # Test whether do_menu() prints correct


    # Test do_exit()
    # Create menu with player and check if return is True

    # Create menu without player and check if player is None and print is correct

    # test cmdloop() -> Use mock.patch to simulate input




if __name__ == "__main__":
    unittest.main()