# Instagram Scraper V2.0

1. On terminal install all requirements
`pip install -r requirements.txt`
2. This scraper requires you to login to instagram and save session cookie to stay login as a user. For this, type your instagram username you wish to use for scrapping purposes with the following command on terminal `instaloader -l (USERNAME)` follow the instructions
3. Run instav2.py `python instav2.py`

Enter your username again, instagram username & company name (this is used to save the filename, can be different from insta profile) you would like to scrape.

**Note: Instagram can easily ban you for scrapping so make sure to not use your personal account. (You dont want to get banned)**

## Possible Problem

The speed of scraping is under instagram's rules of conduct policies but when scraping large numbers of posts and comments for a longer period of time is considered abusive behavior by instagram.

A few things can happen in such instance.
1. Instagram might temporarily block your access and ask you to change password telling it detected suspicious behavior.
2. Instagram might block your ip for 24 hours
3. Instagram might ban your account if you keep abusing again & again.

## General Solution

Keep these guidlines in check when using this scrapper.
1. If it has been more than 3 days since you last logged in from terminal, login again. It will refresh the session cookie.
2. Dont scrape profile after profile repeatedly in small amount of time. Give scrapper some break after each run.
3. Make sure instagram is closed in your browser, phone and pc app. Close all instagram instances before running.
4. Dont run scrapper if same instagram account was being used on any other device in last half an hour.
