import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

class AdjacencyMatrix:
    def __init__(self,point_node_number,maximum_distance):

        self.adjacency_matrix =np.zeros((point_node_number,point_node_number))
        self.maximum_distance = maximum_distance
        self.nodes_number = point_node_number
        self.depot = 0
        self.time_table = {}
        for i in range(0,point_node_number):
           for j in range(0,point_node_number): 
                if i==j:
                    continue
                elif self.adjacency_matrix[i][j] !=self.adjacency_matrix[j][i] :

                    if self.adjacency_matrix[i][j]==0:
                        self.adjacency_matrix[i][j]=self.adjacency_matrix[j][i]
                    elif self.adjacency_matrix[j][i] == 0:
                        self.adjacency_matrix[j][i]=self.adjacency_matrix[i][j]
                    continue
                else:
                    self.adjacency_matrix[i][j] = np.random.randint(1,maximum_distance)
        
        
    def getNodeNumber(self):
        return self.nodes_number 

    def getMaxdistance(self):
        return self.maximum_distance 

    def getAdjacencyMatrix(self):
        return self.adjacency_matrix

class VRPDataset:
    def __init__(self,Adjacency_matrix):
        self.Adjacency_matrix = Adjacency_matrix
        self.adjacency_matrix = self.Adjacency_matrix.getAdjacencyMatrix()
        self.nodes_number = self.Adjacency_matrix.getNodeNumber()
        self.max_distance = self.Adjacency_matrix.getMaxdistance()
        self.depot = 0
        self.num_vehicle=1
        self.time_table = {}
        time_list = list(range(0,self.nodes_number))

        for i in time_list:
            self.time_table['{start}-{end}'.format(start=i,end= i+1)] = -1


    def setTimeWindow(self,time_table_key,node_index):

        for key in self.time_table.keys():
            if self.time_table[key] == node_index:
                print("The node",node_index," already exist in",key)
                return False

        if self.time_table[time_table_key]== -1:
            print("The node",node_index,"is assigned in Timetable",key)
            self.time_table[time_table_key] = node_index
            return True
        else:
            print("Other node",self.time_table[time_table_key],"exists already in Timetable",time_table_key)
            return False
    
    def setDepot(self,depot_index):
        self.depot = depot_index

    def setVehicles(self,num_vehicle):
        self.num_vehicle = num_vehicle

    def getTimeTable(self):
        return self.time_table


    

class Vehecle:
    def __init__(self,capacity,depot,adjacency_matrix):
        self.depot = depot
        self.Node_visit_capacity = capacity
        self.travel_nodes = []
        self.current_positon = self.depot
        self.adjacency_matrix = adjacency_matrix
        
    def updateCurrentPosition(self,position):
        self.current_positon=position
    
    def setTravelNodes(self,travel_nodes):
        self.travel_nodes =travel_nodes


    def getTotalTraveilingDistance(self):
        Travel_total = self.adjacency_matrix[self.depot][self.travel_nodes[0]]
        for i in range(1,len(self.travel_nodes)):
            Travel_total+=self.adjacency_matrix[i-1][i]
            
        return Travel_total

