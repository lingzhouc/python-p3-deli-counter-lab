katz_deli = []

# new person 
def take_a_number(deli_list, name):
    deli_list.append(name)
    place = deli_list.index(name) + 1

    print(f"Welcome, {name}. You are number {place} in line.")

take_a_number(katz_deli, "Ada")
take_a_number(katz_deli, "Grace")
take_a_number(katz_deli, "Kent")

# shows everyone their current place in line
def line(deli_list):
    if (deli_list):
        message = "The line is currently:"
        for name in deli_list:
            place = deli_list.index(name) + 1
            message += f" {place}. {name}"
        print(message)
    else:
        print("The line is currently empty.")
        
line(katz_deli)

# call out next in line
def now_serving(deli_list):
    if(deli_list):
        serving_person = deli_list.pop(0)
        print(f"Currently serving {serving_person}.")
    else:
        print("There is nobody waiting to be served!")

now_serving(katz_deli)


# alternative line() using while loop

# def line(deli_line_list_queue):
#     if (deli_line_list_queue):
#         text = "The line is currently:"
#         num = 0
#         while num < len(deli_line_list_queue):
#             text += f" {num+1}. {deli_line_list_queue[num]}"
#             num += 1
#         print(text)
#     else:
#         print("The line is currently empty.")