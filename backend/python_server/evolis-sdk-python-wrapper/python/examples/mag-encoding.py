#!/usr/bin/env python3
#
# Evolis SDK for Python
#
# THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
# ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
# PARTICULAR PURPOSE.

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import evolis
import utils

EXIT_OK = 0
EXIT_FAILURE = 1

TRACKS = [
    "0123456789AZERTYUIOPMLKJHGFDSQWXCVBN12345678912345123456789012345ABKIYTRLM",
    "1234567891234567891234567891234567891",
    "1234567891234567891234567891234567891"
]

def main() -> int:
    """
    This example shows how to use the magnetic encoding API.
    As you will see by reading the code below, you can encode 1, 2 or 3 tracks
    at the same time.
    """
    name = utils.get_printer_name()
    co = evolis.Connection(name, False)

    if not co.is_open():
        print("> Error: can't open printer context.")
        return EXIT_FAILURE

    ms = evolis.MagSession(co)

    # Write magnetic tracks:
    ms.set_coercivity(evolis.MagCoercivity.HICO)
    ms.set_track(0, evolis.MagFormat.ISO1, TRACKS[0])
    ms.set_track(1, evolis.MagFormat.ISO2, TRACKS[1])
    ms.set_track(2, evolis.MagFormat.ISO3, TRACKS[2])

    rc = ms.write()
    if rc == evolis.ReturnCode.OK:
        print("> Write done.")
    else:
        print(f"> Write error: {rc}.")

    # Read magnetic tracks:
    rc = ms.read()
    if rc == evolis.ReturnCode.OK:
        print(f"> Read:")
        print(f"-  Coercivity: {ms.get_coercivity()}")
        print(f"-  Track 0: {ms.get_format(0)} / {ms.get_data(0)}")
        print(f"-  Track 1: {ms.get_format(1)} / {ms.get_data(1)}")
        print(f"-  Track 2: {ms.get_format(2)} / {ms.get_data(2)}")
    else:
        print(f"> Read error: {rc}.")

    # To write only one track at a time please simply use
    # MagSession#set_track() once.
    #
    # Example of how to write first track only:
    ms.init()
    ms.set_track(0, evolis.MagFormat.ISO1, "HELLO")

    rc = ms.write()
    if rc == evolis.ReturnCode.OK:
        print(f"> Write track done.")
    else:
        print(f"> Write track error: {rc}.")

    co.close()
    return EXIT_OK

if __name__ == "__main__":
    sys.exit(main())
