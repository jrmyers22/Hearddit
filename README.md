# Hearddit
An auditory version of the popular news site, Reddit.com

## State of the Project:
**Functionality:**
- [ ] Retrieve a single post
    - [x] Get the subreddit of the post and read it out
    - [x] Get the title of that post and read it out
        - [ ] Wait a few seconds for some interaction, if interaction then read the description
            - [ ] Wait a few seconds for some interaction, if interaction then read the top level comment
                - [ ] Repeat
            - [ ] Provide ability to get out of the comment section and go to the next post
- [ ] Figure out how to support infinite number of posts


**Bugs:**
- [x] Since it gets the name of the subreddit as a single word, pronunciation suffers
    - [x] Once we figure out which subreddits we will support, could have a dictionary containing the plain english translation of all of them?

- [ ] Detect urls in comment and skip them, if not the voice just reads the whole thing
- [ ] Stop pronouncing the markdown characters (like bold being “asterisk asterisk”)

- [ ] Right now it reads all from one subreddit before switching, want the ability to read 1 from a subreddit then move to the next one
    - [ ] Remove the one that was just read then move on
    - [ ] Put the reading in a while loop, once it hits the end of the “posts” list then reset the index to 


## Stretch Goals:
- [ ] Voice-related:
    - [ ] Parse the comment/description and if they are identified as a female then set the gender of the voice 
- [ ] Ability to save that post for later (would only save on the app, not on their Reddit account)
- [ ] Randomize to a text based subreddit (not specified, using the collection below or a different collection)
- [ ] Ability to upvote, downvote, clear_vote(), guild, save
- [ ] Identifying the link domain name
