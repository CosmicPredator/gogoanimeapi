from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="gogoanime-api",
    version="1.2.458",
    description="Unofficial API Library for Downloading Anime Dubbed and Subbed",
    py_modules=["gogoanimeapi"],
    package_dir={'': 'src'},
    install_requires=["bs4", "requests", "requests_html"],
    extras_require={
                      "dev":[
                          "pytest",
                      ],},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BaraniARR/gogoanimeapi",
    author="BaraiARR",
    author_email="kumarbarani61@gmail.com"

)