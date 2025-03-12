"""this is the script Directory"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from automata_library import DFA


my_DFA = DFA(["q0", "q1", "q2"], ["0", "1"], "q0", ["q2"])
