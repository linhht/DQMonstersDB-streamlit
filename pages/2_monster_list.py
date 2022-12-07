import streamlit as st
from helper_functions import APINames, get_monster_list

# dummy data with test files
# with open('json_test_files/read_monsters.json') as json_file:
#     monster_list = json.load(json_file)

# FastAPI connection
monster_list = get_monster_list(APINames.API_GET_MONSTER_LIST)

st.markdown("## Monster List")
name_search = st.text_input("Search by Name")
family_search = st.selectbox("Search by Family",
                             ['SLIME', 'DRAGON', 'BEAST', 'BIRD', 'PLANT',
                              'BUG', 'DEVIL', 'UNDEAD', 'MATERIAL', '???'])

# Set up column table
name_column, family_column = st.columns(2)
name_column.subheader('Monster Name')
family_column.subheader('Family Type')

for monster in monster_list:
    idx = monster['id']
    name = monster['old_name']
    name_column.write(
        f"<a target='_self' href='monster_detail?id={idx}'>{name}</a>",
        unsafe_allow_html=True
    )
    family_column.write(monster['family']['family_eng'])