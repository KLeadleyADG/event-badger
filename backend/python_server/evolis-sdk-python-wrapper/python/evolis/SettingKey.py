# Evolis SDK for Python
#
# THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
# ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
# PARTICULAR PURPOSE.

from enum import Enum

class SettingKey(Enum):

    @staticmethod
    def from_int(v: int):
        try:
            return SettingKey(v)
        except ValueError:
            return SettingKey.Unknown

    Unknown = 0

    BBlackManagement = 1
    """
    BBlackManagement
    Usable in PrintSessions: true
    Type: LIST
    Possible values: NOBLACKPOINT, ALLBLACKPOINT, TEXTINBLACK, BMPBLACK
    """

    BColorBrightness = 2
    """
    BColorBrightness
    Usable in PrintSessions: true
    Type: INT
    Range: 1-20
    """

    BColorContrast = 3
    """
    BColorContrast
    Usable in PrintSessions: true
    Type: INT
    Range: 1-20
    """

    BDualDeposite = 4
    """
    BDualDeposite
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    BHalftoning = 5
    """
    BHalftoning
    Usable in PrintSessions: true
    Type: LIST
    Possible values: THRESHOLD, FLOYD, DITHERING, CLUSTERED_DITHERING
    """

    BMonochromeContrast = 6
    """
    BMonochromeContrast
    Usable in PrintSessions: true
    Type: INT
    Range: 1-20
    """

    BOverlayContrast = 7
    """
    BOverlayContrast
    Usable in PrintSessions: true
    Type: INT
    Range: 1-20
    """

    BOverlayManagement = 8
    """
    BOverlayManagement
    Usable in PrintSessions: true
    Type: LIST
    Possible values: NOVARNISH, FULLVARNISH, BMPVARNISH, UVVARNISH
    """

    BOverlaySecondManagement = 9
    """
    BOverlaySecondManagement
    Usable in PrintSessions: true
    Type: LIST
    Possible values: NOVARNISH, FULLVARNISH, BMPVARNISH, UVVARNISH
    """

    UIBOverlayManagement = 10
    """
    UIBOverlayManagement
    Usable in PrintSessions: false
    Type: LIST
    Possible values: NOVARNISH, FULLVARNISH, BMPVARNISH, UVVARNISH
    """

    BPageRotate180 = 11
    """
    BPageRotate180
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    BRwErasingSpeed = 12
    """
    BRwErasingSpeed
    Usable in PrintSessions: true
    Type: INT
    Range: 1-10
    """

    BRwErasingTemperature = 13
    """
    BRwErasingTemperature
    Usable in PrintSessions: true
    Type: INT
    Range: 1-20
    """

    BRwManagement = 14
    """
    BRwManagement
    Usable in PrintSessions: true
    Type: LIST
    Possible values: WRITEONLY, FULLREWRITE, BMPREWRITE
    """

    BRwPrintingSpeed = 15
    """
    BRwPrintingSpeed
    Usable in PrintSessions: true
    Type: INT
    Range: 1-10
    """

    BRwPrintingTemperature = 16
    """
    BRwPrintingTemperature
    Usable in PrintSessions: true
    Type: INT
    Range: 1-20
    """

    BUvBrightness = 17
    """
    BUvBrightness
    Usable in PrintSessions: true
    Type: INT
    Range: 1-20
    """

    BUvContrast = 18
    """
    BUvContrast
    Usable in PrintSessions: true
    Type: INT
    Range: 1-20
    """

    BUvManagement = 19
    """
    BUvManagement
    Usable in PrintSessions: true
    Type: LIST
    Possible values: NOUV, BMPUV
    """

    BUvPremium = 20
    """
    BUvPremium
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    Duplex = 21
    """
    Duplex
    Usable in PrintSessions: true
    Type: LIST
    Possible values: NONE, HORIZONTAL
    """

    FBlackManagement = 22
    """
    FBlackManagement
    Usable in PrintSessions: true
    Type: LIST
    Possible values: NOBLACKPOINT, ALLBLACKPOINT, TEXTINBLACK, BMPBLACK
    """

    FColorBrightness = 23
    """
    FColorBrightness
    Usable in PrintSessions: true
    Type: INT
    Range: 1-20
    """

    FColorContrast = 24
    """
    FColorContrast
    Usable in PrintSessions: true
    Type: INT
    Range: 1-20
    """

    FDualDeposite = 25
    """
    FDualDeposite
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    FHalftoning = 26
    """
    FHalftoning
    Usable in PrintSessions: true
    Type: LIST
    Possible values: THRESHOLD, FLOYD, DITHERING, CLUSTERED_DITHERING
    """

    FMonochromeContrast = 27
    """
    FMonochromeContrast
    Usable in PrintSessions: true
    Type: INT
    Range: 1-20
    """

    FOverlayContrast = 28
    """
    FOverlayContrast
    Usable in PrintSessions: true
    Type: INT
    Range: 1-20
    """

    FOverlayManagement = 29
    """
    FOverlayManagement
    Usable in PrintSessions: true
    Type: LIST
    Possible values: NOVARNISH, FULLVARNISH, BMPVARNISH, UVVARNISH
    """

    FOverlaySecondManagement = 30
    """
    FOverlaySecondManagement
    Usable in PrintSessions: true
    Type: LIST
    Possible values: NOVARNISH, FULLVARNISH, BMPVARNISH, UVVARNISH
    """

    UIFOverlayManagement = 31
    """
    UIFOverlayManagement
    Usable in PrintSessions: false
    Type: LIST
    Possible values: NOVARNISH, FULLVARNISH, BMPVARNISH, UVVARNISH
    """

    FPageRotate180 = 32
    """
    FPageRotate180
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    FRwErasingSpeed = 33
    """
    FRwErasingSpeed
    Usable in PrintSessions: true
    Type: INT
    Range: 1-10
    """

    FRwErasingTemperature = 34
    """
    FRwErasingTemperature
    Usable in PrintSessions: true
    Type: INT
    Range: 1-20
    """

    FRwManagement = 35
    """
    FRwManagement
    Usable in PrintSessions: true
    Type: LIST
    Possible values: WRITEONLY, FULLREWRITE, BMPREWRITE
    """

    FRwPrintingSpeed = 36
    """
    FRwPrintingSpeed
    Usable in PrintSessions: true
    Type: INT
    Range: 1-10
    """

    FRwPrintingTemperature = 37
    """
    FRwPrintingTemperature
    Usable in PrintSessions: true
    Type: INT
    Range: 1-20
    """

    FUvBrightness = 38
    """
    FUvBrightness
    Usable in PrintSessions: true
    Type: INT
    Range: 1-20
    """

    FUvContrast = 39
    """
    FUvContrast
    Usable in PrintSessions: true
    Type: INT
    Range: 1-20
    """

    FUvManagement = 40
    """
    FUvManagement
    Usable in PrintSessions: true
    Type: LIST
    Possible values: NOUV, BMPUV
    """

    FUvPremium = 41
    """
    FUvPremium
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    GCardPreloading = 42
    """
    GCardPreloading
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    GDigitalScrambling = 43
    """
    GDigitalScrambling
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    GDuplexType = 44
    """
    GDuplexType
    Usable in PrintSessions: true
    Type: LIST
    Possible values: DUPLEX_CC, DUPLEX_CM, DUPLEX_MC, DUPLEX_MM
    """

    GFeederCfg = 45
    """
    GFeederCfg
    Usable in PrintSessions: true
    Type: LIST
    Possible values: PRINTER, AUTO, FEEDERA, FEEDERB, FEEDERC, FEEDERD, ALTERNATE, FEEDER1, FEEDER2, FEEDER3, FEEDER4, NONE
    """

    GFeederPos = 46
    """
    GFeederPos
    Usable in PrintSessions: true
    Type: LIST
    Possible values: PRINTER, FEEDERA, FEEDERB, FEEDERC, FEEDERD, MIDDLE, OFF
    """

    GHighQualityMode = 47
    """
    GHighQualityMode
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    GInputTray = 48
    """
    GInputTray
    Usable in PrintSessions: true
    Type: LIST
    Possible values: PRINTER, FEEDER, AUTO, MANUAL, HOPPER, BEZEL
    """

    GMagCoercivity = 49
    """
    GMagCoercivity
    Usable in PrintSessions: true
    Type: LIST
    Possible values: OFF, LOCO, HICO
    """

    GMagT1Encoding = 50
    """
    GMagT1Encoding
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ISO1, ISO2, ISO3, SIPASS, C2, JIS2, C4, NONE
    """

    GMagT2Encoding = 51
    """
    GMagT2Encoding
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ISO1, ISO2, ISO3, SIPASS, C2, JIS2, C4, NONE
    """

    GMagT3Encoding = 52
    """
    GMagT3Encoding
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ISO1, ISO2, ISO3, SIPASS, C2, JIS2, C4, NONE
    """

    GOutputTray = 53
    """
    GOutputTray
    Usable in PrintSessions: true
    Type: LIST
    Possible values: PRINTER, HOPPER, REAR, MANUAL, REJECT, BEZEL
    """

    GPipeDetection = 54
    """
    GPipeDetection
    Usable in PrintSessions: true
    Type: LIST
    Possible values: OFF, DEFAULT, CUSTOM
    """

    GRejectBox = 55
    """
    GRejectBox
    Usable in PrintSessions: true
    Type: LIST
    Possible values: PRINTER, DEFAULTREJECT, HOPPER, MANUAL, REJECT, BEZEL
    """

    GRibbonType = 56
    """
    GRibbonType
    Usable in PrintSessions: true
    Type: LIST
    Possible values: RC_YMCKI, RC_YMCKKI, RC_YMCFK, RC_YMCK, RC_YMCKK, RC_YMCKO, RC_YMCKOS, RC_YMCKOS13, RC_YMCKOK, RC_YMCKOKOS, RC_YMCKOO, RM_KO, RM_KBLACK, RM_KWHITE, RM_KRED, RM_KGREEN, RM_KBLUE, RM_KSCRATCH, RM_KMETALSILVER, RM_KMETALGOLD, RM_KSIGNATURE, RM_KWAX, RM_KPREMIUM, RM_HOLO, RM_SOKO, RC_YMCK_A, RC_YMCKK_A, RC_YMCKI_A, RC_YMCKH_A, RC_YMCFK_A, RC_YMCKSI_A
    """

    GRwCard = 57
    """
    GRwCard
    Usable in PrintSessions: true
    Type: LIST
    Possible values: MBLACK, MBLUE, CUSTOM_FRONT, CUSTOM_DUPLEX
    """

    GPrintingMode = 58
    """
    GPrintingMode
    Usable in PrintSessions: true
    Type: LIST
    Possible values: D2T2, RW_2IN1
    """

    GShortPanelManagement = 59
    """
    GShortPanelManagement
    Usable in PrintSessions: true
    Type: LIST
    Possible values: AUTO, CUSTOM, OFF
    """

    GSmoothing = 60
    """
    GSmoothing
    Usable in PrintSessions: true
    Type: LIST
    Possible values: STDSMOOTH, ADVSMOOTH, NOSMOOTH
    """

    IBBlackCustom = 61
    """
    IBBlackCustom
    Usable in PrintSessions: true
    Type: TEXT
    """

    IBBlackLevelValue = 62
    """
    IBBlackLevelValue
    Usable in PrintSessions: true
    Type: INT
    Range: 1-255
    """

    IBDarkLevelValue = 63
    """
    IBDarkLevelValue
    Usable in PrintSessions: true
    Type: INT
    Range: 0-255
    """

    IBNoTransferAreas = 64
    """
    IBNoTransferAreas
    Usable in PrintSessions: true
    Type: TEXT
    """

    IBOverlayCustom = 65
    """
    IBOverlayCustom
    Usable in PrintSessions: true
    Type: TEXT
    """

    IBOverlayDefaultContent = 66
    """
    IBOverlayDefaultContent
    Usable in PrintSessions: false
    Type: BLOB
    """

    IBOverlaySecondCustom = 67
    """
    IBOverlaySecondCustom
    Usable in PrintSessions: true
    Type: TEXT
    """

    IBOverlaySecondDefaultContent = 68
    """
    IBOverlaySecondDefaultContent
    Usable in PrintSessions: false
    Type: BLOB
    """

    IBRwCustom = 69
    """
    IBRwCustom
    Usable in PrintSessions: true
    Type: TEXT
    """

    IBRwCustomBitmap = 70
    """
    IBRwCustomBitmap
    Usable in PrintSessions: false
    Type: BLOB
    """

    IBTextRegion = 71
    """
    IBTextRegion
    Usable in PrintSessions: true
    Type: TEXT
    """

    IBThresholdValue = 72
    """
    IBThresholdValue
    Usable in PrintSessions: true
    Type: INT
    Range: 1-255
    """

    IBUvContent = 73
    """
    IBUvContent
    Usable in PrintSessions: false
    Type: BLOB
    """

    IBUvCustom = 74
    """
    IBUvCustom
    Usable in PrintSessions: true
    Type: TEXT
    """

    IFBlackCustom = 75
    """
    IFBlackCustom
    Usable in PrintSessions: true
    Type: TEXT
    """

    IFBlackLevelValue = 76
    """
    IFBlackLevelValue
    Usable in PrintSessions: true
    Type: INT
    Range: 1-255
    """

    IFDarkLevelValue = 77
    """
    IFDarkLevelValue
    Usable in PrintSessions: true
    Type: INT
    Range: 0-255
    """

    IFNoTransferAreas = 78
    """
    IFNoTransferAreas
    Usable in PrintSessions: true
    Type: TEXT
    """

    IFOverlayCustom = 79
    """
    IFOverlayCustom
    Usable in PrintSessions: true
    Type: TEXT
    """

    IFOverlayDefaultContent = 80
    """
    IFOverlayDefaultContent
    Usable in PrintSessions: false
    Type: BLOB
    """

    IFOverlaySecondCustom = 81
    """
    IFOverlaySecondCustom
    Usable in PrintSessions: true
    Type: TEXT
    """

    IFOverlaySecondDefaultContent = 82
    """
    IFOverlaySecondDefaultContent
    Usable in PrintSessions: false
    Type: BLOB
    """

    IFRwCustom = 83
    """
    IFRwCustom
    Usable in PrintSessions: true
    Type: TEXT
    """

    IFRwCustomBitmap = 84
    """
    IFRwCustomBitmap
    Usable in PrintSessions: false
    Type: BLOB
    """

    IFTextRegion = 85
    """
    IFTextRegion
    Usable in PrintSessions: true
    Type: TEXT
    """

    IFUvContent = 86
    """
    IFUvContent
    Usable in PrintSessions: false
    Type: BLOB
    """

    IFUvCustom = 87
    """
    IFUvCustom
    Usable in PrintSessions: true
    Type: TEXT
    """

    IFThresholdValue = 88
    """
    IFThresholdValue
    Usable in PrintSessions: true
    Type: INT
    Range: 1-255
    """

    IGBlackSub = 89
    """
    IGBlackSub
    Usable in PrintSessions: true
    Type: TEXT
    """

    IGDuplexPreset = 90
    """
    IGDuplexPreset
    Usable in PrintSessions: false
    Type: INT
    Range: 0-99
    """

    IGIQLABC = 91
    """
    IGIQLABC
    Usable in PrintSessions: true
    Type: INT
    Range: 0-20
    """

    IGIQLABM = 92
    """
    IGIQLABM
    Usable in PrintSessions: true
    Type: INT
    Range: 0-20
    """

    IGIQLABY = 93
    """
    IGIQLABY
    Usable in PrintSessions: true
    Type: INT
    Range: 0-20
    """

    IGIQLACC = 94
    """
    IGIQLACC
    Usable in PrintSessions: true
    Type: INT
    Range: 0-20
    """

    IGIQLACM = 95
    """
    IGIQLACM
    Usable in PrintSessions: true
    Type: INT
    Range: 0-20
    """

    IGIQLACY = 96
    """
    IGIQLACY
    Usable in PrintSessions: true
    Type: INT
    Range: 0-20
    """

    IGMonoReaderType = 97
    """
    IGMonoReaderType
    Usable in PrintSessions: false
    Type: LIST
    Possible values: REG, FILE
    """

    IGMonochromeSpeed = 98
    """
    IGMonochromeSpeed
    Usable in PrintSessions: true
    Type: INT
    Range: 1-10
    """

    IGRibbonOptimization = 99
    """
    IGRibbonOptimization
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    IGSendIQLA = 100
    """
    IGSendIQLA
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    IGSendSpoolerSession = 101
    """
    IGSendSpoolerSession
    Usable in PrintSessions: false
    Type: LIST
    Possible values: ON, OFF
    """

    IGDisableAutoEject = 102
    """
    IGDisableAutoEject
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    IGStrictPageSetup = 103
    """
    IGStrictPageSetup
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    IGTextRectErr = 104
    """
    IGTextRectErr
    Usable in PrintSessions: true
    Type: INT
    Range: 0-20
    """

    IOverlayCustomContentAfnor = 105
    """
    IOverlayCustomContentAfnor
    Usable in PrintSessions: false
    Type: BLOB
    """

    IOverlayCustomContentIso = 106
    """
    IOverlayCustomContentIso
    Usable in PrintSessions: false
    Type: BLOB
    """

    IOverlayCustomContentMag = 107
    """
    IOverlayCustomContentMag
    Usable in PrintSessions: false
    Type: BLOB
    """

    IPipeDefinition = 108
    """
    IPipeDefinition
    Usable in PrintSessions: false
    Type: TEXT
    """

    IPostSmoothing = 109
    """
    IPostSmoothing
    Usable in PrintSessions: false
    Type: LIST
    Possible values: STDSMOOTH, ADVSMOOTH, NOSMOOTH
    """

    ISendBlankPanel = 110
    """
    ISendBlankPanel
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    IShortPanelShift = 111
    """
    IShortPanelShift
    Usable in PrintSessions: true
    Type: INT
    Range: 0-9999
    """

    Orientation = 112
    """
    Orientation
    Usable in PrintSessions: true
    Type: LIST
    Possible values: LANDSCAPE_CC90, PORTRAIT
    """

    RawData = 113
    """
    RawData
    Usable in PrintSessions: false
    Type: TEXT
    """

    Resolution = 114
    """
    Resolution
    Usable in PrintSessions: true
    Type: LIST
    Possible values: DPI300260, DPI300, DPI600300, DPI600, DPI1200300
    """

    Track1Data = 115
    """
    Track1Data
    Usable in PrintSessions: false
    Type: TEXT
    """

    Track2Data = 116
    """
    Track2Data
    Usable in PrintSessions: false
    Type: TEXT
    """

    Track3Data = 117
    """
    Track3Data
    Usable in PrintSessions: false
    Type: TEXT
    """

    PrinterIsManaged = 118
    """
    PrinterIsManaged
    Usable in PrintSessions: false
    Type: INT
    Range: 0-1
    """

    srvAddress = 119
    """
    srvAddress
    Usable in PrintSessions: false
    Type: TEXT
    """

    UIBOverlayDefaultAreasList = 120
    """
    UIBOverlayDefaultAreasList
    Usable in PrintSessions: false
    Type: TEXT
    """

    UIBRwCustomAreasList = 121
    """
    UIBRwCustomAreasList
    Usable in PrintSessions: false
    Type: TEXT
    """

    UIFOverlayDefaultAreasList = 122
    """
    UIFOverlayDefaultAreasList
    Usable in PrintSessions: false
    Type: TEXT
    """

    UIFRwCustomAreasList = 123
    """
    UIFRwCustomAreasList
    Usable in PrintSessions: false
    Type: TEXT
    """

    UIMagTrackSettingMode = 124
    """
    UIMagTrackSettingMode
    Usable in PrintSessions: false
    Type: INT
    Range: 0-1
    """

    UIRibbonMode = 125
    """
    UIRibbonMode
    Usable in PrintSessions: false
    Type: INT
    Range: 0-1
    """

    UpdatedByDrv = 126
    """
    UpdatedByDrv
    Usable in PrintSessions: false
    Type: INT
    Range: 0-1
    """

    UpdatedBySrv = 127
    """
    UpdatedBySrv
    Usable in PrintSessions: false
    Type: INT
    Range: 0-1
    """

    GColorProfileMode = 128
    """
    GColorProfileMode
    Usable in PrintSessions: true
    Type: LIST
    Possible values: NOPROFILE, DRIVERPROFILE, CUSTOM
    """

    GColorProfile = 129
    """
    GColorProfile
    Usable in PrintSessions: true
    Type: LIST
    Possible values: STDPROFILE
    """

    GColorProfileRendering = 130
    """
    GColorProfileRendering
    Usable in PrintSessions: true
    Type: LIST
    Possible values: PERCEPTUAL, SATURATION
    """

    IGColorProfileCustom = 131
    """
    IGColorProfileCustom
    Usable in PrintSessions: true
    Type: TEXT
    """

    IGColorProfileContent = 132
    """
    IGColorProfileContent
    Usable in PrintSessions: false
    Type: BLOB
    """

    UIColorProfileName = 133
    """
    UIColorProfileName
    Usable in PrintSessions: false
    Type: TEXT
    """

    WIScanImageDepth = 134
    """
    WIScanImageDepth
    Usable in PrintSessions: false
    Type: LIST
    Possible values: BPP8, BPP16, BPP24, BPP32
    """

    WIScanImageResolution = 135
    """
    WIScanImageResolution
    Usable in PrintSessions: false
    Type: LIST
    Possible values: DPI300, DPI600
    """

    WIScanImageFileFormat = 136
    """
    WIScanImageFileFormat
    Usable in PrintSessions: false
    Type: LIST
    Possible values: JPG, BMP, PNG
    """

    WIScanSpeed = 137
    """
    WIScanSpeed
    Usable in PrintSessions: false
    Type: INT
    Range: 0-40
    """

    WIScanOffset = 138
    """
    WIScanOffset
    Usable in PrintSessions: false
    Type: INT
    Range: 0-40
    """

    WIScanCardSides = 139
    """
    WIScanCardSides
    Usable in PrintSessions: false
    Type: LIST
    Possible values: FRONT_BACK, FRONT_ONLY, BACK_ONLY
    """

    passthrough = 140
    """
    passthrough
    Usable in PrintSessions: false
    Type: TEXT
    """

    PaperSize = 141
    """
    PaperSize
    Usable in PrintSessions: true
    Type: LIST
    Possible values: CR80, ISOCR80, CR120X50, CR150X50, AVANSIACR80
    """

    FGamma = 142
    """
    FGamma
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    FGammaFactor = 143
    """
    FGammaFactor
    Usable in PrintSessions: true
    Type: INT
    Range: 0-100
    """

    BGamma = 144
    """
    BGamma
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    BGammaFactor = 145
    """
    BGammaFactor
    Usable in PrintSessions: true
    Type: INT
    Range: 0-100
    """

    FBlackPrinting = 146
    """
    FBlackPrinting
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    BBlackPrinting = 147
    """
    BBlackPrinting
    Usable in PrintSessions: true
    Type: LIST
    Possible values: ON, OFF
    """

    FSilverManagement = 148
    """
    FSilverManagement
    Usable in PrintSessions: true
    Type: LIST
    Possible values: NOSILVER
    """

    IFSilverCustom = 149
    """
    IFSilverCustom
    Usable in PrintSessions: true
    Type: TEXT
    """

    BSilverManagement = 150
    """
    BSilverManagement
    Usable in PrintSessions: true
    Type: LIST
    Possible values: NOSILVER
    """

    IBSilverCustom = 151
    """
    IBSilverCustom
    Usable in PrintSessions: true
    Type: TEXT
    """

