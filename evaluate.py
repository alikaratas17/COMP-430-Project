from LDP_Algorithms import LDP_Base, RR, GRR
import numpy as np

def evaluate(algorithm: LDP_Base, epsilon, original_data):
    validate_f(LDP_Base, epsilon, original_data)
    validate_g(LDP_Base, original_data)

# validate f satisfies the definition of LDP (p-value test)
def validate_f(algorithm: LDP_Base, epsilon):
    pass


# validate g to see whether the output of g converges to n_v
def validate_g(algorithm: LDP_Base, original_data, f_output_data, threshold):
    estimator = algorithm.g(f_output_data)
    deltas = []
    for item in original_data:
        #print(item)
        #print(estimator[item])
        #print(original_data[item])
        delta = 100.0*abs(estimator[item] - original_data[item])/original_data[item]
        deltas.append(delta)
        #print(delta)
        #if  delta> threshold:
        #    print(f"For threshold {threshold}: g() is not unbiased")
        #    return False
    #print(f"For threshold {threshold}: g() is unbiased")
    #return True
    return np.array(deltas).max(),np.array(deltas).mean()
    
    
