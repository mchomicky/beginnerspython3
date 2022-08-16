def pascals_triangle(n):
    if n == 1:
        return [[1]]
    else:
        result = pascals_triangle(n-1)
        prev_row = result[-1]
        curr_row = [prev_row[0]]
        for i in range(1, len(prev_row) + 1):
            num = prev_row[i-1] if i > 0 else 0
            num += prev_row[i] if i < len(prev_row) else 0
            curr_row.append(num)
        result.append(curr_row)
        return result


print(pascals_triangle(5))
