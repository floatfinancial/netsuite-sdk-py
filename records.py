from enum import Enum


class FileEncoding(Enum):
    """
    https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2019_1/schema/enum/fileencoding.html?mode=package
    """
    AUTO_DETECT = "_autoDetect"
    SHIFT = "_shiftJis"
    UTF8 = "_utf8"
    WINDOWS = "_windows1252"


class MediaType(Enum):
    """
    This is a subset of options from:
    https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2019_1/schema/enum/mediatype.html?mode=package
    """
    JPG = "_JPGIMAGE"
    PDF = "_PDF"
    PNG = "_PNGIMAGE"


class TextFileEncoding(Enum):
    """
    This is a subset of options from:
    https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2019_1/schema/enum/textfileencoding.html?mode=package
    """
    UTF8 = "_utf8"
