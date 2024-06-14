
def ask_question(question, options):
  """Asks a question and validates user input."""
  print(question)
  for i, option in enumerate(options):
    print(f"{i+1}. {option}")
  while True:
    answer = input("Enter your answer (1-4): ")
    try:
      answer = int(answer) - 1
      if 0 <= answer < len(options):
        return answer
      else:
        print("Invalid answer. Please enter a number between 1 and 4.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def check_answer(question, answer, options, correct_index):
  """Checks the user's answer and provides feedback."""
  if answer == correct_index:
    print("Correct!")
  else:
    print(f"Incorrect. The correct answer is {options[correct_index]}")
  print(f"Question: {question}")
  print(f"Your answer: {options[answer]}")

def main():
  """Runs the quiz application."""
  questions = [
    {"question": "What is the capital of France?", "options": ["London", "Paris", "Berlin", "Rome"], "correct_index": 1},
    {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "correct_index": 2},
    {"question": "Who wrote the play Hamlet?", "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "J.R.R. Tolkien"], "correct_index": 0},
  ]
  score = 0
  for question_data in questions:
    question = question_data["question"]
    options = question_data["options"]
    correct_index = question_data["correct_index"]
    answer = ask_question(question, options)
    check_answer(question, answer, options, correct_index)
    if answer == correct_index:
      score += 1
  print(f"Final Score: {score} out of {len(questions)}")

if __name__ == "__main__":
  main()
