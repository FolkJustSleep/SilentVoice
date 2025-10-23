import streamlit as st
import streamlit.components.v1 as components

# this version available to use with full screen layout only

st.set_page_config(
    page_title="ML Project",
    page_icon="🤞🏿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    /* Hide all Streamlit UI */
    #MainMenu, header, .stDeployButton {
        visibility: hidden !important;
        display: none !important;
    }
    
    /* Custom Scrollbar (smaller but still visible) */
    ::-webkit-scrollbar {
        width: 6px !important;
        background: rgba(0, 0, 0, 0.05) !important;
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(0, 0, 0, 0.2) !important;
        border-radius: 3px !important;
    }
    
    /* Enable Scrolling */
    html, body, #root, .stApp {
        width: 100vw !important;
        min-height: 100vh !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow-x: hidden !important;
        overflow-y: auto !important;
    }
    
    /* Override ALL Containers */
    div[data-testid="stAppViewContainer"],
    div[data-testid="stHeader"],
    div[data-testid="stToolbar"],
    .main, .block-container,
    section[data-testid="stSidebar"] {
        padding: 0 !important;
        margin: 0 !important;
        max-width: none !important;
    }
    
    /* Remove Element Margins */
    .element-container {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Force Components Full Width */
    .stMarkdown, .stHTML {
        width: 100% !important;
        max-width: none !important;
    }
    
    /* iframe Responsive (ไม่ fixed) */
    iframe {
        width: 100vw !important;
        border: none !important;
        margin: 0 !important;
        padding: 0 !important;
        display: block !important;
    }
    
    /* Disable Responsive Behavior */
    @media (max-width: 1200px) {
        .stApp {
            width: 100vw !important;
        }
    }
</style>
""", unsafe_allow_html=True)

camera_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ASL Alphabet Detection</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: 
                radial-gradient(ellipse 800px 600px at 15% 40%, rgba(26, 182, 223, 0.4) 0%, transparent 60%),
                radial-gradient(ellipse 700px 500px at 85% 45%, rgba(26, 182, 223, 0.35) 0%, transparent 60%),
                radial-gradient(ellipse 600px 450px at 50% 15%, rgba(26, 182, 223, 0.3) 0%, transparent 55%),
                radial-gradient(ellipse 650px 500px at 25% 80%, rgba(26, 182, 223, 0.35) 0%, transparent 55%),
                radial-gradient(ellipse 700px 550px at 75% 85%, rgba(26, 182, 223, 0.38) 0%, transparent 58%),
                radial-gradient(ellipse 500px 400px at 50% 90%, rgba(26, 182, 223, 0.3) 0%, transparent 52%),
                radial-gradient(ellipse 450px 350px at 60% 60%, rgba(26, 182, 223, 0.2) 0%, transparent 48%),
                radial-gradient(ellipse 400px 320px at 40% 30%, rgba(26, 182, 223, 0.22) 0%, transparent 50%),
                radial-gradient(ellipse 380px 300px at 90% 25%, rgba(26, 182, 223, 0.18) 0%, transparent 45%),
                radial-gradient(ellipse 550px 450px at 10% 75%, rgba(26, 182, 223, 0.28) 0%, transparent 50%),
                radial-gradient(ellipse 480px 380px at 90% 80%, rgba(26, 182, 223, 0.25) 0%, transparent 48%),
                #F1F1F1;
            width: 100%;
            min-height: 100%;
            overflow: visible;
            display: flex;
            flex-direction: column;
            padding-top: 80px;
            margin: 0;
        }
        
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(10px);
            box-shadow: 0 2px 20px rgba(0, 0, 0, 0.08);
            z-index: 1000;
            padding: 20px 5%;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        
        .navbar-brand {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .navbar-title {
            font-size: 20px;
            font-weight: 600;
            color: #1AB6DF;
            margin: 0;
        }
        
        .navbar-menu {
            display: flex;
            gap: 30px;
            align-items: center;
        }
        
        .nav-link {
            color: #2D2D2D;
            text-decoration: none;
            font-size: 15px;
            font-weight: 500;
            transition: color 0.3s ease;
            cursor: pointer;
        }
        
        .nav-link:hover {
            color: #1AB6DF;
        }
        
        .content-wrapper {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 40px 0;
        }
        
        .header-section {
            text-align: center;
            margin-bottom: 40px;
        }
        
        .main-title {
            font-size: 32px;
            font-weight: 700;
            color: #2D2D2D;
            margin-bottom: 8px;
        }
        
        .subtitle {
            font-size: 16px;
            color: #868686;
            font-weight: 400;
        }
        
        .main-container {
            display: flex;
            gap: 7px;
            max-width: 1400px;
            width: 90%;
        }
        
        .camera-panel {
            background: white;
            border-radius: 30px 0px 0px 30px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.15);
            flex: 1;
            display: flex;
            flex-direction: column;
        }
        
        .video-container {
            position: relative;
            width: 100%;
            height: 480px;
            background: #C0C0C0;
            border-radius: 22px 0px 0px 0px;
            overflow: hidden;
            margin-bottom: 25px;
        }
        
        .camera-status {
            position: absolute;
            top: 20px;
            left: 20px;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 8px 20px;
            display: flex;
            align-items: center;
            gap: 10px;
            z-index: 10;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        
        .status-indicator {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #FF0000;
        }
        
        .status-indicator.active {
            background: #00FF00;
            animation: pulse 2s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        
        .status-text {
            font-size: 14px;
            font-weight: 500;
            color: #2D2D2D;
        }
        
        #videoElement {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        .controls {
            display: flex;
            justify-content: center;
            gap: 15px;
            padding-bottom: 30px;
        }
        
        .control-btn {
            width: 130px;
            height: 70px;
            border: none;
            border-radius: 15px;
            cursor: pointer;
            displa: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        
        .control-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.25);
        }
        
        .control-btn:active {
            transform: translateY(-1px);
        }
        
        .control-btn.disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }
        
        .control-btn.disabled:hover {
            transform: none;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        
        .btn-play {
            background: #1AB6DF;
        }
        
        .btn-pause {
            background: #C0C0C0;
        }
        
        .btn-stop {
            background: #FF0000;
        }
        
        .control-btn svg {
            fill: white;
        }
        
        .result-panel {
            background: white;
            border-radius: 0px 30px 30px 0px;
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.15);
            width: 350px;
            display: flex;
            flex-direction: column;
        }
        
        .result-title {
            font-size: 20px;
            font-weight: 600;
            color: #2D2D2D;
            margin-bottom: 20px;
        }
        
        .result-box {
            flex: 1;
            border: 1px solid #d7d7d7;
            border-radius: 18px;
            padding: 20px;
            margin-bottom: 20px;
            min-height: 340px;
            max-height: 340px;
            display: flex;
            align-items: flex-start;
            justify-content: flex-start;
            overflow-y: auto;
            overflow-x: hidden;
        }
        
        .result-box::-webkit-scrollbar {
            width: 4px;
        }
        
        .result-box::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 10px;
        }
        
        .result-box::-webkit-scrollbar-thumb {
            background: #1AB6DF;
            border-radius: 10px;
        }
        
        .result-box::-webkit-scrollbar-thumb:hover {
            background: #1599bf;
        }
        
        .result-placeholder {
            text-align: center;
            color: #d7d7d7;
            font-size: 14px;
            line-height: 1.6;
            width: 100%;
            margin: auto;
        }
        
        .result-text {
            font-size: 20px;
            font-weight: 400;
            color: #737373;
            text-align: left;
            word-wrap: break-word;
            word-break: break-word;
            overflow-wrap: break-word;
            white-space: pre-wrap;
            width: 100%;
            line-height: 1.6;
        }
        
        .clear-btn {
            background: white;
            border: 1px solid #1AB6DF;
            color: #1AB6DF;
            padding: 12px;
            border-radius: 18px;
            font-size: 18px;
            font-weight: 300;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-bottom: 15px;
        }
        
        .clear-btn:hover {
            background: #1ab6df;
            color: white;
        }
        
        .divider-container {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
            gap: 15px;
        }
        
        .divider-line {
            flex: 1;
            height: 1px;
            background: #d7d7d7;
        }
        
        .divider-text {
            color: #d7d7d7;
            font-size: 12px;
            font-weight: 400;
            white-space: nowrap;
        }
        
        .speak-btn {
            background-color: #1AB6DF;
            border: none;
            color: white;
            padding: 12px;
            border-radius: 18px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            box-shadow: 0 4px 15px rgba(26, 182, 223, 0.3);
        }
        
        .waveform {
            display: flex;
            align-items: center;
            gap: 4px;
            height: 24px;
        }
        
        .waveform-bar {
            width: 4px;
            background: white;
            border-radius: 2px;
            animation: wave 1.2s ease-in-out infinite;
        }
        
        .waveform-bar:nth-child(1) { height: 12px; animation-delay: 0s; }
        .waveform-bar:nth-child(2) { height: 20px; animation-delay: 0.1s; }
        .waveform-bar:nth-child(3) { height: 16px; animation-delay: 0.2s; }
        .waveform-bar:nth-child(4) { height: 8px; animation-delay: 0.3s; }
        .waveform-bar:nth-child(5) { height: 4px; animation-delay: 0.4s; }
        .waveform-bar:nth-child(6) { height: 12px; animation-delay: 0.5s; }
        .waveform-bar:nth-child(7) { height: 20px; animation-delay: 0.6s; }
        .waveform-bar:nth-child(8) { height: 16px; animation-delay: 0.7s; }
        .waveform-bar:nth-child(9) { height: 10px; animation-delay: 0.8s; }
        .waveform-bar:nth-child(10) { height: 6px; animation-delay: 0.9s; }
        .waveform-bar:nth-child(11) { height: 14px; animation-delay: 1s; }
        .waveform-bar:nth-child(12) { height: 18px; animation-delay: 1.1s; }
        .waveform-bar:nth-child(13) { height: 8px; animation-delay: 1.2s; }
        .waveform-bar:nth-child(14) { height: 12px; animation-delay: 1.3s; }
        .waveform-bar:nth-child(15) { height: 16px; animation-delay: 1.4s; }
        
        @keyframes wave {
            0%, 100% { transform: scaleY(1); }
            50% { transform: scaleY(1.5); }
        }
        
        .speak-btn:hover {
            background: #1599bf;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(26, 182, 223, 0.3);
        }
        
        .footer {
            background: #0B547F;
            color: white;
            text-align: center;
            padding: 50px 5%;
            border-radius: 30px 30px 0px 0px;
            margin-top: 60px;
            width: 100%;
        }
        
        .footer-content {
            max-width: 100%;
            margin: 0 auto;
        }
        
        .footer-text {
            font-size: 14px;
            font-weight: 400;
            margin: 0;
        }
        
        /* Responsive Design for Mobile */
        @media (max-width: 1024px) {
            body {
                padding: 20px 10px;
            }
            
            .header-section {
                margin-bottom: 25px;
            }
            
            .main-title {
                font-size: 24px;
            }
            
            .subtitle {
                font-size: 14px;
            }
            
            .main-container {
                flex-direction: column;
                width: 95%;
                gap: 15px;
            }
            
            .camera-panel {
                border-radius: 20px;
            }
            
            .video-container {
                height: 320px;
                border-radius: 20px 20px 0px 0px;
                margin-bottom: 20px;
            }
            
            .camera-status {
                top: 15px;
                left: 15px;
                padding: 6px 15px;
                border-radius: 12px;
            }
            
            .status-text {
                font-size: 12px;
            }
            
            .controls {
                padding-bottom: 20px;
                gap: 12px;
            }
            
            .control-btn {
                width: 100px;
                height: 60px;
                border-radius: 12px;
            }
            
            .control-btn svg {
                width: 24px;
                height: 24px;
            }
            
            .result-panel {
                border-radius: 20px;
                padding: 20px;
                width: 100%;
            }
            
            .result-title {
                font-size: 18px;
                margin-bottom: 15px;
            }
            
            .result-box {
                min-height: 250px;
                max-height: 250px;
                padding: 15px;
                margin-bottom: 15px;
            }
            
            .result-text {
                font-size: 18px;
            }
            
            .clear-btn {
                padding: 10px;
                font-size: 16px;
                margin-bottom: 12px;
            }
            
            .divider-container {
                margin-bottom: 12px;
                gap: 12px;
            }
            
            .speak-btn {
                padding: 10px;
                font-size: 14px;
            }
            
            .waveform {
                height: 20px;
                gap: 3px;
            }
            
            .waveform-bar {
                width: 3px;
            }
        }
        
        @media (max-width: 480px) {
            body {
                padding: 15px 5px;
            }
            
            .header-section {
                margin-bottom: 20px;
            }
            
            .main-title {
                font-size: 20px;
            }
            
            .subtitle {
                font-size: 12px;
            }
            
            .main-container {
                width: 98%;
                gap: 12px;
            }
            
            .camera-panel {
                border-radius: 15px;
            }
            
            .video-container {
                height: 240px;
                border-radius: 15px 15px 0px 0px;
                margin-bottom: 15px;
            }
            
            .camera-status {
                top: 10px;
                left: 10px;
                padding: 5px 12px;
                border-radius: 10px;
            }
            
            .status-indicator {
                width: 10px;
                height: 10px;
            }
            
            .status-text {
                font-size: 11px;
            }
            
            .controls {
                padding-bottom: 15px;
                gap: 10px;
            }
            
            .control-btn {
                width: 80px;
                height: 50px;
                border-radius: 10px;
            }
            
            .control-btn svg {
                width: 20px;
                height: 20px;
            }
            
            .result-panel {
                border-radius: 15px;
                padding: 15px;
            }
            
            .result-title {
                font-size: 16px;
                margin-bottom: 12px;
            }
            
            .result-box {
                min-height: 200px;
                max-height: 200px;
                padding: 12px;
                margin-bottom: 12px;
                border-radius: 12px;
            }
            
            .result-placeholder {
                font-size: 12px;
            }
            
            .result-text {
                font-size: 16px;
            }
            
            .clear-btn {
                padding: 8px;
                font-size: 14px;
                margin-bottom: 10px;
                border-radius: 12px;
            }
            
            .divider-container {
                margin-bottom: 10px;
                gap: 10px;
            }
            
            .divider-text {
                font-size: 10px;
            }
            
            .speak-btn {
                padding: 8px;
                font-size: 12px;
                border-radius: 12px;
            }
            
            .waveform {
                height: 18px;
                gap: 2px;
            }
            
            .waveform-bar {
                width: 2.5px;
            }
            
            .waveform-bar:nth-child(1) { height: 10px; }
            .waveform-bar:nth-child(2) { height: 16px; }
            .waveform-bar:nth-child(3) { height: 13px; }
            .waveform-bar:nth-child(4) { height: 7px; }
            .waveform-bar:nth-child(5) { height: 4px; }
            .waveform-bar:nth-child(6) { height: 10px; }
            .waveform-bar:nth-child(7) { height: 16px; }
            .waveform-bar:nth-child(8) { height: 13px; }
            .waveform-bar:nth-child(9) { height: 8px; }
            .waveform-bar:nth-child(10) { height: 5px; }
            .waveform-bar:nth-child(11) { height: 11px; }
            .waveform-bar:nth-child(12) { height: 15px; }
            .waveform-bar:nth-child(13) { height: 7px; }
            .waveform-bar:nth-child(14) { height: 10px; }
            .waveform-bar:nth-child(15) { height: 13px; }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="navbar-brand">
            <h1 class="navbar-title">ML Project</h1>
        </div>
        <!-- <div class="navbar-menu"> <a class="nav-link">more</a> </div> -->
    </nav>
    
    <div class="content-wrapper">
    <div class="header-section">
        <h1 class="main-title">ASL Alphabet Detection</h1>
        <p class="subtitle">Real-time American Sign Language Recognition with Voice Output</p>
    </div>
    
    <div class="main-container">
        <div class="camera-panel">
            <div class="video-container">
                <div class="camera-status">
                    <div class="status-indicator" id="statusIndicator"></div>
                    <span class="status-text" id="statusText">Camera: Inactive</span>
                </div>
                
                <video id="videoElement" autoplay playsinline></video>
            </div>
            
            <div class="controls">
                <button id="playBtn" class="control-btn btn-play">
                    <svg width="30" height="30" viewBox="0 0 24 24">
                        <path d="M8 5v14l11-7z"/>
                    </svg>
                </button>
                <button id="pauseBtn" class="control-btn btn-pause disabled">
                    <svg width="30" height="30" viewBox="0 0 24 24">
                        <path d="M6 4h4v16H6V4zm8 0h4v16h-4V4z"/>
                    </svg>
                </button>
                <button id="stopBtn" class="control-btn btn-stop disabled">
                    <svg width="30" height="30" viewBox="0 0 24 24">
                        <rect x="6" y="6" width="12" height="12"/>
                    </svg>
                </button>
            </div>
        </div>
        
        <div class="result-panel">
            <h2 class="result-title">Detection result</h2>
            <div class="result-box">
                <div class="result-placeholder">
                    Result article will appear here
                </div>
                <div id="resultText" class="result-text" style="display: none;"></div>
            </div>
            <button id="clearBtn" class="clear-btn">Clear</button>
            
            <div class="divider-container">
                <div class="divider-line"></div>
                <span class="divider-text">Tap to Speak</span>
                <div class="divider-line"></div>
            </div>
            
            <button id="speakBtn" class="speak-btn">
                <div class="waveform">
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                </div>
            </button>
        </div>
    </div>
    </div>
    
    <footer class="footer">
        <div class="footer-content">
            <p class="footer-text">© 2025 ML Project. All rights reserved.</p>
        </div>
    </footer>
    
    <script>
        const video = document.getElementById('videoElement');
        const playBtn = document.getElementById('playBtn');
        const pauseBtn = document.getElementById('pauseBtn');
        const stopBtn = document.getElementById('stopBtn');
        const resultText = document.getElementById('resultText');
        const resultPlaceholder = document.querySelector('.result-placeholder');
        const clearBtn = document.getElementById('clearBtn');
        const speakBtn = document.getElementById('speakBtn');
        const statusIndicator = document.getElementById('statusIndicator');
        const statusText = document.getElementById('statusText');
        
        let stream = null;
        let isPlaying = false;
        let isPaused = false;
        let detectedText = '';
        
        function updateCameraStatus(status) {
            if (status === 'active') {
                statusIndicator.classList.add('active');
                statusIndicator.style.background = '';
                statusText.textContent = 'Camera: Active';
            } else if (status === 'paused') {
                statusIndicator.classList.remove('active');
                statusIndicator.style.background = '#FFA500';
                statusText.textContent = 'Camera: Paused';
            } else {
                statusIndicator.classList.remove('active');
                statusIndicator.style.background = '#FF0000';
                statusText.textContent = 'Camera: Inactive';
            }
        }
        
        playBtn.addEventListener('click', async () => {
            try {
                // Resume camera if paused
                if (isPaused && stream) {
                    video.play();
                    isPaused = false;
                    updateCameraStatus('active');
                    
                    playBtn.classList.add('disabled');
                    return;
                }
                
                // Start camera if not initialized
                if (!stream) {
                    stream = await navigator.mediaDevices.getUserMedia({ 
                        video: { 
                            width: { ideal: 1280 },
                            height: { ideal: 720 }
                        } 
                    });
                    video.srcObject = stream;
                }
                
                video.play();
                isPlaying = true;
                isPaused = false;
                
                playBtn.classList.add('disabled');
                pauseBtn.classList.remove('disabled');
                stopBtn.classList.remove('disabled');
                
                updateCameraStatus('active');
                
                // Simulate detection (replace with real ML model)
                startDetection();
            } catch (err) {
                console.error('Camera error:', err);
                alert('Cannot access camera: ' + err.message);
            }
        });
        
        pauseBtn.addEventListener('click', () => {
            if (!pauseBtn.classList.contains('disabled')) {
                video.pause();
                isPaused = true;
                updateCameraStatus('paused');
                
                playBtn.classList.remove('disabled');
            }
        });
        
        stopBtn.addEventListener('click', () => {
            if (!stopBtn.classList.contains('disabled')) {
                if (stream) {
                    stream.getTracks().forEach(track => track.stop());
                    stream = null;
                }
                
                isPlaying = false;
                isPaused = false;
                
                playBtn.classList.remove('disabled');
                pauseBtn.classList.add('disabled');
                stopBtn.classList.add('disabled');
                
                updateCameraStatus('inactive');
            }
        });
        
        clearBtn.addEventListener('click', () => {
            detectedText = '';
            resultText.textContent = '';
            resultText.style.display = 'none';
            resultPlaceholder.style.display = 'block';
        });
        
        speakBtn.addEventListener('click', () => {
            if (detectedText) {
                const utterance = new SpeechSynthesisUtterance(detectedText);
                utterance.lang = 'en-US';  
                utterance.rate = 0.9;
                window.speechSynthesis.speak(utterance);
            } else {
                alert('No text to speak');
            }
        });
        
        // Replace this simulation with actual ML model detection
        function startDetection() {
            const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
            const detectionInterval = setInterval(() => {
                if (!isPlaying || isPaused) {
                    clearInterval(detectionInterval);
                    return;
                }
                
                const randomLetter = letters[Math.floor(Math.random() * letters.length)];
                detectedText += randomLetter;
                
                resultText.textContent = detectedText;
                resultText.style.display = 'block';
                resultPlaceholder.style.display = 'none';
                
                const resultBox = document.querySelector('.result-box');
                resultBox.scrollTop = resultBox.scrollHeight;
            }, 2000);
        }
    </script>
</body>
</html>
"""

components.html(camera_html, height=1040, scrolling=False)