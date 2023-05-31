def main():
    file = open("inputs/day8.txt", "r")

    matrix_of_trees = []
    for line in file:
        line_list = []
        line_list[:0] = line.strip()
        matrix_of_trees.append(line_list)
    file.close()

    SIZE = len(matrix_of_trees)

    #Part one 
    sum = SIZE * 4 - 4
    coords = set()
    for i in range(1, SIZE-1):
        max_left = matrix_of_trees[i][0]
        max_right = matrix_of_trees[i][-1]
        max_top = matrix_of_trees[0][i]
        max_bottom = matrix_of_trees[-1][i]

        for j in range(1, SIZE-1):

            left_elem=matrix_of_trees[i][j]
            if left_elem > max_left:
                coords.add((i, j))
                max_left = left_elem

            right_elem = matrix_of_trees[i][-(j+1)]
            if right_elem > max_right:
                coords.add((i, SIZE-(j+1)))
                max_right = right_elem

            top_elem = matrix_of_trees[j][i]
            if top_elem > max_top:
                coords.add((j, i))
                max_top = top_elem

            bottom_elem = matrix_of_trees[-(j+1)][i]
            if bottom_elem > max_bottom:
                coords.add((SIZE-(j+1), i))
                max_bottom = bottom_elem

    #Part two
    max_scenic_score = 0
    for i in range(1, SIZE-1):
        for j in range(1, SIZE-1):
            right_distance_count = 0
            left_distance_count = 0
            top_distance_count = 0
            bottom_distance_count = 0
            
            #go right 
            for r in range(j + 1, SIZE):
                right_distance_count = right_distance_count + 1
                if matrix_of_trees[i][r] >= matrix_of_trees[i][j]:
                    break
            #go left
            for l in range(0, j):
                left_distance_count = left_distance_count + 1
                if matrix_of_trees[i][j-l-1] >= matrix_of_trees[i][j]:
                    break
            #go down
            for d in range(i + 1, SIZE):
                bottom_distance_count = bottom_distance_count + 1
                if matrix_of_trees[d][j] >= matrix_of_trees[i][j]:
                    break
            #go up
            for u in range(0, i):
                top_distance_count = top_distance_count + 1
                if matrix_of_trees[i-u-1][j] >= matrix_of_trees[i][j]:
                    break

            current_score =  right_distance_count * left_distance_count * top_distance_count * bottom_distance_count
            if current_score >= max_scenic_score: 
                max_scenic_score = current_score

    print("DAY 8. - Part one")
    print(f"THE ANSWER: {sum + len(coords)} trees are visible from outside the grid.")

    print("DAY 8. - Part two")
    print(f"THE ANSWER: The highest scenic score possible for any tree is : {max_scenic_score}")

if __name__== "__main__":
    main()