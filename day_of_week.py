# def is_weekend(day):
#     match day:
#         case "Sunday":
#             return True
#         case 2:        
#             return False
#         case 3:
#             return True
#         case 4: 
#             return False
#         case 5:
#             return True
#         case 6: 
#             return False
#         case 7:
#             return True
#         case _:
#             return False
        
# print(is_weekend(6))        


# def is_weekend(day):
#     match day:
#         case "Saturday" | "Sunday":
#             return True
#         case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#             return False
#         case _:
#             return False
        
# print(is_weekend("Friday"))        

# def birthday_guess(month, day):
#     # Month and day
#     match month:
#         case "January" | "February":
#             season = "Winter"
#         case "March" | "April" | "May":
#             season = "Spring"
#         case "June" | "July" | "August":
#             season = "Summer"
#         case "September" | "October" | "November":
#             season = "Autumn" 

#         case _:

#             season = "Unknown"


#     # day forecast
#     if 1 <= day <= 10:
#         day_range = "1-10"
#     elif 11 <= day <= 20:
#         day_range = "11-20"
#     else:
#         day_range = "21-31"

#     return f"Your birthday date {season} season and {day_range} between ."

# # information 
# month = input("Birth month please: ").capitalize()
# day = int(input("Please enter your brithday: "))

# # 
# print(birthday_guess(month, day))
               