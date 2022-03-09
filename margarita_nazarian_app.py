#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 01:29:07 2022

@author: margaritanazarian
"""

# streamlit run
# /Users/margaritanazarian/Desktop/Cours/streamlit_app/margarita_nazarian_app.py

# Import Libraries

import webbrowser
import statistics
import pandas as pd
import streamlit as st
from PIL import Image
#import plotly.express as px


# Import data & files

#PATH = "/Users/margaritanazarian/Desktop/streamlit_app/"

#data = pd.read_csv(PATH + "table.csv")
#data = data.iloc[:, 1:]

#dishwasher_image = Image.open(PATH + "dishwasher.png")
#oven_image = Image.open(PATH + "oven.png")
#fridge_image = Image.open(PATH + "fridge.png")
#microwave_image = Image.open(PATH + "microwave.png")
#hob_image = Image.open(PATH + "hob.png")
#line_image = Image.open(PATH + "line.png")
#logo = Image.open(PATH + "logo_but.png")

# Layout

st.get_option("theme.base")
st.get_option("theme.primaryColor")
st.get_option("theme.secondaryBackgroundColor")
st.get_option("theme.textColor")
st.get_option("theme.font")

st.set_page_config(
    layout="wide",
    page_title="Kitchen appliances: market prices")


#def main_image():
   # if sidebar_selectbox == "Dishwasher":
  #      st.image(dishwasher_image)
#
  #  elif sidebar_selectbox == "Oven":
 #       st.image(oven_image)

 #   elif sidebar_selectbox == "Fridge":
 #       st.image(fridge_image)

 #   elif sidebar_selectbox == "Microwave":
  #      st.image(microwave_image)

  #  else:
    #    st.image(hob_image)


# Sidebar

st.sidebar.title("   ")
st.sidebar.title("   ")
sidebar_selectbox = st.sidebar.selectbox(
    "What are you planning to buy? Select a product.",
    ("Dishwasher",
     "Oven",
     "Fridge",
     "Microwave",
     "Hob"))
sidebar_slider = st.sidebar.slider(
    "What is your budget? (in €)",
    min_value=0,
    max_value=5000,
    value=400)

# Selected data

#table = data.loc[data["Category"] == sidebar_selectbox]


#def figures():
#    average_price = ("%.2f" % statistics.mean(table["Price"]))
#
 #   quantity = len(table["Price"])
#
 #   max_price = max(table["Price"])
#
 #   min_price = min(table["Price"])

 #   st.header(f"""Average market price: {average_price}€""")
  #  st.subheader(f"""Maximum price: {max_price}€""")
  #  st.subheader(f"""Minimum price: {min_price}€""")
  #  st.subheader(f"""From the prices of {quantity} products""")
 #   st.markdown("---")
 #   st.subheader("Price distribution:")


#def histogram():
 #   fig = px.histogram(table["Price"], nbins=(20))
#
 #   my_value = sidebar_slider
#
 #   fig.update_layout(
  #      showlegend=False,
   #     plot_bgcolor="white",
    #    margin=dict(t=10, l=10, b=10, r=10)
    #)
#
 #   fig.update_traces(marker_color="darkseagreen")
#
 #   fig.update_layout(bargap=0.1)
#
 #   fig.update_layout(shapes=[
  #      dict(
   #         type="line",
    #        yref="paper", y0=0, y1=1,
     #       xref="x", x0=my_value, x1=my_value
      #  )
  #  ])
#
 #   fig.add_annotation(x=my_value,
  #                     text="Your budget",
   #                    showarrow=False,
    #                   yshift=100,
     #                  bordercolor="black",
      #                 borderwidth=2,
       #                borderpad=4,
        #               bgcolor="whitesmoke",
         #              font=dict(
          #                 family="Courier New, monospace",
           #                size=16,
            #               color="black"
             #          ))

  #  st.plotly_chart(fig, use_container_width=True)


#def bugdet_vs_market():
 #   my_value = sidebar_slider
#
  #  under_budget = len([table["Price"]
  #                     for row in table["Price"] if row < my_value])
 #   budget_vs_market = (under_budget / (len(table["Price"]))) * 100
  #  budget_vs_market = ("%.2f" % budget_vs_market)

  #  st.markdown(
      #  f"""***Your budget is higher than the price of {budget_vs_market} % of the products***""")


def source():
    url = "www.but.fr"

    st.image(logo, width=50)

    st.markdown(
        f"""***All products used for the price analysis are coming from {url}.***""",
        unsafe_allow_html=True)


#def shop_now():
 #   if sidebar_selectbox == "Dishwasher":
  #      url = "https://www.but.fr/electromenager/lavage/tous-les-lave-vaisselle/index-c11201.html"

   # elif sidebar_selectbox == "Oven":
   #     url = "https://www.but.fr/electromenager/cuisson/four/index-c11167.html"

   # elif sidebar_selectbox == "Fridge":
    #    url = "https://www.but.fr/electromenager/froid/tous-les-refrigerateurs/index-c11184.html"

   # elif sidebar_selectbox == "Microwave":
    #    url = "https://www.but.fr/electromenager/cuisson/micro-ondes/index-c11168.html"

   # else:
    #    url = "https://www.but.fr/electromenager/cuisson/plaque-de-cuisson/index-c11171.html"

   # if st.button(
      #      "Press this button to get to the web page of the product you selected"):
      #  webbrowser.open_new_tab(url)


def main():
    st.title("CURRENT MARKET PRICES: AM I OVERPAYING ?")
    st.title("     ")

    col1, col2 = st.columns([2, 1])

    with col1:
        #figures()
        #histogram()
        #bugdet_vs_market()
        st.markdown("---")
        source()
        st.markdown("---")
        #shop_now()

    #with col2:
      #  main_image()

    st.title("     ")
    st.title("     ")

    #st.image(line_image)


if __name__ == "__main__":
    main()
