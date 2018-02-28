from instapy import InstaPy
import random
import sys, os
import getpass

try:
  print("Please enter your Instagram credentials")
  username_input = raw_input("Username: ")

  passowrd_input = getpass.getpass('Password: ')

  session = InstaPy(username=username_input, password=passowrd_input)
  session.login()

  #image_url = raw_input("Enter the image url would you like to use: ")
  # session.like_from_image(url=image_url, amount=100)

  #session.like_by_tags(['utahgram', 'instautah', 'igutah', 'iloveutah', 'mountainlife', 'wowutah', 'rockymountains', 'adventureculture', 'optoutside', 'getoutdoors', 'hiking', 'hikeutah', 'utahisrad', 'adventureon', 'utahrocks', 'visitutah', 'exploreutah', 'iloveutah', 'beautahful', 'southernutah', 'utah'], amount=100)

  possible_tags = ['morainelake', 'instautah', 'agameoftones', 'moodygrams', 'mg5k', 'beautifuldestinations', 'explorecanada', 'tourcanada', 'canada', 'banffnationalpark', 'banff', 'canadasworld', 'hikingadventures', 'discoverbanff', 'travelcanada', 'travelphotography', 'mybanff', 'canada', 'travel', 'adventure', 'hicanada', 'canada150', 'parkscanada', 'travelalberta', 'visitcanada', 'tourcanada', 'enjoycanada', 'takemetheretoday', 'imagesofcanada', 'paradiseCanada', 'canadaday']
  tags = random.sample(possible_tags, 15)


  session.like_by_tags(tags, amount=100)

finally:
  """Ending the script"""
  # clears all the cookies, deleting you password and all information from this session
  session.end()

