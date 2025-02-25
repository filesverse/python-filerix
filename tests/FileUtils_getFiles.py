import os
import shutil
import tempfile
import unittest
from filerix.fileUtils import getFiles

class TestFileUtilsGetFiles(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.file1 = os.path.join(self.test_dir, "file1.txt")
        self.file2 = os.path.join(self.test_dir, "file2.txt")

        open(self.file1, "w").close()
        open(self.file2, "w").close()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_getFiles(self):
        files = getFiles(self.test_dir)
        self.assertEqual(len(files), 2)

if __name__ == "__main__":
    unittest.main()
