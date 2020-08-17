from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi
import json

app = Flask(__name__)


@app.route('/transcribe/<videoId>')
def trans(videoId):
    # retrieve the available transcripts
    transcript_list = YouTubeTranscriptApi.list_transcripts(videoId, ['en'])
    list = []
    # iterate over all available transcripts
    for transcript in transcript_list:
        # fetch the actual transcript data
        list.append(transcript.fetch())

    return json.dumps(list)


trans(videoId="qVTAB8Z2VmA")

if __name__ == '__main__':
    app.run()