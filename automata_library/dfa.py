
class DFA:
    def __init__(self , states : list[str], alphabets : list[str] , initial_state : str, final_state : list[str]):
        if initial_state not in states:
            print("NOT a valid initial state")
            return

        if not set(final_state).issubset(set(states)):
            print("Final States are not valid")
            return
        
        self.__final_state  = final_state
        self.__states = states
        self.__alphabets  = alphabets
        self.__initial_state = initial_state
        
        
        self.__transitions = {}
        self.__GetTransitions()

    
    def __GetTransitions(self):
        for state in self.__states:
            transition = {}
            for character in self.__alphabets:
                print(f"Enter transition for state {state} on reading character {character}")
                next_state = input()

                while True:
                    if not next_state:
                        print("Next State cannot be NULL")
                    elif next_state not in self.__states:
                        print("Next State is not Valid")
                    else:
                        break
                transition[character] = next_state 

            self.__transitions[state] = transition
        
    
    def __Isreachable(self, state):
        if state == self.__initial_state:
            return True
        
        reachable = False
        for source in self.__states:
            if reachable:
                break
            if state != source:
                transitions = self.__transitions[source].values()
                if state in transitions:
                    reachable = True
        return reachable


    

    def trim(self):
        for state in self.__states:
            if not self.__Isreachable(state):
                del self.__transitions[state]
    
    def seeTransitions(self):
        print(self.__transitions)

    
    
