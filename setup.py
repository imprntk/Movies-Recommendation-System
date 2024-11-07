from setuptools import setup , find_packages
import os

if os.path.exists("README.md"):
    with open("README.md", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    long_description = "Package for Movies Recommendation"
      
AUTHOR_NAME = "Pranit K"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ["streamlit"]

setup(
    name = SRC_REPO,
    version = "0.0.1",
    author = AUTHOR_NAME,
    
author_email = "pranitkpersonal@gmail.com",
    description = "Package for Movies Recommendation",
    
long_description = long_description,
long_description_content_type = "text/markdown",
    packages=find_packages(),
    python_requires = ">=3.6",
install_requires = LIST_OF_REQUIREMENTS,
)

