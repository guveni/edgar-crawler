#!/usr/bin/env python
import os
import gzip
import argparse


def compress_files(input_path, output_path):
    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Iterate over each file in the input directory
    for filename in os.listdir(input_path):
        if filename.endswith(".json"):
            # Compress the file
            with open(os.path.join(input_path, filename), "rb") as file_in:
                with gzip.open(
                    os.path.join(output_path, f"{filename}.gz"), "wb"
                ) as file_out:
                    file_out.writelines(file_in)

    print("Files compressed and saved successfully!")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Compress files in a directory.")
    parser.add_argument("--input_path", default="/Users/guven/Documents/investment_research/code/edgar-crawler/data/extracted_filings", help="Path to the input directory")
    parser.add_argument("--output_path", default="/Users/guven/Documents/investment_research/code/edgar-crawler/data/extracted_zipped_filings", help="Path to the output directory")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    input_path = args.input_path
    output_path = args.output_path

    compress_files(input_path, output_path)
