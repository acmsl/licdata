def findPcId(licenseId, installationCode, repo, branch):
    try:
        allPcs = repo.get_contents("pcs.json", ref=branch)
    except:
        allPcs = None
    if allPcs:
        allPcsContent = json.loads(allPcs.decoded_content.decode())
        pcs = [x for x in allPcsContent if x["licenseId"] == licenseId]
        if pcs:
            for pc in pcs:
                pcId = pc["id"]
                try:
                    pcFile = repo.get_contents(f"pcs/{pcId}/data.json", ref=branch)
                except:
                    pcFile = None
                if pcFile:
                    pcContent = json.loads(pcFile.decoded_content.decode())
                    if pcContent["installationCode"] == installationCode:
                        return pcId
                else:
                    print(f"No pc file found at pcs/{pcId}/data.json")
        else:
            print(f"No pc found for license {licenseId}")

    return None
