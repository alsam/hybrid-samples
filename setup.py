#!/usr/bin/env python

import setuptools
import argparse
import os
import re
import sys
import sysconfig
import platform
import shutil
import subprocess

from distutils.version import LooseVersion
from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext
from shutil import copyfile, copymode
import glob

ROOTDIR = os.path.abspath(os.path.dirname(__file__))

class MesonExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

class MesonBuild(build_ext):

    def build_extension(self, ext):
        print('ext.name:', ext.name, ' ext.sourcedir: ', ext.sourcedir)
        extdir = os.path.abspath(
            os.path.dirname(self.get_ext_fullpath(ext.name)))
        print('extdir: ', extdir)
        try:
            out = subprocess.check_output(['meson', '--version'])
            print('found meson version', out.decode())
        except OSError:
            raise RuntimeError(
                "meson must be installed to build the following extensions: " +
                ", ".join(e.name for e in self.extensions))

        print('preparing temporary dir for build: ', self.build_temp)
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        meson_args = [ROOTDIR, '--buildtype', 'debug', '-Db_lto=true']

        subprocess.check_call(['meson'] + meson_args, cwd=self.build_temp)
        subprocess.check_call(['ninja'], cwd=self.build_temp)
        # copy generated shared library
        # create the dir if necessary
        if not os.path.exists(extdir):
            print("creating directory {}".format(extdir))
            os.makedirs(extdir)

        shared_ext = 'dll' if platform.system() == "Windows" else 'so'
        print('shared_ext:', shared_ext, ' build_temp: ', self.build_temp)
        #for file in glob.glob(self.build_temp + r'/**/*.' + shared_ext):
        for file in glob.glob(self.build_temp + r'/*.' + shared_ext):
            print('copying file: ', file)
            copyfile(file, extdir + '/' + os.path.basename(file))
            copymode(file, extdir + '/' + os.path.basename(file))
            copyfile(file, 'src/' + os.path.basename(file))
            copymode(file, 'src/' + os.path.basename(file))
        print()  # Add an empty line for cleaner output

with open("README.md", "r") as fh:
    long_description = fh.read()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("--reconfigure", action='store_true',
                        default=False, help='Force a full reconfiguration'
                        ' meaning the build/ folder is removed.'
                        ' You can also use `ninja reconfigure` to just'
                        ' make sure meson is rerun but the build folder'
                        ' is kept.')
    parser.add_argument("--werror", action='store_true',
                        default=False, help="Do not error out on warnings")
    options, args = parser.parse_known_args()
    setup(
        name="vossen-alsam",
        version="0.0.0",
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=setuptools.find_packages('src'),
        package_dir={'':'src'},

        ext_modules=[MesonExtension('vossen')],
        # add custom build_ext command
        cmdclass=dict(build_ext=MesonBuild),
        test_suite='tests',
        zip_safe=False,
    )
