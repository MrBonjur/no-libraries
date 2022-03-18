########################################################################
#                  Create screenshot without libraries                 #
#                      18.03.2022 create MrBonjur                      #
#                To create a screenshot, call the method:              #
#                         ScreenShot().save(path)                      #
#                The path is the full path with the name               #
#                                   or                                 #
#                       just the name of the file                      #
########################################################################

from ctypes.wintypes import LONG, DWORD, WORD
from ctypes import Structure
import ctypes
import struct
import zlib
import sys
import os


class bitmapinfoheader(Structure):
    _fields_ = [
        ("biSize", DWORD),
        ("biWidth", LONG),
        ("biHeight", LONG),
        ("biPlanes", WORD),
        ("biBitCount", WORD),
        ("biCompression", DWORD),
        ("biSizeImage", DWORD),
        ("biXPelsPerMeter", LONG),
        ("biYPelsPerMeter", LONG),
        ("biClrUsed", DWORD),
        ("biClrImportant", DWORD),
    ]


class bitmapinfo(Structure):
    _fields_ = [("bmiHeader", bitmapinfoheader), ("bmiColors", DWORD * 3)]


class windgi:
    CAPTUREBLT = 0x40000000
    DIB_RGB_COLORS = 0
    SRCCOPY = 0x00CC0020


class ScreenShot:
    def __init__(self):
        self.compression_level = None
        self.path = None
        self.bmi = None
        self.width = None
        self.size = None
        self.bmp = None
        self.height = None

        self.user32 = ctypes.WinDLL("user32")
        self.gdi32 = ctypes.WinDLL("gdi32")

        self.buffer = ctypes.create_string_buffer(0)

        self.srcdc = self.user32.GetWindowDC(0)
        self.memdc = self.gdi32.CreateCompatibleDC(self.srcdc)

        self.__set_dpi_awareness()
        
    def get_size_monitor(self):
        get_system_metrics = self.user32.GetSystemMetrics
        monitor = {
            "left": int(get_system_metrics(76)),  # SM_XVIRTUALSCREEN
            "top": int(get_system_metrics(77)),  # SM_YVIRTUALSCREEN
            "width": int(get_system_metrics(78)),  # SM_CXVIRTUALSCREEN
            "height": int(get_system_metrics(79)),  # SM_CYVIRTUALSCREEN
        }
        return monitor
    
    def save(self, path, compression_level=9):  # compression_level = 0-9
        monitor = self.get_size_monitor()
        srcdc, memdc = self.srcdc, self.memdc
        width, height = monitor["width"], monitor["height"]
        src_copy = windgi.SRCCOPY
        capture_blt = windgi.CAPTUREBLT
        dib_rgb_colors = windgi.DIB_RGB_COLORS

        self.size = (width, height)
        self.path = path
        self.compression_level = compression_level

        self.__init_bmi(width, height)

        self.buffer = ctypes.create_string_buffer(width * height * 4)
        self.bmp = self.gdi32.CreateCompatibleBitmap(srcdc, width, height)
        self.gdi32.SelectObject(memdc, self.bmp)

        self.gdi32.BitBlt(memdc, 0, 0, width, height, srcdc, monitor["left"], monitor["top"], src_copy | capture_blt)
        bits = self.gdi32.GetDIBits(memdc, self.bmp, 0, height, self.buffer, self.bmi, dib_rgb_colors)

        if bits != height:
            raise Exception("gdi32.GetDIBits() failed.")

        buffer = bytearray(height * width * 3)
        raw = self.buffer
        buffer[0::3] = raw[2::4]
        buffer[1::3] = raw[1::4]
        buffer[2::3] = raw[0::4]
        self.buffer = bytes(buffer)
        self.__compress()

    def __compress(self):
        if isinstance(self.buffer, bytes):
            buffer = self.buffer
            size = self.size
            level = self.compression_level
            output = self.path

            pack = struct.pack
            crc32 = zlib.crc32
            width, height = size
            line = width * 3
            png_filter = pack(">B", 0)
            scanlines = b"".join([png_filter + buffer[y * line: y * line + line] for y in range(height)])

            magic = pack(">8B", 137, 80, 78, 71, 13, 10, 26, 10)

            # Header: size, marker, data, CRC32
            ihdr = [b"", b"IHDR", b"", b""]
            ihdr[2] = pack(">2I5B", width, height, 8, 2, 0, 0, 0)
            ihdr[3] = pack(">I", crc32(b"".join(ihdr[1:3])) & 0xFFFFFFFF)
            ihdr[0] = pack(">I", len(ihdr[2]))

            # Data: size, marker, data, CRC32
            idat = [b"", b"IDAT", zlib.compress(scanlines, level), b""]
            idat[3] = pack(">I", crc32(b"".join(idat[1:3])) & 0xFFFFFFFF)
            idat[0] = pack(">I", len(idat[2]))

            # Footer: size, marker, None, CRC32
            iend = [b"", b"IEND", b"", b""]
            iend[3] = pack(">I", crc32(iend[1]) & 0xFFFFFFFF)
            iend[0] = pack(">I", len(iend[2]))

            with open(output, "wb") as file:
                file.write(magic)
                file.write(b"".join(ihdr))
                file.write(b"".join(idat))
                file.write(b"".join(iend))
                # Force write of file to disk
                file.flush()
                os.fsync(file.fileno())

    def __init_bmi(self, width, height):
        self.bmi = bitmapinfo()
        self.bmi.bmiHeader.biSize = ctypes.sizeof(bitmapinfoheader)
        self.bmi.bmiHeader.biPlanes = 1
        self.bmi.bmiHeader.biBitCount = 32
        self.bmi.bmiHeader.biCompression = 0
        self.bmi.bmiHeader.biClrUsed = 0
        self.bmi.bmiHeader.biClrImportant = 0

        self.bmi.bmiHeader.biWidth = width
        self.bmi.bmiHeader.biHeight = -height

    
    def __set_dpi_awareness(self):
        version = sys.getwindowsversion()[:2]
        if version >= (6, 3):
            # Windows 8.1+
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        elif (6, 0) <= version < (6, 3):
            # Windows Vista, 7, 8 and Server 2012
            self.user32.SetProcessDPIAware()


ScreenShot().save(path="screen.png", compression_level=0)  # compression_level 0-9
