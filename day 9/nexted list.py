capitals = {
    "france":"paris",
    "germany":"berlin"
}
travel_log = {
    "france":{
        "cities_visited":["paris", "lille", "dijon"],
        "total_visits":12
    },
    "germany":{
        "cities_visited":["berlin", "Stuttgart"],
        "total_visits":12,
    }
}
print(travel_log["france"]["cities_visited"][2])
nested_list = ["A", "B", "C",
    ["D", "E", "F"]]

#print(nested_list[3][1])