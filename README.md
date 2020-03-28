# BBB-Voter
Automatic voter for Big Brother Brasil.

# Getting Started

## Requirements
* Python
* Any Browser (See configurations)

## Usage
* Set the `config.json` file and run `py voter.py`.

Since its using Selenium, it requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

Failure to observe this step will give you an error selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH.

Other supported browsers will have their own drivers available. Links to some of the more popular browser drivers follow.
Chrome: 	https://sites.google.com/a/chromium.org/chromedriver/downloads
Edge: 	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Firefox: 	https://github.com/mozilla/geckodriver/releases
Safari: 	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

Example:

    open a new Firefox browser
    load the page at the given URL

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://seleniumhq.org/')



### Configuration:
* pollURL = url where the poll is located
* targetPosition = the order of the target. For example, if one is the 2nd on the list, this attribute should be 2.
* credentials = The Globo credentials to login.
* webDriverPath = the path to the browser webdriver. If you want to use another browser, change line .
