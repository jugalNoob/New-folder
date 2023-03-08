import streamlit as st
from pytube import YouTube
import time


st.set_page_config(page_title="YouTube Downloader", page_icon=":tv:")
st.title("YouTube Downloader")

url = st.text_input("Enter YouTube video URL:")
resolution = st.selectbox("Select resolution:", ["720p", "480p", "360p", "240p", "144p"])
location = st.text_input("Enter file location (leave blank for current directory):")
download_button = st.button("Download")


if download_button:
    try:
        st.write("Downloading...")
        start_time = time.time()
        yt = YouTube(url)
        if resolution == "720p":
            video = yt.streams.filter(res="720p").first()
        elif resolution == "480p":
            video = yt.streams.filter(res="480p").first()
        elif resolution == "360p":
            video = yt.streams.filter(res="360p").first()
        elif resolution == "240p":
            video = yt.streams.filter(res="240p").first()
        elif resolution == "144p":
            video = yt.streams.filter(res="144p").first()
        else:
            st.write("Invalid resolution selected.")
            st.stop()
        if location == "":
            video.download()
        else:
            video.download(location)
        end_time = time.time()
        st.write("Download complete!")
        st.write(f"Download time: {end_time - start_time:.2f} seconds")
    except Exception as e:
        st.write(f"An error occurred: {e}")
