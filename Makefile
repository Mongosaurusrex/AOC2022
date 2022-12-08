MAKEFLAGS += --silent

run: day_one day_two day_three day_four day_five day_six day_seven day_eight
	cat tree.txt
day_one:
	python3 ./1/main.py
day_two:
	python3 ./2/main.py
day_three:
	python3 ./3/main.py
day_four:
	python3 ./4/main.py
day_five:
	python3 ./5/main.py
day_six:
	python3 ./6/main.py
day_seven:
	python3 ./7/main.py
day_eight:
	python3 ./8/main.py
