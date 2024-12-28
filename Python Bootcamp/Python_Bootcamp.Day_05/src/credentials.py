import json
from wsgiref.simple_server import make_server
from urllib.parse import parse_qs, unquote

species_to_leader = {
    "Cyberman": "John Lumic",
    "Dalek": "Davros",
    "Judoon": "Shadow Proclamation Convention 15 Enforcer",
    "Human": "Leonardo da Vinci",
    "Ood": "Klineman Halpen",
    "Silence": "Tasha Lem",
    "Slitheen": "Coca-Cola salesman",
    "Sontaran": "General Staal",
    "Time Lord": "Rassilon",
    "Weeping Angel": "The Division Representative",
    "Zygon": "Broton"
}


def application(environ, start_response):
    query_string = environ.get('QUERY_STRING', '')
    params = parse_qs(query_string)

    species = params.get('species', [''])[0]
    species = unquote(species)

    if species in species_to_leader:
        credentials = species_to_leader[species]
        status = '200 OK'
    else:
        credentials = "Unknown"
        status = '404 Not Found'

    response_body = json.dumps({"credentials": credentials})

    headers = [
        ('Content-Type', 'application/json'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, headers)
    return [response_body.encode('utf-8')]


if __name__ == "__main__":
    with make_server('127.0.0.1', 8888, application) as httpd:
        print("Serving on port 8888...")
        httpd.serve_forever()
