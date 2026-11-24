bio_data =[ {"name":"Faysal","Age":"15","proffesion":"student"},
            {"name":"Adil","Age":"1","proffesion":"Baby"},    
            {"name":"Emdad","Age":"61","proffesion":"Engineer"},    
            {"name":"Aysha","Age":"22","proffesion":"Businessman"}
            ]

for data in bio_data:

    print(data["name"],f"Age = {data["Age"]}",f"Proffesion = {data["proffesion"]}",sep=", ")
#print(data["name"])