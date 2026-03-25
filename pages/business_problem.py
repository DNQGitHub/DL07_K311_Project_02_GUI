import streamlit as st
import components.sidebar as sidebar

started = False

def main():
    global started
    if not started:
        started = True
        sidebar.display()
        st.write("This is the Business Problem page")
    
main()