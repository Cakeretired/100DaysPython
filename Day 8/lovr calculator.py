def calculate_love_score(name1, name2):
    # Combine names and convert to lowercase
    names = (name1 + name2).lower()

    # Count letters for "TRUE"
    t = names.count("t")
    r = names.count("r")
    u = names.count("u")
    e = names.count("e")
    true_score = t + r + u + e

    # Count letters for "LOVE"
    l = names.count("l")
    o = names.count("o")
    v = names.count("v")
    e = names.count("e") # e counted again
    love_score = l + o + v + e

    # Combine the two numbers
    score = int(str(true_score) + str(love_score))

    print(f"Your score is: {score}")


# Example use
calculate_love_score("Alice", "Bob")