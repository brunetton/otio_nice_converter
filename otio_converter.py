#!/bin/env python
# -*- coding: utf-8 -*-

"""
OTIO converter that tries to be nice with user.

Usage:
    {self_filename} <input_file> [options]
    {self_filename} --list_adapters

Options:
    --list_adapters                 List installed adapters and exit
"""

import opentimelineio as otio
from pathlib import Path
from docopt import docopt
import opentimelineio.exceptions


args = docopt(__doc__.format(self_filename=Path(__file__).name))

if args["--list_adapters"]:
    print(f"Installed OTIO adpaters: {otio.adapters.available_adapter_names()}")
    exit(0)

input_file = Path(args["<input_file>"])

try:
    # read input file
    timeline = otio.adapters.read_from_file(input_file)
except opentimelineio.exceptions.NoKnownAdapterForExtensionError as e:
    print(
        f"{e}\nYou can try to install a missing adapter (pip install otio-XXXX-adapter)"
    )
    print(f"Currently installed adapters: {otio.adapters.available_adapter_names()}")
    # EDL: pip install otio-cmx3600-adapter
    # XML: pip install otio-fcpx-xml-adapter

# write OTIO file
output_file = input_file.parent / Path(input_file.stem + ".otio")
print(f"Writing {output_file}...")
otio.adapters.write_to_file(timeline, output_file)
