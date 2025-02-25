import unittest
from filerix.driveUtils import getDrives

class TestDriveUtilsGetDrives(unittest.TestCase):
    def test_get_drives(self):
        drives = getDrives()
        self.assertIsInstance(drives, list)

        for drive in drives:
            self.assertIsInstance(drive.device, str)
            self.assertIsInstance(drive.mountPoint, str)
            self.assertIsInstance(drive.fsType, str)

if __name__ == "__main__":
    unittest.main()
