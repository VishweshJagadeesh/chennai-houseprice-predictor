from setuptools import setup, find_packages
from typing import List
HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str) -> List[str]:
    """
    Reads the requirements from a file and returns them as a list.
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements if req.strip() and not req.startswith('#')]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
setup(
    name="ml_project",
    version="0.0.1",
    author="Vishwesh",
    author_email="vishweshjagadeesh@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)