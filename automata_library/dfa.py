from itertools import combinations
import math
from .utils import indexer
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
    

    def minimize(self):
        ## assuming the dfa is complete and has no discepencies
        n = len(self.__states)
        table =[[False for _ in range(n)] for _ in range(n)]

        indistinct = math.comb(n, 2)
        for i,j in combinations(range(n) , 2):
            state1, state2 = self.__states[i] , self.__states[j]
            if (state1 not in self.__final_state and state2  in self.__final_state) or (state1 in self.__final_state and state2 not in self.__final_state):
                table[i][j] = True
                indistinct -= 1

        prev = indistinct
        indexed_state_list = indexer(self.__states)
        while True:
            for i,j in combinations(range(n) , 2):
                if table[i][j]:
                    continue
                state1,state2 = self.__states[i] , self.__states[j]
                for a in self.__alphabets:
                    x = indexed_state_list[self.__transitions[state1][a]]
                    y = indexed_state_list[self.__transitions[state2][a]]
                    if table[min(x,y)][max(x,y)]:
                        table[i][j] = True
                        indistinct -= 1
                        break
                    
            
            if prev == indistinct:
                break 
            else:
                prev = indistinct
        

        for row in table:
            print(row)


                  

        
            

        
        pass


    def seeTransitions(self):
        print(self.__transitions)

    
    
