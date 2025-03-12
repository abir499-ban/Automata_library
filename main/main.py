"""this is the script Directory"""


import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),  "..")))


from automata_library import DFA

def run_DFA():
    my_DFA = DFA(["q0", "q1", "q2"], ["a", "b"], "q0", ["q1"])
    my_DFA.trim()
    my_DFA.seeTransitions()


if __name__=="__main__":
    run_DFA()
