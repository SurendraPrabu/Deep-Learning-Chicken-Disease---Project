import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Deep-Learning-Chicken-Disease---Project",
    version="0.0.1",
    author="SurendraPrabu",
    SRC_REPO = "cnnClassifier",
    author_email="surrey33@gmail.com",
    description="A simple CNN classifier for chicken disease detection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{author}/{name}",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)