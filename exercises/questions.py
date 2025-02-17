questions = ["What are rice?", "What is my name?"]
answers = [["Salt", "Rice"], ["Naruto", "Elara", "Daniel"]]
corrects = [1, 1]


# for question in questions:
#     print(question)
#     for index, answer in enumerate(answers[questions.index(question)]):
#         print(index, answer)

score = 0

for question, answer_list, correct in zip(questions, answers, corrects):
    print(question)
    for index, answer in enumerate(answer_list):
        print(index + 1, answer)

    answer_choice = int(input("Select the correct answer:")) - 1

    if answer_choice == correct:
        print("Correct")
        score += 1
    else:
        print(f"Wrong, the correct answer is {correct + 1}")

print(f"Your score is {score} of {len(corrects)}!")

"""
My teacher used json module and dictionaries.
His solution is a bit complicated but useful with 
large contents. 


Maybe?
"""