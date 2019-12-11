#
# Wheel packaging for Vossen project
#

all: bdist_wheel

bdist_wheel:
	python3 setup.py sdist bdist_wheel

setuptools:
	python3 -m pip install --user --upgrade setuptools wheel

pytest:
	python3 setup.py test

clean:
	rm -rf build/ **/*.egg-info/ **/*.so **/__pycache__/ dist/
