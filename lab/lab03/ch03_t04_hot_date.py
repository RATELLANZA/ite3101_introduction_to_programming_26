from datetime import datetime

now = datetime.now()
print('%02d/%02d/%04y' % (now.month, now.day, now.year))
