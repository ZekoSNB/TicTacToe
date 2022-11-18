all:
clean:
	find . -type f -name "*.pyc" -exec rm -f {} \;
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -exec rm -rvf {} \;
	find . -type d -name ".vscode" -exec rm -rvf {} \;

up:
	git add -A 
	git commit -a -m "Updates"
	git push