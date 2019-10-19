def maxIncreaseKeepingSkyline(city_matrix) -> int:
    n = len(city_matrix)
    front_view = [0]*(n)
    side_view = [0]*(n)
    # side_view = [max(row) for row in grid]

    for i in range(n):
        max_row = 0
        for j in range(n):
            if city_matrix[i][j] > max_row:
                max_row = city_matrix[i][j]
            # calculate the side view
            front_view[j] = max(front_view[j], city_matrix[i][j])
        side_view[i] = max_row
    total_height_diff = 0
    for i in range(n):
        for j in range(n):
            new_heigth = min(side_view[i], front_view[j])
            heigth_diff = new_heigth - city_matrix[i][j]
            total_height_diff += heigth_diff
    return total_height_diff
