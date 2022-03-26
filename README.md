# Gannt charts from Excel tables

Some resources to plot Gannt charts. I made the scripts 
able to start from Excel tables (to make it easier
for collaborators to feed me data, as inevitably there will be last minutes updates :) ).

A first approach [ganttrify](https://github.com/giocomai/ganttrify),
an R library by Giorgio Comai, 
and a second example uses [Google charts](https://developers.google.com/chart/interactive/docs/gallery/ganttchart),
a Javascript library for interactive plots. They both start from basically the same Excel template.


* Stand-alone [R script for PDF/PNG output](r-plot)
* Stand-alone [Python script for HTML output](html-plot)
* Integrated package **coming soon**

Example R plot:

![Example](r-plot/gannt.png)

Example HTML plot: [online demo](https://jsfiddle.net/h86Lz94p/)



### See also

* [R Gannt charts](https://jtr13.github.io/cc19/gantt-charts.html)
* [R/Plotly Gannt charts](https://plotly.com/r/gantt/)
