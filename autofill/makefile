help: 
	@echo "Commands:"
	@echo " - help: 	show this help"
	@echo " - new:		create a new file for today"
	@echo " - readme: 	build the new readme with links"
	@echo " - setup:	init the session file"

setup: 
	@touch session.cookie
	@make help

new: 
	@python src/utils/new_file.py

readme:
	@python src/utils/build_md.py