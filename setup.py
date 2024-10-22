from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rotten_korean_romanizer",
    version="0.1.0",
    author="Yonghye Kwon",
    author_email="developer.0hye@gmail.com",
    description="A Python library for romanizing Korean text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/developer0hye/rotten-korean-romanizer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)