import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import evolis

DEFAULT_PRINTER_NAME = "Evolis Primacy 2"

def get_printer_name() -> str:
    import sys

    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        devices = evolis.Evolis.get_devices()
        selected = None

        for device in devices:
            if selected is None or (not selected.isOnline and device.isOnline):
                selected = device
        if selected:
            return selected.name
    return DEFAULT_PRINTER_NAME