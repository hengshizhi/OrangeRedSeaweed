# The content module of OrangeRedSeaweed is mainly used to handle website content
# Belongs to the official module of OrangeRedSeaweed
# Copyright 2023 Starweave
import fileApi.route as route
import fileApi.PathInfo as PathInfo

def AtRuntimeForTheFirstTime():
    ''' Functions that will be executed every time the program runs mod '''
    route.mkdir('./ContentTemplate')

def main():
    pass