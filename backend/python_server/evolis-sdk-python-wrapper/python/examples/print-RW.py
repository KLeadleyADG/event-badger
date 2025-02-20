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
    This example shows how to print on a rewritable card.

    Uncomment FHalftoning setting line and lines configuring rw areas to see
    what is changing on the print.
    """
    name = utils.get_printer_name()
    co = evolis.Connection(name, False)

    if not co.is_open():
        print("> Error: can't open printer context.")
        return EXIT_FAILURE

    ps = evolis.PrintSession(co, rwCard=evolis.RwCardType.MBLACK)

    # Image processing algorithm can be customized with FHalftoning setting.
    #ps.set_setting(evolis.SettingKey.FHalftoning, "FLOYD")

    # Set the image to print to the card:
    if not ps.set_image(evolis.CardFace.FRONT, "resources/back.bmp"):
        print("> Error: can't load file resources/back.bmp")
        return EXIT_FAILURE

    # In addition to the image configured above, you can, optionally, restrict
    # the printed areas with a monochrome image:
    #if not ps.set_rw_areas(evolis.CardFace.FRONT, "resources/black-overlay.bmp"):
    #    print("> Error: can't load file resources/black-overlay.bmp")
    #    return EXIT_FAILURE

    # Print:
    print("> Start printing...")
    r = ps.print()
    print(f"> Print result {str(r)}")

    co.close()
    return EXIT_OK

if __name__ == "__main__":
    sys.exit(main())
