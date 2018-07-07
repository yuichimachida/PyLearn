import os, sys
import configparser

config = configparser.ConfigParser()
config.read('./config.ini', 'UTF-8')
print(config.get('RSS','RSS'))
print(config.get('SavePath','Path'))

basePath = config.get('SavePath','Path')
os.mkdir(basePath + r'/testfolder')
