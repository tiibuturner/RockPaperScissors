## Tiina Ylimäki

import unittest
import GameEngine

class GameTest(unittest.TestCase):
    def test_Tasapeli_Kivi(self):
        user_action = ('rock')
        computer_action = ('rock')
        expectResult = 'It is a tie!'
        result = GameEngine.GameAction(user_action, computer_action)
        self.assertEqual(result, expectResult)
    
    def test_Tasapeli_Sakset(self):
        user_action = ('scissors')
        computer_action = ('scissors')
        expectResult = 'It is a tie!'
        result = GameEngine.GameAction(user_action, computer_action)
        self.assertEqual(result, expectResult)
    
    def test_Tasapeli_Paperi(self):
        user_action = ('paper')
        computer_action = ('paper')
        expectResult = 'It is a tie!'
        result = GameEngine.GameAction(user_action, computer_action)
        self.assertEqual(result, expectResult)
    
    def test_pelaaja_Kivi_voittaa(self):
        user_action = ('rock')
        computer_action = ('scissors')
        expectResult = "Rock beats scissors. You won!"
        result = GameEngine.GameAction(user_action, computer_action)
        self.assertEqual(result, expectResult)
    
    def test_kone_Kivi_voittaa(self):
        user_action = ('scissors')
        computer_action = ('rock')
        expectResult = "Rock beats scissors. You lost!"
        result = GameEngine.GameAction(user_action, computer_action)
        self.assertEqual(result, expectResult)
    
    def test_pelaaja_Paperi_voittaa(self):
        user_action = ('paper')
        computer_action = ('rock')
        expectedResult = "Paper beats rock. You won!"
        result = GameEngine.GameAction(user_action, computer_action)
        self.assertEqual(result, expectedResult)
    
    def test_kone_Paperi_voittaa(self):
        user_action = ('rock')
        computer_action = ('paper')
        expectedResult = "Paper beats rock. You lost!"
        result = GameEngine.GameAction(user_action, computer_action)
        self.assertEqual(result, expectedResult)
    
    def test_pelaaja_Sakset_voittaa(self):
        user_action = ('scissors')
        computer_action = ('paper')
        expectedResult = "Scissors beats paper. You won!"
        result = GameEngine.GameAction(user_action, computer_action)
        self.assertEqual(result, expectedResult)
    
    def test_kone_Sakset_voittaa(self):
        user_action = ('paper')
        computer_action = ('scissors')
        expectedResult = "Scissors beats paper. You lost!"
        result = GameEngine.GameAction(user_action, computer_action)
        self.assertEqual(result, expectedResult)

if (__name__ == "__main__"):
    unittest.main()