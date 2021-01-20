install:
	pip install -r packages.txt

start:
	python app.py

test:
	pytest ./tests/test_config.py

# publish:
# 	npm publish
