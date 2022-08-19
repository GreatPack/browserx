import os
from urlextract import URLExtract
extractor = URLExtract()
class NoUrlsFound(Exception):
    pass
class ApplicationNotFound(Exception):
    pass
def openlink(link):
    if extractor.has_urls(link):
        os.system(f"start {link}")
    else:
        raise NoUrlsFound(f"{link} is not a URL.")
def startapp(app):
    if ".exe" in app:
        os.system(f'start {app}')
    else:
        raise ApplicationNotFound(f"{app} is not a application.\nMaybe you want to open {app}.exe?.")

