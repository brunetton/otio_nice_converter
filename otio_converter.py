#!/bin/env python
# -*- coding: utf-8 -*-

"""
OTIO converter that tries to be nice with user.

Usage:
    {self_filename} <input_file> [options]
"""

import opentimelineio as otio
from pathlib import Path
from docopt import docopt


args = docopt(__doc__.format(self_filename=Path(__file__).name))

input_file = Path(args["<input_file>"])

# read input file
timeline = otio.adapters.read_from_file(input_file)

# write OTIO file
output_file = input_file.parent / Path(input_file.stem + ".otio")
print(f"Writing {output_file}...")
otio.adapters.write_to_file(timeline, output_file)
