'''
Created on 09.05.2016

@author: mkennert
'''
from kivy.uix.gridlayout import GridLayout

from crossSectionView.doubleTView import DoubleTView
from shapes.ashape import AShape


class ShapeDoubleT(GridLayout, AShape):
    # Constructor

    def __init__(self, **kwargs):
        super(ShapeDoubleT, self).__init__(**kwargs)
        self.cols = 2
        # toparea
        self.tw = 0.3
        self.th = 0.2
        # middlearea
        self.mw = 0.1
        self.mh = 0.25
        # bottomarea
        self.bw = 0.3
        self.bh = 0.2
        self.concreteDensity = 2300.
        self.concretePrice = 0.065
        self.concreteStiffness = 30000.
        self.concreteStrength = 3.
        self.view = DoubleTView()
        self.view.set_cross_section(self)

    '''
    return the top-width
    '''

    def get_width_top(self):
        return self.tw

    '''
    set the top-width
    '''

    def set_width_top(self, value):
        self.tw = value
        self.view.update()

    '''
    return the top-height
    '''

    def get_height_top(self):
        return self.th

    '''
    set the top-height
    '''

    def set_height_top(self, value):
        self.th = value
        self.view.update()

    '''
    set the middle-width
    '''

    def set_width_middle(self, value):
        self.mw = value
        self.view.update()
    '''
    return the middle-width
    '''

    def get_width_middle(self):
        return self.mw

    '''
    return the middle-height
    '''

    def get_height_middle(self):
        return self.mh

    '''
    set the middle-height
    '''

    def set_height_middle(self, value):
        self.mh = value
        self.view.update()

    '''
    set the bottom-height
    '''

    def set_height_bottom(self, value):
        self.bh = value
        self.view.update()

    '''
    return the bottom-height
    '''

    def get_height_bottom(self):
        return self.bh

    '''
    set the bottom-width
    '''

    def set_width_bottom(self, value):
        self.bw = value
        self.view.update()

    '''
    return the bottom-width
    '''

    def get_width_bottom(self):
        return self.bw

    '''
    return the cs-height
    '''

    def get_height(self):
        return self.th + self.bh + self.mh

    '''
    return the max-width
    '''

    def get_width(self):
        wmax = self.tw
        if wmax < self.mw:
            wmax = self.mw
        if wmax < self.bw:
            wmax = self.bw
        return wmax

    '''
    set the cs-information
    '''

    def set_information(self, information):
        self.information = information


    '''
    update the cross section information in the cs-information
    '''

    def set_cross_section_information(self):
        self.information.update_cross_section_information(
            self.price, self.weight, self.strength)


    '''
    calculate the weight and price
    '''
    #not finished yet
    def calculate_weight_price(self):
        weight = 0.
        price = 0.
        # go trough all layers and get the weight of them
        for l in self.view.layers:
            cur = l.get_weight()
            weight += cur
            price += cur * l.material.price
        # if the percentOfLayers is not 1 there is a matrix
        # with concrete as material
        
        self.weight = weight
        self.price = price

    '''
    calculate the strength of the cross section
    '''

    def calculate_strength(self):
        self.strength = 0.
        '''
        strength = 0.
        # cur supremum
        self.minOfMaxstrain = 1e10
        # max strain is necessary for other calculations
        self.maxOfMaxstrain = 0
        # find the minimum max_strain and the maximum max_strain
        for l in self.view.layers:
            curStrain = l.getStrain()
            # proof whether the curStrain is smaller as the min
            if curStrain < self.minOfMaxstrain:
                self.minOfMaxstrain = curStrain
            # proof whether the curStrain is bigger as the max
            if curStrain > self.maxOfMaxstrain:
                self.maxOfMaxstrain = curStrain
        # if the percentOfLayers is not 1 there is a matrix
        # with concrete as material
        freePlaces = self.view.getFreePlaces()
        if len(freePlaces) > 0:
            curValue = self.concreteStrength / self.concreteStiffness
            if self.minOfMaxstrain > curValue:
                self.minOfMaxstrain = curValue
            if self.maxOfMaxstrain < curValue:
                self.maxOfMaxstrain = curValue
        # calculate the strength
        csSize = self.th * self.tw + self.mw * self.mh + self.bh * self.bw
        for l in self.view.layers:
            strength += self.minOfMaxstrain * \
                l.material.stiffness * l.getSize() / csSize
        freePlacesSize = 0.
        for i in freePlaces:
            freePlacesSize += (i[1] - i[0]) * i[2]
        strength += self.minOfMaxstrain * \
            freePlacesSize / csSize * self.concreteStiffness
        self.strength = strength
        '''