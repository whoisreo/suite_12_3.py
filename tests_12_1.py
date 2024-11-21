import unittest
from _12_1 import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        human = Runner("Человек")
        for i in range(10):
            human.walk()
        self.assertEqual(human.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        human = Runner("Человек")
        for i in range(10):
            human.run()
        self.assertEqual(human.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        bro = Runner("Б1")
        bro_2 = Runner("Б2")
        for i in range(10):
            bro.run()
            bro_2.walk()
        self.assertNotEqual(bro.distance, bro_2.distance)
