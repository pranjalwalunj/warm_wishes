dobs = [
    {
        "name": "John",
        "birth_date": "1996-03-01"
    },
    {
        "name": "Jim",
        "birth_date": "1997-08-27"
    },
    {
        "name": "Sally",
        "birth_date": "2003-04-14"
    },
    {
        "name": "Emma",
        "birth_date": "2002-09-30"
    },
    {
        "name": "Cyber",
        "birth_date": "1998-02-28"
    },
    {
        "name": "Linda",
        "birth_date": "1999-12-12"
    },
    {
        "name": "Ivan",
        "birth_date": "1996-12-31"
    },
    {
        "name": "Ruby",
        "birth_date": "1995-06-19"
    },
    {
        "name": "James",
        "birth_date": "1997-07-17"
    },
    {
        "name": "Glen",
        "birth_date": "2000-04-22"
    }
]
# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# element = [dobs[index] for index in num]
# print(element)

a = input("enter name from list given : ")
for i in list(dobs):
    if i["name"] == a:
        print(i["birth_date"])
