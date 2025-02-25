import unittest
from filerix.driveUtils import getDrives, getDriveUsage

class TestDriveUtilsGetDriveUsage(unittest.TestCase):
    def test_get_drive_usage(self):
        drives = getDrives()
        if not drives:
            self.skipTest("No drives available to test")

        usage = getDriveUsage(drives[0].partition)
        self.assertGreaterEqual(usage.total, usage.used)

if __name__ == "__main__":
    unittest.main()
