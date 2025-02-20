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
    In some particular case it could be usefull to send a raw command to the
    printer. We also call those commands "escape commands".

    Here is an example of how to send the command and get the printer reply.
    """
    name = utils.get_printer_name()
    co = evolis.Connection(name, False)

    if not co.is_open():
        print("> Error: can't open printer context.")
        return EXIT_FAILURE

    # Send command to printer (Rfv to read firmware version):
    #
    # Sending a command to the printer could fail if printer is reserved
    # by someone else (during print for example).
    #
    # Printers can process only one command at a time.
    reply = co.send_command("Rfv")
    if reply != None:
        print(f"> Rfv => {reply}")
    else:
        print(f"> Error: {co.get_last_error()}")

    co.close()
    return EXIT_OK

if __name__ == "__main__":
    sys.exit(main())
