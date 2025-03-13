from automata_library import DFA
class TestDFA:
    def __init__(self, dfa : DFA):
        self.__test_string=""
        self.__getInput()
        result =  self.__test(dfa)
        if result:
            print("Your Test String was accepted by the DFA")
        else:
            print("Your test input string was rejected by the DFA")
    
    def __getInput(self):
        self.__test_string = input("Enter string to test your dfa against\n")
        print()

    
    def __test(self, dfa :DFA):
        initialState = dfa.getInitialState()
        finalStates = dfa.getFinalState()
        transitions = dfa.getTransitions()

        curr_state = initialState
        for chr in self.__test_string:
            next_state = transitions[curr_state][chr]
            curr_state = next_state
        
        return curr_state in finalStates
