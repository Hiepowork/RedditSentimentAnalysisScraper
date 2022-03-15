import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def getUrls(html, className, scrollLength):
    driver = webdriver.Chrome()
    driver.get(html)
    time.sleep(2)
    scroll_pause_time = 1
    screen_height = driver.execute_script("return window.screen.height;")
    i = 0
    while True:
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
        i += 1
        time.sleep(scroll_pause_time)
        #scroll_height = driver.execute_script("return document.body.scrollHeight;")
        if i >= scrollLength:
            break
    url = driver.page_source
    soup = BeautifulSoup(url, "html.parser")
    information = soup.findAll(class_=className)
    urls = []
    for info in information:
        link = "http://www.reddit.com" + info['href']
        urls.append(link)
    return urls


def getComments(urls, className):
    comments = []
    for url in urls:
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(2)
        scroll_pause_time = 1
        pageSource = driver.page_source
        soup = BeautifulSoup(pageSource, "html.parser")
        information = soup.findAll(class_= className)
        for info in information:
            comment = str(info.get_text())
            https = "https"
            if not len(comment) < 100 and not https in comment:
                comments.append(comment)
        comments.append("##############################################################################################")
    return comments

def writeFile(fileName, comments):
    File_object = open(fileName, "w+")
    for comment in comments:
        try:
            File_object.write(comment + "\n\n")
        except:
            print("Poopoo character alert")
            print(comment)

#Gets the urls of all the different posts
#politics = getUrls('https://www.reddit.com/r/politics/hot','SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE' )
#wholesome = getUrls('https://www.reddit.com/r/wholesome/', 'SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE')


#Gets comments
#politicsComments = getComments(poopsie, '_1qeIAgB0cPwnLhDF9XSiJM')
#wholesomeComments = getComments(oopsie, '_1qeIAgB0cPwnLhDF9XSiJM')

#Writes comments to file
#writeFile("politicalComments.txt", politicsComments)
#writeFile("wholesomeComments.txt", wholesomeComments)

def program():
    link = input("Enter link of subreddit: ")
    fileName = input("Enter file name: ")
    scrollLength = int(input("Enter number of scrolls: "))
    urls = getUrls(link, 'SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE', scrollLength)
    comments = getComments(urls, '_1qeIAgB0cPwnLhDF9XSiJM')
    writeFile(fileName, comments)

def runMultiple():
    runners = []
    while True:
        link = input("Enter link of subreddit: ")
        fileName = input("Enter file name: ")
        scrollLength = int(input("Enter number of scrolls: "))
        adder = [link, fileName, scrollLength]
        runners.append(adder)
        endLoop = input("Press enter to finish or press any other key to keep going: ")
        if (endLoop == ""):
            break
    for runner in runners:
        urls = getUrls(runner[0], 'SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE', runner[2])
        comments = getComments(urls, '_1qeIAgB0cPwnLhDF9XSiJM')
        writeFile(runner[1], comments)

runMultiple()