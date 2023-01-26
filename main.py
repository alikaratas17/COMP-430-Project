import argparse
import evaluate
import random
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--algo", type=str, required=True, help='Enter Algorithm Name')
    parser.add_argument("-e", "--epsilon", type=float, required=True, help='Enter Epsilon Value for the algorithm')
    parser.add_argument("-m", "--mode", type=int, required=True, help='Enter Mode of the experiment: \n1: Convergence \n2: Direct Epsilon Estimation \n3: P-value Estimation\n4: P-value Plot')
    parser.add_argument("-n", "--iteration", type=int,help='Enter number of iterations')
    
    

    args = parser.parse_args()
    exec("from LDP_Algorithms import " + args.algo)
    algo = eval(args.algo + "." + args.algo + "(" + str(args.epsilon) + ")")


    if args.mode == 1:
        n = args.iteration if args.iteration else 100
        arr1, arr2 = evaluate.convergence_experiment(algo, n)
    elif args.mode == 2:
        n = args.iteration if args.iteration else 1000
        result = evaluate.direct_epsilon_estimation_experiment(algo, n)
    elif args.mode == 3:
        n = args.iteration if args.iteration else 1000
        result = evaluate.p_value_estimate_experiment(algo, n)
    elif args.mode == 4:
        n = args.iteration if args.iteration else 1000
        evaluate.p_value_plot_experiment(algo, args.epsilon, [0.00, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0], "result", n)
    else:
        ValueError("Invalid mode")

  
    """
    x = []
    y = []
    y2 = []
    D = 10
    MAX_NUM = 2000
    MIN_NUM = 1000
    #max_str = str(MAX_NUM)
    #min_str = str(MIN_NUM)
    #max_str = max_str[:-3]+","+max_str[-3:]
    #min_str = min_str[:-3]+","+min_str[-3:]
    #print(f"Each v amount in range ({min_str}, {max_str})")
    inputs = {}
    for d in range(D):
        inputs[d]=random.randint(MIN_NUM,MAX_NUM)
    eps = 1.0
    grr = GRR.GRR(eps,D)
    results = {}
    for d in range(D):
        results[d]= 0
    for d in range(D):
        for _ in range(inputs[d]):
            results[grr.f(d)]+=1
    max_change,mean_change = evaluate.validate_g(grr,inputs,results, None)
    total_data =np.array(list(inputs.values())).sum()
    x.append(total_data)
    y.append(max_change)
    y2.append(mean_change)
    #print(f"For Total {total_data} Amount of Input Highest Absolute Change Percentage was {round(max_change*10)/10}%")
    N = 100
    for _ in tqdm(range(N)):
        #MIN_NUM = MIN_NUM* 2
        #MAX_NUM = MAX_NUM* 2
        for d in range(D):
            addition = random.randint(MIN_NUM,MAX_NUM)
            inputs[d]+=addition
            for _ in range(addition):
                results[grr.f(d)]+=1
        max_change,mean_change = evaluate.validate_g(grr,inputs,results, None)
        total_data =np.array(list(inputs.values())).sum()
        x.append(total_data)
        y.append(max_change)
        y2.append(mean_change)
        #print(f"For Total {total_data} Amount of Input Highest Absolute Change Percentage was {round(max_change*10)/10}%")
    plt.plot(x,y)
    plt.plot(x,y2)
    plt.legend(["Max","Mean"])
    plt.xlabel('Total Data Amount')
    plt.ylabel('Absolute Differences in Percentage')
    plt.title('GRR Convergence Experiment with Epsilon = {}'.format(eps))
    plt.show()

"""
'''
def main2():
    D = 10
    MAX_NUM = 200000
    MIN_NUM = 100000
    max_str = str(MAX_NUM)
    min_str = str(MIN_NUM)
    max_str = max_str[:-3]+","+max_str[-3:]
    min_str = min_str[:-3]+","+min_str[-3:]
    print(f"Each v amount in range ({min_str}, {max_str})")
    inputs = {}
    for d in range(D):
        inputs[d]=random.randint(MIN_NUM,MAX_NUM)
    for eps in [0.1,0.5,1.0,2.0]:
        grr = GRR.GRR(eps,D)
        results = {}
        for d in range(D):
            results[d]= 0
        for d in range(D):
            for _ in range(inputs[d]):
                results[grr.f(d)]+=1
        max_change = evaluate.validate_g(grr,inputs,results, None)
        print(f"For Epsilon {eps} Highest Absolute Change Percentage was {round(max_change*10)/10}%")

def main3():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--algo", type=str, required=True)
    #parser.add_argument("-v", "--vectorized", action="store_true")
    parser.add_argument("-e", "--epsilon", type=float, required=True)

    args = parser.parse_args()
    exec("from LDP_Algorithms import " + args.algo)
    algo = eval(args.algo + "." + args.algo + "(" + str(args.epsilon) + ")")
    evaluate.evaluate(algo)

    x = []
    y = []
    y2 = []
    D = 10
    MAX_NUM = 2000
    MIN_NUM = 1000
    #max_str = str(MAX_NUM)
    #min_str = str(MIN_NUM)
    #max_str = max_str[:-3]+","+max_str[-3:]
    #min_str = min_str[:-3]+","+min_str[-3:]
    #print(f"Each v amount in range ({min_str}, {max_str})")
    inputs = {}
    for d in range(D):
        inputs[d]=random.randint(MIN_NUM,MAX_NUM)
    eps = 1.0
    grr = GRR.GRR(eps,D)
    results = {}
    for d in range(D):
        results[d]= 0
    for d in range(D):
        for _ in range(inputs[d]):
            results[grr.f(d)]+=1
    max_change,mean_change = evaluate.validate_g(grr,inputs,results, None)
    total_data =np.array(list(inputs.values())).sum()
    x.append(total_data)
    y.append(max_change)
    y2.append(mean_change)
    #print(f"For Total {total_data} Amount of Input Highest Absolute Change Percentage was {round(max_change*10)/10}%")
    N = 100
    for _ in tqdm(range(N)):
        #MIN_NUM = MIN_NUM* 2
        #MAX_NUM = MAX_NUM* 2
        for d in range(D):
            addition = random.randint(MIN_NUM,MAX_NUM)
            inputs[d]+=addition
            for _ in range(addition):
                results[grr.f(d)]+=1
        max_change,mean_change = evaluate.validate_g(grr,inputs,results, None)
        total_data =np.array(list(inputs.values())).sum()
        x.append(total_data)
        y.append(max_change)
        y2.append(mean_change)
        #print(f"For Total {total_data} Amount of Input Highest Absolute Change Percentage was {round(max_change*10)/10}%")
    plt.plot(x,y)
    plt.plot(x,y2)
    plt.legend(["Max","Mean"])
    plt.xlabel('Total Data Amount')
    plt.ylabel('Absolute Differences in Percentage')
    plt.title('GRR Convergence Experiment with Epsilon = {}'.format(eps))
    plt.show()


def main5():
    D = 10
    MAX_NUM = 200000
    MIN_NUM = 100000
    max_str = str(MAX_NUM)
    min_str = str(MIN_NUM)
    max_str = max_str[:-3]+","+max_str[-3:]
    min_str = min_str[:-3]+","+min_str[-3:]
    print(f"Each v amount in range ({min_str}, {max_str})")
    inputs = {}
    for d in range(D):
        inputs[d]=random.randint(MIN_NUM,MAX_NUM)
    for eps in [0.1,0.5,1.0,2.0]:
        grr = GRR.GRR(eps,D)
        results = {}
        for d in range(D):
            results[d]= 0
        for d in range(D):
            for _ in range(inputs[d]):
                results[grr.f(d)]+=1
        max_change = evaluate.validate_g(grr,inputs,results, None)
        print(f"For Epsilon {eps} Highest Absolute Change Percentage was {round(max_change*10)/10}%")
'''
if __name__ == "__main__":
    main()