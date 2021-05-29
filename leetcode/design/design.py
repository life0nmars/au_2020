155. Min Stack
https://leetcode.com/problems/min-stack/
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        
    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
      
      
232. Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        return self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.stack == []:
            return True
        else:
            return False

          
225. Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/
class MyStack:

    def __init__(self):
    """
    Initialize your data structure here.
    """
        self.stack=[]
    

    def push(self, x):
    """
    Push element x onto stack.
    :type x: int
    :rtype: None
    """
        self.stack.append(x)

    def pop(self):
    """
    Removes the element on top of the stack and returns that element.
    :rtype: int
    """
        return self.stack.pop(-1)

    def top(self):
    """
    Get the top element.
    :rtype: int
    """
        return self.stack[-1]

    def empty(self):
    """
    Returns whether the stack is empty.
    :rtype: bool
    """
        return len(self.stack)==0
        
      
355. Design Twitter
https://leetcode.com/problems/design-twitter/
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        self.global_tweets = []

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if self.users.get(userId) == None:
            self.users[userId] = {"tweets" : [tweetId], "followers":[]}
        else:
            self.users[userId]["tweets"].insert(0, tweetId)
        self.global_tweets.insert(0,tweetId)
        # print(self.users[userId])
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        
        user = self.users.get(userId)
        if user != None:

            feed = []
            for i in user["tweets"]:
                feed.append(i)
            for i in user["followers"]:
                if self.users.get(i)!=None:
                    for j in self.users[i]["tweets"]:
                        feed.append(j)
            ans = []    
            for i in self.global_tweets:
                if i in feed:
                    ans.append(i)
            return ans[:10]
        else:
            return []
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if self.users.get(followerId) == None:
            self.users[followerId] = {"tweets" : [], "followers":[followeeId]}
        else:
            self.users[followerId]["followers"].append(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if self.users.get(followerId) == None:
            self.users[followerId] = {"tweets" : [], "followers":[]}
        else:
            if followeeId in self.users[followerId]["followers"]:
                self.users[followerId]["followers"].remove(followeeId)
            else:
                pass      
