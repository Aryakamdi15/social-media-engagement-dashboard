from googleapiclient.discovery import build
import pandas as pd

API_KEY = "YOUR_API_KEY"

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

# Example channel (TED)
channel_id = "UCX6OQ3DkcsbYNE6H8uQQuVA"

request = youtube.search().list(
    part="snippet",
    channelId=channel_id,
    maxResults=20,
    order="date",
    type="video"
)

response = request.execute()

video_ids = []

for item in response["items"]:
    video_ids.append(item["id"]["videoId"])

request = youtube.videos().list(
    part="snippet,statistics",
    id=",".join(video_ids)
)

response = request.execute()

videos = []

for item in response["items"]:
    videos.append({
        "Title": item["snippet"]["title"],
        "Published": item["snippet"]["publishedAt"],
        "Views": item["statistics"].get("viewCount", 0),
        "Likes": item["statistics"].get("likeCount", 0),
        "Comments": item["statistics"].get("commentCount", 0)
    })

df = pd.DataFrame(videos)

df.to_csv("data/youtube_data.csv", index=False)

print(df.head())

print("CSV Saved Successfully!")