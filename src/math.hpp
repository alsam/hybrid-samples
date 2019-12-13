#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

/*! Add two integers
    \param i an integer
    \param j another integer
*/
int add(int i, int j);
/*! Subtract one integer from another 
    \param i an integer
    \param j an integer to subtract from \p i
*/
int subtract(int i, int j);

void cosfft1(std::vector<double>& data, unsigned n, bool inverse = false);

inline void scale_by_2(Eigen::Ref<Eigen::VectorXd> v) {
    v *= 2;
}

