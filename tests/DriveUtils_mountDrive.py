import unittest
from filerix.driveUtils import mountDrive

def fake_mountDrive(device, mount_point):
    print(f"[MOCK] mountDrive called with {device} -> {mount_point}")
    return True

class TestDriveUtilsMountDrive(unittest.TestCase):
    def setUp(self):
        self.original_mountDrive = mountDrive
        globals()["mountDrive"] = fake_mountDrive

    def tearDown(self):
        globals()["mountDrive"] = self.original_mountDrive

    def test_mount_drive(self):
        result = mountDrive("/dev/sdb1", "/mnt/test_mount")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
