import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WeightedListPicker-SirRolf",
    version="0.0.1",
    author="SirRolf",
    author_email="Flomo123456789@gmail.com",
    description="A Weighted list picker. throw in two lists, One with any type variable and the other with chances in the form of int variables.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SirRolf/WeightedListPicker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
