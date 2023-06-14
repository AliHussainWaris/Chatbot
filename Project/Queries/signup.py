from py2neo import Graph, Node

graph = Graph("bolt://localhost:7687", auth=("neo4j", "Password"))

def signup(name, email,password):
    person = Node("Person", name=name, email=email ,password=password)
    graph.create(person)
    print("Node created successfully!")
