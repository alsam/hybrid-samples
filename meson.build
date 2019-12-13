project('vossen', ['c', 'cpp'],
        meson_version: '>= 0.46',
        default_options: ['c_std=c11',])

src = [
  'src/bindings.cpp',
  'src/math.cpp',
  'src/cft.cpp',
]

pymod = import('python')
py = pymod.find_installation('python3')
py.extension_module('vossen',
                    sources: src,
                    include_directories: ['lib/pybind11/include','/usr/include/eigen3'],
                    dependencies: dependency('python3'))
