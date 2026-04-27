import customtkinter as ctk
from data import database as db
from core import analytics
import matplotlib.pyplot as plt

class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Expense AI Advanced")
        self.geometry("900x600")
        db.init_db()

        self.build()
        self.refresh()

    def build(self):
        self.balance = ctk.CTkLabel(self,text="Balance",font=("Arial",24))
        self.balance.pack(pady=10)

        self.amount = ctk.CTkEntry(self,placeholder_text="Amount")
        self.amount.pack()

        self.cat = ctk.CTkEntry(self,placeholder_text="Category")
        self.cat.pack()

        ctk.CTkButton(self,text="Add Income",command=self.add_income).pack(pady=5)
        ctk.CTkButton(self,text="Add Expense",command=self.add_expense).pack(pady=5)
        ctk.CTkButton(self,text="Show Chart",command=self.show_chart).pack(pady=10)

        self.log = ctk.CTkTextbox(self,height=200)
        self.log.pack(fill="both",expand=True,padx=20,pady=10)

    def add_income(self):
        db.add_transaction(float(self.amount.get()), self.cat.get(), "income", "today")
        self.refresh()

    def add_expense(self):
        db.add_transaction(float(self.amount.get()), self.cat.get(), "expense", "today")
        self.refresh()

    def refresh(self):
        income, expense = analytics.summary()
        self.balance.configure(text=f"Balance: {income-expense}")

        self.log.delete("1.0","end")
        for t in db.get_all():
            self.log.insert("end",f"{t}\n")

    def show_chart(self):
        data = analytics.category_breakdown()
        if not data: return
        plt.figure()
        plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
        plt.title("Expense Breakdown")
        plt.show()
