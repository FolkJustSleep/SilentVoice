# import streamlit as st
# import cv2
# import numpy as np
# import time
# from PIL import Image
# from src.camera.camera import find_available_cameras, capture_images

# st.set_page_config(
#     page_title="ASL Alphabet Detection",
#     page_icon="📷",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# if 'camera_active' not in st.session_state:
#     st.session_state.camera_active = False
# if 'detection_results' not in st.session_state:
#     st.session_state.detection_results = []
# if 'camera_feed' not in st.session_state:
#     st.session_state.camera_feed = None
# if 'available_cameras' not in st.session_state:
#     st.session_state.available_cameras = None
# if 'selected_camera' not in st.session_state:
#     st.session_state.selected_camera = 0


# # CSS section
# st.markdown("""
# <style>
#     * {
#         margin: 0;
#         padding: 0;
#         box-sizing: border-box;
#     }
    
#     .main-container {
#         background: linear-gradient(135deg, #f1f1f1 0%, #e8f4fd 100%);
#         min-height: 100vh;
#         position: relative;
#         overflow: hidden;
#     }
    
#     .header-section {
#         background: white;
#         padding: 20px 0;
#         box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.08);
#         margin-bottom: 40px;
#     }
    
#     .header-title {
#         color: #1ab6df;
#         font-size: 24px;
#         font-weight: 700;
#         text-align: center;
#         margin: 0;
#     }
    
#     .main-title {
#         color: #2d2d2d;
#         font-size: 36px;
#         font-weight: 700;
#         text-align: center;
#         margin: 20px 0 10px 0;
#     }
    
#     .subtitle {
#         color: #191919;
#         font-size: 18px;
#         font-weight: 300;
#         text-align: center;
#         margin-bottom: 40px;
#     }
    
#     .video-card {
#         background: green;
#         border-radius: 30px 0px 0px 30px;
#         width: 100%;
#         height: 750px;
#         margin-bottom: 20px;
#     }
    
#     .results-card {
#         background: red;
#         border-radius: 0px 30px 30px 0px;
#         width: 100%;
#         height: 750px;
#     }
    
#     .results-title {
#         color: #1c1c1c;
#         font-size: 24px;
#         font-weight: 500;
#         margin: 20px 20px 20px 20px;
#         padding: 0;
#     }
    
#     .results-display {
#         background: white;
#         border: 1px solid #c0c0c0;
#         border-radius: 13px;
#         padding: 20px;
#         min-height: 300px;
#         margin-bottom: 20px;
#         font-size: 18px;
#         line-height: 1.6;
#     }
    
#     .camera-status {
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         margin: 20px 0;
#         gap: 10px;
#     }
    
#     .status-indicator {
#         width: 18px;
#         height: 18px;
#         border-radius: 50%;
#         background-color: #ff0000;
#     }
    
#     .status-indicator.active {
#         background-color: #00ff00;
#     }
    
#     .status-text {
#         color: #333;
#         font-weight: 700;
#         font-size: 18px;
#     }
    
#     .control-buttons {
#         display: flex;
#         justify-content: center;
#         gap: 20px;
#         margin: 20px 0;
#     }
    
#     .control-button {
#         padding: 15px 30px;
#         border: none;
#         border-radius: 10px;
#         font-size: 16px;
#         font-weight: 600;
#         cursor: pointer;
#         transition: all 0.3s ease;
#     }
    
#     .play-button {
#         background-color: #1ab6df;
#         color: white;
#     }
    
#     .play-button:hover {
#         background-color: #1590b3;
#         transform: translateY(-2px);
#     }
    
#     .stop-button {
#         background-color: #ff4444;
#         color: white;
#     }
    
#     .stop-button:hover {
#         background-color: #cc0000;
#         transform: translateY(-2px);
#     }
    
#     .video-button {
#         background-color: #c0c0c0;
#         color: white;
#     }
    
#     .video-button:hover {
#         background-color: #a0a0a0;
#         transform: translateY(-2px);
#     }
    
#     .clear-button {
#         width: 100%;
#         padding: 15px;
#         background-color: transparent;
#         border: 2px solid #1ab6df;
#         border-radius: 13px;
#         color: #1ab6df;
#         font-size: 18px;
#         font-weight: 300;
#         cursor: pointer;
#         transition: all 0.3s ease;
#         margin-bottom: 20px;
#     }
    
#     .clear-button:hover {
#         background-color: rgba(26, 182, 223, 0.1);
#         transform: translateY(-1px);
#     }
    
#     .footer-section {
#         background-color: #0b547f;
#         color: white;
#         text-align: center;
#         padding: 30px 0;
#         margin-top: 50px;
#         border-radius: 30px 30px 0 0;
#     }
    
#     .tap-to-speak {
#         text-align: center;
#         color: #636363;
#         font-size: 14px;
#         margin: 20px 0;
#     }
    
#     .stButton > button {
#         width: 100%;
#     }
    
#     .advance-settings {
#         background: white;
#         border-radius: 20px;
#         padding: 30px;
#         margin: 40px 0;
#         box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
#     }
    
#     .advance-settings h2 {
#         color: #1ab6df;
#         text-align: center;
#         margin-bottom: 30px;
#         font-size: 28px;
#         font-weight: 600;
#     }
    
#     .advance-settings h3 {
#         color: #2d2d2d;
#         margin-bottom: 20px;
#         font-size: 20px;
#         font-weight: 500;
#         border-bottom: 2px solid #1ab6df;
#         padding-bottom: 10px;
#     }
    
#     .settings-column {
#         background: #f8f9fa;
#         border-radius: 15px;
#         padding: 20px;
#         margin: 10px 0;
#         border: 1px solid #e9ecef;
#     }
# </style>
# """, unsafe_allow_html = True)



# # HTML section
# #st.markdown('<div class="main-container">', unsafe_allow_html = True)

# # st.markdown("""
# # <div class="header-section">
# #     <h1 class="header-title">ML Project</h1>
# # </div>
# # """, unsafe_allow_html=True)

# st.markdown("""
# <h1 class="main-title">ASL Alphabet Detection</h1>
# <p class="subtitle">Real-time American Sign Language Recognition with Voice Output</p>
# """, unsafe_allow_html = True)

# # display flex function
# col1, col2 = st.columns([2, 1])

# with col1:
#     st.markdown('<div class="video-card">', unsafe_allow_html = True)

#     video_placeholder = st.empty()
    
#     if st.session_state.camera_active:
#         try:
#             camera_index = st.session_state.selected_camera if st.session_state.available_cameras else 0
#             cap = cv2.VideoCapture(camera_index)
#             ret, frame = cap.read()
#             if ret:
#                 frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                 video_placeholder.image(frame_rgb, caption=f"Camera {camera_index} Feed", use_container_width=True)
#             else:
#                 video_placeholder.image("https://via.placeholder.com/800x600/f0f0f0/666666?text=Camera+Not+Available", 
#                                        caption="Camera Feed", use_container_width=True)
#             cap.release()
#         except Exception as e:
#             video_placeholder.image("https://via.placeholder.com/800x600/f0f0f0/666666?text=Camera+Error", 
#                                    caption="Camera Feed", use_container_width=True)
#             st.error(f"Camera error: {str(e)}")
#     else:
#         video_placeholder.image("https://via.placeholder.com/800x600/f0f0f0/666666?text=Click+Start+to+begin+detection", 
#                                caption="Camera Feed", use_container_width=True)
    
#     status_indicator_class = "active" if st.session_state.camera_active else ""
#     status_text = "Camera: Active" if st.session_state.camera_active else "Camera: Inactive"
    
#     st.markdown(f"""
#     <div class="camera-status">
#         <div class="status-indicator {status_indicator_class}"></div>
#         <span class="status-text">{status_text}</span>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown('<div class="control-buttons">', unsafe_allow_html=True)
    
#     col_btn1, col_btn2, col_btn3 = st.columns(3)
    
#     with col_btn1:
#         if st.button("▶️ Start", key="start_btn"):
#             st.session_state.camera_active = True
#             st.rerun()
    
#     with col_btn2:
#         if st.button("📹 Video", key="video_btn"):
#             pass
    
#     with col_btn3:
#         if st.button("⏹️ Stop", key="stop_btn"):
#             st.session_state.camera_active = False
#             st.rerun()
    
#     st.markdown('</div>', unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)

# with col2:
#     results_text = "\n".join(st.session_state.detection_results) if st.session_state.detection_results else "No detection results yet..."

#     st.markdown('''
#     <div class="results-card">
#         <h2 class="results-title">Detection Result</h2>
#         <div class="results-display">
#             {results_text}
#         </div>
#     '''
#     , unsafe_allow_html=True)
        
#     # st.markdown(f"""
#     # <div class="results-display">
#     #     {results_text}
#     # </div>
#     # """, unsafe_allow_html=True)
    
#     if st.button("Clear", key="clear_btn"):
#         st.session_state.detection_results = []
#         st.rerun()
    
#     st.markdown("""
#     <div class="tap-to-speak">Tap to Speak</div>
#     """, unsafe_allow_html=True)
    
#     if st.button("🔊 Speak Results", key="speak_btn"):
#         if st.session_state.detection_results:
#             st.success("Speaking detection results...")
#         else:
#             st.warning("No results to speak")
    
#     st.markdown('</div>', unsafe_allow_html=True)

# if st.session_state.camera_active:
#     if st.button("🔍 Detect Sign", key="detect_btn"):
#         detected_letters = ["A", "S", "L"]
#         new_detection = f"Detected: {' - '.join(detected_letters)} at {time.strftime('%H:%M:%S')}"
#         st.session_state.detection_results.append(new_detection)
#         if len(st.session_state.detection_results) > 10:
#             st.session_state.detection_results = st.session_state.detection_results[-10:]
#         st.rerun()

# # # Advance Settings Section
# # st.markdown("---")
# # st.markdown('<div class="advance-settings">', unsafe_allow_html=True)
# # st.markdown("## ⚙️ Advance Settings")

# # # Create columns for advance settings
# # adv_col1, adv_col2, adv_col3 = st.columns(3)

# # with adv_col1:
# #     st.markdown('<div class="settings-column">', unsafe_allow_html=True)
# #     st.markdown("### 📷 Camera Settings")
# #     if st.button("🔍 Find Available Cameras", key="find_cameras_btn"):
# #         with st.spinner("Searching for cameras..."):
# #             st.session_state.available_cameras = find_available_cameras()
# #         st.success(f"Found {len(st.session_state.available_cameras)} camera(s)")

# #     if st.session_state.available_cameras:
# #         st.write("**Available Cameras:**")
# #         for i, cam_idx in enumerate(st.session_state.available_cameras):
# #             st.write(f"• Camera {cam_idx}")
        
# #         st.session_state.selected_camera = st.selectbox(
# #             "Select Camera:",
# #             st.session_state.available_cameras,
# #             index=0,
# #             key="camera_selector"
# #         )
# #     else:
# #         st.info("Click 'Find Available Cameras' to detect cameras")
# #     st.markdown('</div>', unsafe_allow_html=True)

# # with adv_col2:
# #     st.markdown('<div class="settings-column">', unsafe_allow_html=True)
# #     st.markdown("### 📊 Data Collection")
# #     num_classes = st.number_input("Number of Classes", min_value=1, max_value=26, value=3, key="num_classes")
# #     dataset_size = st.number_input("Images per Class", min_value=1, max_value=100, value=25, key="dataset_size")

# #     if st.button("📸 Start Data Collection", key="start_collection_btn"):
# #         if st.session_state.available_cameras:
# #             with st.spinner("Starting data collection..."):
# #                 success = capture_images(
# #                     number_of_classes=num_classes,
# #                     dataset_size=dataset_size,
# #                     camera_index=st.session_state.selected_camera
# #                 )
# #             if success:
# #                 st.success("Data collection completed!")
# #             else:
# #                 st.error("Data collection failed!")
# #         else:
# #             st.error("Please find available cameras first!")
# #     st.markdown('</div>', unsafe_allow_html=True)

# # with adv_col3:
# #     st.markdown('<div class="settings-column">', unsafe_allow_html=True)
# #     st.markdown("### 📝 Instructions")
# #     st.markdown("""
# #     **Steps to use:**
# #     1. Find Available Cameras
# #     2. Select your preferred camera
# #     3. Set number of classes and dataset size
# #     4. Start Data Collection (optional)
# #     5. Use main interface for detection
    
# #     **Tips:**
# #     - Ensure good lighting for data collection
# #     - Keep hand steady during capture
# #     - Use different angles for better training
# #     """)
# #     st.markdown('</div>', unsafe_allow_html=True)

# # st.markdown('</div>', unsafe_allow_html=True)
# # st.markdown("---")

# # st.markdown("""
# # <div class="footer-section">
# #     <p>© 2025 ML Project. All rights reserved.</p>
# # </div>
# # """, unsafe_allow_html=True)

# # st.markdown('</div>', unsafe_allow_html=True)

# auto_refresh = st.empty()
# if st.session_state.camera_active:
#     time.sleep(0.1)
#     auto_refresh.empty()
#     st.rerun()'



from src.camera.camera import find_available_cameras, capture_images
import streamlit as st

st.markdown("""
<style>
    /* Global reset - highest priority */
    * {
        margin: 0 !important;
        padding: 0 !important;
        box-sizing: border-box !important;
    }

    /* Force full viewport for html and body */
    html {
        margin: 0 !important;
        padding: 0 !important;
        width: 100% !important;
        height: 100% !important;
        overflow-x: hidden !important;
    }

    body {
        margin: 0 !important;
        padding: 0 !important;
        width: 100% !important;
        height: 100% !important;
        overflow-x: hidden !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif !important;
        background-color: #f1f1f1 !important;
    }

    /* Override ALL possible Streamlit containers with maximum specificity */
    div[data-testid="stAppViewContainer"],
    div[data-testid="stAppViewContainer"] > div,
    div[data-testid="stAppViewContainer"] > div > div,
    .stApp,
    .stApp > div,
    .stApp > div > div,
    .stApp > div > div > div,
    .main,
    .main > div,
    section.main,
    section.main > div,
    section.main > div > div,
    .stMain,
    .stMain > div,
    .stMain > div > div,
    .block-container,
    div.block-container,
    .main .block-container,
    section.main .block-container,
    div[class*="block-container"],
    div[class*="main"],
    div[class*="stMain"],
    div[class*="st-emotion-cache"] {
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
        max-width: none !important;
        min-width: 100% !important;
        left: 0 !important;
        right: 0 !important;
        top: 0 !important;
    }

    /* Target all emotion-cache classes that Streamlit uses */
    div[class*="st-emotion-cache-"],
    div[class*="e1f1d6gn"],
    div[class*="e4man"],
    div[class*="ea3mdgi"],
    div[class*="e1tzin5v"] {
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
        max-width: none !important;
    }

    /* Specific targeting for common Streamlit container classes */
    .st-emotion-cache-4rsbii,
    .st-emotion-cache-13ln4jf,
    .st-emotion-cache-16idsys,
    .st-emotion-cache-1d391kg,
    .st-emotion-cache-1wbqy5l,
    .e1f1d6gn0,
    .e1f1d6gn1,
    .e1f1d6gn2,
    .e1f1d6gn3 {
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
        max-width: none !important;
    }

    /* Force container to full width with CSS Grid override */
    .stApp {
        display: block !important;
        padding: 0 !important;
        margin: 0 !important;
        width: 100vw !important;
        max-width: 100vw !important;
        min-width: 100vw !important;
        overflow-x: hidden !important;
    }

    /* Override any flex or grid layouts that might constrain width */
    .stApp > div {
        display: block !important;
        width: 100vw !important;
        max-width: 100vw !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* Force full width using viewport units */
    [data-testid="stAppViewContainer"] {
        width: 100vw !important;
        max-width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
        left: 0 !important;
        right: 0 !important;
    }

    /* Remove any transform or positioning that might affect layout */
    .stApp,
    .stApp > div,
    [data-testid="stAppViewContainer"],
    .main,
    .stMain {
        transform: none !important;
        position: relative !important;
        left: 0 !important;
        right: 0 !important;
    }

    /* Streamlit Toolbar Customization */
    .stAppToolbar,
    [data-testid="stToolbar"],
    div[class*="stAppToolbar"] {
        background-color: white !important;
        border-bottom: 1px solid #e0e0e0 !important;
        height: 60px !important;
        width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    .stAppToolbar::before,
    [data-testid="stToolbar"]::before {
        content: "ML Project" !important;
        position: absolute !important;
        left: 20px !important;
        top: 50% !important;
        transform: translateY(-50%) !important;
        font-size: 20px !important;
        font-weight: 700 !important;
        color: #1ab6df !important;
        letter-spacing: -0.23px !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif !important;
        z-index: 1000 !important;
    }

    /* Hide default Streamlit toolbar content */
    .stAppToolbar > div,
    [data-testid="stToolbar"] > div {
        margin-left: 120px !important;
    }

    /* Additional override for any remaining containers */
    body > div,
    body > div > div,
    body > div > div > div {
        width: 100% !important;
        max-width: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    .container {
        position: relative;
        width: 100%;
        min-width: 1512px;
        min-height: 1314px;
        overflow: hidden;
        background-color: #f1f1f1;
    }

    /* Background Shapes */
        .background-wrapper {
        position: absolute;
        top: 183px;
        left: -21px;
        width: 1573px;
        height: 1102px;
        transform: rotate(-20.30deg);
    }

    .bg-shape {
        position: absolute;
        background-color: #1ab6df;
    }

    .bg-shape-1 {
        top: 1.5px;
        left: 279px;
        width: 375px;
        height: 394px;
        transform: rotate(1.74deg);
        filter: blur(137px);
    }

    .bg-shape-2 {
        top: 642px;
        left: 911px;
        width: 353px;
        height: 449px;
        transform: rotate(77.86deg);
        filter: blur(137px);
    }

    .bg-shape-3 {
        top: 371px;
        left: 54px;
        width: 430px;
        height: 391px;
        border-radius: 215px / 195.5px;
        transform: rotate(20.30deg);
        filter: blur(137px);
    }

    .bg-shape-4 {
        top: 258px;
        left: 1088px;
        width: 430px;
        height: 391px;
        border-radius: 215px / 195.5px;
        transform: rotate(20.30deg);
        filter: blur(137px);
    }

    .bg-image {
        position: absolute;
        transform: rotate(20.30deg);
        opacity: 0.6;
        pointer-events: none;
    }

    .bg-image-1 {
        top: -83px;
        left: 371px;
        width: 938px;
        height: 875px;
    }

    .bg-image-2 {
        top: 263px;
        left: 871px;
        width: 654px;
        height: 772px;
    }

    .bg-image-3 {
        top: 391px;
        left: 226px;
        width: 933px;
        height: 719px;
    }

    .bg-image-4 {
        top: -149px;
        left: 86px;
        width: 715px;
        height: 902px;
    }

    /* Header */
    .header {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 83px;
        z-index: 100;
    }

    .header-bg {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 83px;
        background-color: white;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.08);
    }

    .header-title {
        position: absolute;
        top: 32px;
        left: 129px;
        font-weight: 700;
        color: #1ab6df;
        font-size: 20px;
        letter-spacing: -0.23px;
        line-height: 20px;
        white-space: nowrap;
    }

    .menu-button {
        position: absolute;
        top: 33px;
        left: 1379px;
        width: 16px;
        height: 18px;
        background: transparent;
        border: none;
        cursor: pointer;
        padding: 0;
    }

    .menu-button:hover {
        opacity: 0.7;
    }

    /* Main Content */
    .main-content {
        position: absolute;
        top: 220px;
        left: 129px;
        width: 1254px;
        height: 873px;
        display: flex;
        flex-direction: column;
        gap: 68px;
    }

    .title-section {
        margin-left: 403px;
        width: 452px;
        height: 72px;
        display: flex;
        flex-direction: column;
        gap: 32px;
    }

    .main-title {
        margin-left: 51px;
        width: 346px;
        font-weight: 700;
        color: #2d2d2d;
        font-size: 30px;
        text-align: center;
        letter-spacing: -0.23px;
        line-height: 20px;
        white-space: nowrap;
    }

    .subtitle {
        width: 448px;
        font-weight: 300;
        color: #191919;
        font-size: 15px;
        text-align: center;
        letter-spacing: -0.23px;
        line-height: 20px;
        white-space: nowrap;
    }

    .content-wrapper {
        width: 1254px;
        display: flex;
        gap: 7px;
    }

    /* Video Card */
    .video-card {
        width: 859px;
        height: 733px;
        background-color: white;
        border-radius: 30px 0px 0px 30px;
    }

    .video-container {
        position: relative;
        height: 100%;
    }

    .video-placeholder {
        position: absolute;
        top: 0;
        left: 0;
        width: 859px;
        height: 547px;
        border-radius: 30px 0px 0px 0px;
        object-fit: cover;
        background: linear-gradient(135deg, rgba(26, 182, 223, 0.1), rgba(26, 182, 223, 0.05));
        backdrop-filter: blur(50px) brightness(100%);
    }

    .camera-status {
        position: absolute;
        top: 263px;
        left: 334px;
        width: 194px;
        height: 21px;
        display: flex;
        gap: 1px;
        align-items: center;
    }

    .status-indicator {
        width: 18px;
        height: 18px;
        background-color: #ff0000;
        border-radius: 9px;
    }

    .status-text {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 173px;
        height: 21px;
        font-weight: 700;
        color: black;
        font-size: 20px;
        text-align: center;
        letter-spacing: -0.23px;
        line-height: 20px;
        white-space: nowrap;
    }

    .controls-bg {
        position: absolute;
        top: 587px;
        left: 207px;
        width: 445px;
        height: 98px;
        background-color: #ebe5e5;
        border-radius: 18px;
        backdrop-filter: blur(192px) brightness(100%);
    }

    .control-button {
        position: absolute;
        top: 605px;
        width: 118px;
        height: 63px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        padding: 0;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .control-button:hover {
        opacity: 0.9;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }

    .control-button:active {
        transform: translateY(0);
    }

    .control-play {
        left: 229px;
        background-color: #1ab6df;
    }

    .control-play i {
        color: white;
        font-size: clamp(16px, 2.5vw, 20px);
    }

    .control-video {
        left: 371px;
        background-color: #c0c0c0;
    }

    .control-video i {
        color: white;
        font-size: clamp(16px, 2.5vw, 20px);
    }

    .control-stop {
        left: 513px;
        background-color: #ff0000;
    }

    .control-stop i {
        color: white;
        font-size: clamp(16px, 2.5vw, 20px);
    }

    /* Results Card */
    .results-card {
        position: relative;
        width: 392px;
        height: 733px;
        background-color: white;
        border-radius: 0px 30px 30px 0px;
    }

    .results-title {
        position: absolute;
        top: 47px;
        left: 43px;
        font-weight: 500;
        color: #1c1c1c;
        font-size: 20px;
        white-space: nowrap;
    }

    .results-display {
        position: absolute;
        top: 102px;
        left: 42px;
        width: 303px;
        height: 382px;
        background-color: white;
        border-radius: 13px;
        border: 0.75px solid #c0c0c0;
    }

    .clear-button {
        position: absolute;
        top: 512px;
        left: 43px;
        width: 305px;
        height: 55px;
        border-radius: 13px;
        border: 0.75px solid #1ab6df;
        background-color: transparent;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .clear-button:hover {
        background-color: rgba(26, 182, 223, 0.1);
        transform: translateY(-1px);
        box-shadow: 0 2px 8px rgba(26, 182, 223, 0.2);
    }

    .clear-button:active {
        transform: translateY(0);
    }

    .clear-button span {
        font-weight: 300;
        color: #1ab6df;
        font-size: 20px;
        text-align: center;
        letter-spacing: -0.23px;
        line-height: 20px;
    }

    .tap-to-speak {
        position: absolute;
        bottom: 15%;
        left: 50%;
        transform: translateX(-50%);
        font-weight: 400;
        color: #636363;
        font-size: clamp(10px, 1.5vw, 12px);
        white-space: nowrap;
    }

    .line-left {
        position: absolute;
        bottom: 16%;
        left: 10%;
        width: 25%;
        height: 2px;
        background-color: #636363;
    }

    .line-right {
        position: absolute;
        bottom: 16%;
        right: 10%;
        width: 25%;
        height: 2px;
        background-color: #636363;
    }

    .audio-wave-button {
        position: absolute;
        bottom: 5%;
        left: 10%;
        right: 10%;
        width: 80%;
        height: clamp(40px, 6vh, 55px);
        background-color: #1ab6df;
        border: none;
        border-radius: 15px;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
    }

    .audio-wave-button:hover {
        background-color: #1590b3;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(26, 182, 223, 0.3);
    }

    .audio-wave-button:active {
        transform: translateY(0);
    }

    .audio-wave-button i {
        color: white;
        font-size: clamp(16px, 2.5vw, 20px);
    }

    .audio-wave-button span {
        color: white;
        font-size: clamp(12px, 2vw, 16px);
        font-weight: 500;
    }

    /* Footer */
    .footer {
        position: absolute;
        top: 1212px;
        left: 0;
        width: 100%;
        height: 107px;
    }

    .footer-bg {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 107px;
        background-color: #0b547f;
        border-radius: 30px 30px 0px 0px;
    }

    .footer-text {
        position: absolute;
        top: 37px;
        left: 593px;
        height: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 500;
        color: white;
        font-size: 18px;
        text-align: center;
        letter-spacing: -0.23px;
        line-height: 20px;
        white-space: nowrap;
    }

</style>
""", unsafe_allow_html=True)

st.html ("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>ML Project - ASL Alphabet Detection</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="stylesheet" href="styles.css" />
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body>
        <div class="container">
        <!-- Background Shapes -->
        <div class="background-wrapper">
            <div class="bg-shape bg-shape-1"></div>
            <div class="bg-shape bg-shape-2"></div>
            <div class="bg-shape bg-shape-3"></div>
            <div class="bg-shape bg-shape-4"></div>
        </div>

        <!-- Main Content -->
        <main class="main-content">
            <div class="title-section">
            <h1 class="main-title">ASL Alphabet Detection</h1>
            <p class="subtitle">Real-time American Sign Language Recognition with Voice Output</p>
            </div>

            <div class="content-wrapper">
            <!-- Video Card -->
            <div class="video-card">
                <div class="video-container">

                <div class="camera-status">
                    <div class="status-indicator"></div>
                    <span class="status-text">Camera: Inactive</span>
                </div>

                <div class="controls-bg"></div>

                <button class="control-button control-play" id="playButton">
                    <i class="fas fa-play"></i>
                </button>

                <button class="control-button control-video" id="videoButton">
                    <i class="fas fa-video"></i>
                </button>

                <button class="control-button control-stop" id="stopButton">
                    <i class="fas fa-stop"></i>
                </button>
                </div>
            </div>

            <!-- Results Card -->
            <div class="results-card">
                <h2 class="results-title">Detection result</h2>

                <div class="results-display"></div>

                <button class="clear-button" id="clearButton">
                <span>Clear</span>
                </button>

                <p class="tap-to-speak">Tap to Speak</p>

                <div class="line-left"></div>
                <div class="line-right"></div>

                <button class="audio-wave-button" id="speakButton">
                    <i class="fas fa-volume-up"></i>
                    <span>Speak</span>
                </button>
            </div>
            </div>
        </main>

        <!-- Footer -->
        <footer class="footer">
            <div class="footer-bg"></div>
            <p class="footer-text">© 2025 ML Project. All rights reserved.</p>
        </footer>
        </div>

        <script src="script.js"></script>
    </body>
    </html>
""")