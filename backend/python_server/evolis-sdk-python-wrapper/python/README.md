Evolis SDK for Python
=====================

The directory contains resource to use Evolis printers with Python.

**evolis** directory contains Python module and underlying C library.
Import that module in your Python application to start using the SDK.

Next, you will find an **examples/** directory which contains a set of files
containing code samples to understand how to use the SDK.

How to execute an example ?
---------------------------

Some examples uses files from the resources/ directory. That's why it's a good
idea to run examples from the root of the package :

    $ python3 python/examples/get-status.py

By default, the script will take the first Evolis printer found but you can
choose a specific printer by passing its name to the script :

    $ python3 python/examples/get-status.py "Evolis Primacy 2"

Supported platforms
-------------------

We provide binaries for following platforms :

* Windows
    * x86
    * x86_64
* macOS
    * x86_64
    * arm64
* Linux
    * x86_64
    * aarch64
