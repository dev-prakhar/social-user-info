import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='social-user-info',
    version='0.1',
    author="Prakkhar Shrivastava",
    author_email="prakhars1996@gmail.com",
    description="A python package that helps authorization with social apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dev-prakhar/social-authentication.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
