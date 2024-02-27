def presenteer(dictionary, totaal):
    for key, value in dictionary.items():
        print(f"{key} : {value} euro")
    print("==========================")
    print(f"Totaal : {totaal} euro")

my_dict = {"vis": 10, "vlees": 25, "overig": 15}
total = 50
presenteer(my_dict, total)