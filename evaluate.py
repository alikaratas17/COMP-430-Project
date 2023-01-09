from LDP_Algorithms import LDP_Base, RR, GRR

def evaluate(algorithm: LDP_Base, epsilon, original_data):
    validate_f(LDP_Base, epsilon, original_data)
    validate_g(LDP_Base, original_data)

# validate f satisfies the definition of LDP (p-value test)
def validate_f(algorithm: LDP_Base, epsilon):
    pass


# validate g to see whether the output of g converges to n_v
def validate_g(algorithm: LDP_Base, original_data, f_output_data, treshold):
    estimator = algorithm.g(f_output_data)
    for item in original_data:
        if (abs(estimator[item] - original_data[item]))/max(estimator[item], original_data[item]) > treshold:
            print("g() is not unbiased")
            return False
    print("g() is unbiased")
    return True
    
    
