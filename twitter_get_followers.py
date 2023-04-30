import os
import tweepy
import subprocess
import time

def get_api():
    # Replace the following values with your own API keys and access tokens
    consumer_key = 'api_key'
    consumer_secret = 'api_secret'
    access_token = 'access_token'
    access_token_secret = 'access_secret'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def get_follower_count(api, screen_name):
    user = api.get_user(screen_name=screen_name)
    return user.followers_count

def read_previous_follower_count(file_name):
    if not os.path.exists(file_name):
        return None

    with open(file_name, 'r') as file:
        return int(file.read().strip())

def write_follower_count(file_name, count):
    with open(file_name, 'w') as file:
        file.write(str(count))

def main():
    while True:
        api = get_api()
        screen_name = 'supremebeme'  # Replace with your Twitter handle (without '@')
        followers_count = get_follower_count(api, screen_name)
        
        file_name = 'previous_follower_count.txt'
        previous_count = read_previous_follower_count(file_name)

        if previous_count is not None:
            difference = followers_count - previous_count

            if difference > 0:
                print(f'Your account @{screen_name} gained {difference} new followers since last check.')
                action = 'buy'
            elif difference < 0:
                print(f'Your account @{screen_name} lost {-difference} followers since last check.')
                action = 'sell'
            else:
                print('No new followers, have a nice day!')
                action = None
                #return

            # Call the dex_buy_doge_market.py script with the appropriate action and number of DOGECOIN        
            if action:
                script_path = '.\\dex_buy_doge_market.py'
                subprocess.run(['python', script_path, action, str(abs(difference))])

        print(f'Your account @{screen_name} currently has {followers_count} followers.')

        write_follower_count(file_name, followers_count)

        print("Waiting for 15 minutes before checking again.")
        time.sleep(15 * 60)  # Sleep for 15 minutes    


if __name__ == '__main__':
    main()
