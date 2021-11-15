# Since we will always mantain the points of the line ordered asc,
# we can just compare in order.
# Also, we will always mantain the line AB at the begining of the array


# Compare if two configurations are the same
def equal(c1, c2):
    for i in range(len(c1) - 1):
        if (c1[i][0] != c2[i][0]) or (c1[i][1] != c2[i][1]):
            return False
    return True


# Compare if two configurations are equivalent
def equiv(c1, c2):
    return equiv_recursive(c1, c2, [])


def equiv_recursive(c1, c2, map=[]):
    map.append(c1)
    if equal(c1, c2):
        return True
    m = len(c1)
    for i in range(m):
        if len(set(c1[i % m] + c1[(i + 1) % m])) == 4:
            new_c = move_parallel(c1, i, m)
            if not visited(new_c, map):
                if equiv_recursive(new_c, c2, map):
                    return True
    return False


# Move parallel lines
def move_parallel(c, i, m):
    new_c = list(c)
    new_c[i % m] = list(c[(i + 1) % m])
    new_c[(i + 1) % m] = list(c[i % m])
    if i == 0 or i == m - 1:
        initial_pos = 1
        if i == m - 1:
            initial_pos = m - 1
        shift = list(new_c)
        for j in range(m):
            new_c[j] = list(shift[(initial_pos + j) % m])
    return new_c


# A move is only valid if we have AB|AC|BC. This occurs iff the consecutive
# lines have exactly 3 points
# Or if we have AB|CD. This occurs iff the consecutive lines have 4 points


# Get the list of possible configurations from the given configuration
def get_possible_moves(c):
    moves = []
    m = len(c)
    for i in range(m):

        # If we can pass a point trough a line
        if len(set(c[i % m] + c[(i + 1) % m] + c[(i + 2) % m])) == 3:
            new_c = list(c)
            new_c[i % m] = list(c[(i + 2) % m])
            new_c[(i + 2) % m] = list(c[i % m])
            if i == 0 or i == m - 2:
                initial_pos = 2
                if i == m - 2:
                    initial_pos = m - 2
                shift = list(new_c)
                for j in range(m):
                    new_c[j] = list(shift[(initial_pos + j) % m])
            moves.append(new_c)

        # If we can interchange parallel lines
        if len(set(c[i % m] + c[(i + 1) % m])) == 4:
            new_c = move_parallel(c, i, m)
            moves.append(new_c)

    return moves


# Returns True iff the configuration given is already in the map
def visited(c, map):
    for i in range(len(map)):
        if equal(map[i], c):
            return True
    return False


# Recursive function to visit neighbors
def visit_neighbors(c):
    moves = get_possible_moves(c)
    for move in moves:
        if not visited(move, map):
            map.append(move)
            visit_neighbors(move)


# Recall that ...|AB|CD|... and ...|CD|AB|... are the same
# (if the dots are the same)
def clean_map(map):
    cleaned_map = []
    for configuration in map:
        in_list = False
        for cleaned_configuration in cleaned_map:
            if equiv(configuration, cleaned_configuration):
                in_list = True
        if not in_list:
            cleaned_map.append(configuration)
    return cleaned_map


# Print as lines
def print_pretty(my_list):
    alphabet = "ABCDEFGHIJKLMNOPQRST"
    for configuration in my_list:
        s = "|"
        for line in configuration:
            s += alphabet[line[0]] + alphabet[line[1]] + "|"
        print(s)


# ------------------------------------------------------------

n = 5

# Generate the initial convex configuration
initial_configuration = []
for i in range(n):
  for j in range(i):
    initial_configuration.append([j,i])
print(initial_configuration)

# ------------------------------------------------------------

map = []
adjacency_matrix = []
visit_neighbors(initial_configuration)
cleaned_map = clean_map(map)
print(len(map))
print(len(cleaned_map))

print("Cleaned map:")
print_pretty(cleaned_map)