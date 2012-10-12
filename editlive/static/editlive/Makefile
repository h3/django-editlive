BOOTSTRAP = ./css/editlive.css
BOOTSTRAP_LESS = ./less/base.less
DATE=$(shell date +%I:%M%p)
CHECK=\033[32m✔\033[39m


#
# BUILD DOCS
#

build:
	@echo "Building Bootstrap..."
	@recess --compile ${BOOTSTRAP_LESS} > ${BOOTSTRAP}
	@echo "Compiling LESS with Recess...               ${CHECK} Done"
	@echo "Bootstrap successfully built at ${DATE}."

#
# BUILD SIMPLE BOOTSTRAP DIRECTORY
# recess & uglifyjs are required
#

bootstrap:
	mkdir -p css
	recess --compile ${BOOTSTRAP_LESS} > css/editlive.css
	recess --compress ${BOOTSTRAP_LESS} > css/editlive.min.css

#
# WATCH LESS FILES
#

watch:
	echo "Watching less files..."; \
	watchr -e "watch('less/.*\.less') { system 'make' }"



.PHONY: watch
