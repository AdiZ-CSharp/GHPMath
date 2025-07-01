from simulation_network import run_simulation, Network
from SIR_network import model
# Note lowercase on "model"; we're importing the actual model instance, not the class

nw = Network(model)
nw.add_nodes(6, "Susceptible")   # Add 10 nodes with initial state "Susceptible"
nw.set_state(0, "Infected")      # Initial state for node 0
nw.add_edges(                    # Define edges between nodes
    (0, 1),
    (0, 2),
    (2, 3),
    (2, 4),
    (2, 5),
    (3, 4),
    (4, 5)
)

# Show how to print information about the underlying graph
g = nw.get_nx_graph()
print(g.nodes)

run_simulation(model, nw, num_frames=10)

