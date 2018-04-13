from setuptools import setup

setup(
    name="yamlcd",
    install_requires=[
        "pyyaml",
        "click"
    ],
    packages=["yamlcd"],
    entry_points={"console_scripts": ["yamlcd=yamlcd.cli:main"]}
)
