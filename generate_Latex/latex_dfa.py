from .utils import makeFile
from automata_library import DFA
class LATEX_DFA:
    def __init__(self, dfa : DFA):
        self.__states = dfa.getStates()
        self.__alphabets = dfa.getalphabets()
        self.__transitions = dfa.getTransitions()
        self.__initialState = dfa.getInitialState()
        self.__finalStates = dfa.getFinalState()
        
    
    def generateLatex(self):
        latex_code = r"""
                        \documentclass{article}
                        \usepackage{tikz}
                        \usetikzlibrary{automata, positioning}

                        \begin{document}
                        \section{}

                            \begin{center}
                                \begin{tikzpicture}[shorten >=1pt, node distance=2cm, on grid, auto] 
                    """
        state_lines=[]
        for i,state in enumerate(self.__states):
            x_pos = i % 4
            y_pos = -(i // 4)
            state_type = ""
            if state in self.__initialState:
                state_type += ',initial'
            if state in self.__finalStates:
                state_type += ',accepting'

            state_lines.append(f"\n    \\node [state{state_type}] ({state}) at ({x_pos*2} , {y_pos*2}) {{ {state }}};")
        
        latex_code += "".join(state_lines)


        latex_code += "\n \\path[->]"
        path_lines=[]
        for state in self.__transitions:
            for character in self.__transitions[state]:
                if self.__transitions[state][character] == state:
                    path_lines.append(f"\n      ({state}) edge[loop above] node {{{character}}} ({self.__transitions[state][character]})")
                else:
                    path_lines.append(f"\n      ({state}) edge node {{{character}}} ({self.__transitions[state][character]})")

        latex_code += "".join(path_lines)
        latex_code += ";"

        latex_code += r"""
                        \end{tikzpicture}
                        \end{center}
                        \end{document}
                        """
        try:
            file_path = makeFile(latex_code=latex_code)
            print("file containing latex code is at ", file_path)
        except Exception as e:
            pass
        

    

