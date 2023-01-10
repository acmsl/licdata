import json

import githubrepo


def findById(clientId):
    return githubrepo.findById(clientId, "clients")


def findByEmail(email):
    return githubrepo.findByAttribute(email, "email", "clients")


def insert(email, address, contact, phone):
    item = {}
    item["email"] = email
    item["address"] = address
    item["contact"] = contact
    item["phone"] = phone
    return githubrepo.insert(
        item, "clients", ["email"], ["email", "address", "contact", "phone"]
    )


def update(id, email, address, contact, phone):
    item = {}
    item["id"] = id
    item["email"] = email
    item["address"] = address
    item["contact"] = contact
    item["phone"] = phone
    return githubrepo.update(
        item, "clients", ["email"], ["email", "address", "contact", "phone"]
    )


def delete(id):
    return githubrepo.delete(id, "clients")
