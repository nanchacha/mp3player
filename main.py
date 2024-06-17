import streamlit as st
import os
# from mutagen.mp3 import MP3

# MP3 파일이 저장된 디렉토리 경로
MP3_DIR = "./files"

def list_mp3_files(directory):
    """주어진 디렉토리 내의 MP3 파일 리스트를 반환"""
    return [f for f in os.listdir(directory) if f.endswith('.mp3')]



def main():
    st.title("MP3 파일 재생기")

    mp3_files = list_mp3_files(MP3_DIR)

    if not mp3_files:
        st.write("MP3 파일이 없습니다.")
        return

    selected_mp3 = st.selectbox("재생할 MP3 파일을 선택하세요:", mp3_files)

    if selected_mp3:
        file_path = os.path.join(MP3_DIR, selected_mp3)
        st.audio(file_path)

if __name__ == "__main__":
    main()
