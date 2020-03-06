test: bootstrap
	molecule test --all

test-%: bootstrap
	molecule test -s "$*"

lint: bootstrap
	molecule lint

bootstrap:
	$(eval PIP := $(shell which pip))
	$(if $(PIP),,$(eval PIP := $(shell which pip3)))
	$(if $(PIP),,$(error No pip or pip3 found in PATH))

	$(PIP) install -r requirements.txt

new-version:
	$(if $(shell which npx),,\
		$(error No npx not found in PATH, please install NodeJS))
	$(if $(shell which standard-version),,\
		$(error No standard-version not found in PATH, install with: \
			npm install -g standard-version))

	npx standard-version --tag-prefix=''
