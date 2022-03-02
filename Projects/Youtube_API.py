# https://developers.google.com/explorer-help/code-samples#python

from googleapiclient import discovery
import json

API_KEY = "AIzaSyAjTIveFo_fc-V3J1fBRVOH0N9uPFdCTn8"
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
youtube = discovery.build(API_SERVICE_NAME, API_VERSION,developerKey=API_KEY)


def main():
    request = youtube.activities().list(
        part="contentDetails",
        channelId="UCCezIgC97PvUuR4_gbFUs5g"
    )
    response = request.execute()

    # Formatting the JSON API output into readable format 
    PrettyJson = json.dumps(response, indent=4, separators=(',', ': '))

    print(PrettyJson)

def mostpopular_video_details():
  
    # Call the videos.list method to retrieve video info
    list_videos_byid = youtube.videos().list(
        part = "id, snippet, contentDetails, statistics",
        chart ='mostPopular', regionCode ='IN', 
        maxResults = 4).execute()
  
    # extracting the results from search response
    results = list_videos_byid.get("items", [])
      
    # empty list to store video details
    videos = []
    n = 1
    for result in results:
        videos.append("% s (% s) (% s) (% s) (% s) (% s)"
                        % (n, result["snippet"]["title"],
                        result['snippet']['description'],
                        result["snippet"]["publishedAt"],
                                result['contentDetails'],
                                   result["statistics"]))
        n = n + 1
    print ("Videos:\n", "\n".join(videos), "\n")

if __name__ == "__main__":
    main()