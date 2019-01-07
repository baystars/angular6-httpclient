BASE_HREF = "/ng/"`basename $(PWD)`"/"
OUTPUT_PATH = /var/www${BASE_HREF}

run: serve-network

serve:
	ng serve --live-reload true

serve-open:
	ng serve --open

serve-network:
	ng serve --host 192.168.1.1 --port 4200 --live-reload true

build-prod:
	ng build --prod --output-path=${OUTPUT_PATH} --base-href=${BASE_HREF}

open:
	chromium-browser http://localhost${BASE_HREF}

install:
	npm i

clean:
	rm -fr node_modules

add:
	git add .

commit: add
	git commit -m 'modify'

push: commit
	git push -u origin master
