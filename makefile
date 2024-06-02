test:
	python test.py



run:
	source .venv/bin/activate && python main.py


web:
	cd todolistweb && yarn dev
# source .venv/bin/activate


git:
	git add .
	git commit -m "this commit"
	git push