import numpy
import pandas

august_prof_dev = pandas.read_csv("August_Professional_Development2023-03-13_12_31_18.csv", dtype= {
    "Select your school": str,
    "First Name": str,
    "Last Name": str,
    "Select your training days and slots (50 individuals per slot; booked-out slots will be disabled)": str
})