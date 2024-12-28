import unittest
from Qlearning import Maze, QAgent


class TestQAgent(unittest.TestCase):
    def setUp(self):
        # Create a simple 4x4 maze with no walls for testing
        self.maze = Maze(4, 4)
        self.maze.vertical_walls = [
            [0, 0, 0, 1],
            [1, 0, 1, 1],
            [0, 1, 0, 1],
            [0, 0, 0, 1]
        ]
        self.maze.horizontal_walls = [
            [1, 0, 1, 0],
            [0, 0, 1, 0],
            [1, 1, 0, 1],
            [1, 1, 1, 1]
        ]
        self.end_position = (3, 3)
        self.agent = QAgent(self.maze, self.end_position, alpha=0.1, gamma=0.9, epsilon=0.1)

    def test_choose_action(self):
        state = self.maze.get_state_index(0, 0)
        action = self.agent.choose_action(state)
        self.assertIn(action, self.agent.actions, "Chosen action should be one of the defined actions.")

    def test_update_q_value(self):
        state = self.maze.get_state_index(0, 0)
        action = "right"
        reward = 1
        next_state = self.maze.get_state_index(1, 0)

        initial_q_value = self.agent.q_table[state][self.agent.actions.index(action)]
        self.agent.update_q_value(state, action, reward, next_state)
        updated_q_value = self.agent.q_table[state][self.agent.actions.index(action)]

        self.assertNotEqual(initial_q_value, updated_q_value, "Q-value should be updated after learning.")

    def test_learn(self):
        # Test that learning updates the Q-table
        self.agent.learn(episodes=10)
        updated = False
        for i in range(len(self.agent.q_table)):
            if any(q_value != 0 for q_value in self.agent.q_table[i]):
                updated = True
                break

        self.assertTrue(updated, "Q-table should have at least one updated value after learning.")

    def test_get_optimal_path(self):
        self.agent.learn(episodes=1000)  # Train the agent
        start_position = (0, 0)
        path = self.agent.get_optimal_path(start_position)

        self.assertEqual(path[0], start_position, "Path should start at the initial position.")
        self.assertEqual(path[-1], self.end_position, "Path should end at the goal position.")
        self.assertTrue(len(path) > 0, "Path should contain steps from start to end.")


if __name__ == '__main__':
    unittest.main()
