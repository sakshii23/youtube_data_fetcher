from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from the .env file
API_KEY = os.getenv('YOUTUBE_API_KEY')

if not API_KEY:
    raise Exception("API_KEY is missing in .env file")

youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_channel_id(handle):
    """Fetch the channel ID from the YouTube URL."""
    # Remove 'https://www.youtube.com/@' from the channel handle to get just the username part
    username = handle.replace('https://www.youtube.com/@', '')

    # Search the channel by the handle to fetch the channel ID
    response = youtube.search().list(part='snippet', q=username, type='channel').execute()

    if 'items' not in response or len(response['items']) == 0:
        raise Exception(f"No channel found for handle: {handle}")
    
    return response['items'][0]['id']['channelId']

def get_video_details(channel_id):
    """Fetch video details from the YouTube channel, including statistics and duration."""
    videos = []
    next_page_token = None

    while True:
        response = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for item in response['items']:
            if item['id']['kind'] == 'youtube#video':
                video_id = item['id']['videoId']
                
                # Fetch detailed video information including view count, like count, etc.
                video_stats = youtube.videos().list(
                    part='snippet,statistics,contentDetails',
                    id=video_id
                ).execute()
                
                video_data = video_stats['items'][0]
                
                # Extract video data
                video_details = {
                    'Video ID': video_data['id'],
                    'Title': video_data['snippet']['title'],
                    'Description': video_data['snippet']['description'],
                    'Published Date': video_data['snippet']['publishedAt'],
                    'View Count': video_data['statistics'].get('viewCount', 'N/A'),
                    'Like Count': video_data['statistics'].get('likeCount', 'N/A'),
                    'Comment Count': video_data['statistics'].get('commentCount', 'N/A'),
                    'Duration': video_data['contentDetails']['duration'],
                    'Thumbnail URL': video_data['snippet']['thumbnails']['high']['url'],
                }
                videos.append(video_details)

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return videos


def get_comments(video_id):
    """Fetch the comments and replies for a given video."""
    comments = []
    request = youtube.commentThreads().list(part='snippet', videoId=video_id, maxResults=100)
    response = request.execute()

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comment_data = {
            'Video ID': video_id,
            'Comment ID': item['id'],
            'Comment Text': comment['textDisplay'],
            'Author Name': comment['authorDisplayName'],
            'Published Date': comment['publishedAt'],
            'Like Count': comment['likeCount'],
            'Reply To': None
        }
        comments.append(comment_data)
        # Fetch replies if any
        if 'replies' in item:
            for reply in item['replies']['comments']:
                reply_data = {
                    'Video ID': video_id,
                    'Comment ID': reply['id'],
                    'Comment Text': reply['snippet']['textDisplay'],
                    'Author Name': reply['snippet']['authorDisplayName'],
                    'Published Date': reply['snippet']['publishedAt'],
                    'Like Count': reply['snippet']['likeCount'],
                    'Reply To': item['id']
                }
                comments.append(reply_data)
    return comments

