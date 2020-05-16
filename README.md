# CodeChef-Solutions-Downloader
This is a python tool which I have bulit to download the solutions submitted by me(<a target="_blank" href="https://www.codechef.com/users/cosine1509">cosine1509</a>) on www.codechef.com<br>
This can be done for any user, given their username on CodeChef<br>
*<b>Note</b> that the solutions downloaded are from past contests or practice problems on CodeChef,<br>
which are accessible to everyone.*  
## Technologies used
### Language: Python
Modules used: requests, os, bs4
## Description
The CodeChef user profile page is accessed using python *requests*. From the profile page,<br>
the links for the user's successful submissions and the question codes are scraped using *BeautifulSoup* module.
A folder is created with the name as *username*.<br>
The solution content is fetched through the links and each time a file with the name as
"*questioncode_solutioncode.txt*" is created in the folder.
## Setup
Installing the required modules:<br>
*pip install requests*<br>
*pip install bs4*<br>
*os* module is already available with the Python Standard Library and does not require installation.<br>

Run *cc_scraper.py* in any Python IDE.


