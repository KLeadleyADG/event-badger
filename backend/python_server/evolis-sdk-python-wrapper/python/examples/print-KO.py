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

def main() -> int:
    """
    This example shows how to print a card with KO ribbon.

    In this example, we use a custom bitmap for the overlay panel.
    If we hadn't used a custom bitmap then the overlay panel would have been
    fully printed.
    """
    name = utils.get_printer_name()
    co = evolis.Connection(name, False)

    if not co.is_open():
        print("> Error: can't open printer context.")
        return EXIT_FAILURE

    ps = evolis.PrintSession(co)

    # Set main image:
    if not ps.set_black(evolis.CardFace.FRONT, "resources/back.bmp"):
        print("> Error: can't load file resources/back.bmp")
        return EXIT_FAILURE

    # Set Overlay image:
    if not ps.set_overlay(evolis.CardFace.FRONT, "resources/overlay.bmp"):
        print("> Error: can't load file resources/overlay.bmp")
        return EXIT_FAILURE

    # Print:
    print("> Start printing...")
    r = ps.print()
    print(f"> Print result {str(r)}")

    co.close()
    return EXIT_OK

if __name__ == "__main__":
    sys.exit(main())
