import os
import shutil
import tempfile
import unittest
from filerix.fileUtils import rename

class TestFileUtilsRename(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.src_file = os.path.join(self.test_dir, "oldname.txt")
        self.new_file = os.path.join(self.test_dir, "newname.txt")

        with open(self.src_file, "w") as f:
            f.write("Rename test")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_rename(self):
        self.assertTrue(rename(self.src_file, self.new_file))
        self.assertTrue(os.path.exists(self.new_file))
        self
