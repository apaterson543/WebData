

#### Andrew Paterson

## P1.

For this section, the key word "#coronavirus" was used in
the search function of tweepy's cursor tool. After checking about 
40,000 tweets, the program found 1000 unique links that were not pointing 
to the Twitter domain. These links can be found in the file: [unique_uris](output/unique_urls.txt)


To ensure that there were no duplicates after completion of the program, 
the script [check_links.py](src/check_links.py) was used for verification.

During execution, the program encountered around twelve-thousand 300 response codes, and every link encountered was initally shortened using the t.co service.

To view the link gathering program, click [here](src/unique_links.py).






## P2.
For the program see [gather_timemaps.py](src/gather_timemaps.py).

Sample data can be found in the [timemaps](output/timemaps) folder.

View this [histogram](output/graphs/histogram.png) representing the relation between quantity of mementos and frequency of occurence.

For the program that generated the histogram of the collected timemaps, see: [gather_histogram_data.py](src/gather_histogram_data.py).

The archives for the list of URIs collected in part one are not particularly well archived. Only 346 of the links had archives. 

## P3
* Total URIs: 1000 
* No Mementos: 654

##### The relationship between the age of a URI-R for the most part increased the probability of there being more mementos for it. However, there were many with a low age and a high number of mementos and visa versa. 

View [scatterplot](output/graphs/scatterplot.png) representing the relationship between age of a URI-R and its number of mementos.
View [aging_graph.py](src/aging_graph.py) to see the source code for creating the graph.
