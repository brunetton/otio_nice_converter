#!/bin/env python
# -*- coding: utf-8 -*-

"""
OTIO converter that tries to be nice with user.

Usage:
    {self_filename} <input_file> [options]
    {self_filename} --list_adapters

Options:
    --list_adapters                 List installed adapters and exit
    --adapter=<adapter_name>        Use given adapter (must be listed in --list_adapters)
"""

import opentimelineio as otio
from pathlib import Path
from docopt import docopt
import opentimelineio.exceptions


args = docopt(__doc__.format(self_filename=Path(__file__).name))


def list_adapters_and_exit():
    print(f"Installed OTIO adpaters: {otio.adapters.available_adapter_names()}")
    exit(0)


if args["--list_adapters"]:
    list_adapters_and_exit()

input_file = Path(args["<input_file>"])
adapter_name = args.get("--adapter")
if adapter_name:
    print(f"Using adapter: {adapter_name}")

try:
    # read input file
    timeline = otio.adapters.read_from_file(input_file, adapter_name=adapter_name)
except opentimelineio.exceptions.NoKnownAdapterForExtensionError as e:
    print(
        f"{e}\nYou can try to use the --adapter option to focrce using a specific adapter, or install a missing adapter (pip install otio-XXXX-adapter)"
    )
    list_adapters_and_exit()
    # EDL: pip install otio-cmx3600-adapter
    # XML: pip install otio-fcpx-xml-adapter

# write OTIO file
output_file = input_file.parent / Path(input_file.stem + ".otio")
print(f"Writing {output_file}...")
otio.adapters.write_to_file(timeline, output_file)
