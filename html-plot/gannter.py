#!/usr/bin/env python3
"""
Read an excel file and produces an HTML gannt chart
"""
import os, sys
import pandas as pd
import argparse
import datetime

def getIndex(df, item, check=None):
    """
    Get the index of the row in the dataframe that 
    has the "activity" names starting with "item "
    """
    items = df.index[df['activity'].str.startswith(item)].tolist()
    if check is not None:
        # Check that the "check" index is not in the list
        if check in items:
            raise Exception("{} is in the list".format(check))
    return items
def getDate(start_date, months):
    """
    Get a starting date and add months to it
    """
    return datetime.datetime.strptime(start_date, '%Y-%m-%d') + datetime.timedelta(days=months*30)
header = """
<html>
<body>
<h1>Gannt chart</h1>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<div id="chart_div"></div>
   
</body>
<script>
    google.charts.load('current', {'packages':['gantt']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Task ID');
      data.addColumn('string', 'Task Name');
      data.addColumn('string', 'Site');
      data.addColumn('date', 'Start Date');
      data.addColumn('date', 'End Date');
      data.addColumn('number', 'Duration');
      data.addColumn('number', 'Something');
      data.addColumn('string', 'Dependencies');

      data.addRows([
"""

footer = """
      ]);

      var options = {
        height: 2200,
        gantt: {
          trackHeight: 40
        }
      };

      var chart = new google.visualization.Gantt(document.getElementById('chart_div'));

      chart.draw(data, options);
    }
</script>

"""
if __name__ == "__main__":
    args = argparse.ArgumentParser(description="Read an excel file and produces an HTML gannt chart")
    args.add_argument("-i", "--input", help="Input file", required=True)
    args.add_argument("-o", "--output", help="Output file", default="gannt.html")
    args.add_argument("-s", "--start-date", help="project start date", default="2023-01-01")
    args.add_argument("--deps", help="Show dependencies", action="store_true")
    args = args.parse_args()

    # read the input file
    df = pd.read_excel(args.input)
    

    #    ['2014Spring', 'Spring 2014', 'UOB', new Date(2014, 2, 22), new Date(2014, 5, 20), null, 100,  null],


    body = ""
   
    # loop over each row in the dataframe
    for index, row in df.iterrows():

        # if the row is the last one
        if index == df.shape[0] - 1:
            end = "\n"
        else:
            end = ",\n"

        start_date = getDate(args.start_date,  row["start_date"])
        end_date = getDate(args.start_date,  row["end_date"])

        # Start date is the project start date + start_month   
        start_y = start_date.year
        start_m = start_date.month
        end_y = end_date.year
        end_m = end_date.month

        deps = "null"
        if str(row["depends"]) != "nan" and args.deps:
            dep_names = str(row["depends"]).split(",")
            dep_names = [getIndex(df, x) for x in dep_names]
            # flatten dep_names to a list of strings
            dep_names = [str(x) for sublist in dep_names for x in sublist]

            deps =  "'" + ",".join(dep_names) + "'"
            print(f"{index}\t{row['activity']}\n\t{row['depends']}\t{deps}", file=sys.stderr)
        
        name = row["activity"][0:30]
        body += f"['{index}', '{row['activity']}', '{row['site']}', new Date({start_y}, {start_m}, 1), new Date({end_y}, {end_m}, 1), null, 0, {deps}]{end}"  

    
    print(header + body + footer)