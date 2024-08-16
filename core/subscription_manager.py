class SubscriptionManager:
    def __init__(self, db):
        self.db = db
    
    def add_subscription(self, user_id, repo_name):
        # 添加用户的订阅信息
        self.db.add_subscription(user_id, repo_name)
    
    def get_subscriptions(self, user_id):
        # 获取用户的订阅列表
        return self.db.get_subscriptions(user_id)
