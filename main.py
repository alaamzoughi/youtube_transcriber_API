from youtube_transcript_api import YouTubeTranscriptApi


def trans():
# retrieve the available transcripts
  transcript_list = YouTubeTranscriptApi.list_transcripts('qVTAB8Z2VmA', ['en'])

# iterate over all available transcripts
  for transcript in transcript_list:

    # fetch the actual transcript data
     print(transcript.fetch())

trans()     