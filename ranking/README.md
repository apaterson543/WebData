# Homework 3 - Ranking Webpages
### Andrew Paterson

### Q1. Data Collection

To collect all of the source text from the 1000 files gathered in homework 2, I used the requests .content tool. 
Next, in order to eliminate the non-content text such as HTML tags, I used the lxml library 
and its .clean_html() function. This still left some tags and css. Next I wrote a few regex replace statements to get 
rid of any remaining tags and line break characters. After this process there was still some unwanted text in these files 
but it was little enough to begin further processing. 

The reason this method was chose is because I was unable to get python boilerpipe to run on my computer. I will surely
continue to experiment in order to get that method running for the future.

While gathering the text from these pages I found that since they were collected 2 weeks ago, many of them ceased to exist.
Only 979 of them gave a response.

To view the text collected from the files see [Cleaner](io_text_resources/Cleaner).

To view the raw html originally gathered from the page, see [Raw](io_text_resources/Raw).

To view the python script used to collect this text see [collect_text.py](collect_text.py).



### Q2. Rank with TF-IDF

I chose 'coronavirus' as my query term. The reason I chose this word is because it was my query term on twitter while
initially gathering the 1000 unique links. As mentioned in Q1, only 979 of the links previously collected returned a response.
Of these 979, only a little over 300 actually contained the query word. This is interesting because people put the tag
\#coronavirus but on links that did not contain that word.

In order to maximize my chances of having a non-zero TF-IDF, I scanned through all the text to find the ten files with the 
highest number of occurences of the query term. 

For collection script, see [get_ten.py](get_ten.py).

For the top ten files chosen that contained the query term, a file was generated for each that contained:
* Line 0: URI
* Line 3: Source text
* Line 4: Number of occurences of query term in file

Also the file [number_of_files_containing_term.txt](io_text_resources/TopTen/number_of_files_containing_term.txt)
was generated during the execution of [get_ten.py](get_ten.py) to count the number of files actually containing the term
for calculation of TF.

To view these 10 files, see [TopTen](io_text_resources/TopTen).

After collecting these files, the script [create_TF_IDF.py](create_TF_IDF.py) was used to calculate the TF-IDF for each of the 10 
files collected. For the files in corpus, I used Bing's estimated size of the web. 

Later on for question 4, this same file was manipulated to change Bing's number to the total number of links collected by twitter

This script also generated the .csv file: [TF_IDF_WEB.csv](io_text_resources/Charts/TF_IDF_web.csv).

This table created in the .csv file is also depicted in **Table 1**. 

**Table 1.**  *10 pages with hits for the term "coronavirus", ranked by TF-IDF where corpus size is Bing web size estimation.*

|TF-IDF |TF	|IDF |URI
|---:|---:|---:|---
|0.621773 |0.025132 |24.739500 |https://www.donaldjtrump.com/media/timeline-the-trump-administrations-decisive-actions-to-combat-the-coronavirus/
|1.144139 |0.046247 |24.739500 |https://nodexlgraphgallery.org/Pages/Graph.aspx?graphID=237287
|0.143908 |0.005816 |24.739500 |https://www.wbaltv.com/article/maryland-coronavirus-numbers-map-faq-october-5-11/34271761
|0.576042 |0.023284 |24.739500 |https://www.click2houston.com/health/2020/03/22/chart-houston-area-coronavirus-cases-in-the-past-week/?utm_source=twitter&utm_medium=social&utm_campaign=snd&utm_content=kprc2
|0.236443 |0.009557 |24.739500 |https://www.politico.com/news/2020/10/06/osha-coronavirus-penalties-426828
|0.051653 |0.002087 |24.739500 |https://www.dailymail.co.uk/news/article-8815059/Nicola-Sturgeon-set-BAN-alcohol-Scotlands-pubs-force-6pm-closing.html
|0.180347 |0.007289 |24.739500 |https://www.city-journal.org/trump-coronavirus-diagnosis-models-positive-masculinity
|0.252443 |0.010204 |24.739500 |http://www.msn.com/en-us/news/us/how-much-would-trumps-coronavirus-treatment-cost-most-americans/ar-BB19MG4w?ocid=st
|0.029061 |0.001174 |24.739500 |https://www.dailymail.co.uk/tvshowbiz/article-8813329/Wendy-Williams-mispronounced-coronavirus-cornova-Trumps-return-White-House.html
|0.022490 |0.000909 |24.739500 |https://www.theguardian.com/world/live/2020/oct/07/coronavirus-live-news-six-us-states-see-record-hospital-patients-facebook-deletes-trump-post?CMP=share_btn_tw&page=with:block-5f7db5e18f08ac58bb46810c#block-5f7db5e18f08ac58bb46810c


### Q3. Rank with PageRank

To gather the PageRank of these pages on the web, I chose the tool:

* http://www.prchecker.info/check_page_rank.php
  
After manually entering the 10 URIs collected in **Q2**, It turned out that all of them had a zero page rank. 
This may be because none of the domains are extremely popular and also because all of the pages are a particular article 
and not the landing page of the main domain website.

**Table 2.**  10 pages with hits for the term "coronavirus", ranked by PageRank.

|PageRank	|URI
|-----:|---
|0 |https://www.donaldjtrump.com/media/timeline-the-trump-administrations-decisive-actions-to-combat-the-coronavirus/
|0 |https://nodexlgraphgallery.org/Pages/Graph.aspx?graphID=237287
|0 |https://www.wbaltv.com/article/maryland-coronavirus-numbers-map-faq-october-5-11/34271761
|0 |https://www.click2houston.com/health/2020/03/22/chart-houston-area-coronavirus-cases-in-the-past-week/?utm_source=twitter&utm_medium=social&utm_campaign=snd&utm_content=kprc2
|0 |https://www.politico.com/news/2020/10/06/osha-coronavirus-penalties-426828
|0 |https://www.dailymail.co.uk/news/article-8815059/Nicola-Sturgeon-set-BAN-alcohol-Scotlands-pubs-force-6pm-closing.html
|0 |https://www.city-journal.org/trump-coronavirus-diagnosis-models-positive-masculinity
|0 |http://www.msn.com/en-us/news/us/how-much-would-trumps-coronavirus-treatment-cost-most-americans/ar-BB19MG4w?ocid=st
|0 |https://www.dailymail.co.uk/tvshowbiz/article-8813329/Wendy-Williams-mispronounced-coronavirus-cornova-Trumps-return-White-House.html
|0 |https://www.theguardian.com/world/live/2020/oct/07/coronavirus-live-news-six-us-states-see-record-hospital-patients-facebook-deletes-trump-post?CMP=share_btn_tw&page=with:block-5f7db5e18f08ac58bb46810c#block-5f7db5e18f08ac58bb46810c

*This information can also be observed in [page_rank.csv](io_text_resources/Charts/page_rank.csv).*

## Extra Credit

### Q4. 

Similarly to **Q2** I used the [create_TF_IDF.py](create_TF_IDF.py) script to calculate the TF-IDF of the 10 web pages in [TopTen](io_text_resources/TopTen). However, for this
calculation, the corpus size denoted in the script was changed to 979 to represent the number of files in the corpus of twitter 
links gathered in [unique_urls.txt](io_text_resources/unique_urls.txt) in the last homework assignment.

Once again, the file [number_of_files_containing_term.txt](io_text_resources/TopTen/number_of_files_containing_term.txt) was used for the calculation of TF.

**Table 1.**  *10 pages with hits for the term "coronavirus", ranked by TF-IDF where corpus size is number of active links gathered from Twitter.*

|TF-IDF |TF	|IDF |URI
|---:|---:|---:|---
|0.036577 |0.025132 |1.455384 |https://www.donaldjtrump.com/media/timeline-the-trump-administrations-decisive-actions-to-combat-the-coronavirus/
|0.067307 |0.046247 |1.455384 |https://nodexlgraphgallery.org/Pages/Graph.aspx?graphID=237287
|0.008465 |0.005816 |1.455384 |https://www.wbaltv.com/article/maryland-coronavirus-numbers-map-faq-october-5-11/34271761
|0.033887 |02328431 |1.455384 |https://www.click2houston.com/health/2020/03/22/chart-houston-area-coronavirus-cases-in-the-past-week/?utm_source=twitter&utm_medium=social&utm_campaign=snd&utm_content=kprc2
|0.013909 |0.009557 |1.455384 |https://www.politico.com/news/2020/10/06/osha-coronavirus-penalties-426828
|0.003038 |0.002087 |1.455384 |https://www.dailymail.co.uk/news/article-8815059/Nicola-Sturgeon-set-BAN-alcohol-Scotlands-pubs-force-6pm-closing.html
|0.010609 |0.007289 |1.455384 |https://www.city-journal.org/trump-coronavirus-diagnosis-models-positive-masculinity
|0.014850 |0.010204 |1.455384 |http://www.msn.com/en-us/news/us/how-much-would-trumps-coronavirus-treatment-cost-most-americans/ar-BB19MG4w?ocid=st
|0.001709 |0.001174 |1.455384 |https://www.dailymail.co.uk/tvshowbiz/article-8813329/Wendy-Williams-mispronounced-coronavirus-cornova-Trumps-return-White-House.html
|0.001323 |0.000909 |1.455384 |https://www.theguardian.com/world/live/2020/oct/07/coronavirus-live-news-six-us-states-see-record-hospital-patients-facebook-deletes-trump-post?CMP=share_btn_tw&page=with:block-5f7db5e18f08ac58bb46810c#block-5f7db5e18f08ac58bb46810c

*This information can also be observed in [TF_IDF_twitter.csv](io_text_resources/Charts/TF_IDF_twitter.csv).*

