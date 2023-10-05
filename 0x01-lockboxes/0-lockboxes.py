#!/usr/bin/python3
""" Determine if all the boxes can be opened."""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened.

    Args:
        boxes : A list of boxes

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    visited = [False] * len(boxes)
    visited[0] = True """ First box already unlocked """

    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            """
                If the key corresponds to a box
                that hasn't been visited, mark as visited
            """
            if not visited[key]:
                visited[key] = True
                queue.append(key)
    return all(visited)


if __name__ == "__main__":
    boxes = [[1], [2], [3], [0]]
    result = canUnlockAll(boxes)
    print(result)
