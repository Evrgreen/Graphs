from collections import defaultdict


def earliest_ancestor(ancestors, starting_node):
    mapping = defaultdict(list)
    for link in ancestors:
        mapping[link[1]].append(link[0])

    work_stack = []
    visited = set()
    full_path = []
    work_stack.append([starting_node])
    while len(work_stack) > 0:
        current_path = work_stack.pop()
        print(current_path)
        current_node = current_path[-1]
        if current_node not in visited:
            visited.add(current_node)
            if neighbors := mapping[current_node]:
                for neighbor in neighbors:
                    work_stack.append(current_path + [neighbor])
            elif len(current_path) > 1:
                full_path.append(current_path)
    if full_path:
        longest = max(sorted(full_path, key=lambda item:
                             item[-1]), key=lambda item: len(item))
        return longest[-1]
    return -1


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 9)
