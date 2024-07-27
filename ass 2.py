def find_runner_up(scores):

    unique_scores = list(set(scores))
   
    unique_scores.sort(reverse=True)
    
    return unique_scores[1]

scores = [2 ,3 ,6 ,6 ,5]
runner_up = find_runner_up(scores)
print(f"The runner-up score is: {runner_up}")
