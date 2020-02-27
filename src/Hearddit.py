import praw
import pyttsx3
import random
import re

# Houses all of the posts retrieved by the bot
# ['subname': [list of posts], 'subname2': [list of posts]]
allPosts = {}

# The (surprisingly few) voices that speak english
availableVoices = [
	'com.apple.speech.synthesis.voice.karen',
	'com.apple.speech.synthesis.voice.Alex',
	'com.apple.speech.synthesis.voice.samantha.premium'
]

# Contains all of the subreddits supported so far, with their
# plain English pronounciations
subs = {
	'askreddit' : 'ask reddit'
	'cscareerquestions' : 'computer science career questions'
	'relationship_advice' : 'relationship advice',
	'legaladvice' : 'legal advice'
}

# Create the Reddit instance and log in
reddit = praw.Reddit(client_id='MTJGEDobi5ZS6A',
	client_secret="C7gQm0rTtWargf6oWyLkY-4vryU", 
	password='butts123', user_agent='buckin_boolin_bot',
	username='boolin_bot')

# Create the speech instance
# Library docs: https://pyttsx3.readthedocs.io/en/latest/
# Github: https://github.com/nateshmbhat/pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 180) # raise this to increase the rate of speaking
voices = engine.getProperty('voices')

# def input():
# 	try:
# 		print("You have 5 seconds to respond before moving on")
# 		foo = raw_input()
# 		return foo
# 	except:
# 		# timeout
# 		return

def getPosts(subName, numPosts):
	""" 
		Gets the specified number of posts 
		from the specified subreddit and appends
		them to the allPosts list.
	"""
	subreddit = reddit.subreddit(subName)
	for post in subreddit.hot(limit=numPosts):
		if (subName in allPosts.keys()):
			# already exists, append to the existing list
			allPosts[subName].append(post)
		else:
			temp = [post]
			allPosts[subName] = temp


# Retrieve all of the posts from the specified sub
for sub in subs.keys():
	getPosts(sub, 2)
print(str(allPosts))

# allPosts architecture: ['subname': ['post1', 'post2'], 'subname2': ['post1', 'post2']]
for sub in allPosts:
	for post in allPosts[sub]:
		try:
			# Change voices (randomize)
			randomVoice = random.randint(0, len(availableVoices) - 1)
			engine.setProperty('voice', availableVoices[1])
			engine.say("Sub Reddit: ..." + subs.get(sub) + ",")
			engine.say("Title: ...")
			engine.say(str(post.title) + "...")

			# Read the description if it exists
			if (post.selftext != ""):
				engine.say("... Description: ...")
				engine.say(str(post.selftext))

			# Moves onto the next post if the current one has no comments
			if (post.comments.__len__() < 1): continue
			
			# Gets the first 5 top level comments
			if (post.comments.__len__() >= 5):
				try:
					count = 0
					engine.say("Comments: ...")
					for comment in post.comments.list():
						# check to see if there is a url
						# if so
						#   get the url
						#   get the indexOf the url using the url
						#   if the index is anything other than 0
						#     grab the substring from 0 to the beginning of the url
						#     "Included Hyperlink"
						#     grab the substring from the end of the url to the end of the comment
						#   else if the index is 0
						#     "Included Hyperlink"
						#     grab the substring from the end of the url to the end of the comment

						randomVoice = random.randint(0, len(availableVoices) - 1)
						engine.setProperty('voice', availableVoices[randomVoice])
						engine.say(str(comment.body))
						engine.runAndWait()
						count = count + 1
						if count == 5:
							break
				except AttributeError:
					continue

		except:
			continue
engine.setProperty('voice', availableVoices[1])
engine.say("... End of Posts ..." + subs.get(sub) + ",")
engine.runAndWait()



