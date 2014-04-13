import sys

T = int(sys.stdin.readline())

FARM_COST = 0
RATE_GAIN = 1
END_GOAL = 2

for case in range(1, T + 1):
	farms, cookies, seconds = 0, 0.0, 0.0
	nums = [float(x) for x in sys.stdin.readline().split(' ')]

	while (cookies < nums[END_GOAL]):
		# Current Rate
		rate = 2 + (nums[RATE_GAIN] * farms)
		# No. of seconds to goal on current rate
		seconds_left_current_rate = (nums[END_GOAL] - cookies) / rate
		# No. of seconds to farm cost on current rate
		time_to_farm = (nums[FARM_COST] - cookies) / rate
		# Temp rate assuming farm purchased
		temp_rate = 2 + (nums[RATE_GAIN] * (farms+1))
		# Temp number of cookies after farm purchase
		temp_cookies = (cookies + (time_to_farm * rate)) - nums[FARM_COST]
		# No. of seconds to goal with extra farm
		seconds_left_extra_farm_rate = (nums[END_GOAL] - temp_cookies) / temp_rate

		if (time_to_farm + seconds_left_extra_farm_rate < seconds_left_current_rate):
			# Travel seconds until farm affordable and purchase farm
			seconds += time_to_farm
			cookies += (time_to_farm * rate) - nums[FARM_COST]
			farms += 1
		else:
			# Travel remaining seconds until goal reached
			seconds += seconds_left_current_rate
			cookies += seconds_left_current_rate * rate
	sys.stdout.write('Case #%d: %.7f\n' % (case, seconds))

