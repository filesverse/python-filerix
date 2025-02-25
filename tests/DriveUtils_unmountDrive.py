import unittest
from filerix.driveUtils import unmountDrive

def fake_unmountDrive(device):
    print(f"[MOCK] unmountDrive called with {device}")
    return True

class TestDriveUtilsUnmountDrive(unittest.TestCase):
    def setUp(self):
        self.original_unmountDrive = unmountDrive
        globals()["unmountDrive"] = fake_unmountDrive

    def tearDown(self):
        globals()["unmountDrive"] = self.original_unmountDrive

    def test_unmount_drive(self):
        result = unmountDrive("/dev/sdb1")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
