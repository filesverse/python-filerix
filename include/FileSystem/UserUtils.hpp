#ifndef FILERIX_USER_UTILS_HPP
#define FILERIX_USER_UTILS_HPP

#include <pybind11/pybind11.h>
#include "filerix/FileSystem/UserUtils.h"

namespace py = pybind11;

inline void init_user_utils(py::module_ &m)
{
  py::module userUtils = m.def_submodule("userUtils", "User utilities module");

  userUtils.def("getUserName", []()
                { return std::string(UserUtils::GetUserName()); }, "Retrieve the current username");

  userUtils.def("changePermissions", &UserUtils::ChangePermissions,
                "Change file permissions for a given path");
}

#endif
