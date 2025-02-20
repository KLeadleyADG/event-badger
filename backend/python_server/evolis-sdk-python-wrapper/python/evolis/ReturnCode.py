# Evolis SDK for Python
#
# THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
# ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
# PARTICULAR PURPOSE.

from enum import Enum

class ReturnCode(Enum):
    """
    Return code values.
    """

    def from_int(n:int):
        """
        Create a ReturnCode enum from integer.

        Parameters
        ----------
        n: int
            Value to convert to ReturnCode.

        Returns
        -------
        ReturnCode:
            The converted value.
        """
        rc = ReturnCode.OK
        if n < 0:
            try:
                rc = ReturnCode(n)
            except ValueError:
                rc = ReturnCode.EUNDEFINED
        return rc

    OK = 0
    """ Everything is good. """

    EUNDEFINED = -1
    """ Error code when an undefined error occurs. """

    EUNSUPPORTED = -5
    """ Error code when the library or printer does not support requested feature. """

    EPARAMS = -6
    """ Invalid params given to the API. """

    ETIMEOUT = -7
    """ A timeout occured during function call. """

    SESSION_ETIMEOUT = -10
    """ Printer reservation have expired. """

    SESSION_EBUSY = -11
    """ Printer in use, session detected. """

    SESSION_DISABLED = -12
    """ Session management is disabled. See evolis_set_session_management(). """

    PRINT_EDATA = -20
    """ Bad input data, check images and options. """

    PRINT_NEEDACTION = -21
    """ Printer not ready to print. Cover open ? Feeder ? """

    PRINT_EMECHANICAL = -22
    """ Mechanical error happened while printing. """

    PRINT_WAITCARDINSERT = -23
    """ Avansia only """

    PRINT_WAITCARDEJECT = -24
    """ Avansia only """

    PRINT_EUNKNOWNRIBBON = -25
    """ Missing GRibbonType option. """

    PRINT_ENOIMAGE = -26
    """ No image given. """

    PRINT_WSETTING = -27
    """ Settings were imported from the driver, and at least one could not be read """

    MAG_ERROR = -50
    """ Error reading or writing magnetic data. """

    MAG_EDATA = -51
    """ The data that you are trying to write on the magnetic track is not valid. """

    MAG_EBLANK = -52
    """ Magnetic track is blank. """

    PRINTER_ENOCOM = -60
    """ Printer offline. """

    PRINTER_EREPLY = -61
    """ Printer reply contains "ERR". """

    PRINTER_EOTHER = -62
    """ macOS only. USB printer in use by other software. """

    PRINTER_EBUSY = -63
    """ macOS only. CUPS is printing. """

    PRINTER_NOSTATUS = -64
    """ Status disabled on the printer. """

