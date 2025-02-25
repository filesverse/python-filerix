import os
import shutil
import tempfile
import unittest
from filerix.fileUtils import compress

class TestFileUtilsCompress(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.src_file = os.path.join(self.test_dir, "test.txt")
        self.compressed_file = os.path.join(self.test_dir, "test.zip")

        with open(self.src_file, "w") as f:
            f.write("Compression test")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_compress(self):
        self.assertTrue(compress(self.src_file, self.compressed_file))
        self.assertTrue(os.path.exists(self.compressed_file))

if __name__ == "__main__":
    unittest.main()
