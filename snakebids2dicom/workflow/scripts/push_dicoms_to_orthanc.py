#!/usr/bin/env python

"""Script to recursively push DICOMS to Orthanc."""

import argparse
import os
import os.path
import sys

import requests


def upload_file(path, url, username=None, password=None):
    """Upload a single file to Orthanc through the REST API"""

    with open(path, "rb") as to_upload:
        content = to_upload.read()

    try:
        sys.stdout.write("Importing %s" % path)

        headers = {'content-type': 'application/dicom'}
        auth = None

        if username is not None and password is not None:
            auth = requests.auth.HTTPBasicAuth(username, password)

        resp = requests.post(
            url,
            data=content,
            headers=headers,
            auth=auth
        )

        if resp.status_code == 200:
            sys.stdout.write(" => success\n")
            return True
        sys.stdout.write(
            " => failure (Is it a DICOM file? Is there a password?)\n"
        )
        return False
    except requests.ConnectionError:
        _, value, _ = sys.exc_info()
        sys.stderr.write(str(value))
        sys.stdout.write(
            " => unable to connect. "
            "Is Orthanc running? Is there a password?\n"
        )
        return False


def main():
    """Parse arguments and push all files to Orthanc."""
    parser = argparse.ArgumentParser(
        description="Sample script to recursively push DICOMs to Orthanc."
    )
    parser.add_argument("hostname")
    parser.add_argument("port")
    parser.add_argument("path", help="Path to input DICOM file or dir.")
    parser.add_argument("username", nargs="?")
    parser.add_argument("password", nargs="?")

    args = parser.parse_args()

    upload_path(
        args.hostname,
        args.port,
        args.path,
        args.username,
        args.password
    )


def upload_path(hostname, port, path, username, password):
    """Upload all files at a given path."""
    url = f"http://{hostname}:{port}/instances"

    success_count = 0
    total_file_count = 0

    if os.path.isfile(path):
        total_file_count += 1
        # Upload a single file
        if upload_file(path, url, username, password):
            success_count += 1
    else:
        # Recursively upload a directory
        for root, _, files in os.walk(path):
            for dicom in files:
                total_file_count += 1
                if upload_file(
                    os.path.join(root, dicom),
                    url,
                    username,
                    password
                ):
                    success_count += 1

    if success_count == total_file_count:
        print(f"All {success_count} DICOM file(s) imported.")
    else:
        print(f"{success_count} of {total_file_count} files imported.")


if snakemake:
    upload_path(
        snakemake.config["orthancurl"],
        80,
        snakemake.input[0],
        snakemake.config["orthancusername"],
        snakemake.config["orthancpassword"]
    )
elif __name__ == "__main__":
    main()
