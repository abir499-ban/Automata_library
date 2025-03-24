# Automata Theory Implementation 🖥️

## Overview  
This is my own Implementation of the Automata Theory  in Python from scratch. It provides functionalities such as trimming unreachable states, minimizing the DFA, and managing state transitions.

The library simplifies the process of defining, validating, and manipulating automata through an easy-to-use, object-oriented approach.

---

## Features  
- **Create a DFA** with user-defined states, alphabets, initial state, final states, and transitions.  
- **Trimming of unreachable states** to optimize the DFA by removing unnecessary states.  
- **DFA minimization** using the table-filling algorithm to merge indistinguishable states.  
- **Automated state transition management** with error handling and input validation.
- **Generate latex code** with a predefined template and share your DFA with others.
- **Test your DFA** by passing a test string, and check it is accepted or not.

---

## Installation  
1. Fork the repository by clicking on the Fork icon the on the [repository page](https://github.com/abir499-ban/Automata_library)
   
  Now, go to your terminal and run this commands:
```bsh
  mkdir automata_project
  cd automata_project
  ```
2. Clone this repo
   ```bsh
       git clone https://github.com/abir499-ban/Automata_library.git
   ```
3. Go to main folder
   ```bsh
       cd automata_library
       cd main
   ```
4. Open the main.py file under the ./main folder. Make any changes to the States, the alphabets set , the initial state , the set of final states, anything you want.Just keep in mind you are following the rules of DFA i.e **initial state and the set of final states must be subsets of the set of states**
  This is the code of the `./main/main.py` file lookes like:
  ```python
  """this is the script Directory"""


import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),  "..")))


from automata_library import DFA
from generate_Latex import LATEX_DFA
from tests import TestDFA

def run_DFA():
    my_DFA = DFA(["q0","q1","q2"], ["a"], "q0", ["q1"])    ## make your changes here. The order is the set of states , the Alphabet set , the Initial State, and the Set of final States
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
```
5. Now again go to the terminal, and run the main.py file.
     ```bsh
         python main.py
     ```
6. Next the program will ask you promptly to enter the Transitions for each of the states with respect to each alphabet in the alphabet set.
   Something like this:

   
  ![](https://i.imgur.com/XR678fj.png)

Make sure while filling up the transitions for the DFA, follow the rules that is dont enter any invalid value for the transition from a state upon reading a character. Dont enter any state which does not belong to the set of states.
The application has error catching mechanism, such that it will not proceed with the state transition until, it has a valid transition has been made.

7. When the State Transitions are complete, a meesage like this pops up in the terminal:

![](https://i.imgur.com/s802SqP.png)

Boom!! Your DFA is ready as well as the Latex code of the same. The latex code of the same can be found at ./my_samples folder in a .tex file. Genuinely, the latest .text file will contain your DFA.

8. Testing your DFA:
   After the DFA has been constructed, you are ready to verify it and can test with some random strings.
   ![](https://i.imgur.com/zf1nHG5.png)

  After this message, enter **y** if you want to test it , **n** elsewise.

  If you want to test it and have pressed **y** then continue to enter a tester string:

  ![](blob:https://imgur.com/16717157-e014-4c92-b789-e14f6cb5bc58)

  The verdict will be given by the program itself.

  **note: The string entered must consist of only the characters that is present in the alphabet set.**

-----------------------------------------------------------------------------------

For simplicity, delete all the presaved .tex files under ./my_samples folder, which help to find your .tex file after generating it.


If you liked my project , and its implementation of the Automata Theory, do give it a Star ⭐.

Have fun in your DFA construction😁
