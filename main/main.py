"""this is the script Directory"""


import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),  "..")))


from automata_library import DFA
from generate_Latex import LATEX_DFA
from tests import TestDFA

def run_DFA():
    my_DFA = DFA(["q0","q1","q2"], ["a", "b"], "q0", ["q1"])
    my_DFA.trim()
    my_DFA.minimize()
    #my_DFA.seeTransitions()
    latexDFA = LATEX_DFA(my_DFA)
    print(latexDFA.generateLatex())
    
    def test():
        print("The DFA is ready!! Do you want to test it?? (y/n)")
        choice = str(input())
        if choice.lower() == 'n':
            return
        TestDFA(my_DFA)
        
    test()
        
    


if __name__=="__main__":
    run_DFA()
