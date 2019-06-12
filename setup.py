import setuptools


def requirements():
    req = []
    for line in open('requirements.txt', 'r'):
        req.append(line.split()[0])
    return req


setuptools.setup(
    name='social-user-info',
    version='0.4',
    author="Prakkhar Shrivastava",
    author_email="prakhars1996@gmail.com",
    description="A python package that helps getting the user info from social apps",
    url="https://github.com/dev-prakhar/social-user-info",
    packages=setuptools.find_packages(),
    install_requires=requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
