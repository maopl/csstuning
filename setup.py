import os
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Add benchmarks to data_files
data_files = []
for floder, subfloders, files in os.walk("cssbench"):
    if len(files) > 0:
        data_files.append((floder, [os.path.join(floder, f) for f in files]))

setup(
    name="csstuning",
    version="0.0.1",
    author="An Shao",
    author_email="anshaohac@gmail.com",
    description="Configurable Software System Tuning Benchmark",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neeetman/csstuning",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
    python_requires='>=3.8',
    include_package_data=True,  # This tells setuptools to use MANIFEST.in
    package_data={'csstuning': ['cssbenchmarks/*']}, # include data files in csstuning package
    entry_points={
        "console_scripts": [
            "csstuning=csstuning.kernel:cli"
        ]
    },
    install_requires=[
        "importlib_resources",
    ],
    zip_safe=False
)