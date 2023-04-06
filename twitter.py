import sys
sys.path.insert(0, 'PATH OF TWEEPY FILE IN YOUR LOCAL OR GIT'
                
import tweepy
import requests
                
# Twitter API credentials so you will have to sign up through twitter developer to get these may need to get advanced access
consumer_key = " "
consumer_secret = " "
access_token = " "
access_token_secret = " "

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
                
# Create API object
api = tweepy.API(auth)

# ID of the post you want to collect comments from
post_id = "GO TO THE TWEET COPY THE LINK AND PASTE THE NUMBER AT THE END OF THE URL HERE"
                
                # Collect comments from the post using the API
comments = []
for comment in tweepy.Cursor(api.search_tweets,q=f"to:{api.get_status(post_id).user.screen_name}", since_id=post_id,tweet_mode='extended').items():
    if hasattr(comment, 'in_reply_to_status_id_str'):
        if comment.in_reply_to_status_id_str == post_id:
            comments.append(comment.full_text)
                
# Create empty dictionaries for each data set
data_sets = {
    " "= 0, 
    " "= 0,
    " "= 0,
    " "= 0,
    " "= 0,
}

# Iterate through the comments and count the occurrence of specific keywords/themes
for comment in comments:
    if "THIS IS WHERE YOU WILL PUT THE KEY WORDS YOU ARE USING AS MEASUREMENTS" in comment:
        data_sets["THIS_IS_WHERE_YOU_WILL_PUT_YOUR_DATA_SET_FROM ABOVE THE"] += 1
    if "THIS IS WHERE YOU WILL PUT THE KEY WORDS YOU ARE USING AS MEASUREMENTS" in comment:
        data_sets["THIS_IS_WHERE_YOU_WILL_PUT_YOUR_DATA_SET_FROM ABOVE THE"] += 1
    if "THIS IS WHERE YOU WILL PUT THE KEY WORDS YOU ARE USING AS MEASUREMENTS" in comment:
        data_sets["THIS_IS_WHERE_YOU_WILL_PUT_YOUR_DATA_SET_FROM ABOVE THE"] += 1
    if "THIS IS WHERE YOU WILL PUT THE KEY WORDS YOU ARE USING AS MEASUREMENTS" in comment:
        data_sets["THIS_IS_WHERE_YOU_WILL_PUT_YOUR_DATA_SET_FROM ABOVE THE"] += 1
                
# Print the total number of occurrences of each keyword/theme
print("Number of occurrences of each keyword/theme:")
for data_set, count in data_sets.items():
    print(f"{data_set}: {count}")
