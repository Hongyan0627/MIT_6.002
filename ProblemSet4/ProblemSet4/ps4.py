# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    time_steps = [300,150,75,0]
    
    for j in range(4):
        
        result = []
        
        for dummy_sim in range(numTrials):
            #temp = 0.0
            
            patient = TreatedPatient([ResistantVirus(0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005) for dummy in range(100)], 1000)
            
            for i in range(150):
                patient.update()
            
            patient.addPrescription("guttagonol")
            
            for i in range(time_steps[j]):
                patient.update()
                #temp += (patient.getTotalPop() + 0.0)
            
            patient.addPrescription("grimpex")
        
            for i in range(150):
                patient.update()
                #temp += (patient.getTotalPop() + 0.0)
            
            result.append(patient.getTotalPop())
            
        print numpy.var(numpy.array(result))    
        
        #pylab.subplot(1,1,j+1)
        #pylab.xlabel("total virus")
        #pylab.title(str(time_steps[j]))
        #pylab.hist(result)
        #pylab.show()


simulationDelayedTreatment(100)




#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
