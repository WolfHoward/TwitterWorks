import twitter
from api_access import api_info


api = twitter.Api(consumer_key=api_info['consumer_key'],
                consumer_secret=api_info['consumer_secret'],
                access_token_key=api_info['access_token_key'],
                access_token_secret=api_info['access_token_secret'])


# Do a basic Twitter search by hash tag, returning 100 results sorted by
# most popular
def search_by_hash():
    search_term = input("Enter your search team, sans hash tag: ")
    result_type = input("Enter search type (mixed, popular, recent): ")
    # The '%23' is how Twitter formats a url when searching by hash tag
    query = 'q=%23' + search_term + '&src=typd&result_type=recent&count=100'
    search = api.GetSearch(raw_query=query)

    print(len(search))
    return search


# Grab screen names of users from a list of tweets
# This will only collect unique screen names, so this list of users
# won't necessarily match the number of tweets passed
def get_screen_names(tweets):

    # We will return the screen names as a list of users
    users = []

    # We modify each tweet in the list to render as a dictionary so we
    # can access the screen_name in an easy way
    for tweet in tweets:
        tweet_dict = tweet.AsDict()
        user = tweet_dict['user']['screen_name']

        if user not in users:
            users.append(user)

    return users


# Take a Twitter list and owner as strings, and a list of users
# then add the users to the Twitter list
def post_users_to_list(users):
    list_to_post = input("Enter the name of your list: ")
    list_owner = input("Enter the owner of the list: ")


    api.CreateListsMember(slug=list_to_post,screen_name=users,
                          owner_screen_name=list_owner)
