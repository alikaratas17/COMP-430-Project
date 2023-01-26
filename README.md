# Automated Verifier for Black-box Local Differential Privacy Algorithms
The objective of this project was to develop an automated verifier for black-box Local Differential Privacy (LDP) algorithms. You can run 4 different experiments with this project.

## Proposed Appoach
1. Testing for Convergence in Terms of Unbiased Estimation
2. Violation Detection Through p-value Test


## Algorithms
RR, GR, Simple RAPPOR and OUE algorithms can be found in LDP_Algorithms directory. If you want to add another algortihm, it should be a subclass of LDP_Base class.

## Run Verifier locally

### Step 1: Clone the project
    git clone https://github.com/alikaratas17/COMP-430-Project.git
    cd COMP-430-Project
    
### Step 2: Install needed packages if they are not exist
    sudo apt install -r requirements.txt

### Step 3: Run the project using the following command 
    main.py [-h] -a ALGO -e EPSILON -m MODE [-n ITERATION]
    
ALGO is the name of the algorithm such as RR, GRR, OUE, SimpleRAPPOR. EPSILON is the epsilon value for the algorithm. MODE is an integer value corresponding to the type of the experiment (1: Convergence, 2: Direct Epsilon Estimation, 3: P-value Estimation, 4: P-value Plot). ITERATION is an optional argument that corresponds to the number of iterations. 

### Optional: Add custom algorithms 

If you want to check a custom algorithm, you need to create a class inherits from LDP_Base, then add it to the LDP_Algorithms folder. Make sure the algorithm name in arguments and the name of the python file are the same when you run the code with command line.
    
