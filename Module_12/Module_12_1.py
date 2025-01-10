import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        func_runner = Runner('Walk')
        for i in range(10):
            func_runner.walk()
        self.assertEqual(func_runner.distance, 50)


    def test_run(self):
        func_runner = Runner('Run')
        for i in range(10):
            func_runner.run()
        self.assertEqual(func_runner.distance, 100)

    def test_chellenger(self):
        func_runner = Runner('Walk_1')
        func_runner_1 = Runner('Run_1')
        for i in range(10):
            func_runner.walk()
            func_runner_1.run()
        self.assertNotEqual(func_runner.distance, func_runner_1.distance)

if __name__ =='__main__':
    unittest.main()