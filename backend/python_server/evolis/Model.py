# Evolis SDK for Python
#
# THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
# ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
# PARTICULAR PURPOSE.

from enum import Enum

class Model(Enum):
    """
    References the model of the printer.
    """

    def from_int(v:int):
        try:
            return Model(v)
        except ValueError:
            return Model.INVALID

    INVALID = 0
    Evolis_KC100 = 1
    Evolis_KC100B = 2
    Evolis_KC200 = 3
    Evolis_KC200B = 4
    Evolis_KM500B = 5
    Evolis_KM2000B = 6
    Evolis_Primacy = 7
    Evolis_Altess = 8
    Evolis_Altess_Elite = 9
    BadgePass_NXT5000 = 10
    ID_Maker_Primacy = 11
    Evolis_Elypso = 12
    ID_Maker_Elypso = 13
    Evolis_Zenius = 14
    ID_Maker_Zenius = 15
    Evolis_Apteo = 16
    Durable_Duracard_ID_300 = 17
    Edikio_Access = 18
    Edikio_Flex = 19
    Edikio_Duplex = 20
    Evolis_Badgy100 = 21
    Evolis_Badgy200 = 22
    Evolis_Lamination_Module = 23
    Evolis_KC_Essential = 24
    Evolis_KC_Prime = 25
    Evolis_KC_Max = 26
    Evolis_Primacy_2 = 27
    Evolis_Asmi = 28
    BadgePass_NXTElite = 29
    ID_Maker_Primacy_Infinity = 30
    Plasco_Primacy_2_LE = 31
    Identisys_Primacy_2_SE = 32
    Evolis_Avansia = 33
    Evolis_Agilia = 34
