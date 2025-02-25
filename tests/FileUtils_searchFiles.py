import os
import shutil
import tempfile
import unittest
from filerix.fileUtils import searchFiles

class TestFileUtilsSearchFiles(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.matching_file = os.path.join(self.test_dir, "test_file.txt")
        self.non_matching_file = os.path.join(self.test_dir, "random.txt")

        open(self.matching_file, "w").close()
        open(self.non_matching_file, "w").close()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_searchFiles(self):
        results = searchFiles(self.test_dir, "test")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "test_file.txt")

if __name__ == "__main__":
    unittest.main()
