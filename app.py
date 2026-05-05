import streamlit as st
from bank import Bank

bank = Bank()

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Create Account",
        "Deposit",
        "Withdraw",
        "Show Details",
        "Delete Account"
    ]
)

# CREATE ACCOUNT
if menu == "Create Account":
    st.subheader("Create Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("PIN", type="password")

    if st.button("Create"):
        result = bank.create_account(name, age, email, int(pin))

        if isinstance(result, dict):
            st.success("Account Created")
            st.json(result)
        else:
            st.error(result)

# DEPOSIT
elif menu == "Deposit":
    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        st.success(bank.deposit(acc, int(pin), amount))

# WITHDRAW
elif menu == "Withdraw":
    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        st.success(bank.withdraw(acc, int(pin), amount))

# SHOW DETAILS
elif menu == "Show Details":
    st.subheader("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        user = bank.login(acc, int(pin))

        if user:
            st.json(user)
        else:
            st.error("Invalid Credentials")

# DELETE
elif menu == "Delete Account":
    st.subheader("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        st.warning(bank.delete_account(acc, int(pin)))