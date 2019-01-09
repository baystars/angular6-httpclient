all: serve-network

serve:
	json-server data/data.json

serve-network:
	json-server --host 0.0.0.0 data/data.json

run-flask:
	env FLASK_ENV=development python app.py
