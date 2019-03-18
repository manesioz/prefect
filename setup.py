# Licensed under LICENSE.md; also available at https://www.prefect.io/licenses/beta-eula

import sys

from setuptools import find_packages, setup

import versioneer

## base requirements
install_requires = open("requirements.txt").read().strip().split("\n")
dev_requires = open("dev-requirements.txt").read().strip().split("\n")

extras = {
    "dev": dev_requires,
    "viz": ["graphviz >= 0.8.3"],
    "templates": ["jinja2 >= 2.0, < 3.0"],
}

if sys.version_info >= (3, 6):
    extras["dev"] += ["black"]

extras["all_extras"] = extras["dev"] + extras["viz"] + extras["templates"]


setup(
    name="prefect",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    install_requires=install_requires,
    extras_require=extras,
    scripts=[],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    entry_points={"console_scripts": ["prefect=prefect.cli:cli"]},
    python_requires=">=3.5",
    description="The Prefect Core automation and scheduling engine.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://www.github.com/PrefectHQ/prefect",
    author="Prefect Technologies, Inc.",
    author_email="help@prefect.io",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Monitoring",
    ],
)
