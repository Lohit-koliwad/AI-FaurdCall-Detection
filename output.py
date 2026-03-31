 [
  {
    "import streamlit as st": "import os"
  },
  {
    "import streamlit as st": "import json"
  },
  {
    "import streamlit as st": "import tempfile"
  },
  {
    "import streamlit as st": "import smtplib"
  },
  {
    "import streamlit as st": "import time"
  },
  {
    "import streamlit as st": "from email.mime.text import MIMEText"
  },
  {
    "import streamlit as st": "from email.mime.multipart import MIMEMultipart"
  },
  {
    "import streamlit as st": "import librosa"
  },
  {
    "import streamlit as st": "import soundfile as sf"
  },
  {
    "import streamlit as st": "import noisereduce as nr"
  },
  {
    "import streamlit as st": "from google import genai"
  },
  {
    "import streamlit as st": "from google.genai import types"
  },
  {
    "import streamlit as st": "# =========================================="
  },
  {
    "import streamlit as st": "# CONFIGURATION"
  },
  {
    "import streamlit as st": "# =========================================="
  },
  {
    "import streamlit as st": "GEMINI_API_KEY = KEY"
  },
  {
    "import streamlit as st": "SENDER_EMAIL = EMAIL"
  },
  {
    "import streamlit as st": "SENDER_PASSWORD = PASSWORD"
  },
  {
    "import streamlit as st": "client = genai.Client(api_key=GEMINI_API_KEY)"
  },
  {
    "import streamlit as st": "# =========================================="
  },
  {
    "import streamlit as st": "# EMAIL FUNCTIONS"
  },
  {
    "import streamlit as st": "# =========================================="
  },
  {
    "import streamlit as st": "def test_smtp_connection():"
  },
  {
    "import streamlit as st": "try:"
  },
  {
    "import streamlit as st": "with smtplib.SMTP('smtp.gmail.com', 587) as server:"
  },
  {
    "import streamlit as st": "server.ehlo()"
  },
  {
    "import streamlit as st": "server.starttls()"
  },
  {
    "import streamlit as st": "server.ehlo()"
  },
  {
    "import streamlit as st": "server.login(SENDER_EMAIL, SENDER_PASSWORD)"
  },
  {
    "import streamlit as st": "return True, Connection Established: Email Gateway Online"
  },
  {
    "import streamlit as st": "except Exception as e:"
  },
  {
    "import streamlit as st": "return False, fGateway Error: {e}"
  },
  {
    "import streamlit as st": "def send_email_report(recipient_email, data):"
  },
  {
    "import streamlit as st": "try:"
  },
  {
    "import streamlit as st": "msg = MIMEMultipart()"
  },
  {
    "import streamlit as st": "msg['From'] = fFraudShield AI <{SENDER_EMAIL}>"
  },
  {
    "import streamlit as st": "msg['To'] = recipient_email"
  },
  {
    "import streamlit as st": "status_label = URGENT: SCAM ALERT if data.get('is_scam') else Report: Call Marked Safe"
  },
  {
    "import streamlit as st": "msg['Subject'] = f{status_label} - FraudShield Analysis"
  },
  {
    "import streamlit as st": ""body = f""FRAUDSHIELD AI - OFFICIAL ANALYSIS REPORT""
  },
  {
    "import streamlit as st": "==========================================="
  },
  {
    "import streamlit as st": "Destination: {recipient_email}"
  },
  {
    "import streamlit as st": "Detected Language: {data.get('language')}"
  },
  {
    "import streamlit as st": "[ AI RISK ASSESSMENT ]"
  },
  {
    "import streamlit as st": "{data.get('scam_analysis')}"
  },
  {
    "import streamlit as st": "[ ORIGINAL TRANSCRIPT ]"
  },
  {
    "import streamlit as st": "{data.get('text')}"
  },
  {
    "import streamlit as st": "[ ENGLISH TRANSLATION ]"
  },
  {
    "import streamlit as st": "{data.get('english_text')}"
  },
  {
    "import streamlit as st": "==========================================="
  },
  {
    "import streamlit as st": "Final Status: {'HIGH RISK' if data.get('is_scam') else 'LOW RISK'}"
  },
  {
    "import streamlit as st": """"""
  },
  {
    "import streamlit as st": "msg.attach(MIMEText(body, 'plain'))"
  },
  {
    "import streamlit as st": "with smtplib.SMTP('smtp.gmail.com', 587) as server:"
  },
  {
    "import streamlit as st": "server.ehlo()"
  },
  {
    "import streamlit as st": "server.starttls()"
  },
  {
    "import streamlit as st": "server.ehlo()"
  },
  {
    "import streamlit as st": "server.login(SENDER_EMAIL, SENDER_PASSWORD)"
  },
  {
    "import streamlit as st": "server.send_message(msg)"
  },
  {
    "import streamlit as st": "time.sleep(1)"
  },
  {
    "import streamlit as st": "return True"
  },
  {
    "import streamlit as st": "except Exception as e:"
  },
  {
    "import streamlit as st": "st.error(fMail Delivery Failed: {e})"
  },
  {
    "import streamlit as st": "return False"
  },
  {
    "import streamlit as st": "# =========================================="
  },
  {
    "import streamlit as st": "# UI DESIGN & CSS INJECTION"
  },
  {
    "import streamlit as st": "# =========================================="
  },
  {
    "import streamlit as st": "st.set_page_config(page_title=FraudShield AI, layout=wide, initial_sidebar_state=expanded)"
  },
  {
    "import streamlit as st": ""st.markdown(""""
  },
  {
    "import streamlit as st": "<style>"
  },
  {
    "import streamlit as st": "/* Typography and Header Styling */"
  },
  {
    "import streamlit as st": ".main-title {"
  },
  {
    "import streamlit as st": "font-size: 2.8rem;"
  },
  {
    "import streamlit as st": "font-weight: 800;"
  },
  {
    "import streamlit as st": "color: #1E293B;"
  },
  {
    "import streamlit as st": "letter-spacing: -1px;"
  },
  {
    "import streamlit as st": "margin-bottom: 0px;"
  },
  {
    "import streamlit as st": "padding-bottom: 0px;"
  },
  {
    "import streamlit as st": "}"
  },
  {
    "import streamlit as st": ".sub-title {"
  },
  {
    "import streamlit as st": "font-size: 1.1rem;"
  },
  {
    "import streamlit as st": "color: #64748B;"
  },
  {
    "import streamlit as st": "font-weight: 400;"
  },
  {
    "import streamlit as st": "margin-top: 0px;"
  },
  {
    "import streamlit as st": "margin-bottom: 2rem;"
  },
  {
    "import streamlit as st": "}"
  },
  {
    "import streamlit as st": "/* Custom Card Styling for Results */"
  },
  {
    "import streamlit as st": ".result-card {"
  },
  {
    "import streamlit as st": "background-color: #F8FAFC;"
  },
  {
    "import streamlit as st": "border: 1px solid #E2E8F0;"
  },
  {
    "import streamlit as st": "border-radius: 12px;"
  },
  {
    "import streamlit as st": "padding: 24px;"
  },
  {
    "import streamlit as st": "margin-top: 16px;"
  },
  {
    "import streamlit as st": "margin-bottom: 16px;"
  },
  {
    "import streamlit as st": "}"
  },
  {
    "import streamlit as st": ".alert-high {"
  },
  {
    "import streamlit as st": "background-color: #FEF2F2;"
  },
  {
    "import streamlit as st": "border-left: 6px solid #EF4444;"
  },
  {
    "import streamlit as st": "color: #991B1B;"
  },
  {
    "import streamlit as st": "padding: 20px;"
  },
  {
    "import streamlit as st": "border-radius: 8px;"
  },
  {
    "import streamlit as st": "font-weight: 600;"
  },
  {
    "import streamlit as st": "font-size: 1.2rem;"
  },
  {
    "import streamlit as st": "}"
  },
  {
    "import streamlit as st": ".alert-safe {"
  },
  {
    "import streamlit as st": "background-color: #F0FDF4;"
  },
  {
    "import streamlit as st": "border-left: 6px solid #22C55E;"
  },
  {
    "import streamlit as st": "color: #166534;"
  },
  {
    "import streamlit as st": "padding: 20px;"
  },
  {
    "import streamlit as st": "border-radius: 8px;"
  },
  {
    "import streamlit as st": "font-weight: 600;"
  },
  {
    "import streamlit as st": "font-size: 1.2rem;"
  },
  {
    "import streamlit as st": "}"
  },
  {
    "import streamlit as st": "/* Section Headers */"
  },
  {
    "import streamlit as st": ".section-header {"
  },
  {
    "import streamlit as st": "font-size: 1.2rem;"
  },
  {
    "import streamlit as st": "font-weight: 600;"
  },
  {
    "import streamlit as st": "color: #334155;"
  },
  {
    "import streamlit as st": "border-bottom: 2px solid #E2E8F0;"
  },
  {
    "import streamlit as st": "padding-bottom: 8px;"
  },
  {
    "import streamlit as st": "margin-bottom: 16px;"
  },
  {
    "import streamlit as st": "margin-top: 32px;"
  },
  {
    "import streamlit as st": "}"
  },
  {
    "import streamlit as st": "</style>"
  },
  {
    "import streamlit as st": """", unsafe_allow_html=True)""
  },
  {
    "import streamlit as st": "# =========================================="
  },
  {
    "import streamlit as st": "# SIDEBAR: SYSTEM SETTINGS"
  },
  {
    "import streamlit as st": "# =========================================="
  },
  {
    "import streamlit as st": "with st.sidebar:"
  },
  {
    "import streamlit as st": "st.markdown('<p style=font-size: 1.5rem; font-weight: 700; color:#0F172A;>System Settings</p>', unsafe_allow_html=True)"
  },
  {
    "import streamlit as st": "st.markdown(Manage backend configurations and verify system health.)"
  },
  {
    "import streamlit as st": "with st.expander(Email Gateway Diagnostics, expanded=True):"
  },
  {
    "import streamlit as st": "st.write(Verify the SMTP server is actively accepting connections.)"
  },
  {
    "import streamlit as st": "if st.button(Run Diagnostic Ping, use_container_width=True):"
  },
  {
    "import streamlit as st": "with st.spinner(Pinging gateway...):"
  },
  {
    "import streamlit as st": "success, message = test_smtp_connection()"
  },
  {
    "import streamlit as st": "if success:"
  },
  {
    "import streamlit as st": "st.success(message)"
  },
  {
    "import streamlit as st": "else:"
  },
  {
    "import streamlit as st": "st.error(message)"
  },
  {
    "import streamlit as st": "st.divider()"
  },
  {
    "import streamlit as st": "st.caption(FraudShield AI Engine v2.0)"
  },
  {
    "import streamlit as st": "st.caption(Powered by Google Gemini 2.5 Flash)"
  },
  {
    "import streamlit as st": "# =========================================="
  },
  {
    "import streamlit as st": "# MAIN APP BODY"
  },
  {
    "import streamlit as st": "# =========================================="
  },
  {
    "import streamlit as st": "st.markdown('<p class=main-title>FraudShield AI</p>', unsafe_allow_html=True)"
  },
  {
    "import streamlit as st": "st.markdown('<p class=sub-title>Automated Voice Threat Detection & Telecom Scam Analysis</p>', unsafe_allow_html=True)"
  },
  {
    "import streamlit as st": "# --- STEP 1: INPUTS ---"
  },
  {
    "import streamlit as st": "st.markdown('<div class=section-header>Step 1: Configuration & Payload</div>', unsafe_allow_html=True)"
  },
  {
    "import streamlit as st": "col1, col2 = st.columns([1, 1], gap=large)"
  },
  {
    "import streamlit as st": "with col1:"
  },
  {
    "import streamlit as st": "st.markdown(**1. Target Destination**)"
  },
  {
    "import streamlit as st": "user_email = st.text_input(Report Delivery Address, placeholder=security_team@domain.com, label_visibility=collapsed)"
  },
  {
    "import streamlit as st": "st.caption(The analysis report will be securely dispatched to this address.)"
  },
  {
    "import streamlit as st": "with col2:"
  },
  {
    "import streamlit as st": "st.markdown(**2. Audio Evidence**)"
  },
  {
    "import streamlit as st": "uploaded_file = st.file_uploader(Upload Audio Payload, type=[wav], label_visibility=collapsed)"
  },
  {
    "import streamlit as st": "st.caption(Accepted format: .WAV (Max 10MB recommended))"
  },
  {
    "import streamlit as st": "# --- STEP 2: EXECUTION ---"
  },
  {
    "import streamlit as st": "st.markdown('<div class=section-header>Step 2: Security Analysis</div>', unsafe_allow_html=True)"
  },
  {
    "import streamlit as st": "if st.button(Execute Threat Analysis, type=primary, use_container_width=True):"
  },
  {
    "import streamlit as st": "if not user_email or not uploaded_file:"
  },
  {
    "import streamlit as st": "st.warning(Action Required: Please provide both a delivery address and an audio file before executing.)"
  },
  {
    "import streamlit as st": "else:"
  },
  {
    "import streamlit as st": "with st.status(Initializing FraudShield Pipeline..., expanded=True) as status:"
  },
  {
    "import streamlit as st": "with tempfile.NamedTemporaryFile(delete=False, suffix=.wav) as tmp_in:"
  },
  {
    "import streamlit as st": "tmp_in.write(uploaded_file.getvalue())"
  },
  {
    "import streamlit as st": "input_path = tmp_in.name"
  },
  {
    "import streamlit as st": "output_path = input_path + _clean.wav"
  },
  {
    "import streamlit as st": "gemini_audio = None"
  },
  {
    "import streamlit as st": "try:"
  },
  {
    "import streamlit as st": "# 1. Noise Reduction"
  },
  {
    "import streamlit as st": "status.update(label=Process [1/3]: Applying acoustic noise suppression...)"
  },
  {
    "import streamlit as st": "audio, sr = librosa.load(input_path, sr=None)"
  },
  {
    "import streamlit as st": "reduced_audio = nr.reduce_noise(y=audio, sr=sr)"
  },
  {
    "import streamlit as st": "sf.write(output_path, reduced_audio, sr)"
  },
  {
    "import streamlit as st": "# 2. Upload to Gemini"
  },
  {
    "import streamlit as st": "status.update(label=Process [2/3]: Encrypting and uploading to AI matrix...)"
  },
  {
    "import streamlit as st": "gemini_audio = client.files.upload(file=output_path)"
  },
  {
    "import streamlit as st": "# 3. Prompt Configuration"
  },
  {
    "import streamlit as st": ""prompt = """"
  },
  {
    "import streamlit as st": "Transcribe this audio, detect the language, translate to English, and determine if it is a scam."
  },
  {
    "import streamlit as st": "Look for 'Digital Arrest', 'FedEx', or 'CBI/Police' impersonation."
  },
  {
    "import streamlit as st": "Return ONLY JSON:"
  },
  {
    "import streamlit as st": "{"
  },
  {
    "import streamlit as st": "language: Language,"
  },
  {
    "import streamlit as st": "text: Transcription,"
  },
  {
    "import streamlit as st": "english_text: Translation,"
  },
  {
    "import streamlit as st": "is_scam: true/false,"
  },
  {
    "import streamlit as st": "scam_analysis: Reason"
  },
  {
    "import streamlit as st": "}"
  },
  {
    "import streamlit as st": """"""
  },
  {
    "import streamlit as st": "status.update(label=Process [3/3]: Running Deep-NLP threat detection...)"
  },
  {
    "import streamlit as st": "response = client.models.generate_content("
  },
  {
    "import streamlit as st": "model='gemini-2.5-flash',"
  },
  {
    "import streamlit as st": "contents=[prompt, gemini_audio],"
  },
  {
    "import streamlit as st": "config=types.GenerateContentConfig(response_mime_type=application/json)"
  },
  {
    "import streamlit as st": ")"
  },
  {
    "import streamlit as st": "result = json.loads(response.text)"
  },
  {
    "import streamlit as st": "status.update(label=Pipeline Execution Complete., state=complete)"
  },
  {
    "import streamlit as st": "except Exception as e:"
  },
  {
    "import streamlit as st": "status.update(label=Critical Failure in Pipeline, state=error)"
  },
  {
    "import streamlit as st": "st.error(fExecution Error: {e})"
  },
  {
    "import streamlit as st": "st.stop()"
  },
  {
    "import streamlit as st": "finally:"
  },
  {
    "import streamlit as st": "if gemini_audio:"
  },
  {
    "import streamlit as st": "try: client.files.delete(name=gemini_audio.name)"
  },
  {
    "import streamlit as st": "except: pass"
  },
  {
    "import streamlit as st": "if os.path.exists(input_path): os.remove(input_path)"
  },
  {
    "import streamlit as st": "if os.path.exists(output_path): os.remove(output_path)"
  },
  {
    "import streamlit as st": "# =========================================="
  },
  {
    "import streamlit as st": "# RESULTS DASHBOARD UI"
  },
  {
    "import streamlit as st": "# =========================================="
  },
  {
    "import streamlit as st": "st.markdown('<div class=section-header>Threat Assessment Dashboard</div>', unsafe_allow_html=True)"
  },
  {
    "import streamlit as st": "# 1. Primary Verdict Box"
  },
  {
    "import streamlit as st": "if result.get('is_scam'):"
  },
  {
    "import streamlit as st": "st.markdown('<div class=alert-high>CRITICAL ALERT: High Probability of Telecom Fraud / Digital Arrest Scam Detected.</div>', unsafe_allow_html=True)"
  },
  {
    "import streamlit as st": "else:"
  },
  {
    "import streamlit as st": "st.markdown('<div class=alert-safe>CLEARED: No immediate indicators of telecom fraud detected.</div>', unsafe_allow_html=True)"
  },
  {
    "import streamlit as st": "# 2. Metadata Cards"
  },
  {
    "import streamlit as st": "st.markdown('<div class=result-card>', unsafe_allow_html=True)"
  },
  {
    "import streamlit as st": "metric_col1, metric_col2 = st.columns(2)"
  },
  {
    "import streamlit as st": "with metric_col1:"
  },
  {
    "import streamlit as st": "st.markdown(**Detected Dialect/Language**)"
  },
  {
    "import streamlit as st": "st.markdown(f<h3 style='margin-top:0px; color:#1E293B;'>{result.get('language', 'Unknown')}</h3>, unsafe_allow_html=True)"
  },
  {
    "import streamlit as st": "with metric_col2:"
  },
  {
    "import streamlit as st": "st.markdown(**System Confidence**)"
  },
  {
    "import streamlit as st": "st.markdown(<h3 style='margin-top:0px; color:#1E293B;'>High (AI Verified)</h3>, unsafe_allow_html=True)"
  },
  {
    "import streamlit as st": "st.markdown('</div>', unsafe_allow_html=True)"
  },
  {
    "import streamlit as st": "# 3. AI Reasoning"
  },
  {
    "import streamlit as st": "st.markdown(**AI Behavioral Analysis:**)"
  },
  {
    "import streamlit as st": "st.info(result.get('scam_analysis', 'No behavioral data provided.'))"
  },
  {
    "import streamlit as st": "# 4. Transcripts (Hidden by default to keep UI clean)"
  },
  {
    "import streamlit as st": "with st.expander(View Raw Intelligence (Transcripts & Translations)):"
  },
  {
    "import streamlit as st": "st.markdown(**Source Audio (Transcribed):**)"
  },
  {
    "import streamlit as st": "st.write(result.get('text', 'No transcript available.'))"
  },
  {
    "import streamlit as st": "st.divider()"
  },
  {
    "import streamlit as st": "st.markdown(**English Localization:**)"
  },
  {
    "import streamlit as st": "st.write(result.get('english_text', 'No translation available.'))"
  },
  {
    "import streamlit as st": "# 5. Email Dispatch Status"
  },
  {
    "import streamlit as st": "with st.spinner(Dispatching official report to gateway...):"
  },
  {
    "import streamlit as st": "if send_email_report(user_email, result):"
  },
  {
    "import streamlit as st": "st.toast(fSecure report successfully transmitted to {user_email})"
  },
  {
    "import streamlit as st": "else:"
  },
  {
    "import streamlit as st": "st.error(Report generated locally, but email gateway transmission failed.)"
  }
]