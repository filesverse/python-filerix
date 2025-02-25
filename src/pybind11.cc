#include <pybind11/pybind11.h>
#include "FileSystem/DriveUtils.hpp"
#include "FileSystem/FileUtils.hpp"
#include "FileSystem/UserUtils.hpp"
#include "Listeners/DriveListener.hpp"
#include "Listeners/FileListener.hpp"

PYBIND11_MODULE(filerix, m)
{
  m.doc() = "Python bindings for Filerix";
  init_drive_utils(m);
  init_file_utils(m);
  init_user_utils(m);
  init_drive_listener(m);
  init_file_listener(m);
}
