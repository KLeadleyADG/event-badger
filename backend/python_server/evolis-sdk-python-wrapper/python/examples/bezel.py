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
    This example shows how to configure the printer BEZEL.
    The BEZEL is only available, as an option, for KC/KM printers.

    It can be configured in 3 ways :
      - The behavior : What to do if the card is not taken ?
    Re-insert, reject or nothing (the card is kepts in the bezel).
      - The delay : After how many times we consider that the card was not
    taken.
      - The offset : How much the card is ejected (in millimeters).
    """
    name = utils.get_printer_name()
    co = evolis.Connection(name, False)

    if not co.is_open():
        print("> Error: can't open printer context.")
        return EXIT_FAILURE

    # After card ejection, re-insert the card if it's not taken.
    ok = co.set_bezel_behavior(evolis.BezelBehavior.INSERT)

    # If ok, we set the bezel delay to 5 seconds.
    if ok:
        ok = co.set_bezel_delay(5)

    # If ok, we set the bezel offset to 2cm.
    if ok:
        ok = co.set_bezel_offset(20)

    co.close()
    return EXIT_OK

if __name__ == "__main__":
    sys.exit(main())
