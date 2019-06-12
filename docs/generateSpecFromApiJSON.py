import json

with open("./api.spec.json") as f:
    spec = json.load(f)

out = {"routes": []}
for path in spec["paths"]:
    p = spec["paths"][path]

    temp = {}
    op = "GET"
    if "get" in p:
        op = "GET"
    
    if "post" in p:
        op = "POST"
    if "patch" in p:
        op = "PATCH"
    if "DELETE" in p:
        op = "DELETE"
    
    temp["method"] = op
    temp["name"] = p[op.lower()]["sdkName"]
    temp["description"] = p[op.lower()]["summary"]
    temp["path"] = path
    link = path.replace("/", "~1")
    temp["link"] = f"https://iotery.io/docs/embedded/#tag/Embedded/paths/{link}/{op}"


    out["routes"].append(temp)

with open("./api.out.json", "w") as f:
    json.dump(out, f)