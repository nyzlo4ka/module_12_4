import unittest
import logging
import rt_with_exceptions


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        try:
            run1 = rt_with_exceptions.Runner('Max', -1)
            for _ in range(10):
                run1.walk()
            self.assertEqual(run1.distance, 50, f'{run1.name} ran {run1.distance}m, but should have done 50m')
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        try:
            run2 = rt_with_exceptions.Runner(22)
            for _ in range(10):
                run2.run()
            self.assertEqual(run2.distance, 100, f'{run2.name} ran {run2.distance}m, but should have done 100m')
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        run1 = rt_with_exceptions.Runner('Max')
        run2 = rt_with_exceptions.Runner('Dan')
        for _ in range(10):
            run1.run()
            run2.walk()
        self.assertNotEqual(run1.distance, run2.distance)


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding='UTF-8',
                    format='| %(asctime)s | %(levelname)s | %(message)s | %(funcName)s')

if __name__ == '__main__':
    unittest.main()
