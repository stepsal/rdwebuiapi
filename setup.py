""" See:
https://github.com/stepsal/rdwebuiapi/"
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="rdwebuiapi",
    version="0.0.1",
    description="Python API client for Run Diffusion installation of AUTOMATIC1111/stable-diffusion-webui",
    url="https://github.com/stepsal/rdwebuiapi/",
    author="Stephen Salmon",
    author_email="stephensalmon.mayo@gmail.com",
    keywords="stable-diffuion-webui, AUTOMATIC1111, stable-diffusion, api, Run Diffusion",
    packages=["rdwebuiapi"],
    #packages=find_packages(),
    python_requires=">=3.7, <4",
    install_requires=['requests',
                      'Pillow',],
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
)
