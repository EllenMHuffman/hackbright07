import os
from sys import argv
import twitter
import markov

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    )

# print api.VerifyCredentials()

def first_tweet():
    input_path = argv[1]

    # Open the file and turn it into one long string
    input_text = markov.open_and_read_file(input_path)

    # Get a Markov chain
    chains = markov.make_chains(input_text, int(argv[2]))

    new_tweet = markov.make_text(chains, int(argv[2]))
    api.PostUpdate(new_tweet)
    print new_tweet
    return chains


def repeat_tweet(chains):
    """"""
    response = raw_input('Enter to tweet again (q to quit): ')
    if response == '':
        next_tweet = markov.make_text(chains, int(argv[2]))
        api.PostUpdate(next_tweet)
        print next_tweet
        repeat_tweet(chains)
    else:
        pass

chains = first_tweet()
repeat_tweet(chains)
# print status.text