import pandas as pd
import instaloader

USER = input("Enter your instagram username: ") # Your user name
company_ig = input("Enter the company's instagram profile username: ") # Instagram profile username to scrape
company_name = input("Enter the company name: ") # Type how you like it to appear in output file


# Data Frame Header
data = pd.DataFrame(columns=["Company_Name", "Post_URL", "Comment","Post_Date", "Username"])

########################### Add rows in data frame ########################

def addRow(dataframe, company_name, post_url, comment, date, username):
    df_temp = pd.DataFrame(
        {"Company_Name": [company_name],
        "Post_URL": [post_url],
        "Comment": [comment],
        "Post_Date": [date],
        "Username": [username]}
        )
    df = pd.concat([dataframe, df_temp], ignore_index=True)
    return df

########################### Instagram Integration ##########################

L = instaloader.Instaloader()
L.load_session_from_file(USER) # (load session created with `instaloader -l USERNAME`)
profile = instaloader.Profile.from_username(L.context, f"{company_ig}")
posts = profile.get_posts()

################################ Scrape Data ################################

count = 0
pc = posts.count
try:
    for post in posts:
        count += 1
        pc -= 1
        url = f"https://www.instagram.com/p/{post.shortcode}/"
        print(f"Number of posts left: {pc}\tScrapping Comments...")
        comments = post.get_comments()
        data = addRow(data, company_name, url, post.caption, post.date, profile.username)
        for comment in comments:
            data = addRow(data, company_name, url, comment.text, comment.created_at_utc, comment.owner.username)
        print(f"Number of Posts Scraped: {count}")
except:
    print(f"Terminated on exception. Exporting data to {company_name}.xlsx")
    data.to_excel(f"{company_name}.xlsx", index=False)
    
################################ Output Data ################################
try:
    print("All Posts Scraped Successfully".capitalize())
    print(f"Number of posts scraped:\t{count}")
    print(f"Number of comments scraped:\t{len(data.index)}")
    
except:
    pass
print(f"Exporting data to {company_name}.xlsx")
data.to_excel(f"{company_name}.xlsx", index=False)
    
