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

def show_active_flags(status: evolis.Status):
    print("> Flags on:")
    for flag in status.active_flags():
        print(f"    {repr(flag)}")

def main() -> int:
    """
    This examples shows how you can get data about the printer state.
    There are two types of data "hardware status" and "state" :

      - Hardware status (aka printer flags) are a set of flags split in 4
    categories : CONFIG, INFO, WARNING and ERROR.
    CONFIG flags will describe your printer configuration (if you have magnetic
    encoder or not, dual side printer or not, etc...).
    INFO flags contain information about what the printer is doing.
    For example, you will find flags to know if the printer is printing or not,
    what is the card position in the printer and so on.
    WARNING flags indicate potential issues with the printer
    For example if the cover is open, or the feeder is empty.
    ERROR flags will be raised during a print job when something wrong happens.
    Here you will find flags like ERR_MECHANICAL that will be raised if a
    mechanical error occurred during print or ERR_HOPPER_FULL if the output tray
    is full.

      - The state is split in two substates named MAJOR and MINOR.
    We have 4 MAJOR states : OFF, READY, WARNING and ERROR. The first one means
    that your printer is offline and you should power it on to use it. The
    READY state means that everything is fine : you can print. The WARNING state
    means that your printer is ok but you have to fix something before printing.
    The ERROR state means that something went wrong : The printer will remain
    blocked until the problem is resolved.
    The MINOR state gives a little more detail on the MAJOR state.

    Hardware status is fine-grained data about your printer while state is more
    an overview of the whole printer state.
    """
    name = utils.get_printer_name()
    co = evolis.Connection(name, False)

    if not co.is_open():
        print("> Error: can't open printer context.")
        return EXIT_FAILURE

    # Get printer flags:
    #
    # Flags can be retrieved at every time even when printer is reserved
    # by someone else, processing a command or during print.
    status = co.get_status()
    if status:
        # Check, for example, if there is cards in the feeder:
        if status.is_on(evolis.Status.WarFlag.WAR_FEEDER_EMPTY):
            print("> No cards in the feeder.")

        # Check if printer cover is open:
        if status.is_on(evolis.Status.WarFlag.WAR_COVER_OPEN):
            print("> Printer cover is open, please close it.")

        show_active_flags(status)

    # Get printer logical state:
    #
    # The printer state allows you to know if the printer state is ready or
    # not and gives you hint on the issue.
    state = co.get_state()
    if state:
        if state.major == evolis.State.Major.READY:
            print("> Printer is READY.");
        else:
            print(f"> Printer state is {state.major}:{state.minor}")

    co.close()
    return EXIT_OK

if __name__ == "__main__":
    sys.exit(main())
