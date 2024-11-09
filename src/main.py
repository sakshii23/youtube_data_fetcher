from youtube_api import get_channel_id, get_video_details, get_comments
from excel_exporter import save_to_excel

def main(channel_handle):
    try:
        # Fetch the channel ID using the channel handle
        channel_id = get_channel_id(channel_handle)
        
        # Fetch video details for the channel
        video_data = get_video_details(channel_id)
        
        # Fetch comments for each video
        all_comments = []
        for video in video_data:
            comments = get_comments(video['Video ID'])
            all_comments.extend(comments)
        
        # Save data to an Excel file
        save_to_excel(video_data, all_comments)
        print("Data has been successfully fetched and saved.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    channel_handle = 'https://www.youtube.com/@channelhandle'  # Replace with the actual channel handle
    main(channel_handle)






