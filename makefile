install:
	pip install -r requirements.txt

start:
	python ./app/app.py

test:
	pytest ./tests/test_config.py

# publish:
# 	python publish.py
