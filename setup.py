from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Manav664",
    description="A small package for dvc ml pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Manav664/MLOps-Demo.git",
    author_email="19bce062@nirmauni.ac.in",
    packages=["src"],
    python_requires=">=3.6",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)