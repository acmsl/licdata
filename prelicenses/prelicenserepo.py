import json
import datetime


from githubrepo import githubrepo


def findById(prelicenseId):
    repo = githubrepo.getRepo()
    branch = githubrepo.getBranch()
    prelicense = None
    try:
        file = repo.get_contents(f"prelicenses/{prelicenseId}/data.json", ref=branch)
    except:
        file = None
    if file:
        prelicense = json.loads(file.decoded_content.decode())
        prelicense["prelicenseEnd"] = datetime.datetime.strptime(
            license.get("prelicenseEnd", "1970/01/01"), "%Y/%m/%d"
        )
    return prelicense


def insert(name, clientId, product, productVersion):
    repo = githubrepo.getRepo()
    branch = githubrepo.getBranch()
    result = githubrepo.newId()

    now = datetime.datetime.now()
    orderDate = now.strftime("%Y/%m/%d")
    deliveryDate = orderDate
    prelicenseEnd = (now + datetime.timedelta(days=2)).strftime("%Y/%m/%d")
    item = {}
    item["id"] = result
    item["name"] = name
    item["clientId"] = clientId
    item["product"] = product
    item["productVersion"] = productVersion
    item["liberationCode"] = ""
    try:
        file = repo.get_contents("prelicenses/data.json", ref=branch)
    except:
        file = None
    if file is None:
        now = datetime.datetime.now()
        content = []
        content.append(item)
        repo.create_file(
            "prelicenses/data.json",
            "First prelicense",
            json.dumps(content),
            branch=branch,
        )
    else:
        content = json.loads(file.decoded_content.decode())
        content.append(item)
        repo.update_file(
            "prelicenses/data.json",
            "acmsl-licdata",
            json.dumps(content),
            file.sha,
            branch=branch,
        )

    item["orderDate"] = orderDate
    item["prelicenseEnd"] = prelicenseEnd
    repo.create_file(
        f"prelicenses/{result}/data.json",
        f"Created {result} prelicense",
        json.dumps(item),
        branch=branch,
    )
    return result


def findByNameProductAndProductVersion(name, productName, productVersion):
    repo = githubrepo.getRepo()
    branch = githubrepo.getBranch()
    prelicense = None
    try:
        allPrelicenses = repo.get_contents("prelicenses/data.json", ref=branch)
    except:
        allPrelicenses = None
    if allPrelicenses:
        prelicenses = json.loads(allPrelicenses.decoded_content.decode())
        prelicense = filterByProductAndProductVersion(
            prelicenses, product, productVersion, repo, branch
        )
        if prelicense and name in prelicense["name"]:
            return findById(prelicense["id"])
        else:
            print(f"No prelicense found with name {name}")
    else:
        print("No pcs found")

    return None
    try:
        file = repo.get_contents(f"prelicenses/data.json", ref=branch)
    except:
        file = None
    if file:
        prelicenses = json.loads(file.decoded_content.decode())
        prelicense["prelicenseEnd"] = datetime.datetime.strptime(
            prelicense.get("prelicenseEnd", "1970/01/01"), "%Y/%m/%d"
        )
    return prelicense
