from pyspark.sql import SparkSession

#data_path = "agg_match_stats_0_100000.csv"
data_path = "agg_match_stats_0.csv"

# Créer une session Spark
spark = SparkSession.builder.appName("ExemplePySpark").getOrCreate()

# Chargement du jeu de données
df = spark.read.csv(data_path, header=True, inferSchema=True)

"""# Classement des kills"""

# # Sélection des colonnes pertinentes (player_name, player_kills, match id)
# selected_columns = ["player_name","match_id","player_kills"]
# df_selected = df.select(selected_columns)

# #df_selected.show()

# # Convert DataFrame to RDD and perform transformations
# rdd = df.rdd.map(lambda x: (x["player_name"], (x["match_id"], x["player_kills"])))

# # Count the number of games played and calculate the total kills for each player
# rdd_total_kill = rdd.groupByKey().mapValues(lambda values: (len(values), sum(v[1] for v in values)))

# # Calculate the average kills per game for each player
# rdd_kill = rdd_total_kill.mapValues(lambda stats: (stats[1] / stats[0],stats[0]))

# # Filter errors
# rdd_kill = rdd_kill.filter(lambda x: x[0] is not None and x[0] != "None")

# # Display the result

# #result = rdd_kill.take(10)
# #for row in result:
#     #print(row)
#     #print(f"Player Name: {row[0]}, Number of Games: {row[1][1]:.2f}, Average Kills per Game: {row[1][0]:.2f}")

# # Sort the RDD by descending order of average kills
# sorted_rdd_kill = rdd_kill.sortBy(lambda x: x[1][0], ascending=False)

# # Display the top 10 results
# print("Top 10 des classements au kill")
# top_10 = sorted_rdd_kill.take(10)
# for i, row in enumerate(top_10, start=1):
#     print(f"{i}. Killer Name: {row[0]}, Number of Games: {row[1][1]:.2f}, Average Kills per Game: {row[1][0]:.2f}")

# # Filter players with at least 4 games
# filtered_players_kill = sorted_rdd_kill.filter(lambda x: x[1][1] >= 4)

# # Process a specific player
# specific_player_kill = sorted_rdd_kill.filter(lambda x: x[0] == 'gogolnyg')

# print("\nPlayers with at least 4 games:")
# filter = filtered_players_kill.take(10)
# for i, row in enumerate(filter, start=1):
#     print(f"{i}. Killer Name: {row[0]}, Number of Games: {row[1][1]:.2f}, Average Kills per Game: {row[1][0]:.2f}")

# print("\nSpecific Player Data:")
# specific = specific_player_kill.take(10)
# for i, row in enumerate(specific, start=1):
#     print(f"{i}. Killer Name: {row[0]}, Number of Games: {row[1][1]:.2f}, Average Kills per Game: {row[1][0]:.2f}")


"""#Classement des positions"""

# Sélection des colonnes pertinentes (player_name, player_kills, team_placement)
selected_columns = ["player_name","team_placement","match_id"]
df_selected = df.select(selected_columns)

#df_selected.show()

# Convert DataFrame to RDD and perform transformations
rdd = df.rdd.map(lambda x: (x["player_name"], (x["match_id"], x["team_placement"])))

# Count the number of games played and calculate the total kills for each player
rdd_total_pos = rdd.groupByKey().mapValues(lambda values: (len(values), sum(v[1] for v in values)))

# Calculate the average kills per game for each player
rdd_pos = rdd_total_pos.mapValues(lambda stats: (stats[1] / stats[0],stats[0]))

# Filter errors
rdd_pos = rdd_pos.filter(lambda x: x[0] is not None and x[0] != "None")

# Display the result

#result = rdd_pos.take(10)
#for row in result:
    #print(row)
    #print(f"Player Name: {row[0]}, Number of Games: {row[1][1]:.2f}, Average placement per Game: {row[1][0]:.2f}")

# Sort the RDD by descending order of average placement
sorted_rdd_pos = rdd_pos.sortBy(lambda x: x[1][0], ascending=True)

# Display the top 10 results
print("Top 10 des classements moyen")
top_10 = sorted_rdd_pos.take(10)
for i, row in enumerate(top_10, start=1):
    print(f"{i}. Player Name: {row[0]}, Number of Games: {row[1][1]:.2f}, Average placement per Game: {row[1][0]:.2f}")

# Filter players with at least 4 games
filtered_players_pos = sorted_rdd_pos.filter(lambda x: x[1][1] >= 4)

# Process a specific player
specific_player_pos = sorted_rdd_pos.filter(lambda x: x[0] == 'gogolnyg')

print("\nPlayers with at least 4 games:")
filter = filtered_players_pos.take(10)
for i, row in enumerate(filter, start=1):
    print(f"{i}. Player Name: {row[0]}, Number of Games: {row[1][1]:.2f}, Average placement per Game: {row[1][0]:.2f}")

print("\nSpecific Player Data:")
specific = specific_player_pos.take(10)
for i, row in enumerate(specific, start=1):
    print(f"{i}. player Name: {row[0]}, Number of Games: {row[1][1]:.2f}, Average placement per Game: {row[1][0]:.2f}")


"""# Classement combiné"""

# Function to calculate the score based on specified criteria
def calculate_score(assists, damage, eliminations, placement):
    return 50 * assists + damage + 100 * eliminations + (1000 - 10 * placement)

# Select relevant columns
selected_columns = ["player_name", "player_assists", "player_dmg", "player_dbno", "player_kills", "team_placement"]
df_selected = df.select(selected_columns)

# Convert DataFrame to RDD and perform transformations
rdd = df_selected.rdd.map(lambda x: (x["player_name"], x["player_assists"], x["player_dmg"], x["player_dbno"], x["player_kills"], x["team_placement"]))

# Calculate the score for each player
rdd_scores = rdd.map(lambda x: (x[0], calculate_score(x[1], x[2], x[4], x[5])))

# Sort the RDD by descending order of scores
sorted_rdd_scores = rdd_scores.sortBy(lambda x: x[1], ascending=False)

# Display the top 10 results
print("Top 10 des classements combine")
top_10_scores = sorted_rdd_scores.take(10)
for i, row in enumerate(top_10_scores, start=1):
    print(f"{i}. Player: {row[0]}, Score: {row[1]:.2f}")

# Stop the Spark session
spark.stop()