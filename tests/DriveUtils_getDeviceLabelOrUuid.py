import unittest
from filerix.driveUtils import getDrives, getDeviceLabelOrUuid

class TestDriveUtilsGetDeviceLabelOrUUID(unittest.TestCase):
    def test_get_device_label_or_uuid(self):
        drives = getDrives()
        if not drives:
            self.skipTest("No drives available to test")

        label_or_uuid = getDeviceLabelOrUuid(drives[0].device)
        self.assertIsInstance(label_or_uuid, str)

if __name__ == "__main__":
    unittest.main()
