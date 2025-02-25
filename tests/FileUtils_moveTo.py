import os
import shutil
import tempfile
import unittest
from filerix.fileUtils import moveTo

class TestFileUtilsMoveTo(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.dest_dir = tempfile.mkdtemp()
        self.src_file = os.path.join(self.test_dir, "test.txt")
        self.dest_file = os.path.join(self.dest_dir, "test.txt")

        with open(self.src_file, "w") as f:
            f.write("Move test")

    def tearDown(self):
        shutil.rmtree(self.test_dir)
        shutil.rmtree(self.dest_dir)

    def test_moveTo(self):
        self.assertTrue(moveTo(self.src_file, self.dest_file))
        self.assertTrue(os.path.exists(self.dest_file))
        self.assertFalse(os.path.exists(self.src_file))

if __name__ == "__main__":
    unittest.main()
