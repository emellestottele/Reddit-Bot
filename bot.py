import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment function from the madlibs assignment here
madlibs = [
    "[DONALD_TRUMP] is an [AMERICAN] [POLITICIAN]. He is also a [MEDIA_PERSONALITY] and [BUSINESS_MAN] He is very [RICH].", 
    "[DONALD_TRUMP] was the republican [NOMINEE] in the 45th presidentail [ELECTIONS]. He [DEFEATED] [HILARY_CLINTON] and [WON] the [RACE]",
    "[TRUMP] is a [BAD] [PRESIDENT].  He [COULD_DO] [LOTS] of [GOOD] [THINGS].",
    "[BUT] [HE] [DID_NOT] and was a [HORRIBLE] [PRESIDENT]. I [HATE] [TRUMP].", 
    "[TRUMP] had horrible [POLICIES]. They did not [BENEFIT] the [MAJORITY] of the [PEOPLE]",
    "[TRUMP] is also [UGLY]. His hair is [VERY] [ORANGE]. He is also [FAT]"
    ]

replacements = {
    'TRUMP' : ['Trump', 'Donald', 'Mr Trump'],
    'BAD' : ['bad', 'horrible', 'poor', 'inadequate', 'unpleasant'],
    'PRESIDENT' : ['president', 'leader', 'head of state', 'chief of state' ],
    'COULD_DO' : ['could do', 'could have', 'would be able to do', 'was enabled to do', 'could have done'],
    'LOTS'  : ['lots', 'a whole lot', 'ridiculous amounts'],
    'GOOD' : ['lots', 'valuable', 'important', 'impactful', 'effectvie'],
    'THINGS' : ['things', 'actions', 'policies', 'undertakings'], 
    'BUT' : ['But', 'yet', 'nonetheless', 'nevertheless', 'however', 'still'],
    'HE' : ['he', 'Trump', 'TRUMP', 'the president,', 'the bad president', 'that man ', 'the 45th president'],
    'DID_NOT' : ['did not', 'should', 'must', 'need to'],
    'HORRIBLE' : ['horrible', 'dreadful', 'terrible', 'appalling', 'shocking'],
    'HATE' : ['hate', 'dislike', 'despise', 'dont like', 'dont like' ],
    'DONALD_TRUMP' : ['donald trump', 'trump', 'TRUMP', 'Mr Trump', 'Donald'],
    'AMERICAN' : ['american', 'US', 'United Statesian'], 
    'POLITICIAN' : ['politican', 'legislator', 'government employee', 'public servant', 'law maker'], 
    'MEDIA_PERSONALITY': ['media personality', 'socialite', 'celebrity', 'celeb'],
    'BUSINESS_MAN' : ['business man', 'entrepreneur', 'business person', 'tycoon'],
    'RICH' :  ['rich', 'wealthy', 'affluent', 'well off', 'cash rich'], 
    'NOMINEE' : ['nominee', 'representative', 'candidate', 'appointee', 'selectee'], 
    'ELECTIONS' : ['elections', 'vote', 'general election', 'public vote'],
    'DEFEATED' : ['defeated' 'beat', 'was victorious over', 'conquered'],
    'HILARY_CLINTON': ['hilary clinton', 'Clinton', 'Mrs Clinton', 'Hilary', 'the other candiate'],
    'WON' : ['won', 'secured', 'was victorious in', 'secured'], 
    'RACE' : ['race', 'elections', 'competition', 'presidential race', 'presidential campaign'],
    'POLICIES' : ['policies','programs', 'actions', 'strategies', 'protocol'],
    'BENEFIT' : ['benefit', 'serve', 'satisfy', 'advantage'],
    'MAJORITY' : ['majority', 'bulk', 'the masses', 'predominance'], 
    'PEOPLE' : ['people', 'americans', 'persons', 'citizens', 'individuals'],
    'UGLY' : ['ugly', 'hideous', 'unattractive', 'displeasing', 'unsightly'],
    'VERY' : ['very', 'extremely', 'especially', 'overly', 'immensley'],
    'ORANGE' : ['orange', 'red', 'bright', 'flat', 'thin', 'non existant'],
    'FAT' : ['fat', 'large', 'obese', 'overweight', 'plump']
    }

def generate_comment():
    s = random.choice(madlibs)
    for k in replacements.keys():
        s = s.replace('['+k+']', random.choice(replacements[k]))
    return(s)

# FIXME:
# connect to reddit 
reddit = praw.Reddit('emelle_bot')

# FIXME:
# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://www.reddit.com/r/BotTown2/comments/r4nt42/the_uk_labour_party_is_now_in_a_massive_sixpoint/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    submission.comments.replace_more(limit=None)
    
    all_comments =  []
    for comment in submission.comments.list():
        all_comments.append(comment)
    #all_comments = submission.comments.list()
    
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []

    for comment in all_comments:
        if str(comment.author) != 'emelle_bot':
            not_my_comments.append(comment)
    
    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=', len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    print('has not commented = ', has_not_commented)

    if has_not_commented:
        text = generate_comment()
        submission.reply(text)

        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        pass

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []

        for comment in all_comments:
            for reply in comment.replies:
                comment_reply_author = []
                if reply.author == 'emelle_bot':
                    comment_reply_author.append(reply.author)
                if 'emelle_bot' in comment_reply_author:
                    pass
                else:
                    comments_without_replies.append(comment)
                    try:
                        comment.reply(generate_comment())
                    except praw.exceptions.RedditAPIException:
                        pass

        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        comment = random.choice(comments_without_replies)
        try:
            comment.reply(generate_comment())
        except praw.exceptions.APIException:
            print("not replying to a deleted comment.")
        except praw.exceptions.RedditAPIException:
            print("Hit the rate limit. Will sleep for 10 seconds before trying again.")
            time.sleep(1)
    
    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    submission = random.choice(list(reddit.subreddit("BotTown2").hot(limit=5)))
    print('submission=', submission)

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(1)