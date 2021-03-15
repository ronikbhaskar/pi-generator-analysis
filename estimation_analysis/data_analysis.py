
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from math import sqrt

#analysis

#stat class
class Statistic:
    def __init__(self, filename,
                 exp_values,
                 res_values,
                 total, individuals,
                 data,
                 st_dev, mean,
                 med, q1,q3,minimum,maximum):
        self.filename = filename
        self.exp_values = exp_values
        self.res_values = res_values
        self.total = total
        self.individuals = individuals
        self.data = data
        self.st_dev = st_dev; self.mean = mean
        self.med = med; self.q1 = q1; self.q3 = q3
        self.minimum = minimum; self.maximum = maximum
        read_data()
        fill_in_stats()

    def __init__(self, filename):
        self.filename = filename
        self.exp_values = []
        self.res_values = []
        self.total = self.individuals = 0
        self.data = {}
        self.st_dev = self.mean = 0
        self.med = self.q1 = self.q3 = 0
        self.minimum = self.maximum = 0
        self.read_data()
        self.fill_in_stats()
        

    #read the data from the file
    def read_data(self):
        with open(self.filename + ".txt","r") as file:
            for line in file.readlines(): # file is written as exp:res, like a dict
                line = line.split(":")
                exp = float(line[0])
                res = int(line[1])
            
                self.exp_values.append(exp)
                self.res_values.append(res)
                self.total += exp*res #value times frequency
                
            self.individuals = sum(self.res_values)
        #store data in variable
        self.data = dict(zip(self.exp_values,self.res_values))

    def get_stdev(self):
        total = 0
        for exp,res in self.data.items():
            total += res * ((exp - self.mean)**2)
        total /= self.individuals - 1
        total = sqrt(total)
        return total

    #fill in the rest of the stuff
    def fill_in_stats(self):
        self.mean = self.total/self.individuals
        if self.individuals % 2 == 0:
            self.med = (self.find(self.individuals//2) \
                       + self.find(self.individuals//2+1)) \
                       /2
        else:
            self.med = self.find(self.individuals//2+1)
        self.stdev = self.get_stdev()
        

    #find the value at a given index
    def find(self,index):
        for exp,res in self.data.items():
            index -= res
            if index <= 0:
                return exp
        else:
            return None

    #generate graph
    def create_distribution_graph(self):
        x = []
        for exp,res in self.data.items():
            for _ in range(res):
                x.append(exp)
        num_bins = 15
        n, bins, patches = plt.hist(x, num_bins, density=1, facecolor='blue', alpha=0.5)
        #plt.plot(self.exp_values,self.res_values)
        plt.xlabel("Estimation Value")
        plt.ylabel("Frequency")
        plt.title(r'$\mu={0: .5f}$, $\sigma={1: 0.5f}$'.format(self.mean,self.stdev))
        plt.show()


"""
no_sqrt_stat = Statistic("no_sqrt")
print("med:",no_sqrt_stat.med)
print("mean:",no_sqrt_stat.mean)
print("stdev:",no_sqrt_stat.stdev)
no_sqrt_stat.create_distribution_graph()

w_sqrt_stat = Statistic("w_sqrt")
print("med:",w_sqrt_stat.med)
print("mean:",w_sqrt_stat.mean)
print("stdev:",w_sqrt_stat.stdev)
w_sqrt_stat.create_distribution_graph()
"""


