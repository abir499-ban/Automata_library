"""this is the script Directory"""


import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),  "..")))


from automata_library import DFA
from generate_Latex import LATEX_DFA

def run_DFA():
    my_DFA = DFA(["q0", "q1","q2", "q3" , "q4" , "q5" , "q6" , "q7" , "q8"], ["a", "b"], "q0", ["q0" , "q1" , "q3" , "q4"], {'q0': {'a': 'q3', 'b': 'q1'}, 'q1': {'a': 'q3', 'b': 'q2'}, 'q2': {'a': 'q5', 'b': 'q2'}, 'q3': {'a': 'q6', 'b': 'q1'}, 'q4': {'a': 'q6', 'b': 'q2'}, 'q5': {'a': 'q8', 'b': 'q2'}, 'q6': {'a': 'q6', 'b': 'q7'}, 'q7': {'a': 'q6', 'b': 'q8'}, 'q8': {'a': 'q8', 'b': 'q8'}})
    my_DFA.trim()
    my_DFA.minimize()
    #my_DFA.seeTransitions()
    latexDFA = LATEX_DFA(my_DFA)
    print(latexDFA.generateLatex())
    


if __name__=="__main__":
    run_DFA()
