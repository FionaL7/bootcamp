.PHONY: run build-docker run-docker clean build-package publish-package

run:
	python main.py --watch

build-docker:
	docker build -t file-pipeline .

run-docker:
	docker run -p 8000:8000 -v "$(pwd)/watch_dir:/app/watch_dir" file-pipeline

clean:
	rm -rf __pycache__ *.pyc

build-package:
	python setup.py sdist bdist_wheel

publish-package:
	twine upload dist/*
