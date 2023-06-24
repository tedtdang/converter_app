import tempfile
from pathlib import Path as p

import streamlit as st

from Converter import AudioConverter

st.set_page_config('🎈 Video / Audio Conversion')
st.title('🎈 Video / Audio Converter')
## Upload file ##
st.sidebar.header('Upload file')
uploaded_file = st.sidebar.file_uploader("Choose a file", type=list(AudioConverter.audio_extensions.
                                                                    union(AudioConverter.video_extensions)))
extension = st.sidebar.selectbox('Choose file extension to convert',
                                 list(AudioConverter.audio_extensions))
print(extension)
## Display gif generation parameters once file has been uploaded ##
if uploaded_file and extension:
    ## Save to temp file ##
    # tfile = tempfile.NamedTemporaryFile(delete=False)
    # tfile.write(uploaded_file.read())

    # ## Open file ##
    # clip = VideoFileClip(tfile.name)
    #
    # st.session_state.clip_duration = clip.duration
    #
    # ## Input widgets ##
    # st.sidebar.header('Input parameters')
    # selected_resolution_scaling = st.sidebar.slider('Scaling of video resolution', 0.0, 1.0, 0.5 )
    # selected_speedx = st.sidebar.slider('Playback speed', 0.1, 10.0, 5.0)
    # selected_export_range = st.sidebar.slider('Duration range to export', 0, int(st.session_state.clip_duration), (0, int(st.session_state.clip_duration) ))
    #
    # ## Resizing of video ##
    # clip = clip.resize(selected_resolution_scaling)
    #
    # st.session_state.clip_width = clip.w
    # st.session_state.clip_height = clip.h
    # st.session_state.clip_duration = clip.duration
    # st.session_state.clip_total_frames = clip.duration * clip.fps
    # st.session_state.clip_fps = st.sidebar.slider('FPS', 10, 60, 20)
    #
    # ## Display output ##
    # st.subheader('Metrics')
    # col1, col2, col3, col4, col5 = st.columns(5)
    # col1.metric('Width', st.session_state.clip_width, 'pixels')
    # col2.metric('Height', st.session_state.clip_height, 'pixels')
    # col3.metric('Duration', st.session_state.clip_duration, 'seconds')
    # col4.metric('FPS', st.session_state.clip_fps, '')
    # col5.metric('Total Frames', st.session_state.clip_total_frames, 'frames')
    #
    # # Extract video frame as a display image
    # st.subheader('Preview')
    #
    # with st.expander('Show image'):
    #   selected_frame = st.slider('Preview a time frame (s)', 0, int(st.session_state.clip_duration), int(np.median(st.session_state.clip_duration)) )
    #   clip.save_frame('frame.gif', t=selected_frame)
    #   frame_image = Image.open('frame.gif')
    #   st.image(frame_image)
    #
    # ## Print image parameters ##
    # st.subheader('Image parameters')
    # with st.expander('Show image parameters'):
    #   st.write(f'File name: `{uploaded_file.name}`')
    #   st.write('Image size:', frame_image.size)
    #   st.write('Video resolution scaling', selected_resolution_scaling)
    #   st.write('Speed playback:', selected_speedx)
    #   st.write('Export duration:', selected_export_range)
    #   st.write('Frames per second (FPS):', st.session_state.clip_fps)

    ## Export animated GIF ##
    st.subheader('Convert file')
    conversion_button = st.button('Convert file now!')
    if conversion_button:
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
                    bytes = f.read()
                    st.download_button(
                        label="Download Audio File",
                        data=bytes,
                        file_name=download_file_name,
                        mime="audio/mp3"
                    )
            except RuntimeError as e:
                st.error(str(e))
            else:
                st.warning("Click the 'Convert' button to convert the video to audio.")

## Default page ##
else:
    st.warning('👈 Upload a video file')
