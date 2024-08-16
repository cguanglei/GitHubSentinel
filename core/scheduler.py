import schedule
import time

class Scheduler:
    def __init__(self, task, interval='daily'):
        self.task = task
        self.interval = interval
    
    def start(self):
        if self.interval == 'daily':
            schedule.every().day.at("10:00").do(self.task)
        elif self.interval == 'weekly':
            schedule.every().monday.at("10:00").do(self.task)
        
        while True:
            schedule.run_pending()
            time.sleep(1)
