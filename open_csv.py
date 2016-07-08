import pandas as pd 

# Funcao que abre arquivo CSV e retorna lista com nome e link
def open_csv_and_return_data(csv_file):
    df = pd.read_csv(csv_file)
    video_name = df.Videotitle_link
    video_link = df.Videotitle_link_link
    return [video_name,video_link]
