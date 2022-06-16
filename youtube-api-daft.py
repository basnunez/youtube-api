from googleapiclient.discovery import build
import pandas as pd
from IPython.display import JSON

api_key = 'AIzaSyD1kEYSHiFM_fyzCDGvZlwBldvDRhCt6lM'

channel_ids = ['UC_kRDKYrUlrbtrSiyu5Tflg',
               #Aqui pueden ir mas canales
              ]

api_service_name = "youtube"
api_version = "v3"

    # Get credentials and create an API client
youtube = build(
    api_service_name, api_version, developerKey=api_key)

def get_channel_stats(youtube, channel_ids):
    
    all_data = []
    
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=','.join(channel_ids)
    )
    
    response = request.execute()
    
    #loop a traves de los items
    for item in response['items']:
        data = {'channelName': item['snippet']['title'],
                'suscribers': item['statistics']['subscriberCount'],
                'views': item['statistics']['viewCount'],
                'totalViews': item['statistics']['videoCount'],
                'playlistId': item['contentDetails']['relatedPlaylists']['uploads']
               }
        all_data.append(data)
    return(pd.DataFrame(all_data))

channel_stats = get_channel_stats(youtube, channel_ids)
channel_stats
print('Proceso completado de manera exitosa!')