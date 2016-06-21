'''
Created on 14.04.2016

@author: mkennert
'''


class Layer:
    # Constructor
    def __init__(self, x, y, h, w):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        
    '''
    the method set_height change the height of the small_keyboard-rectangle
    '''
    def set_height(self, value):
        self.h = value

    '''
    return the weight of the layer
    '''

    def get_weight(self):
        v = self.h * self.w
        w = self.material.density * v
        return w
    
    '''
    set the material
    '''
    def set_Material(self,material):
        self.material=material
    
    '''
    return the strain of the layer
    '''

    def get_strain(self):
        return self.material.strength / self.material.stiffness