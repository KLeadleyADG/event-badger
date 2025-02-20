# Evolis SDK for Python
#
# THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
# ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
# PARTICULAR PURPOSE.

import ctypes
from enum import IntFlag

class _CStatus(ctypes.Structure):
    _fields_ = [
        ("config", ctypes.c_uint32),
        ("information", ctypes.c_uint32),
        ("warning", ctypes.c_uint32),
        ("error", ctypes.c_uint32),
        ("exts", ctypes.c_uint32 * 4),
        ("session", ctypes.c_uint32),
    ]

class Status:
    """
    Printer status flags.
    """

    class CfgFlag(IntFlag):
        CFG_X01 = 0x80000000
        """Raised for Primacy, KC200B, KC200, Issengo"""

        CFG_X02 = 0x40000000
        """Raised for Zenius"""

        CFG_R02 = 0x20000000
        """Raised for Agilia"""

        CFG_X04 = 0x10000000
        """Raised for Elypso"""

        CFG_EXTENSION_1 = 0x08000000
        """Extension 1 is used"""

        CFG_S01 = 0x04000000
        """Raised for Badgy, Apteo"""

        CFG_X07 = 0x02000000
        """Not used"""

        CFG_KC200 = 0x01000000
        """Raised for KC200B, KC200"""

        CFG_WIFI = 0x00800000
        """WiFi option is detected"""

        CFG_ETHERNET = 0x00400000
        """Ethernet option is detected"""

        CFG_USB_OVER_IP = 0x00200000
        """USB over IP option is set"""

        CFG_FLIP = 0x00100000
        """Flip-over option is detected"""

        CFG_CONTACTLESS = 0x00080000
        """Contactless option is detected"""

        CFG_SMART = 0x00040000
        """Smart option is detected"""

        CFG_MAGNETIC = 0x00020000
        """Magnetic option is detected"""

        CFG_REWRITE = 0x00010000
        """Rewrite mode is activated"""

        CFG_FEED_MANUALLY = 0x00008000
        """Card feeding is configured as manual"""

        CFG_FEED_BY_CDE = 0x00004000
        """Card feeding is set as manual once the feeding command is received"""

        CFG_FEED_BY_FEEDER = 0x00002000
        """Card feeding is configured as feeder"""

        CFG_EJECT_REVERSE = 0x00001000
        """Card ejection goes to manual feeder"""

        CFG_FEED_CDE_REVERSE = 0x00000800
        """Card insertion is set to the rear of the printer"""

        CFG_EXTENDED_RESOLUTION = 0x00000400
        """Extended resolution supported (600DPI, 1200DPI)"""

        CFG_LCD = 0x00000200
        """LCD option detected"""

        CFG_LOCK = 0x00000100
        """Locking system detected"""

        CFG_OEM = 0x00000080
        """Raised for rebranded products"""

        CFG_JIS_MAG_HEAD = 0x00000040
        """JIS magnetic option detected"""

        CFG_REJECT_SLOT = 0x00000020
        """Reject slot enabled"""

        CFG_IO_EXT = 0x00000010
        """IO extender detected"""

        CFG_MONO_ONLY = 0x00000008
        """Monochrome only printing authorized"""

        CFG_KC100 = 0x00000004
        """Raised for KC100"""

        CFG_KINE = 0x00000002
        """Kineclipse option is available"""

        CFG_WIFI_ENA = 0x00000001
        """WiFi option is activated"""


    class InfFlag(IntFlag):
        INF_CLAIM = 0x80000000
        """Raised when EPS printing"""

        INF_CARD_HOPPER = 0x40000000
        """Card present at the hopper"""

        INF_CARD_FEEDER = 0x20000000
        """Card present in the feeder"""

        INF_CARD_FLIP = 0x10000000
        """Card present in the flip-over"""

        INF_CARD_CONTACTLESS = 0x08000000
        """Card present in contactless card station"""

        INF_CARD_SMART = 0x04000000
        """Card present in smart card station"""

        INF_CARD_PRINT = 0x02000000
        """Card present in printing position"""

        INF_CARD_EJECT = 0x01000000
        """Card present in eject position"""

        INF_PRINTER_MASTER = 0x00800000
        """Error management is set to 'printer'"""

        INF_PCSVC_LOCKED = 0x00400000
        """The EPS is supervising the printer"""

        INF_SLEEP_MODE = 0x00200000
        """Printer is in sleep mode"""

        INF_UNKNOWN_RIBBON = 0x00100000
        """Installed ribbon is unknown/unreadable"""

        INF_RIBBON_LOW = 0x00080000
        """Remaining ribbon is below low limit"""

        INF_CLEANING_MANDATORY = 0x00040000
        """Cleaning is mandatory"""

        INF_CLEANING = 0x00020000
        """Cleaning is recommended"""

        INF_RESET = 0x00010000
        """Printer has just rebooted"""

        INF_CLEAN_OUTWARRANTY = 0x00008000
        """Warranty lost, cleaning has not been done in time"""

        INF_CLEAN_LAST_OUTWARRANTY = 0x00004000
        """Cleaning is mandatory, next card printed will lose the warranty"""

        INF_CLEAN_2ND_PASS = 0x00002000
        """Cleaning sequence requires the second cleaning card"""

        INF_READY_FOR_CLEANING = 0x00001000
        """Printer ready for cleaning (ribbon has been removed and cover closed)"""

        INF_CLEANING_ADVANCED = 0x00000800
        """Advanced cleaning requested"""

        INF_WRONG_ZONE_RIBBON = 0x00000400
        """Installed ribbon has not the right zone"""

        INF_RIBBON_CHANGED = 0x00000200
        """Installed ribbon is different from the previous one"""

        INF_CLEANING_REQUIRED = 0x00000100
        """Cleaning is required"""

        INF_PRINTING_RUNNING = 0x00000080
        """Printing is in progress"""

        INF_ENCODING_RUNNING = 0x00000040
        """Encoding is in progress (smart, contactless or magnetic)"""

        INF_CLEANING_RUNNING = 0x00000020
        """Cleaning is in progress"""

        INF_WRONG_ZONE_ALERT = 0x00000010
        """Installed ribbon has wrong zone, there are only a few prints remaining before printing is blocked"""

        INF_WRONG_ZONE_EXPIRED = 0x00000008
        """Installed ribbon has wrong zone, printing is not allowed"""

        INF_SYNCH_PRINT_CENTER = 0x00000004
        """Raised by EPS during a pop-up"""

        INF_UPDATING_FIRMWARE = 0x00000002
        """Firmware is currently downloading"""

        INF_BUSY = 0x00000001
        """The printer is busy (printing, encoding)"""


    class WarFlag(IntFlag):
        WAR_POWER_SUPPLY = 0x80000000
        """Power supply voltage is too low"""

        WAR_REMOVE_RIBBON = 0x40000000
        """Ribbon must be removed (in rewrite mode)"""

        WAR_RECEPTACLE_OPEN = 0x10000000
        """Not used"""

        WAR_REJECT_BOX_FULL = 0x08000000
        """Reject box is full"""

        WAR_CARD_ON_EJECT = 0x04000000
        """Card in eject position and has to be removed (in manual insertion mode)"""

        WAR_WAIT_CARD = 0x02000000
        """Printer is waiting for manual card insertion"""

        WAR_FEEDER_EMPTY = 0x01000000
        """Feeder is empty"""

        WAR_COOLING = 0x00200000
        """Print head temperature too high: cooling down"""

        WAR_HOPPER_FULL = 0x00100000
        """Printer hopper is full"""

        WAR_RIBBON_ENDED = 0x00080000
        """Installed ribbon reached its end"""

        WAR_PRINTER_LOCKED = 0x00040000
        """Printer is locked (used with locking system)"""

        WAR_COVER_OPEN = 0x00020000
        """Printer cover is opened"""

        WAR_NO_RIBBON = 0x00010000
        """No ribbon detected in the printer"""

        WAR_UNSUPPORTED_RIBBON = 0x00008000
        """Installed ribbon is not supported by the printer"""

        WAR_NO_CLEAR = 0x00002000
        """No clear ribbon installed"""

        WAR_CLEAR_END = 0x00001000
        """Clear ribbon reached its end"""

        WAR_CLEAR_UNSUPPORTED = 0x00000800
        """Installed clear ribbon is not supported by the printer"""

        WAR_REJECT_BOX_COVER_OPEN = 0x00000400
        """Reject box cover is open"""

        WAR_EPS_NO_AUTO = 0x00000200
        """For tagless ribbons, indicates to the EPS to not automatically set the ribbon"""

        WAR_FEEDER_OPEN = 0x00000100
        """Printer feeder is opened"""


    class ErrFlag(IntFlag):
        ERR_HEAD_TEMP = 0x20000000
        """Job interrupted because the print head temperature was too high"""

        ERR_NO_OPTION = 0x10000000
        """Requested option is not available"""

        ERR_FEEDER_ERROR = 0x08000000
        """Error while feeding a card"""

        ERR_RIBBON_ERROR = 0x04000000
        """Ribbon error during printing"""

        ERR_COVER_OPEN = 0x02000000
        """Job interrupted by an open cover"""

        ERR_MECHANICAL = 0x01000000
        """Mechanical error (card jam, ribbon jam, ...)"""

        ERR_REJECT_BOX_FULL = 0x00800000
        """Card sent to reject box but it was full"""

        ERR_BAD_RIBBON = 0x00400000
        """Job interrupted because the installed ribbon is not the one expected"""

        ERR_RIBBON_ENDED = 0x00200000
        """Job interrupted because the ribbon is finished"""

        ERR_HOPPER_FULL = 0x00100000
        """Card sent to hopper but it was full"""

        ERR_BLANK_TRACK = 0x00080000
        """No data on track after magnetic reading"""

        ERR_MAGNETIC_DATA = 0x00040000
        """Magnetic data is not matching the settings"""

        ERR_READ_MAGNETIC = 0x00020000
        """Corrupted/absent data on track after magnetic reading"""

        ERR_WRITE_MAGNETIC = 0x00010000
        """Corrupted/absent data on track after magnetic encoding"""

        ERR_FEATURE = 0x00008000
        """Job sent is not supported by the printer"""

        ERR_RET_TEMPERATURE = 0x00004000
        """Retransfer roller couldn't reach its operating temperature in time"""

        ERR_CLEAR_ERROR = 0x00002000
        """Clear ribbon error during printing"""

        ERR_CLEAR_ENDED = 0x00001000
        """Job interrupted because the clear ribbon is finished"""

        ERR_BAD_CLEAR = 0x00000800
        """Job interrupted because the installed clear ribbon is not the one expected"""

        ERR_REJECT_BOX_COVER_OPEN = 0x00000400
        """Card sent to reject box but its cover was open"""

        ERR_CARD_ON_EJECT = 0x00000200
        """Card in eject position was not removed in time (in manual insertion mode)"""

        ERR_NO_CARD_INSERTED = 0x00000100
        """No card was presented in time (in manual insertion mode)"""

        ERR_FEEDER_OPEN = 0x00000080
        """Job interrupted because the printer feeder is opened"""


    class Ex1Flag(IntFlag):
        EX1_CFG_EXTENSION_2 = 0x80000000
        """Extension 2 is used"""

        EX1_CFG_KIOSK = 0x40000000
        """Raised for KM500B, KM2000B"""

        EX1_CFG_QUANTUM = 0x20000000
        """Raised for Quantum"""

        EX1_CFG_SECURION = 0x10000000
        """Raised for Securion"""

        EX1_CFG_DUALYS = 0x08000000
        """Raised for Dualys"""

        EX1_CFG_PEBBLE = 0x04000000
        """Raised for Pebble"""

        EX1_CFG_SCANNER = 0x02000000
        """Scanner option is detected"""

        EX1_CFG_MEM_LAMINATION_MODULE_2 = 0x01000000
        """Printer has previously seen 2 lamination modules simultaneously"""

        EX1_INF_NO_LAMINATION_TO_DO = 0x00800000
        """Lamination module is set to 'pass through' mode"""

        EX1_CFG_SEICO_FEEDER = 0x00400000
        """Seico feeder configured"""

        EX1_CFG_KYTRONIC_FEEDER = 0x00200000
        """Kytronics feeder configured"""

        EX1_CFG_HOPPER = 0x00100000
        """Not used"""

        EX1_CFG_LAMINATOR = 0x00080000
        """Lamination module detected"""

        EX1_INF_LAMI_ALLOW_TO_INSERT = 0x00040000
        """Lamination module ready to insert card"""

        EX1_INF_LAMINATING_RUNNING = 0x00020000
        """Lamination process is running"""

        EX1_INF_CLEAN_REMINDER = 0x00010000
        """Reminder to clean the laminator"""

        EX1_INF_LAMI_TEMP_NOT_READY = 0x00008000
        """Lamination roller is heating up, but its temperature is currently too low for the lamination process"""

        EX1_INF_SYNCHRONOUS_MODE = 0x00004000
        """Lamination process is set to synchronous"""

        EX1_INF_LCD_BUT_ACK = 0x00002000
        """LCD pop up button acknowledged"""

        EX1_INF_LCD_BUT_OK = 0x00001000
        """LCD pop up OK button pressed"""

        EX1_INF_LCD_BUT_RETRY = 0x00000800
        """LCD pop up Retry button pressed"""

        EX1_INF_LCD_BUT_CANCEL = 0x00000400
        """LCD pop up Cancel button pressed"""

        EX1_CFG_BEZEL = 0x00000200
        """Bezel option installed"""

        EX1_INF_FEEDER_NEAR_EMPTY = 0x00000100
        """Feeder is near empty (low level sensor)"""

        EX1_INF_FEEDER1_EMPTY = 0x00000080
        """Feeder 1 is empty for KM2000B"""

        EX1_INF_FEEDER2_EMPTY = 0x00000040
        """Feeder 2 is empty for KM2000B"""

        EX1_INF_FEEDER3_EMPTY = 0x00000020
        """Feeder 3 is empty for KM2000B"""

        EX1_INF_FEEDER4_EMPTY = 0x00000010
        """Feeder 4 is empty for KM2000B"""

        EX1_INF_FEEDER1_NEAR_EMPTY = 0x00000008
        """Feeder 1 is near empty for KM2000B"""

        EX1_INF_FEEDER2_NEAR_EMPTY = 0x00000004
        """Feeder 2 is near empty for KM2000B"""

        EX1_INF_FEEDER3_NEAR_EMPTY = 0x00000002
        """Feeder 3 is near empty for KM2000B"""

        EX1_INF_FEEDER4_NEAR_EMPTY = 0x00000001
        """Feeder 4 is near empty for KM2000B"""


    class Ex2Flag(IntFlag):
        EX2_CFG_EXTENSION_3 = 0x80000000
        """Extension 3 is used"""

        EX2_INF_SA_PROCESSING = 0x40000000
        """Sensor adjustment is running"""

        EX2_INF_SCP_PROCESSING = 0x20000000
        """Cleaning sequence is running"""

        EX2_INF_OPT_PROCESSING = 0x10000000
        """Option activation is running (with activation key)"""

        EX2_INF_X08_PRINTER_UNLOCKED = 0x08000000
        """Lock system currently unlocked"""

        EX2_INF_X08_FEEDER_OPEN = 0x04000000
        """Feeder cover is open (used with locking system)"""

        EX2_INF_X08_EJECTBOX_FULL = 0x02000000
        """Locking system feeder eject box full"""

        EX2_INF_X08_PRINT_UNLOCKED = 0x01000000
        """Printing is currently unlocked, both mechanically and firmware-wise"""

        EX2_CFG_LAMINATION_MODULE_2 = 0x00800000
        """Second lamination module detected"""

        EX2_INF_LAMINATE_UNKNOWN = 0x00400000
        """Installed laminate film is unknown/unreadable"""

        EX2_INF_LAMINATE_LOW = 0x00200000
        """Laminate film is close to its end"""

        EX2_INF_LAMI_CARD = 0x00100000
        """Card present in the lamination module"""

        EX2_INF_LAMI_CLEANING_RUNNING = 0x00080000
        """Lamination module cleaning process is running"""

        EX2_INF_LAMI_UPDATING_FIRMWARE = 0x00040000
        """Lamination module firmware update is running"""

        EX2_INF_LAMI_READY_FOR_CLEANING = 0x00020000
        """Lamination module ready for cleaning (no laminate film and cover closed)"""

        EX2_INF_CARD_REAR = 0x00010000
        """Card present at the rear of the printer"""

        EX2_DEF_NO_LAMINATE = 0x00008000
        """No laminate film installed"""

        EX2_DEF_LAMI_COVER_OPEN = 0x00004000
        """Lamination module cover is open"""

        EX2_DEF_LAMINATE_END = 0x00002000
        """Laminate film reached its end"""

        EX2_DEF_LAMI_HOPPER_FULL = 0x00001000
        """Lamination module hopper is full"""

        EX2_DEF_LAMINATE_UNSUPPORTED = 0x00000800
        """Installed laminate film is not supported"""

        EX2_INF_CLEAR_UNKNOWN = 0x00000400
        """Installed clear ribbon is unknown"""

        EX2_INF_CLEAR_LOW = 0x00000200
        """Remaining clear ribbon is below the low limit"""

        EX2_INF_WRONG_ZONE_CLEAR = 0x00000100
        """Installed clear ribbon has not the right zone"""

        EX2_ERR_LAMI_TEMPERATURE = 0x00000080
        """Job interrupted because the laminator temperature was too high"""

        EX2_ERR_LAMINATE = 0x00000040
        """Error on the laminate film"""

        EX2_ERR_LAMI_MECHANICAL = 0x00000020
        """Mechanical error on the lamination module (card jam, ribbon jam, ...)"""

        EX2_ERR_LAMINATE_END = 0x00000010
        """Job interrupted because the laminate film is finished"""

        EX2_ERR_LAMI_COVER_OPEN = 0x00000008
        """Job interrupted by an open lamination module cover"""

        EX2_INF_CLEAR_CHANGED = 0x00000004
        """Installed clear ribbon is different from the previous one"""

        EX2_INF_WRONG_ZONE_CLEAR_ALERT = 0x00000002
        """Installed clear ribbon has wrong zone: only a few prints remaining before printing is blocked"""

        EX2_INF_WRONG_ZONE_CLEAR_EXPIRED = 0x00000001
        """Installed clear ribbon has wrong zone: printing not allowed"""


    class Ex3Flag(IntFlag):
        EX3_CFG_EXTENSION_4 = 0x80000000
        """Extension 4 is used"""

        EX3_INF_RETRANSFER_RUNNING = 0x40000000
        """Retransfer sequence is running"""

        EX3_INF_HEATING = 0x20000000
        """Printer is heating up"""

        EX3_INF_CARD_MAN_FEED = 0x08000000
        """Card present in the manual feeding module"""

        EX3_INF_HEAT_ROLLER_WORN_OUT = 0x04000000
        """Heat roller reached its maximum recommended of retransfers"""

        EX3_INF_PRE_HEATING_PRINT_HEAD = 0x02000000
        """Print head pre heating in progress"""

        EX3_ERR_PRE_HEATING_PRINT_HEAD = 0x01000000
        """Print head pre heating : target not reach under the timeout on the last cycle"""


    def __init__(self, c_status: _CStatus):
        self.config = int(c_status.config)
        self.information = int(c_status.information)
        self.warning = int(c_status.warning)
        self.error = int(c_status.error)
        self.exts = [
            int(c_status.exts[0]),
            int(c_status.exts[1]),
            int(c_status.exts[2]),
            int(c_status.exts[3]),
        ]
        self.session = int(c_status.session)

    def is_on(self, flag) -> bool:
        if type(flag) == Status.CfgFlag:
            return bool(self.config & flag)
        if type(flag) == Status.InfFlag:
            return bool(self.information & flag)
        if type(flag) == Status.WarFlag:
            return bool(self.warning & flag)
        if type(flag) == Status.ErrFlag:
            return bool(self.error & flag)
        if type(flag) == Status.Ex1Flag:
            return bool(self.exts[0] & flag)
        if type(flag) == Status.Ex2Flag:
            return bool(self.exts[1] & flag)
        if type(flag) == Status.Ex3Flag:
            return bool(self.exts[2] & flag)
        return False

    def is_session_free(self):
        return self.session == 0

    def is_session_busy(self):
        return not self.is_session_free()

    def active_flags(self) -> list:
        l = []

        for flags in [Status.CfgFlag, Status.InfFlag, Status.WarFlag, Status.ErrFlag, Status.Ex1Flag, Status.Ex2Flag]:
            for e in flags:
                if self.is_on(e):
                    l.append(e)
        return l
