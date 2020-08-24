.PHONY: server
server:
	cd tele-vue-back && python -m star_wheel

.PHONY: front
front:
	cd tele-vue-front && npm run serve

.PHONY: test
test:
	cd tele-vue-back && python -m pytest
