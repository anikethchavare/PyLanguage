# PyLanguage - setup.py

''' This is the 'setup.py' file. '''

'''
Copyright 2023 Aniketh Chavare

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

# Imports
from setuptools import setup, find_packages

# README.md
with open("README.md") as readme_file:
    README = readme_file.read()

# Setup Arguments
setup_args = dict (
    name = "PyLanguage",
    version = "1.1.0",
    description = "This Python package contains classes, modules, and functions associated with communication and language.",
    long_description = README,
    long_description_content_type = "text/markdown",
    license = "Apache License 2.0",
    packages = find_packages(),
    include_package_data = True,
    author = "Aniketh Chavare",
    author_email = "anikethchavare@outlook.com",
    url = "https://github.com/anikethchavare/PyLanguage",
    download_url = "https://pypi.org/project/PyLanguage",
    install_requires = [
        "beautifulsoup4",
        "colorama",
        "requests",
        "importlib-metadata",
        "pyttsx3"
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development"
    ]
)

# Running the Setup File
if __name__ == "__main__":
    setup(**setup_args)