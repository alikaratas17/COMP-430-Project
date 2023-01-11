# Automated Verifier for Black-box Local Differential Privacy Algorithms
It is used to test Local Differential Privacy Protocols whether the algorithm preserves population statistics and satisfies the LDP’s definition.

## Proposed Appoach
1. Testing for Convergence in Terms of Unbiased Estimation
2. Violation Detection Through p-value Test


## Algorithms
RR, GR, Simple RAPPOR and OUE algorithms can be found in LDP_Algorithms directory. If you want to add another algortihm, it should be a subclass of LDP_Base class.

