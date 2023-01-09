import evaluate
from LDP_Algorithms import RR

def main():
    evaluate.validate_g(RR.RR(), {0: 10, 1: 15}, {0: 12, 1: 13}, 0.15)

if __name__ == "__main__":
    main()