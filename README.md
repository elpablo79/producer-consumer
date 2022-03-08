# A simple Producer/Consumer web link extractor

This Python project implements a basic web link extractor using the Producer/Consumer approach.
An input file with a list of URLs to be retrieved is processed and a list of URLs found on each page is returned.

## Requirements

The libraries that need to be installed are specified in the file requirements.txt.

## How to use

1. A file called input inside the data folder contains a single URL per line

2. Run the file main.py

3. The output file is written inside the data folder

The output is in CSV format, containing the provided URLs from the input file with the extracted URLs following it.
If there are errors while retrieving any URL or parsing its content, those URLs are not considered.
In case there are no URLs following the supplied URL, it means that no links are retrieved from that page.