from io import StringIO
import streamlit as st
from Maze import Maze

# page = st.sidebar.selectbox('Выбери страницу', ['лабиринт', 'пещера'])

tab1, tab2 = st.tabs(["Загрузить из файла", "Сгенерировать"])
with tab1:
    uploaded_file = st.file_uploader(label="Выбери файл с описанием лабиринта")
    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read().replace('\n', '')
        maze = Maze(1,1)
        maze.save_to_file_(file_path='maze.txt', data=string_data)
        maze.load_from_file(file_path='maze.txt')
        maze.draw()
        st.image('maze.jpg', use_column_width=True)
    else:
        pass
with tab2:
    col1, col2 = st.columns(2)
    with col1:
        rows = int(st.number_input("Количество строк", placeholder=2, min_value=1, max_value=50, step=1))
    with col2:
        cols = int(st.number_input("Количество столбцов", placeholder=2, min_value=1, max_value=50, step=1))
    maze = Maze(rows, cols)
    maze.generate_maze()
    maze.draw()
    maze.save_to_file('maze.txt')
    maze.load_from_file(file_path='maze.txt')
    st.image('maze.jpg', use_column_width=True)
    st.title('Решение лабиринта')
    col3, col4, col5, col6 = st.columns(4)
    with col3:
        row_start = int(st.number_input("Стартовая строка", placeholder=2, min_value=1, max_value=50, step=1)) - 1
    with col4:
        col_start = int(st.number_input("Стартовый столобец", placeholder=2, min_value=1, max_value=50, step=1)) - 1
    with col5:
        row_end = int(st.number_input("Конечная строка", placeholder=2, min_value=1, max_value=50, step=1)) - 1
    with col6:
        col_end = int(st.number_input("Конечный столбец", placeholder=2, min_value=1, max_value=50, step=1)) - 1
    maze.solve_maze((row_start, col_start), (row_end, col_end))
    maze.draw(with_solution=True)
    maze.save_to_file('maze.txt')
    maze.load_from_file(file_path='maze.txt')
    st.image('maze.jpg', use_column_width=True)


