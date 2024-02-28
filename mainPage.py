import streamlit as st
import pandas as pd
import random

st.title("Random Topic Generator")

df = pd.DataFrame(
    [
       {"name": "侑", "topic": ""},
       {"name": "愛", "topic": ""},
       {"name": "元", "topic": ""},
       {"name": "哲", "topic": ""},
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic")
names = edited_df["name"].tolist()
topics = edited_df["topic"].tolist()
shuffled_topics = topics.copy()

button_disabled = True
topic_count = 0
for topic in topics:
    if topic == "":
        st.error("Please fill in all topics")
        break
    topic_count += 1

if topic_count == len(edited_df):
    button_disabled = False

if st.button("Generate Random Order", disabled=button_disabled):
    while True:
        random.shuffle(shuffled_topics)
        for i in range(len(edited_df)):
            if shuffled_topics[i] == topics[i]:
                break
        if i < 3:
            continue
        elif i == 3: 
            break

    order = list(range(1, len(edited_df)+1))
    random.shuffle(order)

    for i in range(len(edited_df)):
        teacher_name = edited_df[edited_df["topic"] == shuffled_topics[i]]["name"].values[0]
        st.write(f"考官：{teacher_name} / 考生：{names[i]} / 主題：{shuffled_topics[i]} / 順序：{order[i]}")

