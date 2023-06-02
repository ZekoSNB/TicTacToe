all:
clean:
	@find . -type f -name "*.pyc" -exec rm -f {} \;
	@find . -type d -name "__pycache__" -delete
	@find . -type d -name ".pytest_cache" -exec rm -rvf {} \;
	@find . -type d -name ".vscode" -exec rm -rvf {} \;

up:
	@find . -type f -name "*.pyc" -exec rm -f {} \;
	@find . -type d -name "__pycache__" -delete
	@find . -type d -name ".pytest_cache" -exec rm -rvf {} \;
	@find . -type d -name ".vscode" -exec rm -rvf {} \;
	@git add -A 
	@git commit -a -m "Updates"
	@git push

upco:
	@find . -type f -name "*.pyc" -exec rm -f {} \;
	@find . -type d -name "__pycache__" -delete
	@find . -type d -name ".pytest_cache" -exec rm -rvf {} \;
	@find . -type d -name ".vscode" -exec rm -rvf {} \;
	@git add -A 
	@read -p "Enter comment: " comment; \
	git commit -a -m "$$comment"
	@git push
run:
	@python run.py 
