import streamlit as st

# 페이지 제목과 설명
st.title("YOU ARE RICKROLLED")

video_html = """
    <video id="myVideo" width="100%" height="auto" autoplay muted playsinline>
        <source src="rickroll.mp4" type="video/mp4">
        브라우저가 video 태그를 지원하지 않습니다.
    </video>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            var video = document.getElementById('myVideo');
            video.play();
        });
    </script>
"""

st.markdown(video_html, unsafe_allow_html=True)
