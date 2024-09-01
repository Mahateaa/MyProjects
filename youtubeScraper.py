from pytube import YouTube

# List of video URLs you want to scrape
video_urls = [
    "https://youtu.be/arj7oStGLkU?si=UxrTfU77oBV53JkC",
    "https://youtu.be/eIho2S0ZahI?si=YlHlhb5yRLCzYh1c",
    "https://youtu.be/6Af6b_wyiwI?si=LqZ4RHlyY2MDUFdw"
]

# Function to get video details
def get_video_details(url):
    try:
        video = YouTube(url)
        details = {
            "Title": video.title,
            "Views": video.views,
            "Length (seconds)": video.length,
            "Author": video.author,
            "Description": video.description,
            "Publish Date": video.publish_date,
            "Rating": video.rating,
            "URL": url
        }
        return details
    except Exception as e:
        print(f"Error fetching details for {url}: {e}")
        return None

# Scrape details for each video
video_details_list = []
for url in video_urls:
    details = get_video_details(url)
    if details:
        video_details_list.append(details)

# Print the scraped data
for video in video_details_list:
    print(video)
