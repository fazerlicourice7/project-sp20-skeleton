from parse import *
import networkx as nx
import solver_hl
import os

if __name__ == "__main__":
    output_dir = "output"
    input_dir = "large-remaining"
    failed_path = "./failed.txt"
    for input_path in os.listdir(input_dir):
        graph_name = input_path.split(".")[0]
        if graph_name.split("-")[0] == "large":
                if int(graph_name.split("-")[1]) > 400:
                    out = input_path.replace('inputs', 'out').replace('.in', '.out') 
                    G = read_input_file("/inputs"+input_path)
                    try:
                        T = solver_hl.solve(G)
                        write_output_file(T, out)
                    except:
                        print(graph_name)
                        with open(failed_path, 'a') as f:
                            f.writelines([graph_name])

