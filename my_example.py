from instapy import InstaPy
import random
import sys, os
import getpass

try:
  print("Please enter your Instagram credentials")
  username_input = raw_input("Username: ")

  passowrd_input = getpass.getpass('Password: ')

  session = InstaPy(username=username_input, password=passowrd_input)
  session.max_likes = random.randint(700,950)
  print "Max likes: {}".format(session.max_likes)
  session.login()

  #image_url = raw_input("Enter the image url would you like to use: ")
  # session.like_from_image(url=image_url, amount=100)

  #session.like_by_tags(['utahgram', 'instautah', 'igutah', 'iloveutah', 'mountainlife', 'wowutah', 'rockymountains', 'adventureculture', 'optoutside', 'getoutdoors', 'hiking', 'hikeutah', 'utahisrad', 'adventureon', 'utahrocks', 'visitutah', 'exploreutah', 'iloveutah', 'beautahful', 'southernutah', 'utah'], amount=100)

  possible_tags = ['morainelake', 'instautah', 'agameoftones', 'moodygrams', 'mg5k', 'beautifuldestinations', 'explorecanada', 'tourcanada', 'canada',
  'banffnationalpark', 'banff', 'canadasworld', 'hikingadventures', 'discoverbanff', 'travelcanada', 'travelphotography', 'mybanff', 'canada', 'travel',
  'adventure', 'hicanada', 'canada150', 'parkscanada', 'travelalberta', 'visitcanada', 'tourcanada', 'enjoycanada', 'takemetheretoday', 'imagesofcanada',
  'paradiseCanada', 'canadaday',
  'naturephoto',
  'watchthisinstagood',
  'artofvisuals',
  'awesome_earthpix',
  'landscape_captures',
  'rsa_rural',
  'natureaddict',
  'nature_wizards',
  'awesomeearth',
  'naturediversity',
  'ourplanetdaily',
  'earth_deluxe',
  'instanaturelover',
  'nature_prefection',
  'allnatureshots',
  'gottalove_a_',
  'nature_brilliance',
  'EarthVisuals',
  'fantastic_earth',
  'unlimitedplanet',
  'main_vision',
  'planetdiscovery',
  'welivetoexplore',
  'landscape_lovers',
  'sky_captures',
  'landscapephotography',
  'fantastic_earth',
  'landscape_captures',
  'ic_landscapes',
  'ig_exquisite',
  'nature_wizards',
  'nature_shooters',
  'landscapestyles_gf',
  'ourplanetdaily',
  'landscapehunter',
  'special_shots',
  'naturediversity',
  'landscapelovers',
  'earth_deluxe',
  'instanaturelover',
  'nature_prefection',
  'nature_brilliance',
  'gottalove_a_',
  'allnatureshots',
  'EarthVisuals',
  'welivetoexplore']

  tags = random.sample(possible_tags, len(possible_tags))

  #session.like_by_feed(amount=10, randomize=True, unfollow=True, interact=True)
  session.like_by_tags(tags, amount=100)

except:
    raise

finally:
  """Ending the script"""
  # clears all the cookies, deleting you password and all information from this session
  session.end()

