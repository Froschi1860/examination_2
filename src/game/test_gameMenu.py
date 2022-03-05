from lib2to3.pgen2.literals import test
import unittest, gameMenu, player, game, io, sys


class TestGameMenu(unittest.TestCase):
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
        test_player_1 = player.Player("test_1")
        test_gameMenu = gameMenu.GameMenu(player_1=test_player_1, test_mode=True)
        test_gameMenu.onecmd("setup pvc invalid")
        self.assertEqual(test_gameMenu.player_2.player_id, "com")
        self.assertEqual(test_gameMenu.setup, ("pvc", "com"))



if __name__ == "__main__":
    unittest.main()