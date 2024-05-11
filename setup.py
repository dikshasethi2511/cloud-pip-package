from setuptools import setup, find_packages

setup(
    name="my_pip_package",
    version="0.2",
    packages=find_packages(),
    install_requires=["grpcio", "protobuf"],
    author="Diksha Sethi",
    author_email="diksha20056@iiitd.ac.in",
    url="https://github.com/dikshasethi2511/cloud-pip-package",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
