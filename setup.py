from setuptools import find_packages , setup
from typing import List

HYPHEN_E_DOT = '-e .'
def getrequirements(file_path: str)->List[str]:
  requirements =[]
  with open(file_path) as file_obj:
    requirements = file_obj.readlines()
    requirements = [ req.replace('\n' ,"") for req in requirements]
    if (HYPHEN_E_DOT) in requirements:
      requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Praveen',
    author_email='praveenpandey709@gmail.com',
    install_requires=getrequirements('requirements.txt'),
    packages=find_packages()
)