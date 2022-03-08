# A simple Producer/Consumer web link extractor

This Python project implements a basic web link extractor using the Producer/Consumer approach.
An input file with a list of URLs to be retrieved is processed and a list of URLs found on each page is returned.

## Requirements

The libraries that need to be installed are specified in the file requirements.txt.

## How to use
Clone (or download and unzip) the repository and move inside the producer-consumer folder.

Create a new Python virtual environment:
```
python3 -m venv env
```
Activate the virtual environment and install the dependencies:
```
source env/bin/activate
pip install -r requirements.txt
```
There is a file called input inside the data folder that contains a single URL per line: feel free to modify it with the URLs you want to use.

Run the main file:
```
python3 main.py
```
The output file will be written inside the data folder.

The output is in CSV format, containing the provided URLs from the input file with the extracted URLs following it.
If there are errors while retrieving any URL or parsing its content, those URLs are not considered.
In case there are no URLs following the supplied URL, it means that no links are retrieved from that page.