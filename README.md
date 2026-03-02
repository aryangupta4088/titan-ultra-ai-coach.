# titan-ultra-ai-coach.
🏋️‍♂️ Titan Ultra: Adaptive AI Biomechanics Coach
Titan Ultra is a high-performance, multimodal AI personal trainer that transforms a standard webcam into an elite coaching experience. By leveraging real-time computer vision and conversational AI, Titan Ultra bridges the gap between static workout apps and expensive human coaching.

🚀 Overview
Unlike traditional fitness trackers that only count movement, Titan Ultra understands it. The agent engages the user in a "Discovery Phase" to identify their skill level and then monitors their form, speed, and safety in real-time. It provides immediate vocal feedback—correcting posture and encouraging performance—before delivering a comprehensive biometric report.

🧠 Key AI Features:

Adaptive Leveling: Conversational interface to set Beginner/Pro goals.

Biometric Safety: Real-time detection of knee valgus (caving) and arm imbalance.

Velocity Tracking: Monitors "ascent speed" to detect muscle fatigue and adjust coaching intensity.

Executive Summary: Final report covering calories, mechanical efficiency, and workout duration.

🛠️ Tech Stack & Architecture
Titan Ultra orchestrates three industry-leading AI ecosystems into a single synchronous agent:

Brain (Vision & Reasoning): Gemini 3 Flash. Processes video at 3 FPS for real-time spatial reasoning and temporal movement analysis.

Voice (Interaction): ElevenLabs TTS. Provides human-like, low-latency vocal coaching and motivational cues.

Transport (Infrastructure): Stream Video SDK (WebRTC). Provides the ultra-low latency "edge" network required to stream video to the AI brain.

Orchestration: Python (Asyncio). A state-based logic engine managing transitions between greeting, coaching, and reporting.

⚙️ Installation & Setup
Clone the repository:

Bash
git clone https://github.com/YOUR_USERNAME/titan-ultra-ai-coach.git
cd titan-ultra-ai-coach
Install Dependencies:

Bash
pip install -r requirements.txt
Configure Environment Variables:
Create a .env file in the root directory and add your API keys:

Plaintext
GOOGLE_API_KEY=your_gemini_key
STREAM_API_KEY=your_stream_key
ELEVENLABS_API_KEY=your_elevenlabs_key
Run the Coach:

Bash
python coach.py
📹 How to Demo
Run the script and open the provided URL in Chrome.

Grant camera/microphone permissions.

Respond to the Coach's greeting (e.g., "I am a Beginner").

Perform your reps and receive real-time form corrections.

Listen for the final Executive Summary at the end of your set.

📈 Learning & Growth
This project demonstrates the power of Multimodal AI Orchestration. The primary challenge was managing real-time latency between three different global APIs while ensuring the AI's "eyes" (Gemini) and "voice" (ElevenLabs) stayed synced with the user's physical movement.
