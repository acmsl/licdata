import sys

sys.path.insert(0, "infrastructure/aws_lambda")
sys.path.insert(0, "infrastructure/github")

from githubclientrepo import GithubClientRepo
import rest
import params


def retrievePk(body, event):
    return [ params.retrieveEmail(body, event) ]


def retrieveAttributes(body, event):
    return rest.retrieveAttributesFromParams(body, event, GithubClientRepo().attributes())
