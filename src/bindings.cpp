#include "math.hpp"

PYBIND11_MAKE_OPAQUE(std::vector<double>);
PYBIND11_MODULE(vossen, m)
{
    py::bind_vector<std::vector<double>>(m, "VectorDouble", py::buffer_protocol());
    m.def("add", &add);
    m.def("subtract", &subtract);
    m.def("cosfft1", &cosfft1, py::arg("data"), py::arg("n"), py::arg("inverse") = false);
    m.def("cft2", &cft2, py::arg("data"), py::arg("nn"), py::arg("inverse") = false);
    m.def("scale_by_2", &scale_by_2);
}
