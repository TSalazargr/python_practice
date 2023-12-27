import datetime

with open("tweet_archive.txt", "a") as file:
  pass

def add_tweet():
    timestamp = datetime.datetime.now() # Creates a timestamp
    tweet = input("Write your tweet here: ")
    
    with open("tweet_archive.txt", "r") as file:
      old_tweets = file.read()
    
    with open("tweet_archive.txt", "w") as file:
      file.write(f"{timestamp}:{tweet}" + "\n" + old_tweets) # Adds the last tweet first and then the old ones to print in reverse chronological order

def next_10_tweets(start_tweet, last_tweet):
    with open("tweet_archive.txt") as file:
      tweet_archive = file.readlines()
      print_10_tweets = tweet_archive[start_tweet:last_tweet] # Displays last 10 tweets
      for i in print_10_tweets:
          print(i)

def view_tweets():
  start_tweet = 0
  last_tweet = 11
  while True:
    next_10_tweets(start_tweet, last_tweet)
    print_more = input("Would you like to print 10 more tweets?: y/n")
    if print_more == "n":
      break
    else:
      start_tweet = last_tweet # Update start_tweet so the first tweet is the one after the last one
      last_tweet += 10

while True:
  menu = input("Would you like to: \n 1 Add a tweet \n 2 View a tweet \n 1/2: ")
  while menu != "1" and menu != "2":
    print("Invalid value. Try again.")
    menu = input("Would you like to: \n 1 Add a tweet \n 2 View a tweet \n 1/2: ")
  if menu == "1":
    add_tweet()
  else:
    view_tweets()
