import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="ECE Paraprofessional III — Monday Exam Prep", page_icon="🎓", layout="wide")

st.markdown("""
<style>
.block-container {max-width: 1050px; padding-top: 1.5rem;}
.big-title {font-size: 2.3rem; font-weight: 800;}
.subtitle {font-size: 1.1rem;}
</style>
""", unsafe_allow_html=True)

QUESTIONS = [
# Child Development
("Child Development","Preschoolers generally learn best through:",["Hands-on play","Long lectures","Worksheets only","Silent independent work"],0,"Your study sheet says preschoolers learn best through hands-on play."),
("Child Development","When supporting development, the best principle is to:",["Judge children against one another","Support development without judging it","Expect identical development","Ignore developmental differences"],1,"The study sheet states: Support development, don't judge it."),
("Child Development","Which is described as a typical preschool skill in your study material?",["Following 2–3 step directions","Reading college textbooks","Driving independently","Managing a classroom"],0,"Following 2–3 step directions is listed among typical preschool skills."),
("Child Development","A possible developmental red flag listed in the study material is:",["No pretend play","Enjoying play","Showing emotions","Beginning cooperative play"],0,"No pretend play is one of the listed red flags."),
("Child Development","A child develops at a different pace. What is the best approach based on the study material?",["Judge the child","Support the child's development","Compare the child publicly","Ignore the difference"],1,"The key principle is to support development, not judge it."),
# Behavior
("Behavior Support","A child is upset. Which response best matches the study guide?",["Yell","Validate feelings","Threaten punishment","Ignore the child"],1,"The guide recommends validating feelings."),
("Behavior Support","A child refuses an activity. Which strategy is recommended?",["Offer choices","Shame the child","Yell","Punish harshly"],0,"Offering choices can increase cooperation."),
("Behavior Support","A child is disrupting the classroom. What should you do?",["Redirect calmly","Yell","Threaten","Embarrass the child"],0,"The scenario pattern says: Disruption → redirect calmly."),
("Behavior Support","Which approach should be avoided?",["Positive reinforcement","Calm redirection","Shaming or threatening","Offering choices"],2,"The guide says never shame, threaten, yell, or punish harshly."),
("Behavior Support","A behavior plan is in place. You should:",["Follow it exactly","Change it yourself","Ignore it","Invent a different plan"],0,"The study guide says to follow behavior plans exactly."),
("Behavior Support","Which is an example of positive reinforcement?",["'I like how you're cleaning up.'","'You're always bad.'","'Stop or else.'","'Everyone is better than you.'"],0,"The study sheet gives positive feedback about cleaning up as an example."),
("Behavior Support","A child is upset. A helpful statement is:",["'Stop crying.'","'I see you're upset. I'm here to help.'","'You're making everyone angry.'","'Go away.'"],1,"This is the example of validating feelings in the study sheet."),
# Safety
("Safety & Supervision","Active supervision means:",["Move, scan, and know where every child is","Stay seated","Watch only one child","Wait for problems"],0,"The study guide defines active supervision this way."),
("Safety & Supervision","On a playground, the paraprofessional should:",["Stay mobile and prevent risky behavior","Use a phone","Stay in one place","Let children supervise each other"],0,"The guide emphasizes mobility and prevention of risky behavior."),
("Safety & Supervision","In an emergency, the paraprofessional should:",["Follow protocol and notify the teacher immediately","Invent a new procedure","Wait","Diagnose the situation"],0,"That is the emergency guidance in the study sheet."),
("Safety & Supervision","The study guide says a paraprofessional should never:",["Diagnose or give medication","Supervise","Use precautions","Follow protocol"],0,"The material specifically says never diagnose or give medication."),
("Safety & Supervision","For bodily fluids, the study guide recommends:",["Using gloves","Ignoring them","Touching them directly","Waiting for a child to clean them"],0,"Universal precautions include gloves and sanitation."),
("Safety & Supervision","If you notice a safety problem, your first priority should be:",["Ensure safety","Finish paperwork","Ignore it","Wait until later"],0,"The quick scenario pattern begins with ensuring safety."),
# IEP
("Special Education & IEPs","An IEP is described as a:",["Legal document","Suggestion only","Optional note","Classroom decoration"],0,"The study sheet identifies an IEP as a legal document."),
("Special Education & IEPs","IEP accommodations should be:",["Followed exactly","Changed whenever convenient","Ignored","Rewritten by the paraprofessional"],0,"The guide says to follow accommodations exactly."),
("Special Education & IEPs","If an IEP instruction is unclear, you should:",["Ask the teacher","Guess","Ignore it","Ask another child"],0,"The guide says to ask the teacher if unclear."),
("Special Education & IEPs","Inclusion means:",["Supporting the child in the general classroom","Removing the child automatically","Ignoring accommodations","Replacing the teacher"],0,"That matches the study guide's definition."),
("Special Education & IEPs","Confidentiality is:",["Mandatory","Optional","Only for administrators","Not important"],0,"The study material says confidentiality is mandatory."),
("Special Education & IEPs","You should reinforce:",["Specialist strategies","Personal opinions","Unapproved changes","Rumors"],0,"The guide says to reinforce specialist strategies."),
# Professionalism
("Communication & Professionalism","The recommended communication tone is:",["Calm, respectful, professional","Loud and threatening","Sarcastic","Dismissive"],0,"The professionalism section emphasizes calm, respectful, professional communication."),
("Communication & Professionalism","If you need clarification, you should:",["Ask for clarification","Guess","Ignore the task","Ask a child"],0,"The study guide says to ask for clarification when needed."),
("Communication & Professionalism","A paraprofessional should protect:",["Confidentiality","Gossip","Private opinions","Rumors"],0,"Protecting confidentiality is emphasized."),
("Communication & Professionalism","Which quality is specifically recommended?",["Reliable and punctual","Unpredictable","Frequently late","Unprepared"],0,"The guide says to be consistent, reliable, and punctual."),
("Communication & Professionalism","A paraprofessional should maintain:",["Professional boundaries","No boundaries","Personal conflicts","Private investigations"],0,"Maintaining boundaries is listed under professionalism."),
# Classroom
("Classroom Support","A paraprofessional may:",["Support small groups","Replace the teacher","Create legal requirements","Diagnose children"],0,"Supporting small groups is a listed responsibility."),
("Classroom Support","A paraprofessional reinforces:",["Teacher instruction","Personal teaching plans","Rumors","Unapproved rules"],0,"The guide says to reinforce teacher instruction."),
("Classroom Support","Which is a classroom-support responsibility?",["Help with transitions","Replace the teacher","Ignore routines","Diagnose children"],0,"Helping with transitions is specifically listed."),
("Classroom Support","A paraprofessional should encourage:",["Independence","Dependence","Fear","Shame"],0,"Encouraging independence is one of the core responsibilities."),
("Classroom Support","The key role principle is:",["You assist — you don't replace the teacher","You replace the teacher","You work without direction","You make all classroom decisions"],0,"This is the key principle in the study sheet."),
("Classroom Support","Which areas may a paraprofessional support?",["Literacy, math, play, and routines","Only discipline","Only paperwork","Only lunch"],0,"Those areas are specifically listed."),
# Core
("Core Principles","What comes first in the 10 Core Rules?",["Safety first","Offer choices","Validate feelings","Encourage independence"],0,"Safety first is Rule #1."),
("Core Principles","Which is one of the 10 Core Rules?",["Protect confidentiality","Punish harshly","Yell","Ignore safety"],0,"Protect confidentiality is one of the core rules."),
("Core Principles","Which response is recommended for disruption?",["Redirect calmly","Yell","Threaten","Shame"],0,"Redirect calmly."),
("Core Principles","Which response is recommended for refusal?",["Offer choices","Punish","Yell","Ignore"],0,"Offer choices."),
("Core Principles","Which response is recommended when a child is upset?",["Validate feelings","Dismiss feelings","Yell","Threaten"],0,"Validate feelings."),
("Core Principles","If unsure, the scenario pattern says to:",["Ask the teacher","Guess","Ignore the issue","Ask a child"],0,"Unsure → ask the teacher."),
# Scenarios
("Scenario Practice","A child begins unsafe behavior on the playground. What is the best first action?",["Ensure safety","Start paperwork","Ignore it","Wait"],0,"Safety comes first."),
("Scenario Practice","A child refuses to clean up. What is the best approach?",["Offer choices and encourage cooperation","Yell","Shame","Threaten"],0,"Refusal → offer choices."),
("Scenario Practice","A child cries after becoming frustrated. What is the best response?",["Validate feelings and offer help","Tell the child to stop","Punish","Ignore"],0,"Upset → validate feelings."),
("Scenario Practice","A behavior plan gives a specific strategy. What should you do?",["Follow the plan","Replace it with your own","Ignore it","Change it without direction"],0,"Behavior plan → follow exactly."),
("Scenario Practice","You are unsure how to carry out an IEP accommodation. What should you do?",["Ask the teacher","Guess","Ignore it","Ask a student"],0,"Confusion → ask the teacher."),
("Scenario Practice","A classroom disruption begins. Which response best fits the study pattern?",["Redirect calmly","Yell loudly","Threaten punishment","Shame the child"],0,"Disruption → redirect calmly."),
]

CORE_RULES = [
"Safety first.","Follow teacher direction.","Use positive reinforcement.","Redirect calmly.",
"Offer choices.","Validate feelings.","Follow IEP accommodations.","Protect confidentiality.",
"Use active supervision.","Encourage independence."
]
CONFIDENCE = ["I stay calm.","I follow the plan.","I keep children safe.","I support the teacher.","I know what I'm doing."]

def start_exam(n=25):
    st.session_state.exam_questions = random.sample(QUESTIONS, min(n, len(QUESTIONS)))
    st.session_state.exam_i = 0
    st.session_state.exam_score = 0
    st.session_state.exam_answered = False
    st.session_state.exam_selected = None
    st.session_state.exam_wrong = []
    st.session_state.exam_started = True

def start_topic(domain, n=10):
    pool = [q for q in QUESTIONS if q[0] == domain]
    st.session_state.exam_questions = random.sample(pool, min(n, len(pool)))
    st.session_state.exam_i = 0
    st.session_state.exam_score = 0
    st.session_state.exam_answered = False
    st.session_state.exam_selected = None
    st.session_state.exam_wrong = []
    st.session_state.exam_started = True

if "exam_started" not in st.session_state:
    st.session_state.exam_started=False

st.title("🎓 ECE Paraprofessional III — Exam Prep")
st.markdown("### Monday Evening Exam • Inglewood, California")
st.caption("Practice tool based on your uploaded ECE Paraprofessional III study materials. It does not reproduce actual exam questions.")

tabs=st.tabs(["🏠 Home","📚 Study","📝 Practice Exam","🎯 Scenarios","💪 Exam-Day Mode"])

with tabs[0]:
    st.markdown("## Your goal: be calm, prepared, and consistent.")
    st.info("The most important scenario pattern: **Safety → Calm → Validate → Redirect → Follow plan.**")
    st.success("Use the app tonight for practice. Monday, use Exam-Day Mode for a short warm-up.")
    st.markdown("### Recommended plan")
    st.write("**Tonight:** Study → 25-question practice exam → review mistakes → repeat weak topics.")
    st.write("**Monday:** 15–20 question warm-up → review Core Rules → Confidence Booster → exam.")
    st.markdown("### Six core areas")
    for x in ["Child Development","Behavior Support","Safety & Supervision","Special Education & IEPs","Communication & Professionalism","Classroom Support"]:
        st.write("• "+x)

with tabs[1]:
    st.header("📚 Focused Study Guide")
    study = {
        "Child Development":["Hands-on play supports preschool learning.","Typical skills include following 2–3 step directions, simple sentences, big emotions, and beginning cooperative play.","Support development; don't judge it."],
        "Behavior Support":["Use positive reinforcement.","Redirect unsafe or disruptive behavior calmly.","Validate feelings.","Offer choices.","Follow behavior plans exactly.","Never shame, threaten, yell, or punish harshly."],
        "Safety & Supervision":["Move, scan, and know where every child is.","Stay mobile on the playground.","Use universal precautions such as gloves and sanitation.","Follow emergency protocol and notify the teacher immediately.","Never diagnose or give medication."],
        "Special Education & IEPs":["An IEP is a legal document.","Follow accommodations exactly.","Ask the teacher if unclear.","Reinforce specialist strategies.","Support inclusion in the general classroom.","Protect confidentiality."],
        "Communication & Professionalism":["Use a calm, respectful, professional tone.","Follow teacher direction.","Ask for clarification when needed.","Maintain boundaries.","Protect confidentiality.","Be consistent, reliable, and punctual."],
        "Classroom Support":["Support small groups.","Reinforce teacher instruction.","Help with transitions.","Encourage independence.","Model behavior.","Prepare materials as instructed.","Support literacy, math, play, and routines.","You assist — you don't replace the teacher."]
    }
    for title, bullets in study.items():
        with st.expander(title, expanded=False):
            for b in bullets: st.write("• "+b)
    st.subheader("🧠 10 Core Rules")
    for i,r in enumerate(CORE_RULES,1): st.write(f"{i}. {r}")

with tabs[2]:
    st.header("📝 Practice Exam")
    st.write("Choose a mode, then answer one question at a time.")
    c1,c2,c3=st.columns(3)
    if c1.button("25-Question Exam", type="primary"): start_exam(25); st.rerun()
    if c2.button("50-Question Exam"): start_exam(50); st.rerun()
    if c3.button("100-Question Exam"): start_exam(100); st.rerun()
    domain=st.selectbox("Or practice one topic", sorted(set(q[0] for q in QUESTIONS)))
    if st.button("Start Topic Practice"): start_topic(domain,10); st.rerun()

    if st.session_state.exam_started:
        qs=st.session_state.exam_questions; i=st.session_state.exam_i
        if i < len(qs):
            q=qs[i]
            st.progress(i/len(qs))
            st.write(f"**Question {i+1} of {len(qs)} • {q[0]}**")
            st.subheader(q[1])
            selected=st.radio("Choose one:",q[2],index=None,key=f"choice_{i}")
            if not st.session_state.exam_answered:
                if st.button("Submit Answer",type="primary"):
                    if selected is None: st.warning("Select an answer first.")
                    else:
                        st.session_state.exam_selected=q[2].index(selected)
                        st.session_state.exam_answered=True
                        if st.session_state.exam_selected==q[3]: st.session_state.exam_score+=1
                        else: st.session_state.exam_wrong.append(q)
                        st.rerun()
            else:
                if st.session_state.exam_selected==q[3]: st.success("✅ Correct!")
                else:
                    st.error("❌ Review this one.")
                    st.write("**Correct answer:** "+q[2][q[3]])
                st.info(q[4])
                if st.button("Next Question",type="primary"):
                    st.session_state.exam_i+=1; st.session_state.exam_answered=False; st.session_state.exam_selected=None; st.rerun()
        else:
            total=len(qs); pct=round(st.session_state.exam_score/total*100)
            st.success(f"Finished! **{st.session_state.exam_score}/{total} ({pct}%)**")
            if pct>=90: st.balloons(); st.success("Excellent preparation.")
            elif pct>=80: st.success("Strong preparation. Review missed questions.")
            else: st.warning("Review the weak areas and take another practice set.")
            if st.session_state.exam_wrong:
                st.subheader("Review your missed questions")
                for q in st.session_state.exam_wrong:
                    st.write("• "+q[1])
            if st.button("Start Another Exam"): start_exam(25); st.rerun()

with tabs[3]:
    st.header("🎯 Scenario Practice")
    st.markdown("### Memorize this pattern")
    st.info("**Unsafe → ensure safety**  |  **Upset → validate feelings**  |  **Refusal → offer choices**  |  **Disruption → redirect calmly**  |  **IEP → follow exactly**  |  **Unsure → ask the teacher**")
    st.subheader("Quick scenarios")
    scenario_q=[q for q in QUESTIONS if q[0]=="Scenario Practice"]
    for q in scenario_q:
        with st.expander(q[1]):
            st.write("**Best answer:** "+q[2][q[3]])
            st.write(q[4])

with tabs[4]:
    st.header("💪 Monday Exam-Day Mode")
    st.warning("Keep this short. The goal is calm focus, not cramming.")
    st.subheader("1. Reset your breathing — 20 seconds")
    st.write("Inhale 4 seconds → hold 2 → exhale 6. Repeat twice.")
    st.subheader("2. Say these five lines out loud")
    for x in CONFIDENCE: st.write("• "+x)
    st.subheader("3. Recall the 10 Core Rules")
    for i,r in enumerate(CORE_RULES,1): st.write(f"{i}. {r}")
    st.subheader("4. Last-minute scenario pattern")
    st.success("Safety → Calm → Validate → Redirect → Follow plan")
    st.subheader("5. Final mindset")
    st.success("**“I’m prepared. I’m steady. I’m ready.”**")
    st.caption("Your uploaded Morning-Of checklist recommends quiet confidence, relaxed shoulders, and one deep breath before entering the test.")

st.divider()
st.caption("Practice content derived from the uploaded ECE Paraprofessional III study materials. This is a study aid, not an official exam or answer key.")
