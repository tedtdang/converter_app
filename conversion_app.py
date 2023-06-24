import tempfile
from pathlib import Path as p

import streamlit as st

from Converter import AudioConverter

st.set_page_config('🎈 Video / Audio Conversion')
st.title('🎈 Video / Audio Converter')
## Upload file(s) ##
st.sidebar.header('Upload file')
uploaded_files = st.sidebar.file_uploader("Choose a file",
                                          type=list(AudioConverter.audio_extensions.
                                                    union(AudioConverter.video_extensions)),
                                          accept_multiple_files=True)
extension = st.sidebar.selectbox('Choose file extension to convert',
                                 list(AudioConverter.audio_extensions))
print(extension)
## Display gif generation parameters once file has been uploaded ##
if uploaded_files and extension:
    st.subheader('Convert file')
    conversion_button = st.button('Convert file(s) now!')
    if conversion_button:
        for uploaded_file in uploaded_files:
            # Save uploaded file to a temporary file on disk
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(uploaded_file.read())
                temp_file.flush()
                temp_file.close()

            converter = AudioConverter(temp_file.name)
            if conversion_button:
                try:
                    converted_file = converter.convert_to_audio(extension)
                    download_file_name = str(p(uploaded_file.name).with_suffix('').with_suffix(extension))
                    # Add a download button for the converted file
                    with open(converted_file, "rb") as f:
                        st.download_button(
                            label="Download Audio File",
                            data=f.read(),
                            file_name=download_file_name,
                            mime=f"audio/{extension.lstrip('.')}"
                        )
                except RuntimeError as e:
                    st.error(str(e))
                else:
                    st.warning("Click the 'Convert' button to convert the video to audio.")
else:
    st.warning('👈 Upload video / audio files')
