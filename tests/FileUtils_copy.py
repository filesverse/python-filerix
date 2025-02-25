import os
import shutil
import tempfile
import unittest
from filerix.fileUtils import copy

class TestFileUtilsCopy(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.src_file = os.path.join(self.test_dir, "test1.txt")
        self.dest_file = os.path.join(self.test_dir, "copied.txt")

        with open(self.src_file, "w") as f:
            f.write("Hello, world!")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_copy(self):
        self.assertTrue(copy(self.src_file, self.dest_file))
        self.assertTrue(os.path.exists(self.dest_file))

if __name__ == "__main__":
    unittest.main()
