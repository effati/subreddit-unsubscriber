from datetime import datetime
import praw
import credentials


def clear_new(subreddit, exp_date='2018-01-01'):
    # For subreddits that hasn't been updated since exp_date
    for new_post in subreddit.new():
        date = datetime.utcfromtimestamp(new_post.created).strftime('%Y-%m-%d')
        date = datetime.strptime(date, '%Y-%m-%d')
        cmp_date = datetime.strptime(exp_date, '%Y-%m-%d').date()
        if date.date() < cmp_date:
            subreddit.unsubscribe()
        return


def clear_unpopular(subreddit, upvote_limit=15, subscribers_limit=1000):
    # For subreddits with posts with less upvotes than upvote_limit, or less subscribers than subscribers_limit
    for post in subreddit.hot():
        if post.stickied:
            continue
        if post.ups < upvote_limit:
            subreddit.unsubscribe()
        if subreddit.subscribers < subscribers_limit:
            subreddit.unsubscribe()
        return


def start():
    for subreddit in reddit.user.subreddits(limit=None):
        print("."),
        clear_new(subreddit)
        clear_unpopular(subreddit)


if __name__ == '__main__':
    reddit = praw.Reddit(client_id=credentials.client_id,
                         client_secret=credentials.client_secret,
                         password=credentials.password,
                         user_agent=credentials.user_agent,
                         username=credentials.username)
    start()
