CHOICE_QST = 20
PASS_MARK = 15

def main():
	counter = 1
	count_correct = 0
	wrong_answer_list = []
	
	# Create a list for correct answers
	correct_answer = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
	
	# Students answer function
	student_answer()
	
	# Read the student's answer to a list
	stud_answers_list = read_answer()
	
	# Compare correct answers with students answer to check how many questions was answered right
	
	for index in range(CHOICE_QST):
		if correct_answer[index] == stud_answers_list[index]:
			count_correct += 1
		else:
			wrong_answer_list.append(index+1)
			
	print()
	input("Press (Enter) to continue and check how well you've done in this exam: ")
	if count_correct >= PASS_MARK:
		print("Congratulations. You have passed this exam.")
	else:
		print("Sorry!! You failed this exam. We'll be pleased to have you back next year.")
	
	print()
			
	# Display the total number of correctly answered questions
	print("Correctly Answered Questions:")
	print("You answered", count_correct, "questions correctly.")
	print()
	
	# Display the total number of incorrectly answered questions
	print("Incorrectly Answered Questions")
	print("You missed", len(wrong_answer_list), "questions.")
	print()
	
	# Lists showing the number of incorrectly answered questions
	
	print("These are the Question numbers you missed...")
	
	for wrong in wrong_answer_list:
		print(wrong, end="")
		if counter < len(wrong_answer_list):
			print(end=", ")
			counter += 1
	
	
# This section creates a list of choices that the student has picked and write them to an output file.
def student_answer():
	# Open a file to write students answers
	outfile = open("answers.txt", "w")
	
	print("From choice of A to D, select appropriate answers.")
	print("There are 20 multiple questions...")
	input("Press Enter to start: ")
	for qst in range(CHOICE_QST):
		ans = input("Answer question #" + str(qst+1) + ": ").upper()
		
		# Write your answer to the file
		outfile.write(ans + "\n")
		
	# Close the file
	outfile.close()
	

def read_answer():
	infile = open("answers.txt", "r")
	stud_ans = infile.readlines()
	
	for index in range(len(stud_ans)):
		stud_ans[index] = stud_ans[index].rstrip("\n")
	
	infile.close()
		
	return stud_ans
	
	
main()
	
	