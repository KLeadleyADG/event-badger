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
    This example shows how to use the scan API (`ScanSession`) to acquire
    images from the scanner (if option available in your printer).

    If the printer is not supervised by the Evolis Premium Suite, you will have
    to load the WiseCube library by yourself. WiseCube is the provider of the
    scanners embedded in our printers.

    Scan API only supported on Windows systems.
    """
    name = utils.get_printer_name()
    co = evolis.Connection(name, False)

    if not co.is_open():
        print("> Error: can't open printer context.")
        return EXIT_FAILURE

    scan = evolis.ScanSession(co)

    # If printer is not supervised by Evolis service (evoservice), you
    # need to configure the WiseCube SDK by defining DLL's path :
    #evolis.ScanSession.set_library_path("<PATH-TO-wsdef.dll>")

    reply = scan.send_command("#GV")
    print(f"> Send command \"#GV\"")
    print(f"    => rc={scan.get_last_error()}, reply={reply}")

    print(f"> Scan image")
    if scan.acquire():
        print(f"    => Ok")
        scan.save_image(evolis.ScanImage.TOP, "_top.bmp")
        scan.save_image(evolis.ScanImage.TOP_IR, "_top_ir.bmp")
        scan.save_image(evolis.ScanImage.BOTTOM, "_bottom.bmp")
        scan.save_image(evolis.ScanImage.BOTTOM_IR, "_bottom_ir.bmp")
    else:
        print(f"    => {scan.get_last_error()}")

    co.close()
    return EXIT_OK

if __name__ == "__main__":
    sys.exit(main())
