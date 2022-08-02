# RedditSentimentAnalysisScraper
This is my reddit sentimental analysis web scraper. It was an application I used in order to learn more about web crawling and web scraping. Its purpose
was to see how happy or angry various subreddits were and compare them This program displays information in the console, so something like an IDE or the 
command promp is needed. To use, there are two files that have different functions. The main file is main.py in which a user can enter any reddit subreddit 
link, and how much they would like to scroll within that reddit link to gather information under that subreddit. From there, every link that was viewed is 
open and all comments are taken from each posts in the subreddit. A file is then stored that contains every comment up until where a user chooses to scroll 
in the subreddit. After this, sentiment.py can be ran in which the user enters the name of the file that a subreddit was saved under in order to view the average 
sentiment of the subreddit according to comments.

An example of me using this application was I used it on r/wholesome to compare it to r/politics, and wholesome had better sentiment than politics. 

Technologies used in this application were the Beautiful Soup and Selenium python libraries.
Beaufitul Soup was used as the main driver in gathering information, and selenium was used to scroll the subreddits. This is because Reddit is dynamically loaded, which
meant that the program was required to scroll in order to gather new information.
