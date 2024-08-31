import numpy as np
import gudhi as gd
import pandas as pd
import os
import matplotlib.pyplot as plt
from gudhi.representations import Landscape

def getDgms(dist, side, idx, save=False):
    rips = gd.RipsComplex(distance_matrix=dist, 
                          max_edge_length=1.1)
    simplexTree = rips.create_simplex_tree(max_dimension=2)
    simplexTree.compute_persistence()
    dgm0, dgm1 = simplexTree.persistence_intervals_in_dimension(0),simplexTree.persistence_intervals_in_dimension(1)
    dgm0[-1][1] = 1
    if save:
        dgm = simplexTree.persistence()
        saveDgm(dgm, side, idx)
    return dgm0, dgm1

def saveDgm(dgm, side, idx):
    dgmPlot = gd.plot_persistence_diagram(dgm)
    dgmPlot.set_title(f"{side} {idx}")
    plt.savefig(f"dgms/{side}/corr_{idx}.png") 


#takes in directory with two subfolders, open and closed 
def protein_landscape(dir, n, target_directory, k0, k1, resolution=50, saveDiagrams=False):
    idx = 0
    H0 = np.zeros(n)
    H1 = np.zeros(n)
    landObj0 = Landscape(num_landscapes=k0,resolution=resolution)
    landObj1 = Landscape(num_landscapes=k1,resolution=resolution)

    for side in ('open', 'closed'): 
        directory = f"{dir}/{side}"
        for file in os.listdir(directory):    
            if not file.endswith("txt"): continue
            file = os.path.join(directory, file)
            print(file)
            corr = pd.read_csv(file, header=None, delim_whitespace=True) 
            dist = 1-np.abs(corr.to_numpy())
            dgm0, dgm1 = getDgms(dist, side, idx, save=saveDiagrams)
            H0[idx] = landObj0.fit_transform([dgm0]).sum()/resolution
            H1[idx] = landObj1.fit_transform([dgm1]).sum()/resolution
            idx+=1
            
    np.savetxt(os.path.join(target_directory, "landscape_values_H0.txt"), H0)
    np.savetxt(os.path.join(target_directory, "landscape_values_H1.txt"), H1)

