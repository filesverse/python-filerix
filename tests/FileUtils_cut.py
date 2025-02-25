import os
import shutil
import tempfile
import unittest
from filerix.fileUtils import cut

class TestFileUtilsCut(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.src_file = os.path.join(self.test_dir, "test1.txt")
        self.dest_file = os.path.join(self.test_dir, "moved.txt")

        with open(self.src_file, "w") as f:
            f.write("Python cut test")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_cut(self):
        self.assertTrue(cut(self.src_file, self.dest_file))
        self.assertTrue(os.path.exists(self.dest_file))
        self.assertFalse(os.path.exists(self.src_file))

if __name__ == "__main__":
    unittest.main()
