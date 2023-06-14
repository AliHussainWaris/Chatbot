from py2neo import Graph

graph = Graph("bolt://localhost:7687", auth=("neo4j", "Password"))

def datasend(name,human,bot):
    if name and bot:
        query = "MATCH (p:Person {name: $name}) RETURN p.name"
        result = graph.run(query, name=name)
        if result.evaluate() == name:
            query2 = "CREATE (c:Chat {bot: $bot, name: $name}) RETURN c"
            result2 = graph.run(query2, bot=bot, name=name)

            query4 = "CREATE (h:Human {human: $human, name: $name}) RETURN h"
            result4 = graph.run(query4, human=human, name=name)

            relation_query = """
            MATCH (a:Person {name: $name}), (b:Chat {bot: $bot})
            CREATE (a)-[r:BOT_CHAT]->(b)
            RETURN r
            """
            relation_result = graph.run(relation_query, name=name, bot=bot)

            relation_query2 = """
            MATCH (a:Person {name: $name}), (b:Human {human: $human})
            CREATE (a)-[r:Human_Chat]->(b)
            RETURN r
            """
            relation_result2 = graph.run(relation_query2, name=name, human=human)
            print(relation_result2)

            relation_query3 = """
            MATCH (a:Human {human: $human}), (b:Chat {bot: $bot})
            CREATE (b)-[r:REPLY]->(a)
            RETURN r
            """
            relation_result3 = graph.run(relation_query3, bot=bot, human=human)
            print(relation_result3)

        else:
            print("Person not found with the given name")
    else:
        print("Missing name or bot parameter")

    return result