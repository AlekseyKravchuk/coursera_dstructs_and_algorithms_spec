# Import required functions
from setuptools import setup, find_packages

# Call setup() function
setup(
    author="Aleksey Kravchuk",
    description="A complete package for linear regression.",
    name="mysklearn",
    version="0.1.0",
    packages=find_packages(include=["mysklearn", "mysklearn.*"])
)

# As you develop the package you will increment numbers in "version"
# version_number = (major number).(minor number).(patch number)
