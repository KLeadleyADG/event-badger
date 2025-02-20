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

def configure_card_in_out(co: evolis.Connection) -> bool:
    r = True

    # Set card insertion mode :
    if r:
        r = co.set_input_tray(evolis.InputTray.FEEDER)

    # Set card ejection mode :
    if r:
        r = co.set_output_tray(evolis.OutputTray.STANDARD)

    # Set card rejection mode :
    if r:
        r = co.set_error_tray(evolis.OutputTray.ERROR)

    return r

def print_card(co: evolis.Connection) -> bool:
    # Set bitmaps to print :
    ps = evolis.PrintSession(co)
    if not ps.set_image(evolis.CardFace.FRONT, "resources/front.bmp"):
        print("> Error: can't load file resources/front.bmp")
        return EXIT_FAILURE

    # Print :
    print("> Start printing...")
    rc = ps.print()
    if rc == evolis.ReturnCode.OK:
        print("> Print done.")
    elif rc == evolis.ReturnCode.PRINT_NEEDACTION:
        # One of those flags is on :
        # ------------------------
        #
        # WAR_COVER_OPEN)
        # WAR_UNSUPPORTED_RIBBON)
        # WAR_RIBBON_ENDED)
        # WAR_NO_RIBBON)
        # WAR_FEEDER_EMPTY)
        # WAR_PRINTER_LOCKED)
        # WAR_REMOVE_RIBBON)
        # WAR_HOPPER_FULL)
        # WAR_REJECT_BOX_FULL))
        # if (EX1_CFG_LAMINATOR)
        #     EX2_DEF_LAMI_HOPPER_FULL
        #     EX2_DEF_LAMI_COVER_OPEN)
        #     EX2_DEF_LAMINATE_UNSUPPORTED)
        #     EX2_DEF_LAMINATE_END)
        #     EX2_DEF_NO_LAMINATE))
        #
        # Example :
        # -------
        status = co.get_status()
        if status and status.is_on(evolis.Status.WarFlag.WAR_COVER_OPEN):
            print("> Please close the cover before print.")
    elif rc == evolis.ReturnCode.PRINT_EMECHANICAL:
        print("> Clearing printer errors.")
        ps.clear_mechanical_errors()

def main() -> int:
    """
    This code is a full example with the following steps :
      - Make a card insertion.
      - Move the card to contact less station for smart encoding.
      - <The smart encoding is made by your side.>
      - If the smart encoding is ok :
        - We proceed to a magnetic encoding.
        - If the magnetic encoding is ok :
          - The card is printed.

    At the end of the example, you will find a sample code to understand
    how to check if the print is ok or not.
    """
    name = utils.get_printer_name()
    co = evolis.Connection(name, False)

    if not co.is_open():
        print("> Error: can't open printer context.")
        return EXIT_FAILURE

    # Getting the state of the printer.
    state = co.get_state()
    if state.major != evolis.State.Major.READY:
        print(f"> Error: printer is not ready: {state.major} / {state.minor}")
        return EXIT_FAILURE

    if configure_card_in_out(co):
        encodingOk = True

        # Insert the card then move it to SMART station.
        co.insert_card()
        co.set_card_pos(evolis.CardPos.CONTACTLESS)
        # ... Please do your encoding process here ...

        if encodingOk:
            print_card(co)

    co.close()
    return EXIT_OK

if __name__ == "__main__":
    sys.exit(main())
