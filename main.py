import os
from urlextract import URLExtract
extractor = URLExtract()
class nothadurlerror(Exception):
    pass
def openlink(link):
    if extractor.has_urls(link):
        os.system(f"start {link}")
        return "the link was opened successfully"
        exit(200)
    else:
        raise nothadurlerror("attribute not contains link")
        exit(400)
def startapp(app):
    os.system(f'start {app}')
    return 'the app was opened successfully'
    exit(200)
openlink('www.youtube.com')
startapp("calc.exe")

