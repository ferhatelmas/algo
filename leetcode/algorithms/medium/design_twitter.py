from collections import defaultdict


class Twitter(object):
    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.t = 0

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((self.t, tweetId))
        self.t += 1

    def getNewsFeed(self, userId):
        tweets = sorted(
            [f for i in set([userId]) | self.followers[userId] for f in self.tweets[i]],
            reverse=True,
        )[:10]
        return [t[1] for t in tweets]

    def follow(self, followerId, followeeId):
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        s = self.followers[followerId]
        if followeeId in s:
            s.remove(followeeId)
