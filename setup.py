import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WeightedListPicker",
    version="0.0.2",
    author="SirRolf",
    author_email="Flomo123456789@gmail.com",
    description="A Weighted list picker. throw in two lists, One with any type variable and the other with chances in the form of int variables.",
    long_description="A handy library that can pick a variable out of a list, but you can give certain weights to variables out of the list. You can do this by making to lists, one with the variables you want to pick out and one with the chances of each variable.",
    long_description_content_type="text/markdown",
    url="https://github.com/SirRolf/WeightedListPicker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
