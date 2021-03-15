from estimate_pi import *

#data gatherer and file writer

#data gatherer
def collect_pi_estimates(trials,individuals,estimation_function):
    pop = []
    percent = -1
    for i in range(individuals):
        pop.append(estimation_function(trials))
        if i%(individuals//100)==0:
            percent += 1
            print(str(percent) + "% done")
    return sorted(pop)

#data storer
def save_data(pop,filename):
    data = {}
    for indiv in pop:
        data[indiv] = data.get(indiv,0) + 1
    with open(filename + ".txt","w") as file:
        for value,count in data.items():
            file.write("%s:%s\n" % (value, count))

"""
#save_data(collect_pi_estimates(10000,1000000),"data")
save_data(collect_pi_estimates(10000,200,estimate_pi),"no_sqrt")
save_data(collect_pi_estimates(10000,200,estimate_pi_w_sqrt),"w_sqrt")
"""

