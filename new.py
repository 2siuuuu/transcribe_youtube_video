import assemblyai as aai
import yt_dlp
from dotenv import load_dotenv
import os

load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.environ.get("DEFAULT_API_KEY")
if not api_key:
    raise ValueError("환경 변수에 DEFAULT_API_KEY가 설정되어 있지 않습니다. .env 파일을 확인해주세요.")


def transcribe_youtube_video(video_url: str, api_key: str) -> str:
    """
    Transcribe a YouTube video given its URL.
    
    Args:
        video_url: The YouTube video URL to transcribe
        api_key: AssemblyAI API key
    
    Returns:
        The transcript text
    """
    # Configure yt-dlp options for audio extraction
    ydl_opts = {
    'format': 'm4a/bestaudio/best',
    'outtmpl': '%(id)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }],
    'ffmpeg_location': 'C:\\vscode\\AssemblyAI\\Youtube_Trancribe\\ffmpeg-2025-03-13-git-958c46800e-essentials_build\\bin\\'  # FFmpeg 경로 추가
    }

    # Download and extract audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
        # Get video ID from info dict
        info = ydl.extract_info(video_url, download=False)
        video_id = info['id']
    
    # Configure AssemblyAI
    aai.settings.api_key = api_key
    
    # Transcribe the downloaded audio file
    transcriber = aai.Transcriber()
    #transcript = transcriber.transcribe(f"{video_id}.m4a")
    transcript = transcriber.transcribe("qn738hVKJe4.m4a")
    
    return transcript.text

transcript_text = transcribe_youtube_video("https://www.youtube.com/watch?v=qn738hVKJe4", api_key)

# transcript_text 안에 있는 데이터를 output.txt 파일로 출력하는 코드
with open("output.txt", "w") as f:
    f.write(transcript_text)



#print(transcript_text)
