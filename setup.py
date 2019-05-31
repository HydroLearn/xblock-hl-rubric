"""Setup for xblock-hl-rubric XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


# Constants #########################################################
VERSION = '1.0.0'

# xblocks  #########################################################
PREREQs = [
    'XBlock',
    'xblock-utils',
    'hl-text-xblock',

]

BLOCKS = [
    # the main learning obj block
    'hl_rubric_text = hl_rubric:HL_Rubric_text_XBlock',

]

setup(
    name='hl-rubric-xblock',
    version=VERSION,
    author="cRivet",
    description='Custom Xblock for providing rubric template for use in HydroLearn platform.',
    packages=[
        'hl_rubric',
    ],
    install_requires=PREREQs,
    entry_points={
        'xblock.v1': BLOCKS
    },
    package_data=package_data("hl_rubric",
                              [
                                    "static",
                                    "public",
                                    "templates"
                              ]),
)
