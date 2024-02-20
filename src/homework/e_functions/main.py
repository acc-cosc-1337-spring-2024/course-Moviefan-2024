## main_program.py

import value_return


epoch_seconds = 3800
hour = value_return.get_hour(epoch_seconds)
minutes = value_return.get_minutes(epoch_seconds)
seconds = value_return.get_seconds(epoch_seconds)
print(f"The time is: {hour:02d}:{minutes:02d}:{seconds:02d}")


