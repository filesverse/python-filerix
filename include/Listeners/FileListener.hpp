#ifndef FILERIX_FILE_LISTENER_HPP
#define FILERIX_FILE_LISTENER_HPP

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include "filerix/Listeners/FileListener.h"

namespace py = pybind11;

inline void init_file_listener(py::module_ &m)
{
  py::module fileListener = m.def_submodule("fileListener", "File event monitoring module");

  py::class_<FileListener::FileMonitor>(fileListener, "FileMonitor")
      .def(py::init<const std::string &>(), py::arg("directory"),
           "Initialize the file monitor for a specific directory")
      .def("start", &FileListener::FileMonitor::Start, py::arg("callback"),
           "Start monitoring file events with a callback function")
      .def("stop", &FileListener::FileMonitor::Stop,
           "Stop monitoring file events");
}

#endif
