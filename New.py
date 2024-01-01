import subprocess
import datetime
from random import randint
from itertools import count

my_num = 0
counter = count(1, 3)
command = r'git commit -am "" --date "4/20/2024"'
start_date = datetime.date(year=2023, month=12, day=31)
for x in range(2):
    my_num += 1
    start_date += datetime.timedelta(days=1)
    for y in range(randint(6, 10)):
        command = rf'git commit -am "test_change {hex(my_num)}{oct(x + y + next(counter))}" --date "{start_date.strftime('%m/%d/%Y')}"'
        subprocess.run(command)
