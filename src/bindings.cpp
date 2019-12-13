#include <pybind11/pybind11.h>
#include <pybind11/stl_bind.h>
#include "math.hpp"

namespace py = pybind11;
//PYBIND11_MAKE_OPAQUE(std::vector<double>);
PYBIND11_MODULE(vossen, m)
{
    m.def("add", &add);
    m.def("subtract", &subtract);
    m.def("cosfft1", &cosfft1, py::arg("data"), py::arg("n"), py::arg("inverse") = false);
}
