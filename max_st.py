from parse import *
import networkx as nx
import solver_hl
import os

if __name__ == "__main__":
    output_dir = "output"
    input_dir = "inputs"
    for input_path in os.listdir(input_dir):
        graph_name = input_path.split(".")[0]
        if graph_name.split("-")[0] == "large":
	        out = input_path.replace('inputs', 'out').replace('.in', '.out') 
	        G = read_input_file("/inputs"+input_path)
	        T = solver_hl.solve(G)
	        write_output_file(T, out)

