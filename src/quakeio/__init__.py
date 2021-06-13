# Claudio Perez
__version__ = "0.0.0"

import json
from pathlib import Path

from .core import GroundMotionEvent, GroundMotionRecord, GroundMotionSeries
from . import csmip, nga, basic_formats


FILE_TYPES = {}
FILE_TYPES.update(csmip.FILE_TYPES)
FILE_TYPES.update(basic_formats.FILE_TYPES)

DEFAULT_TYPES = {
    ".zip": "csmip.zip",
    ".v2": "csmip.v2",
    ".json": "json.record",
}


def read(read_file, *args, **kwds):
    """
    Generic ground motion reader
    """
    if "input_format" in kwds and kwds["input_format"]:
        typ = kwds["input_format"]
    else:
        try:
            typ = DEFAULT_TYPES[Path(read_file).suffix]
        except KeyError:
            raise ValueError("Unable to deduce input format")
    return FILE_TYPES[typ]["read"](read_file, *args, **kwds)


def write(write_file, ground_motion, write_format=None, *args, **kwds):
    if write_format:
        typ = write_format
    else:
        try:
            typ = DEFAULT_TYPES[Path(write_file).suffix]
        except KeyError:
            raise ValueError("Unable to deduce output format")
    #with open_quake(write_file,"w") as f:
    FILE_TYPES[typ]["write"](write_file, ground_motion, *args, **kwds)
