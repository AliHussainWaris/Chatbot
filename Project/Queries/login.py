from py2neo import Graph, Node

graph = Graph("bolt://localhost:7687", auth=("neo4j", "Password"))

def login(email, password):
    query = "MATCH (p:Person {email: $email, password: $password}) RETURN p"
    result = graph.run(query, email=email, password=password)
    if email and password:
        if result.data():
            query = "MATCH (p:Person {email: $email, password: $password}) RETURN p.name"
            name_result = graph.run(query, email=email, password=password)
            name = name_result.data()[0]['p.name']
            print("Login Successful")
            return name
        else:
            print("Login Failed")
    else:
        print(email , password)
        print("Email and password are required.")