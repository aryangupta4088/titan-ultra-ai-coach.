import asyncio
import os
import webbrowser
import time
from dotenv import load_dotenv
from vision_agents.core import agents, User
from vision_agents.plugins import gemini, getstream, elevenlabs

load_dotenv()

async def start_coach():
    # 1. Setup Brain and Voice
    llm = gemini.Realtime(fps=3) 
    tts = elevenlabs.TTS()

    # 2. ADAPTIVE COACH LOGIC
    # Fixed the double 'agent =' call here
    agent = agents.Agent(
        instructions="""
You are Titan Ultra, an AI Biomechanics Expert. 

### 1. EVALUATION PHASE
- Greet the user. Ask: "Level? (Beginner/Pro)" and "Target? (Strength/Fatigue)."
- Based on their answer, set the 'Rep Goal' (10 for Beginner, 30 for Pro).

### 2. BIOMETRIC MONITORING (LIVE)
- VELOCITY: Measure the speed of the ascent. If it slows down by more than 30%, say: "Bar speed is dropping! Power through!"
- SAFETY (SQUATS): Watch the knees. If they cave inward, shout: "Knees out! Keep them stable!"
- SAFETY (CHEST): If one arm is higher than the other, say: "Balance your grip! Left side is lagging."

### 3. RECOVERY & DATA
- ADAPTIVE REST: Once a set ends, start a timer. If the user starts the next set too soon, say: "Wait! Take 15 more seconds."
- CALORIE CALCULATION: 
    - Squat = 0.8 kcal/rep
    - Chest Press = 0.5 kcal/rep
    - Apply a 1.2x multiplier if the 'Velocity' was high.

### 4. THE EXECUTIVE SUMMARY
After the final rep, deliver this exact report:
- "Workout Duration: [X] minutes."
- "Total Volume: [Total Reps] movements."
- "Mechanical Efficiency: [Percentage]."
- "Total Burn: [Calculated Calories] kcal."
- "Coach's Verdict: [Level up recommendation]."
""",
        llm=llm,
        tts=tts,
        edge=getstream.Edge(), 
        agent_user=User(name="Titan Coach", id="coach-agent")
    )

    print("🚀 Adaptive Coach is coming online...")
    
    # 3. Create Session
    await agent.create_user()
    session_id = f"titan-adaptive-{int(time.time())}"
    call = await agent.create_call(call_type="default", call_id=session_id)
    
    # 4. Generate Credentials
    token = agent.edge.client.create_token("coach-agent")
    api_key = os.getenv('STREAM_API_KEY')
    
    # URL for joining the session
    url = (
        f"https://getstream.io/video/demos/sdk/?"
        f"app_key={api_key}&"
        f"user_id=coach-agent&"
        f"token={token}&"
        f"call_id={session_id}&"
        f"call_type=default"
    )
    
    print(f"\n" + "="*50)
    print(f"✅ ADAPTIVE SESSION READY")
    print(f"🔗 JOIN HERE: {url}")
    print("="*50 + "\n")
    
    webbrowser.open(url)

    # 5. Execute
    async with agent.join(call):
        print("🎙️ Coach is in the room. Waiting for you to say your level...")
        while True:
            await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(start_coach())
    except KeyboardInterrupt:
        print("\n👋 Coach signing off.")
    except Exception as e:
        print(f"\n❌ Error: {e}")