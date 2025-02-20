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
    This example shows how to print with a YMCKO ribbon.

    As you will see below, we also use some functions to configure
    how the card is inserted and ejected.
    """
    name = utils.get_printer_name()
    co = evolis.Connection(name, False)

    if not co.is_open():
        print("> Error: can't open printer context.")
        return EXIT_FAILURE

    # Set card insertion mode :
    co.set_input_tray(evolis.InputTray.FEEDER)

    # Set card ejection mode :
    co.set_output_tray(evolis.OutputTray.STANDARD)

    # Set card rejection mode :
    co.set_error_tray(evolis.OutputTray.ERROR)

    # Set front and back faces :
    ps = evolis.PrintSession(co)

    # If you want to use the settings set by driver :
    #ps.init_from_driver_settings()

    # If you want to force YMCKO ribbon :
    #ps.init_with_ribbon(evolis.RibbonType.YMCKOO)

    # If you don't want to eject the card post print.
    #ps.set_auto_eject(False)

    if not ps.set_image(evolis.CardFace.FRONT, "resources/front.bmp"):
        print("> Error: can't load file resources/front.bmp")
        return EXIT_FAILURE
    if not ps.set_image(evolis.CardFace.BACK, "resources/back.bmp"):
        print("> Error: can't load file resources/back.bmp")
        return EXIT_FAILURE

    # Print :
    print("> Start printing...")
    rc = ps.print()
    print(f"> Print result: {rc}.")

    # Trigger card ejection if "ps.set_auto_eject(False)" was used
    #co.eject_card()

    co.close()
    return EXIT_OK

if __name__ == "__main__":
    sys.exit(main())
