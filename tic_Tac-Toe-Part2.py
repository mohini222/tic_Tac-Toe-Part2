# print()
# print("                                       PART 2                            ")
# print()
# print("****************************")
# print("WELCOME TO TIC TAC TAO GAME")
# print("****************************")
# print()
 
# print("T1"+"|"+"T2"+"|"+"T3")
# print("__"+"|"+"__"+"|"+"__")
# print("M1"+"|"+"M2"+"|"+"M3")
# print("__"+"|"+"__"+"|"+"__")
# print("B1"+"|"+"B2"+"|"+"B3")

# list1 = ["T1","T2","T2","T3","M1","M2","M3","B1","B2","B3"]

# print("______________________________")
# print()

# P1=input("ENTER PLAYER FIRST NAME :")
# print("SECOND PLAYER WILL BE COMPUTER ITSELF")
# print()

# dic={"T1":" ","T2":" ","T3":" ",
#     "M1":" ","M2":" ","M3":" ",
#      "B1":" ","B2":" ","B3":" "}
# player=1
# total_move=0
# check=0
# game="run"
# def checkwins():
#     if player==0:
#         if dic["T1"]=="X"and dic["T2"]=="X" and dic["T3"]=="X":
#             print("!****",P1,"WON THIS GAME🎉🎉🎉🎉 🥳🥳","****!")
#             return 1
#         if dic["T1"]=="X"and dic["M1"]=="X" and dic["B1"]=="X":
#             print("!****",P1,"WON THIS GAME🎉🎉🎉🎉 🥳🥳","****!")
#             return 1
#         if dic["T2"]=="X"and dic["M2"]=="X" and dic["B2"]=="X":
#             print("!****",P1,"WON THIS GAME🎉🎉🎉🎉 🥳🥳","****!")
#             return 1
#         if dic["T3"]=="X"and dic["M3"]=="X" and dic["B3"]=="X":
#             print("!****",P1,"WON THIS GAME🎉🎉🎉🎉 🥳🥳","****!")
#             return 1
#         if dic["M1"]=="X"and dic["M2"]=="X" and dic["M3"]=="X":
#             print("!****",P1,"WON THIS GAME🎉🎉🎉🎉 🥳🥳","****!")
#             return 1
#         if dic["B1"]=="X"and dic["B2"]=="X" and dic["B3"]=="X":
#             print("!****",P1,"WON THIS GAME🎉🎉🎉🎉 🥳🥳","****!")
#             return 1
#         if dic["T1"]=="X"and dic["M2"]=="X" and dic["B3"]=="X":
#             print("!****",P1,"WON THIS GAME🎉🎉🎉🎉 🥳🥳","****!")
#             return 1
#         if dic["T3"]=="X"and dic["M2"]=="X" and dic["B1"]=="X":
#             print("!****",P1,"WON THIS GAME🎉🎉🎉🎉 🥳🥳","****!")
#             return 1
#     if player==1:
#         if dic["T1"]=="0"and dic["T2"]=="0" and dic["T3"]=="0":
#             print("!**** COMPUTER WON THIS GAME🎉🎉🎉🎉 🥳🥳","****!")
#             return 1
#         if dic["T1"]=="0"and dic["M1"]=="0" and dic["B1"]=="0":
#             print("!**** COMPUTER WON THIS GAME🎉🎉🎉🎉 🥳🥳","****!")
#             return 1
#         if dic["T2"]=="0"and dic["M2"]=="0" and dic["B2"]=="0":
#             print("!**** COMPUTER WON THIS GAME🎉🎉🎉🎉 🥳🥳","****!")
#             return 1
#         if dic["T3"]=="0"and dic["M3"]=="0" and dic["B3"]=="0":
#             print("!**** COMPUTER WON THIS GAME🎉🎉🎉🎉 🥳🥳","****!")
#             return 1
#         if dic["M1"]=="0"and dic["M2"]=="0" and dic["M3"]=="0":
#             print("!**** COMPUTER WON THIS GAME🎉🎉🎉🎉 🥳🥳","****!")
#             return 1
#         if dic["B1"]=="0"and dic["B2"]=="0" and dic["B3"]=="0":
#             print("!**** COMPUTER WON THIS GAME🎉🎉🎉🎉 🥳🥳","****!")
#             return 1
#         if dic["T1"]=="0"and dic["M2"]=="0" and dic["B3"]=="0":
#             print("!**** COMPUTER WON THIS GAME🎉🎉🎉🎉 🥳🥳","****!")
#             return 1
#         if dic["T3"]=="0"and dic["M2"]=="0" and dic["B1"]=="0":
#             print("!**** COMPUTER WON THIS GAME🎉🎉🎉🎉 🥳🥳","****!")
#             return 1
# def boardshow():
#     print(dic["T1"]+"|"+dic["T2"]+"|"+dic["T3"]) 
#     print("_"+"|"+"_"+"|"+"_")
#     print(dic["M1"]+"|"+dic["M2"]+"|"+dic["M3"])
#     print("_"+"|"+"_"+"|"+"_")
#     print(dic["B1"]+"|"+dic["B2"]+"|"+dic["B3"])
#     print() 
# while game=="run":
#     if player==1:
#         if total_move==9 or check==1:
#             print("!****** GAME ENDS NOW THANK YOU ******!")
#             game="end"
#             break
#             print()
        
#         print(P1,end=" ")
#         player1_input=input("ENTER YOUR PLACE OF 'X' : ")
#         list1.remove(player1_input)
#         if player1_input.upper() in dic and dic[player1_input]==" ":
#             dic[player1_input.upper()]="X"
#             boardshow()
#             player=0
#             total_move+=1
#             check=checkwins()
#         else:
#             print("invalid input")
#     else:
#         if player==0:
#             if total_move==9 or check==1:
#                 print("!****** GAME ENDS NOW THANK YOU ******!")
#                 game="end"
#                 break
#                 print()
#             import random
#             player0_input=(random.choice(list1))
#             list1.remove(player0_input)    
#             if player0_input.upper() and dic[player0_input]==" ":
#                 dic[player0_input.upper()]="0"
#                 boardshow()
#                 player=1
#                 total_move+=1
#                 check=checkwins()
                
                
                
# https://www.codecademy.com/workspaces/63665489e5f0ddb2df3700f2
# LINK FOR GAME