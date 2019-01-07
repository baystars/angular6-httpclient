run-backend:
	cd "$(PWD)/backend" && make serve-network

run-frontend:
	cd "$(PWD)/frontend" && make serve-network

install:
	cd "$(PWD)/frontend" && make install

clean:
	cd "$(PWD)/frontend" && make clean

add:
	git add .

commit: add
	git commit -m 'modify'

push: commit
	git push -u origin master
