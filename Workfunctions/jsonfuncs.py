import tweepy
def info_twitter(name_of_twit, amount):
    '''
    (str, int) -> list(dict)
    Returns list of dictionaries with json info about friends.
    '''
    myfriends = []
    auth = tweepy.OAuthHandler("0PlKlKMbNYWL9UeVuC6DPxX4B", "dpvpCGjA9udpjsPkCVfdxZhmAOLMXFeZcZEVLbH3usRiv8fHfN")
    auth.set_access_token("963011359737774080-mYiiiIGOarKbuYGVdVTJBPcYC39RkqC", "f8031GVQo6dJXX35RRVbDlGxMcitrAt7uyAUVgKuO1E0R")
    api = tweepy.API(auth, wait_on_rate_limit=True)
    user = api.get_user(name_of_twit)
    for friend in user.friends(count = amount):
        string = dict(friend._json)
        myfriends.append(string)
    return myfriends

def json_working(username, fr_amount, key, minefriends):
    '''
    (str, int, str, list) -> dict[key]
    Return the piece of data from json files got through Twitter API.
    '''
    result = []
    for fr in minefriends:
        result.append(fr[key])
    return result
