""" Simple setup.py """

from setuptools import setup

setup_info = {
    "name": "videogame",
    "version": "0.1",
    "description": "A package to support writing games with PyGame",
    # TODO: Optional, add more information to the setup.py script
    # "long_description": open("README.md").read(),
    # "author": "Erik Williams",
    # "author_email": "erikpw009@gmail.com",
    # "url": "https://some.url/somehwere/maybe/github",
}

setup(**setup_info)