import os
import shutil
import tempfile
import unittest
from filerix.fileUtils import decompress

class TestFileUtilsDecompress(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.src_file = os.path.join(self.test_dir, "test.zip")
        self.dest_dir = os.path.join(self.test_dir, "decompressed")

        with open(self.src_file, "w") as f:
            f.write("Fake compressed data")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_decompress(self):
        self.assertTrue(decompress(self.src_file, self.dest_dir))
        self.assertTrue(os.path.exists(self.dest_dir))

if __name__ == "__main__":
    unittest.main()
