'''
355. Design Twitter

Design a simplified version of Twitter.

Implement the Twitter class:

    Twitter()
        Initializes the object.

    void postTweet(int userId, int tweetId)
        User posts a new tweet.

    List<Integer> getNewsFeed(int userId)
        Returns the 10 most recent tweet IDs posted by the user and users they follow.

    void follow(int followerId, int followeeId)
        followerId starts following followeeId.

    void unfollow(int followerId, int followeeId)
        followerId stops following followeeId.

Example 1:
    Input:
        ["Twitter","postTweet","getNewsFeed","follow",
         "postTweet","getNewsFeed","unfollow","getNewsFeed"]

        [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]

    Output:
        [null,null,[5],null,null,[6,5],null,[5]]

Constraints:
    1 <= userId, followerId, followeeId <= 500
    0 <= tweetId <= 10^4
    At most 3 * 10^4 calls will be made.
'''

# Heap + HashMap Design

from typing import List
from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        self.following[userId].add(userId)

        for followee in self.following[userId]:
            tweets = self.tweets[followee]

            if tweets:
                index = len(tweets) - 1
                time, tweet = tweets[index]

                heapq.heappush(
                    heap,
                    (-time, tweet, followee, index - 1)
                )

        news_feed = []

        while heap and len(news_feed) < 10:
            _, tweet, followee, index = heapq.heappop(heap)
            news_feed.append(tweet)

            if index >= 0:
                time, tweet = self.tweets[followee][index]

                heapq.heappush(
                    heap,
                    (-time, tweet, followee, index - 1)
                )

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.following[followerId].discard(followeeId)


# Example usage
twitter = Twitter()

twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))
# Output: [5]

twitter.follow(1, 2)

twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))
# Output: [6,5]

twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))
# Output: [5]

twitter.postTweet(1, 7)
twitter.postTweet(2, 8)

twitter.follow(1, 2)
print(twitter.getNewsFeed(1))
# Output: [8,7,6,5]
