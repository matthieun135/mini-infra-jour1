import yaml, json, os

DESIRED_FILE = "ressources.yml"
STATE_FILE = "state.json"

def load_desired():
    with open(DESIRED_FILE) as f:
        return yaml.safe_load(f)["resources"]

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return []

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def apply():
    desired = load_desired()
    state = load_state()
    existing_names = {r["name"] for r in state}
    changed = False

    for res in desired:
        if res["name"] not in existing_names:
            print(f"+ creer {res['type']} '{res['name']}'")
            state.append(res)
            changed = True
        else:
            print(f"= {res['type']} '{res['name']}' deja conforme")

    if changed:
        save_state(state)
        print("Etat sauvegarde dans", STATE_FILE)
    else:
        print("Aucun changement necessaire.")

if __name__ == "__main__":
    apply()
