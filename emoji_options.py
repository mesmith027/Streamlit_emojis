import streamlit as st
import requests
import json

st.set_page_config(page_title= "Streamlit Emojis",page_icon="random")

def get_key(val, my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key

    return "key doesn't exist"

st.title("Emoji options in Streamlit")
st.write("""
An app to help you find all the emojis that are available to display in a Streamlit app! :star:
""")

# load options from GitHub
url = "https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json"
resp = requests.get(url)
data = json.loads(resp.text)

# make sidebar
with st.sidebar:
    st.subheader("Search by name:")
    options = st.multiselect("Names of Emojis",data.keys())

    st.subheader("Search by emoji:")

    emoji = st.multiselect("Emojis", data.values())

col1,col2 = st.columns(2)
with col1:
    st.subheader("Emoji name:")
    if len(options) > 0:
        for i in options:
            st.write("`:{a}:` = {b}".format(a=i,b=data[i]))

with col2:
    st.subheader("Emoji:")
    if len(emoji) > 0:
        emoji_list = [data.values()]
        for i in emoji:
            key = get_key(i,data)
            st.write("{b} = `:{a}:`".format(a=key,b=i))

#data = json.loads("https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json")
check = st.sidebar.checkbox("Show all options")
if check:
    st.write("---")
    st.json(data)
