import time
import threading
from datetime import datetime, timedelta
from utils.logger import logger

class ScheduleManager:
    """Handles recurring tasks for file organization."""
    
    def __init__(self):
        self.jobs = []
        self._stop_event = threading.Event()
        self._thread = None

    def add_daily_job(self, task_fn, hour=2, minute=0):
        """Schedules a task to run daily at a specific time."""
        self.jobs.append({
            "fn": task_fn,
            "type": "daily",
            "hour": hour,
            "minute": minute,
            "last_run": None
        })
        logger.info(f"Scheduled daily job at {hour:02d}:{minute:02d}")

    def start(self):
        """Starts the scheduler in a background thread."""
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()
        logger.info("Scheduler started.")

    def stop(self):
        """Stops the scheduler."""
        self._stop_event.set()
        if self._thread:
            self._thread.join()

    def _run_loop(self):
        """Internal loop to check and execute scheduled jobs."""
        while not self._stop_event.is_set():
            now = datetime.now()
            for job in self.jobs:
                if self._should_run(job, now):
                    try:
                        logger.info(f"Executing scheduled job: {job['type']}")
                        job['fn']()
                        job['last_run'] = now.date()
                    except Exception as e:
                        logger.error(f"Error in scheduled job: {e}")
            
            # Check every minute
            time.sleep(60)

    def _should_run(self, job, now):
        """Checks if a job is due for execution."""
        if job["type"] == "daily":
            if now.hour == job["hour"] and now.minute == job["minute"]:
                if job["last_run"] != now.date():
                    return True
        return False

if __name__ == "__main__":
    def my_task(): print("Task executed!")
    sm = ScheduleManager()
    sm.add_daily_job(my_task, now=True) # Modified for test
    sm.start()
    time.sleep(5)
    sm.stop()
