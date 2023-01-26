from LDP_Algorithms import LDP_Base, RR, GRR,SimpleRAPPOR
import numpy as np
from p_value_test import pValueTestVectorized, pValueTestNonVectorized,plot_result
import random
from tqdm import tqdm
from direct_epsilon_estimation import estimateEpsilonNonVectorized,estimateEpsilonVectorized
from convergence_test import convergence_test_vectorized,convergence_test_non_vectorized

def p_value_plot_experiment(algo:LDP_Base,original_epsilon,epsilon_values,plot_save_name,N):
    epsilon_results = {}
    result = []
    for epsilon in tqdm(epsilon_values):
        if algo.isVectorized():
            result = result + pValueTestVectorized(algo, epsilon, N)
        else:
            result = result + pValueTestNonVectorized(algo, epsilon, N)
    epsilon_results[original_epsilon] = result
    plot_result(epsilon_results, "epsilon","p_value", plot_save_name)

def p_value_estimate_experiment(algo:LDP_Base,N):
    estimate = 0.5
    delta_eps = 0.5
    prev_dir = None
    multip_N = 2
    P_VAL_ERROR_MARGIN=0.01
    while delta_eps > 0.01:
        if algo.isVectorized():
            p_val = pValueTestVectorized(algo, estimate, N)[0][-1]
        else:
            p_val = pValueTestNonVectorized(algo, estimate, N)[0][-1]
        #print(p_val)
        if p_val <0.05:
            if prev_dir=='BACKWARD':
                delta_eps /=2
                N =round(N* multip_N)
            estimate += delta_eps
            #print(estimate)
            prev_dir = 'FORWARD'
        else:
            if prev_dir=='FORWARD':
                delta_eps /=2
                N =round(N* multip_N)
            prev_dir = 'BACKWARD'
            estimate -=delta_eps
            #print(estimate)
    return estimate

def direct_epsilon_estimation_experiment(algo:LDP_Base,N):
    if algo.isVectorized():
        return estimateEpsilonVectorized(algo,N)
    else:
        return estimateEpsilonNonVectorized(algo,N)

def convergence_experiment(algo,N,nums=None):
    if algo.isVectorized():
        return convergence_test_vectorized(algo,N,nums)
    else:
        return convergence_test_non_vectorized(algo,N,nums)


if __name__ == '__main__':
    a,b = convergence_experiment(GRR.GRR(0.9,10),100)
    #a,b = convergence_experiment(SimpleRAPPOR.SimpleRAPPOR(0.9,10),100)
    p_value_plot_experiment(GRR.GRR(0.9,10),0.9,[0.00, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0],"GRR6",1000)
    print(a)
    print(b)
    #print(convergence_experiment(SimpleRAPPOR.SimpleRAPPOR(0.9,4),10000))
    #print(direct_epsilon_estimation_experiment(SimpleRAPPOR.SimpleRAPPOR(0.9,4),10000))
