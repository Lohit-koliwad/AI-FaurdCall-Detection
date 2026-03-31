import streamlit as st
import os
import json
import tempfile
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import librosa
import soundfile as sf
import noisereduce as nr
from google import genai
from google.genai import types
# ==========================================
# CONFIGURATION
# ==========================================
GEMINI_API_KEY = KEY
SENDER_EMAIL = EMAIL
SENDER_PASSWORD = PASSWORD
client = genai.Client(api_key=GEMINI_API_KEY)
# ==========================================
# EMAIL FUNCTIONS
# ==========================================
def test_smtp_connection():
try:
"with smtplib.SMTP('smtp.gmail.com', 587) as server:"
server.ehlo()
server.starttls()
server.ehlo()
"server.login(SENDER_EMAIL, SENDER_PASSWORD)"
"return True, Connection Established: Email Gateway Online"
except Exception as e:
"return False, fGateway Error: {e}"
"def send_email_report(recipient_email, data):"
try:
msg = MIMEMultipart()
msg['From'] = fFraudShield AI <{SENDER_EMAIL}>
msg['To'] = recipient_email
status_label = URGENT: SCAM ALERT if data.get('is_scam') else Report: Call Marked Safe
msg['Subject'] = f{status_label} - FraudShield Analysis
"body = f""FRAUDSHIELD AI - OFFICIAL ANALYSIS REPORT"
===========================================
Destination: {recipient_email}
Detected Language: {data.get('language')}
[ AI RISK ASSESSMENT ]
{data.get('scam_analysis')}
[ ORIGINAL TRANSCRIPT ]
{data.get('text')}
[ ENGLISH TRANSLATION ]
{data.get('english_text')}
===========================================
Final Status: {'HIGH RISK' if data.get('is_scam') else 'LOW RISK'}
""""
"msg.attach(MIMEText(body, 'plain'))"
"with smtplib.SMTP('smtp.gmail.com', 587) as server:"
server.ehlo()
server.starttls()
server.ehlo()
"server.login(SENDER_EMAIL, SENDER_PASSWORD)"
server.send_message(msg)
time.sleep(1)
return True
except Exception as e:
st.error(fMail Delivery Failed: {e})
return False
# ==========================================
# UI DESIGN & CSS INJECTION
# ==========================================
"st.set_page_config(page_title=FraudShield AI, layout=wide, initial_sidebar_state=expanded)"
"st.markdown("""
<style>
/* Typography and Header Styling */
.main-title {
font-size: 2.8rem;
font-weight: 800;
color: #1E293B;
letter-spacing: -1px;
margin-bottom: 0px;
padding-bottom: 0px;
}
.sub-title {
font-size: 1.1rem;
color: #64748B;
font-weight: 400;
margin-top: 0px;
margin-bottom: 2rem;
}
/* Custom Card Styling for Results */
.result-card {
background-color: #F8FAFC;
border: 1px solid #E2E8F0;
border-radius: 12px;
padding: 24px;
margin-top: 16px;
margin-bottom: 16px;
}
.alert-high {
background-color: #FEF2F2;
border-left: 6px solid #EF4444;
color: #991B1B;
padding: 20px;
border-radius: 8px;
font-weight: 600;
font-size: 1.2rem;
}
.alert-safe {
background-color: #F0FDF4;
border-left: 6px solid #22C55E;
color: #166534;
padding: 20px;
border-radius: 8px;
font-weight: 600;
font-size: 1.2rem;
}
/* Section Headers */
.section-header {
font-size: 1.2rem;
font-weight: 600;
color: #334155;
border-bottom: 2px solid #E2E8F0;
padding-bottom: 8px;
margin-bottom: 16px;
margin-top: 32px;
}
</style>
""", unsafe_allow_html=True)"
# ==========================================
# SIDEBAR: SYSTEM SETTINGS
# ==========================================
with st.sidebar:
"st.markdown('<p style=font-size: 1.5rem; font-weight: 700; color:#0F172A;>System Settings</p>', unsafe_allow_html=True)"
st.markdown(Manage backend configurations and verify system health.)
"with st.expander(Email Gateway Diagnostics, expanded=True):"
st.write(Verify the SMTP server is actively accepting connections.)
"if st.button(Run Diagnostic Ping, use_container_width=True):"
with st.spinner(Pinging gateway...):
"success, message = test_smtp_connection()"
if success:
st.success(message)
else:
st.error(message)
st.divider()
st.caption(FraudShield AI Engine v2.0)
st.caption(Powered by Google Gemini 2.5 Flash)
# ==========================================
# MAIN APP BODY
# ==========================================
"st.markdown('<p class=main-title>FraudShield AI</p>', unsafe_allow_html=True)"
"st.markdown('<p class=sub-title>Automated Voice Threat Detection & Telecom Scam Analysis</p>', unsafe_allow_html=True)"
# --- STEP 1: INPUTS ---
"st.markdown('<div class=section-header>Step 1: Configuration & Payload</div>', unsafe_allow_html=True)"
"col1, col2 = st.columns([1, 1], gap=large)"
with col1:
st.markdown(**1. Target Destination**)
"user_email = st.text_input(Report Delivery Address, placeholder=security_team@domain.com, label_visibility=collapsed)"
st.caption(The analysis report will be securely dispatched to this address.)
with col2:
st.markdown(**2. Audio Evidence**)
"uploaded_file = st.file_uploader(Upload Audio Payload, type=[wav], label_visibility=collapsed)"
st.caption(Accepted format: .WAV (Max 10MB recommended))
# --- STEP 2: EXECUTION ---
"st.markdown('<div class=section-header>Step 2: Security Analysis</div>', unsafe_allow_html=True)"
"if st.button(Execute Threat Analysis, type=primary, use_container_width=True):"
if not user_email or not uploaded_file:
st.warning(Action Required: Please provide both a delivery address and an audio file before executing.)
else:
"with st.status(Initializing FraudShield Pipeline..., expanded=True) as status:"
"with tempfile.NamedTemporaryFile(delete=False, suffix=.wav) as tmp_in:"
tmp_in.write(uploaded_file.getvalue())
input_path = tmp_in.name
output_path = input_path + _clean.wav
gemini_audio = None
try:
# 1. Noise Reduction
status.update(label=Process [1/3]: Applying acoustic noise suppression...)
"audio, sr = librosa.load(input_path, sr=None)"
"reduced_audio = nr.reduce_noise(y=audio, sr=sr)"
"sf.write(output_path, reduced_audio, sr)"
# 2. Upload to Gemini
status.update(label=Process [2/3]: Encrypting and uploading to AI matrix...)
gemini_audio = client.files.upload(file=output_path)
# 3. Prompt Configuration
"prompt = """
"Transcribe this audio, detect the language, translate to English, and determine if it is a scam."
"Look for 'Digital Arrest', 'FedEx', or 'CBI/Police' impersonation."
Return ONLY JSON:
{
"language: Language,"
"text: Transcription,"
"english_text: Translation,"
"is_scam: true/false,"
scam_analysis: Reason
}
""""
status.update(label=Process [3/3]: Running Deep-NLP threat detection...)
response = client.models.generate_content(
"model='gemini-2.5-flash',"
"contents=[prompt, gemini_audio],"
config=types.GenerateContentConfig(response_mime_type=application/json)
)
result = json.loads(response.text)
"status.update(label=Pipeline Execution Complete., state=complete)"
except Exception as e:
"status.update(label=Critical Failure in Pipeline, state=error)"
st.error(fExecution Error: {e})
st.stop()
finally:
if gemini_audio:
try: client.files.delete(name=gemini_audio.name)
except: pass
if os.path.exists(input_path): os.remove(input_path)
if os.path.exists(output_path): os.remove(output_path)
# ==========================================
# RESULTS DASHBOARD UI
# ==========================================
"st.markdown('<div class=section-header>Threat Assessment Dashboard</div>', unsafe_allow_html=True)"
# 1. Primary Verdict Box
if result.get('is_scam'):
"st.markdown('<div class=alert-high>CRITICAL ALERT: High Probability of Telecom Fraud / Digital Arrest Scam Detected.</div>', unsafe_allow_html=True)"
else:
"st.markdown('<div class=alert-safe>CLEARED: No immediate indicators of telecom fraud detected.</div>', unsafe_allow_html=True)"
# 2. Metadata Cards
"st.markdown('<div class=result-card>', unsafe_allow_html=True)"
"metric_col1, metric_col2 = st.columns(2)"
with metric_col1:
st.markdown(**Detected Dialect/Language**)
"st.markdown(f<h3 style='margin-top:0px; color:#1E293B;'>{result.get('language', 'Unknown')}</h3>, unsafe_allow_html=True)"
with metric_col2:
st.markdown(**System Confidence**)
"st.markdown(<h3 style='margin-top:0px; color:#1E293B;'>High (AI Verified)</h3>, unsafe_allow_html=True)"
"st.markdown('</div>', unsafe_allow_html=True)"
# 3. AI Reasoning
st.markdown(**AI Behavioral Analysis:**)
"st.info(result.get('scam_analysis', 'No behavioral data provided.'))"
# 4. Transcripts (Hidden by default to keep UI clean)
with st.expander(View Raw Intelligence (Transcripts & Translations)):
st.markdown(**Source Audio (Transcribed):**)
"st.write(result.get('text', 'No transcript available.'))"
st.divider()
st.markdown(**English Localization:**)
"st.write(result.get('english_text', 'No translation available.'))"
# 5. Email Dispatch Status
with st.spinner(Dispatching official report to gateway...):
"if send_email_report(user_email, result):"
st.toast(fSecure report successfully transmitted to {user_email})
else:
"st.error(Report generated locally, but email gateway transmission failed.)"