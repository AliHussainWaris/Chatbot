from py2neo import Graph

graph = Graph("bolt://localhost:7687", auth=("neo4j", "Password"))

def chatfetch(name):
    query = "match (p:Person {name:$name}),(n:Chat) - [r :REPLY]->(d : Human) return n.bot,r,d.human "
    result = graph.run(query , name = name)
    # print(result)
    chats = []
    humans = []

    for record in result:
        chat = record["n.bot"]
        human = record["d.human"]

        chats.append(chat)
        humans.append(human)
    return chats, humans