import sqlalchemy
import controllers.db_utils as db_utils

def get_profile_info(id):
    db = db_utils.Database()
    return db.get_profile_info(id)

def get_profile_achievements(id):
    db = db_utils.Database()
    return db.get_profile_achievements(id)


if __name__ == "__main__":
    print("***Profile controller***")
    key = "0"
    while key != "9":
        print("1 - get_profile_info(id)")
        print("2 - get_profile_achievements(id)")
        print("9 - exit")
        key = input("Make a choice: ")
        if key == "1":
            id = int(input("Id: "))
            print(get_profile_info(id))
        if key == "2":
            id = int(input("Id: "))
            print(get_profile_achievements(id))