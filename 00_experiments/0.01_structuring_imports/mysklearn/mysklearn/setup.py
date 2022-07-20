# Import required functions
from setuptools import setup, find_packages

# Call setup() function
setup(
    author="Aleksey Kravchuk",
    description="A complete package for linear regression.",
    name="mysklearn",
    version="0.1.0",  # (major number).(minor number).(patch number)
    packages=find_packages(include=["mysklearn", "mysklearn.*"]),
    install_requires=['pandas>=1.0', 'scipy==1.1', 'matplotlib>=2.2.1,<3'],
    python_requires=['>=3.9, !=2.*']
)

# As you develop the package you will increment numbers in "version"
# version_number = (major number).(minor number).(patch number)
