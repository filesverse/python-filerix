#ifndef FILERIX_DRIVE_LISTENER_HPP
#define FILERIX_DRIVE_LISTENER_HPP

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include "filerix/Listeners/DriveListener.h"

namespace py = pybind11;

inline void init_drive_listener(py::module_ &m)
{
  py::module driveListener = m.def_submodule("driveListener", "Drive event monitoring module");

  py::class_<DriveListener::DriveMonitor>(driveListener, "DriveMonitor")
      .def(py::init<>())
      .def("start", &DriveListener::DriveMonitor::Start, py::arg("callback"),
           "Start monitoring drive events with a callback function")
      .def("stop", &DriveListener::DriveMonitor::Stop,
           "Stop monitoring drive events");
}

#endif
