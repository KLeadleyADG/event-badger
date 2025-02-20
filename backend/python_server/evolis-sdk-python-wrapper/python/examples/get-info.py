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
    This example shows how to get :
      - Printer information : model, serial number, ...
      - Ribbon information : type, capacity, ...
      - Cleaning information : remaining card before next cleaning, ...
    """
    name = utils.get_printer_name()
    co = evolis.Connection(name, False)

    if not co.is_open():
        print("> Error: can't open printer context.")
        return EXIT_FAILURE

    info = co.get_info()
    if info:
        print("> Printer infos:")
        print("-   Name: ", info.name)
        print("-   Model: ", info.modelName)
        print("-   Serial number: ", info.serialNumber)
        print("-   Duplex printer: ", "yes" if info.hasFlip else "no")
        print("-   ...")

    info = co.get_ribbon_info()
    if info:
        print("> Ribbon infos:")
        print("-   Name: ", info.description)
        print("-   Type: ", info.type)
        print("-   Remaining capacity: %d over %d" %
          (info.remaining, info.capacity))
        print("-   ...")

    info = co.get_cleaning_info()
    if info:
        print("> Cleaning infos:")
        print("-   Number of card before next cleaning: ",
              info.cardCountBeforeWarning)
        print("-   Print head under warranty: ",
              "yes" if info.printHeadUnderWarranty else "no")
        print("-   Number of regular cleaning: ",
              info.regularCleaningCount)
        print("-   Number of advanced cleaning: ",
              info.advancedCleaningCount)
        print("-   ...")

    co.close()
    return EXIT_OK

if __name__ == "__main__":
    sys.exit(main())
