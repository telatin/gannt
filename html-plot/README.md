# Google Gannt Chart

### Input

The script takes the Excel sheet with this structure:

wp | activity | start | end | site | depends
---|----------|-------|-----|------|----------
Task|Subtask1 | 1     | 8   | A    | NA

and generates the HTML version, coloring each bar
according to the "site" column.

:bulb: start and end are month number, where 1 is the first
month of the project (see `--start-date`).

### Output

[Example](gannt.html)

### Usage

usage: gannter.py [-h] -i INPUT [-o OUTPUT] [-s START_DATE] [--deps]

Read an excel file and produces an HTML gannt chart

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file
  -o OUTPUT, --output OUTPUT
                        Output file
  -s START_DATE, --start-date START_DATE
                        project start date
  --deps                Show dependencies