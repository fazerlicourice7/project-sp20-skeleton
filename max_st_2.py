from parse import *
import networkx as nx
import solver_hl
import os

if __name__ == "__main__":
    output_dir = "output/large/"
    input_dir = "large_remaining"
    failed_path = "./failed.txt"
    for input_path in os.listdir(input_dir):
        graph_name = input_path.split(".")[0]
        if graph_name.split("-")[0] == "large":
                #print("input path: {}".format(input_path))
                #print("graph name: {}".format(graph_name))
                if int(graph_name.split("-")[1])  in range(240, 270):
                    out = output_dir + input_path.replace('.in', '.out')
                    print("output dir: {}".format(out))
                    G = read_input_file("{}/{}".format(input_dir, input_path))
                    print("starting: {}".format(graph_name))
                    try:
                        T = solver_hl.solve(G)
                        write_output_file(T, out)
                        print("solved: {}".format(input_path))
                    except:
                        print(graph_name)
                        with open(failed_path, 'a') as f:
                            f.writelines([graph_name])
