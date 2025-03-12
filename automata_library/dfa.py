
class DFA:
    def __init__(self , states : list[str], alphabets : list[str] , initial_state : str, final_state : list[str]):
        self.__states = states
        self.__alphabets  = alphabets
        self.__initial_state = initial_state
        self.__final_state  = final_state
        self.__transitions = {}
        self.__GetTransitions()

    
    def __GetTransitions(self):
        for state in self.__states:
            transition = {}
            for character in self.__alphabets:
                print(f"Enter transition for state {state} on reading character {character}")
                transition[character] = input()
            self.__transitions[state] = transition
        
        

    
    def sayHI(self):
        print("HI")
