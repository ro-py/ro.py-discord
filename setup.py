import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup_info = {
    "name": "ro.py-bloxlink",
    "version": "2.0.0",
    "author": "jmkdev",
    "author_email": "jmk@jmksite.dev",
    "description": "Small library to connect bloxlink and ro.py",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "https://github.com/jmkd3v/ro.py-bloxlink",
    "packages": setuptools.find_packages(),
    "classifiers": [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: AsyncIO",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Topic :: Software Development :: Libraries"
    ],
    "project_urls": {
        "Discord": "https://discord.gg/tjRfCbDMSk",
        "Issue Tracker": "https://github.com/jmkd3v/ro.py-bloxlink/issues",
        "GitHub": "https://github.com/jmkd3v/ro.py-bloxlink",
        "Twitter": "https://twitter.com/jmkdev"
    },
    "python_requires": '>=3.7',
    "install_requires": []  # fixme
}


setuptools.setup(**setup_info)
