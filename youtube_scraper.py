import re
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
from tqdm import tqdm


def extract_video_id(url):
    """Extract the video ID from a YouTube URL."""
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    return None


def get_comments(video_url, api_key, max_comments=100):
    """
    Scrape comments from a YouTube video.
    Args:
        video_url (str): The URL of the YouTube video.
        api_key (str): YouTube Data API key.
        max_comments (int): Maximum number of comments to fetch.
    Returns:
        List[str]: List of comment texts.
    """
    video_id = extract_video_id(video_url)
    if not video_id:
        raise ValueError('Invalid YouTube URL')

    youtube = build('youtube', 'v3', developerKey=api_key)
    comments = []
    next_page_token = None

    with tqdm(total=max_comments, desc='Fetching comments') as pbar:
        while len(comments) < max_comments:
            request = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                pageToken=next_page_token,
                maxResults=min(100, max_comments - len(comments)),
                textFormat='plainText'
            )
            response = request.execute()
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append(comment)
                pbar.update(1)
                if len(comments) >= max_comments:
                    break
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break
    return comments 