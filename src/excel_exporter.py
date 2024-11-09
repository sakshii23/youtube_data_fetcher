import pandas as pd

def save_to_excel(video_data, comment_data, filename='YouTube_Data.xlsx'):
    """Save the video and comment data to an Excel file."""
    df_videos = pd.DataFrame(video_data)
    df_comments = pd.DataFrame(comment_data)
    
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df_videos.to_excel(writer, sheet_name='Video Data', index=False)
        df_comments.to_excel(writer, sheet_name='Comments Data', index=False)






