from crontab import CronTab
# cron = CronTab(user='root')
with CronTab(user='root') as cron:
    job = cron.new(command='echo hello_world')
    job.minute.every(1)
print('cron.write() was just executed')
# job = cron.new(command='python data.py')
# job.hour.every(24)
# job.minute.every(5)
cron.write()