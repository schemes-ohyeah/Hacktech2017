import scraper
import json
import config
import requests
import requests.auth
import praw
import weight
from urllib.parse import urlparse
import time

# getTagImage(), getCelebrity(), getOCR()
def print_comments(thread):
    COMMENTS_SECTION = 1
    print("Thread:", "", thread)
    try:
        print("Before requests")
        req = requests.get(thread)
        req.text
        data_2 = req.json()
        comments = []
        print("after requests")
        for value in data_2[COMMENTS_SECTION]['data']['children']:
            if value['kind'] == "t1":
                comments.append(value['data']['body'])
        print("Filled array")
        for val in comments: # This is where it prints stuff
            print(val)
    except Exception as e:
        print(e)
        print("Error in print_comments")
        print("json from print_comments")
        print(json.dumps(data_2, indent=4))

def get_urls():
    url_count = 0
    subreddits = ["all", "funny", "pics"]
    images = {}

    reddit = praw.Reddit('bot1')

    for subreddit in subreddits:
        for thread in reddit.subreddit(subreddit).top(limit=10):
            if thread.url[-4:] == ".jpg" or thread.url[-4:] == ".png":
                comms = []
                submission = reddit.submission(thread.id)
                submission.comment_sort = 'top'
                submission.comments.replace_more(limit=0) # makes sure it has a body (Not the "more" button)
                for comment in submission.comments.list():
                    comms.append(comment.body)
                images[thread.url] = comms
                url_count = url_count + 1
            elif urlparse(thread.url).netloc == "imgur.com":
                url = "{parsed_url.scheme}://i.{parsed_url.netloc}/{parsed_url.path}.png".format(parsed_url=urlparse(thread.url))
                comms = []
                submission = reddit.submission(thread.id)
                submission.comment_sort = 'top'
                submission.comments.replace_more(limit=0)  # makes sure it has a body (Not the "more" button)
                for comment in submission.comments.list():
                    comms.append(comment.body)
                images[url] = comms
                url_count = url_count + 1
    """PRINTS
    for key in images:
        print(key)
        for com in images[key]:
            print(com)
    """
    return images
    #print(url_count)

    # file.close()

def main():
    get_urls()


main()