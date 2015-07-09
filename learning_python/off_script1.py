user_prompt1 = "Enter a bunch of numbers (separated by commas): "
user_prompt2 = "Which number do you want to remove? "
user_list = []
user_input1 = input(user_prompt1)
user_list.append(int(user_input1))
user_input2 = input(user_prompt2)
user_choice = int(user_input2)

print("You entered: " + str(user_list))
print("I am going to remove all the " + str(user_input2) + "'s from that list.")

for i in range(0,user_list.count(user_choice)):
    user_list.remove(user_choice)

print(user_list)


