import yaml as y
with open('person.yml','r') as yaml_file:
        ouryaml = y.safe_load(yaml_file)
print(ouryaml)
print(f"Nom : {ouryaml['nom']}")
print(f"Loisirs : {ouryaml['loisirs']}")
