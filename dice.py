from random import *
import streamlit as st

st.title('Dice Simulator 1.0')
st.header('Click the button to roll the dice.')

def dice_roll():
    num=1

    dice={
        1:(" [---------]\n "
        "    |         |\n "
        "    |    o    |\n "
        "    |         |\n "
        "    [---------]\n "),
        2:(" [---------] "
        "    |         | "
        "    |   o o   | "
        "    |         | "
        "    [---------] "),
        3:(" [---------] "
        "    |         | "
        "    |  o o o  | "
        "    |         | "
        "    [---------] "),
        4:(" [---------] "
        "    |    o    | "
        "    |   o o   | "
        "    |    o    | "
        "    [---------] "),
        5:(" [---------] "
        "    |  o   o  | "
        "    |    o    | "
        "    |  o   o  | "
        "    [---------] "),
        6:(" [---------] "
        "    |  o   o  | "
        "    |  o   o  | "
        "    |  o   o  | "
        "    [---------] ")
    }

    
    return dice[num]



if st.button('Roll Dice'):
    run=dice_roll()
    st.text(run)