from setuptools import find_packages, setup
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Srinivas"
DESCRIPTION="This is the First Machine Learing Project"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    This function is going to return list of requirement
    mention in requirements.txt file

    return This function is goint to return a list which will contain name of libraries mentioned in requirements.txt file

    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines()
setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
    )
