import random as rand
import sys
import distutils.util as dist


def helloWorld(seed, showProblem=False, showSolution=False, outdir=''):
    
    # initialize the pseudo-random engine with the seed:
    rand.seed(seed)

    # like that all calls and hence the psuedo-rnadom numbers output by that engine will be deterministic:
    a = rand.randint(25, 40)
    b = rand.randint(15, 40)

    if showProblem:
        print("Problem: What is "+str(a)+"+"+str(b)+"?")

    if showSolution:
        print("Solution: The solution to "+str(a)+"+"+str(b)+" is "+str(a+b)+".")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("specify seed as first parameter")

    seed = int(sys.argv[1])
    helloWorld(seed, dist.strtobool(sys.argv[2]), dist.strtobool(sys.argv[3]))
