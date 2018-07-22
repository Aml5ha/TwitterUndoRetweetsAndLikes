# TwitterUndoRetweetsAndLikes
Code for undoing a majority of your most recent retweets and likes

The code does not have error checking in case the login information is incorrect. This code is not perfect, as sometimes it misses certain retweets on the page - I am still trying to figure out the cause of this behavior. The performance of this code also depends on how long the user decides to scroll down the page and how many times it is run in succession, as twitter sometimes stops loading tweets/cooperating. 

Like any selenium project, the performance of the program depends on the machine and network. The code may have to be slightly altered to account for slower machines/networks.

The chromedriver used in this project is v 2.4 which supports Chrome v66-68. In the future a more recent version of chromedriver may be needed.

## Overview: 
This code works by logging in to the user's twitter and navigating to their page. Then, the program scrolls for a inputted number of seconds and searches for 'undoable-buttons' on the page. Then the program loops through the list of found items and trys to click on each one. 

## Copyright:
I made this myself and am fine with anyone improving it or using it. I'd love to hear your thoughts on the project!
