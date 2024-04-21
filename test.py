import unittest
from unittest.mock import (patch, MagicMock)
import io
import sys
from snakegame import gameLoop

class TestSnakeGame(unittest.TestCase):
    def testgameovermessage(self):
        # Mock sys.stdout
        mock_stdout = MagicMock()


        with patch('sys.stdout', mock_stdout):
            gameLoop()


        mock_stdout.write.assert_called()


        expected_output = "You Lost! Press Q-Quit or C-Play Again\n"
        mock_stdout.write.assert_called_with(expected_output)

if __name == '__main':
    unittest.main()