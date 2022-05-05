import re
import setuptools
from glob import glob


def read_requirements(path: str):
    with open(path, "r") as fh:
        return [line.strip() for line in fh.readlines() if not line.startswith("#")]


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = read_requirements("requirements.txt")

extras_require = {}
for path in glob("requirements.*.txt"):
    match = re.search("(?<=\.).+(?=\.)", path)
    if match:
        mode = match.group(0)
        extras_require[mode] = read_requirements(path)

__VERSION__ = "0.1.0"
__DESCRIPTION__ = "This Niffler finds shiny variables in text"


setuptools.setup(
    name="tiffler",
    packages=setuptools.find_packages(),
    version=__VERSION__,
    author="nghoangdat",
    author_email="dat.nh.216@gmail.com",
    description=__DESCRIPTION__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require=extras_require,
    python_requires=">=3.6",
    install_requires=requirements,
    include_package_data=True,
    keywords=[],
)
