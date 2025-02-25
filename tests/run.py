import unittest

def run_all_tests():
    loader = unittest.TestLoader()
    suite = loader.discover("tests", pattern="*.py")

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_all_tests()
