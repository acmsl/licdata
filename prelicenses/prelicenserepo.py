import githubrepo


def findById(id):
    return githubrepo.findById(id, "prelicenses")


def findByNameProductAndProductVersion(name, productName, productVersion):
    filter = {}
    filter["name"] = name
    filter["product"] = product
    filter["productVersion"] = productVersion
    return githubrepo.findAllByAttributes(filter, "prelicenses")


def insert(name, clientId, product, productVersion):
    item = {}
    item["name"] = name
    item["clientId"] = clientId
    item["product"] = product
    item["productVersion"] = productVersion
    return githubrepo.insert(
        item,
        "prelicenses",
        ["name"],
        ["name", "clientId", "product", "productVersion"],
    )


def update(id, name, clientId, product, productVersion, liberationCode):
    item = {}
    item["id"] = id
    item["name"] = name
    item["clientId"] = clientId
    item["product"] = product
    item["productVersion"] = productVersion
    item["liberationCode"] = liberationCode

    return githubrepo.update(
        item,
        "prelicenses",
        ["name"],
        ["name", "clientId", "product", "productVersion", "liberationCode"],
    )


def delete(id):
    return githubrepo.delete(id, "prelicenses")
