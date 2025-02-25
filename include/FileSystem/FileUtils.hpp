#ifndef FILERIX_FILE_UTILS_HPP
#define FILERIX_FILE_UTILS_HPP

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "filerix/FileSystem/FileUtils.h"
#include "filerix/FileSystem/FileInfo.h"

namespace py = pybind11;

inline void init_file_utils(py::module_ &m)
{
  py::module fileUtils = m.def_submodule("fileUtils", "File utilities module");

  py::class_<FileInfo>(fileUtils, "FileInfo")
      .def_readonly("name", &FileInfo::name)
      .def_readonly("type", &FileInfo::type)
      .def_readonly("path", &FileInfo::path)
      .def_readonly("size", &FileInfo::size)
      .def_readonly("isDirectory", &FileInfo::isDirectory);

  py::class_<FileList>(fileUtils, "FileList")
      .def_readonly("files", &FileList::files)
      .def_readonly("count", &FileList::count);

  fileUtils.def("copy", &FileUtils::Copy, "Copy a file from source to destination");
  fileUtils.def("cut", &FileUtils::Cut, "Cut a file from source to destination");
  fileUtils.def("rename", &FileUtils::Rename, "Rename a file");
  fileUtils.def("moveTo", &FileUtils::MoveTo, "Move a file to a new location");
  fileUtils.def("compress", &FileUtils::Compress, "Compress a file");
  fileUtils.def("decompress", &FileUtils::Decompress, "Decompress a file");

  fileUtils.def("getFiles", &FileUtils::GetFiles, "Get list of files in a directory");
  fileUtils.def("searchFiles", &FileUtils::SearchFiles, "Search for files in a directory");
}

#endif
