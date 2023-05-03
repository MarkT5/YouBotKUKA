from collections import deque
from mjpeg import read_mjpeg_frame, open_mjpeg_stream, read_header_line
import urllib.request
import urllib.error
from mjpeg.client import Buffer
import mjpeg

deb = True


def debug(inf, /, end="\n"):
    """
    Prints info if variable deb is True
    :param inf: info to print
    """
    if deb:
        print(inf, end=end)


def range_cut(mi, ma, val):
    """
    Cuts value from min to max
    :param mi: minimum value
    :param ma: maximum value
    :param val: value
    :return: cut value
    """
    return min(ma, max(mi, val))


def test_MJPEG_client(url):
    _incoming = deque()
    rv = []
    for i in range(0, 5):
        rv.append(Buffer(65536))
    for buf in rv:
        _incoming.append(buf)
    try:
        with urllib.request.urlopen(url,timeout=4) as s:
            boundary = open_mjpeg_stream(s)
            for i in range(10):
                try:
                    buf = _incoming.pop()
                    mem = buf.data
                    length = buf.length
                except IndexError:
                    buf = None
                    mem = None
                    length = 0
                try:
                    read_mjpeg_frame(s, boundary, mem, length)
                except mjpeg.ProtoError:
                    return False
                except TimeoutError:
                    return False
    except urllib.error.URLError:
        return False
    return True
