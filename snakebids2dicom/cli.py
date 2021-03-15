#!/usr/bin/env python3

"""Console script for snakebids2dicom."""

import os
import sys
from snakebids.app import SnakeBidsApp
import boutiques.creator as bc


def get_parser():
    """Exposes parser for sphinx doc generation, cwd is the docs dir"""
    app = SnakeBidsApp('../snakebids2dicom', skip_parse_args=True)
    return app.parser


def gen_boutiques(out_path="boutiques_descriptor.json"):
    """Generates boutiques descriptor for Snakebids-specific CLI."""
    new_descriptor = bc.CreateDescriptor(
        get_parser(),
        execname="snakebids2dicom"
    )
    new_descriptor.save(out_path)


def main():
    """Console script for snakebids2dicom."""
    app = SnakeBidsApp(os.path.abspath(os.path.dirname(__file__)))
    app.run_snakemake()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
