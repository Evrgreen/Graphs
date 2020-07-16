from random import randint
from collections import deque


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def shuffle(self, list):
        for index in range(0, len(list)):
            random_index = randint(index, len(list)-1)
            list[random_index], list[index] = list[index], list[random_index]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(num_users):
            self.add_user(user)
        # Create friendships
        friendships = []
        for user in range(1, self.last_id+1):
            for friend in range(user+1, num_users+1):
                friendships.append((user, friend))

        self.shuffle(friendships)

        total_friendships = num_users * avg_friendships
        random_friendships = friendships[:total_friendships//2]

        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        work_stack = deque()
        visited = {}
        # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        visited[user_id] = [user_id]
        work_stack.append([user_id])
        while len(work_stack) > 0:
            current_friendship = work_stack.popleft()
            current_user = current_friendship[-1]
            friends = {
                user for user in self.friendships[current_user] if user is not user_id and user not in visited}
            for friend in friends:
                visited[friend] = [*current_friendship, friend]
                work_stack.append(visited[friend])

        return visited

    def __str__(self):
        return f'Users: {self.users} and Friendships {self.friendships}'


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
