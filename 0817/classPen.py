'''
Created on 2023. 8. 17.

@author: hbi
'''

class Pen:
    def __init__(self, length, color):
        self.length = length
        self.color = color
        
    def write(self, hours):
        self.length -= hours/10