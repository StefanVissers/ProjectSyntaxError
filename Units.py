__author__ = 'Michel'
import pygame

class player(object):

    def __init__(self, name, color):
        self.name = name
        self.color = color

        self.Mill = {'price':10, 'num':0, 'desc':"Collects 5 FOOD every turn with bonus."}
        self.Quarry = {'price':15, 'num':0, 'desc':"Collects 5 GOLD every turn with bonus."}
        self.LumberYard = {'price':15, 'num':1, 'desc':"Collects 5 WOOD every turn with bonus."}
        self.factory = {'price':50, 'num':0, 'desc':"Collects 20 of EVERY resource each turn NO BONUS."}
        self.Wonder = {'price':1000, 'num':0, 'desc':"Wins you the game."}

        self.spy = {'price':15, 'num':0, 'desc':"Lets you see opponent's resources, buildings, and advances."}
        self.raider = {'price':25, 'num':0, 'desc':"Destroys one of the most common building in enemy's base"}
        self.thief = {'price':20, 'num':0, 'desc':"Steals 5 of an opponents resource of your choice"}

        #self.sharperaxes = {'price':2, 'level':1, 'desc':"}        Dictionaries for advances. to add. too lazy.

        self.gold = {'num': 5, 'desc':"Used to research new advances for faster resource collection."}
        self.wood = {'num': 5, 'desc':"Used to build buildings."}
        self.food = {'num': 5, 'desc':"Used to train units."}

        #self.rescources = {'GOLD':5, 'WOOD':10, 'FOOD':5}
        self.resources = {'GOLD':self.gold, 'WOOD':self.wood, 'FOOD':self.food}
        self.buildings = {'MILL':self.Mill, 'QUARRY':self.Quarry, 'LUMBER YARD':self.LumberYard, 'FACTORY':self.factory, 'WONDER':self.Wonder}
        self.advances = {'SHARPER AXES':1, 'CROP ROTATION':1, 'SHARPER PICKS':1}
        self.units = {'SPY': self.spy, 'RAIDER':self.raider, 'THIEF':self.thief}

class soldier():
    cost = 150

    atk_value = 1
    def_value = 1
    move_value = 1
    atk_range = 1

class robot():
    cost = 300
    atk_value = 2
    def_value = 2
    move_value = 1
    atk_range = 1

class tank():
    cost = 750
    atk_value = 2
    def_value = 2
    move_value = 1
    atk_range = 2

class boat():
    cost = 1000
    atk_value = 0
    def_value = 0
    move_value = 2
    #loadUnit = 1
    #maxUnits = 3
