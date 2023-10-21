tree = {
    "4096": [
        {
            "2048": [
                {
                    "1024": [
                        {},
                        {}
                    ]
                },
                {
                    "1024": [
                        {},
                        {}
                    ]
                }
            ]
        },
        {
            "2048": [
                {
                    "1024": [
                        {},
                        {}
                    ]
                },
                {
                    "1024": [
                        {},
                        {}
                    ]
                }
            ]
        }
    ]
}


def update_tree(tree, key_path, new_value):
    if not key_path:
        return new_value

    current_key = key_path[0]
    if isinstance(tree, list):
        index = int(current_key)
        tree[index] = update_tree(tree[index], key_path[1:], new_value)
    elif isinstance(tree, dict):
        tree[current_key] = update_tree(tree[current_key], key_path[1:], new_value)

    return tree


key_path = ["4096", "0", "2048", "0", "1024", "0"]
new_value = 1022

updated_tree = update_tree(tree, key_path, new_value)
print(updated_tree)
