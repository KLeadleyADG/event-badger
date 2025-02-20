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
    KC Max printers can be use like any other EVOLIS printers.
    The only difference is the management of the 4 feeders.

    Basically, you can use the same flags that you would have use
    on other printers : WAR_FEEDER_EMPTY, EX1_INF_FEEDER_NEAR_EMPTY.
    Those flags will give the state of the feeder currently in front of the
    printer. So if you want the state of the feeder C, you have to configure
    the feeder C as the current one.

    Change the value given to `Connection.set_feeder()` to see what happens
    on the printer. Remove cards from one of the feeder to see the status
    change.
    """
    name = utils.get_printer_name()
    co = evolis.Connection(name, False)
    ps = evolis.PrintSession(co)
    status = None

    if not co.is_open():
        print("> Error: can't open printer context.")
        return EXIT_FAILURE

    # Disable/Enable auto ejection at end of print.
    # Ejection is enabled by default.
    ps.set_auto_eject(False)

    # Choose feeder to be used.
    co.set_feeder(evolis.Feeder.C)

    # Retrieve printer flags.
    status = co.get_status()
    if status:
        # Check the state of the feeder.
        if status.is_on(evolis.Status.WarFlag.WAR_FEEDER_EMPTY):
            print("> Error: the feeder is empty.")
        else:
            print("> Everything is good. Make your print here.")

            # Don't forget to eject card if default behavior was disabled.
            co.eject_card()

    co.close()
    return EXIT_OK

if __name__ == "__main__":
    sys.exit(main())
