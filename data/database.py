class Database:
    def __init__(self):
        self.subscriptions = {}
        self.updates = {}
    
    def add_subscription(self, user_id, repo_name):
        if user_id not in self.subscriptions:
            self.subscriptions[user_id] = []
        self.subscriptions[user_id].append(repo_name)
    
    def get_subscriptions(self, user_id):
        return self.subscriptions.get(user_id, [])
    
    def add_update(self, repo_name, update):
        if repo_name not in self.updates:
            self.updates[repo_name] = []
        self.updates[repo_name].append(update)
