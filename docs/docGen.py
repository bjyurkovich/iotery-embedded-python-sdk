import json


def get_params(path):
    """Extracts params from a given route path"""
    split_route = path.split("/")
    params = []
    for s in split_route:
        if len(s) > 0 and s[0] == ":":
            params.append(s[1:])
    return params


with open("iotery_embedded_python_sdk/api.json", "r") as f:
    spec = json.load(f)

    gets = []
    posts = []
    patches = []
    deletes = []

    for route in spec["routes"]:
        if route["method"] == "GET":
            gets.append(route)
        if route["method"] == "POST":
            posts.append(route)
        if route["method"] == "PATCH":
            patches.append(route)
        if route["method"] == "DELETE":
            deletes.append(route)

    headers = """|    `methodName`    | `input` | link |  `description`
|:-----------:|:-----------:|:-----------:|:-----------:|"""
    with open("./docs/template.md", "r") as r:
        template = r.read()
        gs = [headers]
        pos = [headers]
        pas = [headers]
        ds = [headers]

        for g in gets:
            params = "`,`".join(get_params(g["path"]))
            gs.append(
                f'| {g["name"]} | `{params}` | [link]({g["link"]}) | {g["description"]} |')

        for po in posts:
            params = "`,`".join(get_params(po["path"]))
            pos.append(
                f'| {po["name"]} | `{params}` | [link]({po["link"]}) | {po["description"]} |')

        for pa in patches:
            params = "`,`".join(get_params(g["path"]))
            pas.append(
                f'| {pa["name"]} | `{params}` | [link]({pa["link"]}) | {pa["description"]} |')

        for d in deletes:
            params = "`,`".join(get_params(d["path"]))
            ds.append(
                f'| {d["name"]} | `{params}` | [link]({d["link"]}) | {d["description"]} |')

        template = template.replace("[[GETS]]",  "\n".join(gs))
        template = template.replace("[[POSTS]]",  "\n".join(pos))
        template = template.replace("[[PATCHES]]",  "\n".join(pas))
        template = template.replace("[[DELETES]]",  "\n".join(ds))

        with open("iotery_embedded_python_sdk/README.md", "w") as w:
            w.write(template)
            print("Generated.")
