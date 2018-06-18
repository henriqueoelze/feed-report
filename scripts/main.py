from selenium import webdriver
import configparser

import readFeed
import takeFullPageScreenshot
import exportCsv
import configparser

def main():
    extractFeed()

def extractFeed():
    config = loadConfig()
    url = config['url']

    items = readFeed.execute(url)
    print('Found {} items!'.format(len(items)))

    print("Set up web driver ...")
    driver = setupDriver()

    relatorio = []
    counter = int(config['counterValue'])
    for  index, item in enumerate(items):
        print("Processing {} --> {}...".format((index + 1), item['title']))
        counterValue = str(counter).zfill(4)

        relatorio.append(extractValues(item, counterValue))

        fileNamePattern = config['fileNamePattern']
        takeFullPageScreenshot.execute(driver, item['link'], fileNamePattern.format(counterValue))
        counter = counter + 1

    csvName = config['csvName']
    exportCsv.execute(relatorio, csvName)
    print("\nQuitting web driver ...")
    driver.quit()

def loadConfig():
     config = configparser.ConfigParser()
     config.read('config.ini')

     return config['DEFAULT']

def setupDriver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def extractValues(item, counter):
    returnValue = {}
    returnValue['id'] = counter
    returnValue['title'] = item['title']
    returnValue['date'] = item['published']
    returnValue['link'] = item['link']
    returnValue['type'] = 'noticia'

    return returnValue


if __name__ == "__main__": main()
