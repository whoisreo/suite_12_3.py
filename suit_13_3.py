import unittest
import tests_12_2
import tests_12_1


athleticsTS = unittest.TestSuite()
athleticsTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
athleticsTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
ut_runner = unittest.TextTestRunner(verbosity=2)
ut_runner.run(athleticsTS)
