#include <pybind11/pybind11.h>
#include "math.hpp"

namespace py = pybind11;

PYBIND11_MODULE(vossen, m)
{
    m.def("add", &add);
    m.def("subtract", &subtract);
}
