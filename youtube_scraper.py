import os
from googleapiclient.discovery import build
import re

def get_video_id(url):
    """
    Extract video ID from YouTube URL.
    """
    video_id = None
    match = re.search(r"(?<=v=)[^&#]+", url)
    if not match:
        match = re.search(r"(?<=be/)[^&#]+", url)
    if match:
        video_id = match.group(0)
    return video_id

def get_comments(video_url, api_key, max_comments):
    video_id = get_video_id(video_url)
    if not video_id:
        raise ValueError("Invalid YouTube URL")

    youtube = build('youtube', 'v3', developerKey=api_key)
    
    comments = []
    
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=min(max_comments, 100),
        textFormat='plainText'
    )
    
    while request and len(comments) < max_comments:
        response = request.execute()
        
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
        
        if 'nextPageToken' in response:
            request = youtube.commentThreads().list_next(
                previous_request=request,
                previous_response=response
            )
        else:
            request = None
            
    return comments[:max_comments] 