import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easystyle",
    version="1.2.1",
    author="Ethan Robbins",
    author_email="ethan.d.robbins@gmail.com",
    description="A package to allow for basic visuals with pandas dataframes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ethandrobbins/easystyle",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)