#ifndef FILERIX_DRIVE_UTILS_HPP
#define FILERIX_DRIVE_UTILS_HPP

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "filerix/FileSystem/DriveUtils.h"

namespace py = pybind11;

inline void init_drive_utils(py::module_ &m)
{
  py::module driveUtils = m.def_submodule("driveUtils", "Drive utilities module");

  py::class_<DriveUtils::DriveUsage>(driveUtils, "DriveUsage")
      .def_readonly("used", &DriveUtils::DriveUsage::used)
      .def_readonly("total", &DriveUtils::DriveUsage::total);

  py::class_<DriveUtils::DriveInfo>(driveUtils, "DriveInfo")
      .def_readonly("device", &DriveUtils::DriveInfo::device)
      .def_readonly("status", &DriveUtils::DriveInfo::status)
      .def_readonly("unmountable", &DriveUtils::DriveInfo::unmountable)
      .def_readonly("mountPoint", &DriveUtils::DriveInfo::mountPoint)
      .def_readonly("partition", &DriveUtils::DriveInfo::partition)
      .def_readonly("fsType", &DriveUtils::DriveInfo::fsType);

  driveUtils.def("getDrives", &DriveUtils::GetDrives, "Retrieve a list of drives");
  driveUtils.def("getDriveUsage", &DriveUtils::GetDriveUsage, "Retrieve usage stats for a drive");
  driveUtils.def("getDeviceLabelOrUuid", &DriveUtils::GetDeviceLabelOrUUID, "Get device label or UUID");
  driveUtils.def("mountDrive", &DriveUtils::MountDrive, "Mount a drive");
  driveUtils.def("unmountDrive", &DriveUtils::UnmountDrive, "Unmount a drive");
}

#endif
