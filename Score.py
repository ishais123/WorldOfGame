
def add_score(difficulty):
    score = difficulty*3+5
    try:
        with open('Scores.txt', 'r') as file:
             score_file = file.readlines()
             current_score = score_file[0]
             final_score = score + int(current_score)
        with open('Scores.txt', 'w') as file:
            file.write(str(final_score))
    except IndexError:
        with open('Scores.txt', 'w') as file:
            file.write(str(score))


add_score(3)
