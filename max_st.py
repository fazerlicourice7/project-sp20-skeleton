from parse import *
import networkx as nx
import solver_hl
import os

if __name__ == "__main__":
    output_dir = "output"
    input_dir = "inputs"
    for input_path in os.listdir(input_dir):
<<<<<<< HEAD
        graph_name = input_path.split(".")[0]
        if graph_name.split("-")[0] == "medium":
	        out = input_path.replace('inputs', 'out').replace('.in', '.out') 
	        G = read_input_file(f"{input_dir}/{input_path}")
	        T = solver_hl.solve(G)
	        write_output_file(T, out)
=======
    	graph_name = input_path.split(".")[0]
		out = input_path.replace('inputs', 'out').replace('.in', '.out') 
		G = read_input_file("inputs/" + input_path)
		T = solver_hl.solve(G)
		write_output_file(T, out)
>>>>>>> baa540ddae4ad38396650c8fdab1406cbd6f3c70
