from data import database as db

def summary():
    data = db.get_all()
    income = sum(t[1] for t in data if t[3]=='income')
    expense = sum(t[1] for t in data if t[3]=='expense')
    return income, expense

def category_breakdown():
    data = db.get_all()
    result = {}
    for t in data:
        if t[3]=='expense':
            result[t[2]] = result.get(t[2],0)+t[1]
    return result
