import yaml as y
with open('myfile.yaml','r') as yaml_file:
	ouryaml = y.safe_load(yaml_file)
print(ouryaml)
print(f"Token d'accès : {ouryaml['access_token']}")
print(f"Validité en secondes : {ouryaml['expires_in']}")
print(f"Token refresh : {ouryaml['access_token']}")
print(f"Validité du token refresh en secondes : {ouryaml['expires_in']}")
