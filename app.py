import streamlit as st
import random

st.set_page_config(page_title="Inglewood IUSD Paraprofessional III ECE Exam Prep", page_icon="🎓", layout="wide")
QUESTIONS=[{'section': 'PTKLF',
  'type': 'mc',
  'question': 'Which classroom activity is most consistent with developmentally appropriate preschool/TK learning?',
  'options': ['Children explore counting with blocks and explain how they grouped them',
              'Children complete a long timed worksheet without materials',
              'Children memorize answers without discussion',
              'Children copy a page of definitions'],
  'answers': ['Children explore counting with blocks and explain how they grouped them'],
  'why': 'Hands-on exploration, language, and reasoning are consistent with developmentally appropriate early learning.'},
 {'section': 'PTKLF',
  'type': 'mc',
  'question': 'A child keeps trying different ways to make a block bridge stand. Which approach-to-learning skill is most evident?',
  'options': ['Persistence and problem-solving', 'Rote memorization', 'Avoidance', 'Dependence'],
  'answers': ['Persistence and problem-solving'],
  'why': 'Trying different strategies and staying engaged shows persistence and flexible problem-solving.'},
 {'section': 'PTKLF',
  'type': 'mc',
  'question': 'A multilingual child uses a home-language word while explaining a picture. The best response is to:',
  'options': ['Value the communication and support continued language development',
              'Tell the child only English is allowed',
              'Ignore the explanation',
              'Correct the child publicly'],
  'answers': ['Value the communication and support continued language development'],
  'why': "California's current early-learning framework is culturally and linguistically responsive and recognizes children's language assets."},
 {'section': 'PTKLF',
  'type': 'mc',
  'question': 'Which activity best supports phonological awareness?',
  'options': ["Clapping the syllables in children's names", 'Sorting blocks by size', 'Running an obstacle course', 'Painting with sponges'],
  'answers': ["Clapping the syllables in children's names"],
  'why': 'Phonological awareness involves noticing and working with sounds in spoken language.'},
 {'section': 'PTKLF',
  'type': 'mc',
  'question': 'A child counts six objects and understands that the final number means there are six in all. This demonstrates:',
  'options': ['Cardinality', 'Rhyming', 'Dramatic play', 'Gross-motor coordination'],
  'answers': ['Cardinality'],
  'why': 'Cardinality is understanding that the last number counted represents the quantity of the set.'},
 {'section': 'PTKLF',
  'type': 'mc',
  'question': 'Children predict whether objects will sink or float and then test them. This primarily supports:',
  'options': ['Scientific inquiry', 'Print awareness', 'Self-care', 'Music'],
  'answers': ['Scientific inquiry'],
  'why': 'Prediction, testing, observation, and comparison are core inquiry behaviors.'},
 {'section': 'PTKLF',
  'type': 'mc',
  'question': 'A child becomes frustrated when a tower falls. The best adult response is to:',
  'options': ['Acknowledge the feeling and encourage another strategy',
              'Build the tower for the child immediately',
              'Tell the child frustration is silly',
              'Compare the child with a peer'],
  'answers': ['Acknowledge the feeling and encourage another strategy'],
  'why': 'Emotion coaching plus support for persistence promotes social-emotional development and learning.'},
 {'section': 'PTKLF',
  'type': 'mc',
  'question': 'Which adult response best promotes independence?',
  'options': ['Provide only the assistance needed and allow the child to complete the rest',
              'Complete every difficult task for the child',
              'Never offer assistance',
              'Ask another child to do the task'],
  'answers': ['Provide only the assistance needed and allow the child to complete the rest'],
  'why': "Scaffolding should support successful participation without unnecessarily replacing the child's effort."},
 {'section': 'PTKLF',
  'type': 'mc',
  'question': 'Which classroom material best supports open-ended creative expression?',
  'options': ['Blocks, fabric, boxes, and loose parts', 'Only preprinted worksheets', 'Only flash cards', 'Only teacher-made models to copy'],
  'answers': ['Blocks, fabric, boxes, and loose parts'],
  'why': 'Open-ended materials allow children to plan, represent, construct, and create.'},
 {'section': 'PTKLF',
  'type': 'mc',
  'question': 'Which observation statement is most objective?',
  'options': ['Maya left the carpet twice during the 12-minute story.',
              'Maya was disrespectful.',
              'Maya did not care about the story.',
              'Maya wanted to cause trouble.'],
  'answers': ['Maya left the carpet twice during the 12-minute story.'],
  'why': 'Objective observation describes observable behavior rather than motives or labels.'},
 {'section': 'Professional Practice',
  'type': 'mc',
  'question': 'A parent asks why another child receives special classroom support. The paraprofessional should:',
  'options': ["Protect the child's confidentiality and refer appropriately",
              "Explain the child's disability",
              "Show the parent the child's plan",
              'Ask other children to explain'],
  'answers': ["Protect the child's confidentiality and refer appropriately"],
  'why': 'Student information should be protected and shared only as authorized.'},
 {'section': 'Professional Practice',
  'type': 'mc',
  'question': 'A child with an IEP needs assistance during an activity. The paraprofessional should:',
  'options': ["Follow the student's plan and teacher direction while supporting independence",
              'Create a new accommodation independently',
              'Ignore the plan',
              'Discuss the plan with other families'],
  'answers': ["Follow the student's plan and teacher direction while supporting independence"],
  'why': 'Paraprofessionals support implementation of authorized plans and teacher direction.'},
 {'section': 'Professional Practice',
  'type': 'mc',
  'question': 'A child repeatedly grabs materials. The best guidance response is to:',
  'options': ['Calmly teach and reinforce how to request or wait for a turn',
              'Call the child selfish',
              'Remove all materials for the day',
              'Publicly shame the child'],
  'answers': ['Calmly teach and reinforce how to request or wait for a turn'],
  'why': 'Positive guidance teaches an appropriate replacement skill.'},
 {'section': 'Professional Practice',
  'type': 'mc',
  'question': 'During active playground supervision, the paraprofessional should:',
  'options': ['Position, scan, move, and monitor children and hazards',
              'Use a personal phone while children play',
              'Stay in one place with limited visibility',
              'Watch only children who are loud'],
  'answers': ['Position, scan, move, and monitor children and hazards'],
  'why': 'Active supervision requires continuous awareness of children and the environment.'},
 {'section': 'Professional Practice',
  'type': 'mc',
  'question': 'A child is moving toward an immediate hazard. What should the paraprofessional do FIRST?',
  'options': ['Act immediately to protect the child from the hazard',
              'Finish documenting another event',
              'Wait for the teacher to notice',
              'Ask another child what to do'],
  'answers': ['Act immediately to protect the child from the hazard'],
  'why': 'Immediate safety is the first priority when a child faces an urgent hazard.'},
 {'section': 'DRDP',
  'type': 'mc',
  'question': 'What is the main purpose of the DRDP in early education?',
  'options': ['To assess developmental progress and help inform curriculum planning',
              'To rank children publicly',
              'To diagnose every disability',
              'To replace teacher observation'],
  'answers': ['To assess developmental progress and help inform curriculum planning'],
  'why': 'The DRDP is a developmental assessment used to understand progress and inform planning.'},
 {'section': 'DRDP',
  'type': 'mc',
  'question': 'Which evidence is most useful when completing a developmental assessment?',
  'options': ['Repeated observations of what a child actually does in natural activities',
              'A guess about what the child probably can do',
              "One adult's opinion without evidence",
              'Comparisons intended to rank classmates'],
  'answers': ['Repeated observations of what a child actually does in natural activities'],
  'why': 'Developmental assessment should be grounded in observable evidence across meaningful contexts.'},
 {'section': 'DRDP',
  'type': 'mc',
  'question': 'The current DRDP 2025 is designed to include:',
  'options': ['Children with disabilities and dual language learners',
              'Only children without IEPs',
              'Only kindergarten children',
              'Only children who speak English'],
  'answers': ['Children with disabilities and dual language learners'],
  'why': 'The revised DRDP is designed for all children and includes more inclusive examples.'},
 {'section': 'DRDP',
  'type': 'mc',
  'question': 'A child demonstrates a skill using sign language or an AAC system. When observing development, the educator should:',
  'options': ['Recognize the demonstrated skill rather than requiring spoken language',
              'Ignore the skill',
              'Automatically rate the child lower',
              'Require the child to repeat it verbally'],
  'answers': ['Recognize the demonstrated skill rather than requiring spoken language'],
  'why': 'Current DRDP guidance includes inclusive ways children may demonstrate competencies.'},
 {'section': 'DRDP',
  'type': 'mc',
  'question': 'For California State Preschool Programs beginning July 1, 2026, which version is required?',
  'options': ['DRDP (2025)', 'DRDP (2001)', 'No developmental profile', 'A locally invented profile only'],
  'answers': ['DRDP (2025)'],
  'why': 'CDE states that DRDP (2025) is required for CSPP contractors beginning July 1, 2026.'},
 {'section': 'CLASS',
  'type': 'mc',
  'question': 'CLASS is best understood as a tool focused on:',
  'options': ['The quality of classroom interactions and learning environment',
              "A child's medical diagnosis",
              "A student's home address",
              'Payroll procedures'],
  'answers': ['The quality of classroom interactions and learning environment'],
  'why': 'CLASS is an observational approach used to examine classroom interactions rather than diagnose individual children.'},
 {'section': 'CLASS',
  'type': 'mc',
  'question': 'Which adult behavior would generally reflect stronger classroom interaction quality?',
  'options': ['Warm, responsive interaction with meaningful feedback',
              'Frequent public humiliation',
              "Ignoring children's ideas",
              'Using threats as the main guidance strategy'],
  'answers': ['Warm, responsive interaction with meaningful feedback'],
  'why': 'Responsive, supportive interaction is more consistent with high-quality classroom practice.'},
 {'section': 'ASQ',
  'type': 'mc',
  'question': 'The ASQ is commonly used in early childhood settings as:',
  'options': ['A developmental screening tool', 'A final medical diagnosis', 'A teacher performance evaluation', 'A high-school achievement test'],
  'answers': ['A developmental screening tool'],
  'why': 'ASQ is a screening tool; screening is not the same as diagnosis.'},
 {'section': 'ASQ',
  'type': 'mc',
  'question': 'If a developmental screening raises a concern, the paraprofessional should generally:',
  'options': ['Follow program procedures and communicate with the appropriate teacher/staff',
              'Diagnose the child',
              'Tell other parents',
              'Promise a specific diagnosis'],
  'answers': ['Follow program procedures and communicate with the appropriate teacher/staff'],
  'why': 'A paraprofessional should follow authorized procedures rather than independently diagnose.'},
 {'section': 'ASQ-SE',
  'type': 'mc',
  'question': 'ASQ-SE is especially focused on:',
  'options': ['Social-emotional development', 'Algebra', 'Physical height only', 'Spelling'],
  'answers': ['Social-emotional development'],
  'why': 'ASQ-SE is designed to screen social-emotional development.'},
 {'section': 'Assessment',
  'type': 'mc',
  'question': 'Which statement best distinguishes screening from diagnosis?',
  'options': ['Screening can identify possible concerns; diagnosis requires appropriate qualified evaluation',
              'They are exactly the same',
              'A paraprofessional can diagnose from one screening',
              'Screening guarantees a disability'],
  'answers': ['Screening can identify possible concerns; diagnosis requires appropriate qualified evaluation'],
  'why': 'Screening flags possible concerns; it does not itself establish a diagnosis.'},
 {'section': 'Assessment',
  'type': 'mc',
  'question': 'A paraprofessional notices a new behavior during observation. The best documentation is:',
  'options': ['Record what was seen and heard, including relevant context',
              'Write a negative personality label',
              "Guess the child's intention",
              'Change the record to match expectations'],
  'answers': ['Record what was seen and heard, including relevant context'],
  'why': 'Objective, contextualized observation is more useful and professional than labels or guesses.'},
 {'section': 'Reading',
  'type': 'mc',
  'question': 'During center time, Ms. Lee notices that Jordan watches two classmates build a road with blocks. Jordan moves closer but does not '
              'speak. Ms. Lee places two extra cars nearby and says, “Jordan, you can add a car to the road if you would like.” Jordan picks up a '
              'car and joins the play.\n'
              '\n'
              'What did Ms. Lee do to support Jordan?',
  'options': ['She provided a low-pressure way to join the play',
              'She required Jordan to speak first',
              'She ended center time',
              'She removed the blocks'],
  'answers': ['She provided a low-pressure way to join the play'],
  'why': 'Ms. Lee created an accessible entry into peer play without forcing participation.'},
 {'section': 'Reading',
  'type': 'mc',
  'question': 'The class planted bean seeds in two cups. One cup was placed near a sunny window and the other in a darker area. Each day, children '
              'observed the cups and recorded changes with drawings.\n'
              '\n'
              'What is the main purpose of this activity?',
  'options': ['To observe and compare how conditions affect plant growth',
              'To practice handwriting speed',
              'To memorize plant names only',
              'To teach children to compete'],
  'answers': ['To observe and compare how conditions affect plant growth'],
  'why': 'The activity emphasizes observation, comparison, and recording change.'},
 {'section': 'Reading',
  'type': 'mc',
  'question': 'A classroom procedure says that when a child is injured, staff should first ensure immediate safety and provide appropriate care, '
              'then notify designated personnel and document the incident according to program rules.\n'
              '\n'
              'According to the passage, what comes before documentation?',
  'options': ['Immediate safety, care, and required notification', 'Calling every family', 'Determining blame', 'Finishing the lesson'],
  'answers': ['Immediate safety, care, and required notification'],
  'why': 'The stated sequence places safety, care, and notification before documentation.'},
 {'section': 'Reading',
  'type': 'mc',
  'question': 'Ana speaks both Spanish and English. During a story discussion she answers part of a question in Spanish. The teacher acknowledges '
              'her idea, restates it in English, and invites Ana to continue.\n'
              '\n'
              'What principle is illustrated?',
  'options': ["Building on a child's existing language as an asset",
              'Prohibiting home-language use',
              'Correcting through embarrassment',
              'Avoiding participation'],
  'answers': ["Building on a child's existing language as an asset"],
  'why': "The teacher values Ana's communication while supporting English development."},
 {'section': 'Reading',
  'type': 'mc',
  'question': 'The teacher asks children to sort buttons. One child sorts by color; another sorts by size. The teacher asks each child to explain '
              'the rule used.\n'
              '\n'
              'Why does the teacher ask children to explain?',
  'options': ['To make their mathematical reasoning visible',
              'To determine who is fastest',
              'To discourage different strategies',
              'To practice memorization only'],
  'answers': ['To make their mathematical reasoning visible'],
  'why': "Explaining a sorting rule reveals children's reasoning about attributes and classification."},
 {'section': 'Writing & Grammar',
  'type': 'mc',
  'question': 'Which sentence is written most professionally?',
  'options': ['The student completed the activity with one verbal reminder.',
              'The student done the activity good.',
              'Student, she completed activity.',
              'The student complete it yesterday.'],
  'answers': ['The student completed the activity with one verbal reminder.'],
  'why': 'The first sentence uses clear, standard grammar.'},
 {'section': 'Writing & Grammar',
  'type': 'mc',
  'question': 'Choose the sentence with correct subject-verb agreement.',
  'options': ['The children are playing outside.',
              'The children is playing outside.',
              'The children was plays outside.',
              'The children be playing outside.'],
  'answers': ['The children are playing outside.'],
  'why': "A plural subject 'children' takes 'are.'"},
 {'section': 'Writing & Grammar',
  'type': 'mc',
  'question': 'Which sentence uses punctuation correctly?',
  'options': ['After snack, the children washed their hands.',
              'After snack the children, washed their hands.',
              'After snack the children washed, their hands.',
              'After, snack the children washed their hands.'],
  'answers': ['After snack, the children washed their hands.'],
  'why': 'The introductory phrase is correctly followed by a comma.'},
 {'section': 'Writing & Grammar',
  'type': 'mc',
  'question': 'Which note is most appropriate for an incident report?',
  'options': ['At 10:05 a.m., Luis pushed the blue chair approximately two feet.',
              'Luis was acting terrible again.',
              'Luis clearly wanted to make everyone angry.',
              'Luis is always a problem.'],
  'answers': ['At 10:05 a.m., Luis pushed the blue chair approximately two feet.'],
  'why': 'Professional documentation uses observable facts rather than labels.'},
 {'section': 'Writing & Grammar',
  'type': 'mc',
  'question': 'Which revision is clearest?',
  'options': ['The teacher gave the child two choices for cleanup.',
              'Two choices for cleanup were the thing the teacher gave.',
              'For cleanup choices teacher two gave child.',
              'The child, choices, teacher cleanup.'],
  'answers': ['The teacher gave the child two choices for cleanup.'],
  'why': 'The first version is concise and grammatically clear.'},
 {'section': 'Writing & Grammar',
  'type': 'mc',
  'question': 'Choose the correctly spelled word.',
  'options': ['supervision', 'supervison', 'supervission', 'suprvision'],
  'answers': ['supervision'],
  'why': "'Supervision' is the correct spelling."},
 {'section': 'Writing & Grammar',
  'type': 'mc',
  'question': 'Which sentence is most concise?',
  'options': ['Please place the books on the shelf.',
              'It would be appreciated if you could possibly place the books up there on the shelf.',
              'The books, if possible, maybe put them there.',
              'Could you perhaps maybe put books somewhere?'],
  'answers': ['Please place the books on the shelf.'],
  'why': 'The first sentence is direct and clear.'},
 {'section': 'Writing & Grammar',
  'type': 'mc',
  'question': "Which word best completes the sentence? 'The paraprofessional ___ the teacher during small-group instruction.'",
  'options': ['assists', 'assist', 'assisting', 'have assist'],
  'answers': ['assists'],
  'why': "A singular subject takes the verb 'assists.'"},
 {'section': 'Mathematics',
  'type': 'mc',
  'question': 'A classroom has 24 crayons shared equally among 6 children. How many crayons does each child receive?',
  'options': ['4', '3', '5', '6'],
  'answers': ['4'],
  'why': '24 ÷ 6 = 4.'},
 {'section': 'Mathematics',
  'type': 'mc',
  'question': 'There are 18 children. Three are absent. How many are present?',
  'options': ['15', '14', '16', '21'],
  'answers': ['15'],
  'why': '18 - 3 = 15.'},
 {'section': 'Mathematics',
  'type': 'mc',
  'question': 'A teacher has 5 tables with 4 children at each table. How many children are seated?',
  'options': ['20', '9', '16', '25'],
  'answers': ['20'],
  'why': '5 × 4 = 20.'},
 {'section': 'Mathematics',
  'type': 'mc',
  'question': 'Snack begins at 10:15 a.m. and ends at 10:40 a.m. How long is snack?',
  'options': ['25 minutes', '15 minutes', '20 minutes', '35 minutes'],
  'answers': ['25 minutes'],
  'why': 'From 10:15 to 10:40 is 25 minutes.'},
 {'section': 'Mathematics',
  'type': 'mc',
  'question': 'A box contains 30 markers. If 12 are used, how many remain?',
  'options': ['18', '16', '20', '22'],
  'answers': ['18'],
  'why': '30 - 12 = 18.'},
 {'section': 'Mathematics',
  'type': 'mc',
  'question': 'A class has 8 boys and 12 girls. What fraction of the 20 children are boys?',
  'options': ['2/5', '3/5', '1/4', '4/5'],
  'answers': ['2/5'],
  'why': '8/20 simplifies to 2/5.'},
 {'section': 'Mathematics',
  'type': 'mc',
  'question': 'A supply costs $7.50 and another costs $2.25. What is the total?',
  'options': ['$9.75', '$9.25', '$10.25', '$8.75'],
  'answers': ['$9.75'],
  'why': '7.50 + 2.25 = 9.75.'},
 {'section': 'Mathematics',
  'type': 'mc',
  'question': 'A 60-minute activity block is divided equally among 3 centers. How many minutes per center?',
  'options': ['20', '15', '30', '25'],
  'answers': ['20'],
  'why': '60 ÷ 3 = 20.'},
 {'section': 'Mathematics',
  'type': 'mc',
  'question': 'There are 16 children and 4 adults. What is the ratio of children to adults in simplest form?',
  'options': ['4:1', '1:4', '8:1', '2:1'],
  'answers': ['4:1'],
  'why': '16:4 simplifies by dividing both numbers by 4.'},
 {'section': 'Mathematics',
  'type': 'mc',
  'question': 'A child completes 9 of 12 tasks. What percentage is that?',
  'options': ['75%', '70%', '80%', '90%'],
  'answers': ['75%'],
  'why': '9 ÷ 12 = 0.75 = 75%.'},
 {'section': 'Scenario Challenge',
  'type': 'mc',
  'question': 'A child is crying and says another child took a toy. What is the BEST first response?',
  'options': ['Approach calmly, acknowledge the feeling, and help gather what happened',
              'Immediately punish the other child',
              'Tell the crying child to stop',
              'Ignore both children'],
  'answers': ['Approach calmly, acknowledge the feeling, and help gather what happened'],
  'why': 'Start with a calm, supportive response and gather facts before deciding what support is needed.'},
 {'section': 'Scenario Challenge',
  'type': 'mc',
  'question': 'A child with limited English does not respond to a verbal direction. What is the BEST next step?',
  'options': ['Use a gesture or visual and model the expected action',
              'Assume the child is refusing',
              'Raise your voice',
              'Remove the child from the activity'],
  'answers': ['Use a gesture or visual and model the expected action'],
  'why': 'Visuals, gestures, and modeling can increase access without assuming intent.'},
 {'section': 'Scenario Challenge',
  'type': 'mc',
  'question': 'You see a child put a small object in their mouth. What should you do FIRST?',
  'options': ['Address the immediate safety risk', 'Write an incident report', 'Finish the activity', 'Ask the child why'],
  'answers': ['Address the immediate safety risk'],
  'why': 'Immediate safety takes priority.'},
 {'section': 'Scenario Challenge',
  'type': 'mc',
  'question': "A teacher asks you to observe one child's peer interactions. Which note is BEST?",
  'options': ["11:05 — Sam asked, 'Can I play?' and waited beside the block area.",
              'Sam was very social today.',
              'Sam likes everyone.',
              'Sam behaved perfectly.'],
  'answers': ["11:05 — Sam asked, 'Can I play?' and waited beside the block area."],
  'why': 'The first note is specific, observable, and time-linked.'},
 {'section': 'Scenario Challenge',
  'type': 'mc',
  'question': 'A child can wash hands independently but asks you to do it for them. BEST response?',
  'options': ['Encourage the child to do the steps they can manage, assisting only if needed',
              'Do every step',
              'Refuse to supervise',
              'Skip handwashing'],
  'answers': ['Encourage the child to do the steps they can manage, assisting only if needed'],
  'why': 'Support independence while maintaining appropriate supervision.'},
 {'section': 'Scenario Challenge',
  'type': 'mc',
  'question': "A family member asks you for another child's screening result. BEST response?",
  'options': ['Do not disclose it; protect confidentiality and refer appropriately',
              'Share the score',
              'Give a copy of the record',
              'Discuss it in the hallway'],
  'answers': ['Do not disclose it; protect confidentiality and refer appropriately'],
  'why': 'Screening and student information should remain confidential.'},
 {'section': 'Scenario Challenge',
  'type': 'mc',
  'question': 'A child is having difficulty following a classroom routine. What should you do before labeling the child defiant?',
  'options': ['Observe possible causes and provide appropriate support',
              'Punish immediately',
              'Compare the child with peers',
              'Tell the family the child is defiant'],
  'answers': ['Observe possible causes and provide appropriate support'],
  'why': 'Observation and support are more appropriate than assumptions about motive.'},
 {'section': 'Scenario Challenge',
  'type': 'mc',
  'question': 'You are unsure whether a medication authorization is current. BEST action?',
  'options': ['Do not guess; follow site procedures and verify with authorized staff',
              'Administer it anyway',
              'Ask another child',
              'Estimate the dose'],
  'answers': ['Do not guess; follow site procedures and verify with authorized staff'],
  'why': 'Medication procedures require authorization and verification.'},
 {'section': 'Scenario Challenge',
  'type': 'mc',
  'question': 'Two children disagree about whether a rock will sink. BEST instructional response?',
  'options': ['Invite predictions and test the rock together',
              'Tell them the answer and end the activity',
              "Choose the older child's answer",
              'Tell them disagreement is inappropriate'],
  'answers': ['Invite predictions and test the rock together'],
  'why': 'Testing predictions turns disagreement into scientific inquiry.'},
 {'section': 'Scenario Challenge',
  'type': 'mc',
  'question': 'A child becomes frustrated with a zipper. BEST response?',
  'options': ['Help only with the step the child cannot yet manage, then let the child continue',
              'Zip it completely every time',
              'Tell the child to stop trying',
              'Ask a peer to do it'],
  'answers': ['Help only with the step the child cannot yet manage, then let the child continue'],
  'why': 'Partial assistance is an effective scaffold for independence.'},
 {'section': 'Health & Safety',
  'type': 'multi',
  'question': 'Select ALL practices that support active supervision.',
  'options': ['Scan the environment',
              'Position yourself to see children',
              'Move as needed to reduce blind spots',
              'Use a personal phone for messages',
              'Leave children unattended'],
  'answers': ['Scan the environment', 'Position yourself to see children', 'Move as needed to reduce blind spots'],
  'why': 'Active supervision requires continuous awareness, strategic positioning, and movement.'},
 {'section': 'Professional Practice',
  'type': 'multi',
  'question': 'Select ALL appropriate responses when you are unsure about an authorized student procedure.',
  'options': ['Ask the supervising teacher or authorized staff',
              'Review the applicable plan/procedure if authorized',
              'Guess based on what usually works',
              'Create a new rule yourself'],
  'answers': ['Ask the supervising teacher or authorized staff', 'Review the applicable plan/procedure if authorized'],
  'why': 'When procedures are unclear, use authorized sources and supervision rather than improvising.'},
 {'section': 'Assessment',
  'type': 'tf',
  'question': 'True or False: A screening result by itself is the same as a formal diagnosis.',
  'options': ['True', 'False'],
  'answers': ['False'],
  'why': 'Screening may identify a possible concern; it is not itself a diagnosis.'},
 {'section': 'DRDP',
  'type': 'tf',
  'question': 'True or False: The DRDP 2025 is designed to assess developmental progression for children including those with an IFSP or IEP.',
  'options': ['True', 'False'],
  'answers': ['True'],
  'why': 'CDE describes the DRDP 2025 as inclusive of children with IFSPs or IEPs.'},
 {'section': 'PTKLF',
  'type': 'tf',
  'question': "True or False: California's PTKLF address nine domains of early learning and development.",
  'options': ['True', 'False'],
  'answers': ['True'],
  'why': 'The current PTKLF organize early learning and development into nine domains.'}]

SECTIONS=sorted(set(q["section"] for q in QUESTIONS))
for k,v in {"run":[],"i":0,"score":0,"answered":False,"selected":[],"wrong":[],"label":""}.items():
    if k not in st.session_state: st.session_state[k]=v

def start(pool,label,n=None):
    chosen=pool[:] if n is None else random.sample(pool,min(n,len(pool)))
    random.shuffle(chosen)
    st.session_state.run=chosen
    st.session_state.i=0; st.session_state.score=0; st.session_state.answered=False
    st.session_state.selected=[]; st.session_state.wrong=[]; st.session_state.label=label

def widget(q,i):
    opts=q["options"][:]
    random.Random(i+9000+len(q["question"])).shuffle(opts)
    if q["type"]=="multi":
        return st.multiselect("Select ALL answers that apply:",opts,key=f"m_{i}")
    val=st.radio("Choose one:",opts,index=None,key=f"r_{i}")
    return [] if val is None else [val]

st.title("🎓 Inglewood IUSD Paraprofessional III — ECE Exam Prep")
st.caption("Targeted independent study app using original practice questions. Not an official IUSD or eSkill assessment.")

tabs=st.tabs(["🏠 Home","🎯 What to Focus On","📚 Study Guide","📝 Mock Exams","🧠 Topic Practice","🎯 Scenario Challenge","➗ Reading/Writing/Math","✅ Final Review"])
home,focus,study,tests,topics,scenario,academic,final=tabs

with home:
    st.header("Targeted to the current IUSD Paraprofessional III – ECE posting")
    st.write("This version combines California PTKLF, DRDP, CLASS, ASQ/ASQ-SE concepts, safe preschool supervision, professional judgment, and reading/writing/mathematics practice.")
    st.info("Suggested order: **Study Guide → Mock Exam 1 → review weak areas → Scenario Challenge → Mock Exam 2 → Final Review**.")
    st.warning("The actual district/eSkill assessment can be customized. These are original practice questions, not leaked or official exam questions.")


with focus:
    st.header("🎯 What to Focus On Before the Exam")
    st.info("Suggested study-time split: **50% ECE/scenario questions • 25% PTKLF + DRDP/CLASS/ASQ • 25% reading/writing/math**")

    st.subheader("1. Scenario Questions — Highest-Value Practice")
    st.write("When a question asks **FIRST**, **BEST**, or **MOST appropriate**, use this decision sequence:")
    st.success("**Safety → Stay calm → Protect dignity → Teach/support → Follow the authorized plan/procedure → Document objectively**")
    st.markdown("""
- **Safety:** If anyone faces an immediate hazard, address it first.
- **Stay calm:** Use a calm voice and professional behavior; avoid yelling, threatening, or overreacting.
- **Protect dignity:** Do not shame, label, embarrass, or publicly discuss private information.
- **Teach/support:** Help the child learn an appropriate replacement behavior rather than only punishing the mistake.
- **Follow procedure:** Follow teacher direction and authorized IEP/behavior, health, safety, emergency, and medication procedures.
- **Document objectively:** Record what you actually saw and heard, not your opinion about motives.
""")
    with st.expander("Example: FIRST means immediate priority"):
        st.write("**Situation:** A preschooler runs toward an open gate leading to a parking lot.")
        st.write("**Best FIRST action:** Immediately intervene to keep the child safe.")
        st.caption("Documentation and investigation may come later. Immediate danger makes safety the first priority.")

    st.subheader("2. Behavior Questions")
    st.write("Do not automatically choose punishment. Look for the answer that **teaches the missing or replacement skill**.")
    st.markdown("""
For a toy conflict, for example, the missing skills may be **requesting, waiting, communicating, sharing, or taking turns**.

**Memory rule:** Don't just stop the behavior — teach the replacement behavior.
""")

    st.subheader("3. PTKLF")
    st.write("Think of PTKLF as: **What should young children be developing, and how should adults appropriately support that development?**")
    st.markdown("""
Look for developmentally appropriate support of **play, persistence, problem-solving, language, literacy, mathematics, science, social-emotional development, physical development, health, arts, and growing independence**.

When stuck between two answers, ask:

**Which response best helps the child learn, participate, communicate, explore, solve problems, and become increasingly independent?**
""")

    st.subheader("4. DRDP")
    st.write("**DRDP = developmental progress over time.**")
    st.markdown("""
Think **observe → collect evidence → understand progress → inform planning**.

Strong documentation:
- “At 10:15, Maya counted six blocks, touching each block once, and said, ‘There are six.’”

Weak documentation:
- “Maya is very smart at math.”

Choose **specific + observable + factual + objective** evidence rather than labels, opinions, or assumptions.
""")

    st.subheader("5. Keep the Assessment Tools Straight")
    st.table({
        "Tool":["PTKLF","DRDP","CLASS","ASQ","ASQ-SE"],
        "Quick meaning":[
            "What young children are learning/developing",
            "Observe and assess developmental progress",
            "Quality of classroom interactions",
            "Developmental screening",
            "Social-emotional screening"
        ]
    })
    st.warning("**Screening ≠ diagnosis.** A screening may identify a possible concern; it does not by itself establish a diagnosis.")
    st.markdown("""
**Memory sentence:**  
**PTKLF** = WHAT develops • **DRDP** = HOW development is progressing • **CLASS** = INTERACTIONS • **ASQ** = SCREENING • **ASQ-SE** = SOCIAL-EMOTIONAL screening.
""")

    st.subheader("6. Reading")
    st.write("Practice workplace-style reading comprehension: **main idea, sequence, what happened first, supported statements, and reasonable conclusions**.")
    st.success("Answer from the passage — not from what you personally know.")

    st.subheader("7. Writing & Grammar")
    st.markdown("""
Prioritize:
- Subject-verb agreement
- Verb tense
- Spelling and punctuation
- Sentence clarity
- Professional workplace writing
- Objective incident documentation

Better: **“At 10:20 a.m., James pushed the chair approximately three feet.”**  
Weaker: **“James was being terrible again.”**
""")

    st.subheader("8. Mathematics")
    st.markdown("""
Focus on practical fundamentals:
- Addition and subtraction
- Multiplication and division
- Fractions
- Percentages
- Ratios
- Money
- Elapsed time

Examples: **24 ÷ 6 = 4** • **9/12 = 75%** • **16:4 = 4:1** • **10:15–10:40 = 25 minutes**
""")

    st.subheader("9. When Two Answers Sound Correct")
    st.write("Look closely at the question word. If it asks **FIRST**, choose the immediate priority. If it asks **BEST/MOST appropriate**, choose the most professional, developmentally appropriate, respectful, inclusive, and supportive response.")
    with st.expander("Example: several answers may eventually be correct"):
        st.write("A child becomes upset and begins throwing blocks.")
        st.write("Explaining the rule, teaching another way to express frustration, and documenting may all be appropriate later.")
        st.write("**FIRST:** Ensure the child and other children are safe.")

    st.subheader("10. Exam-Day Memory Sheet")
    st.markdown("""
- **FIRST** = immediate priority; when a hazard exists, think safety.
- **BEST** = developmentally appropriate + respectful + professional.
- **Behavior problem** = teach a replacement skill.
- **Child struggling** = scaffold; don't automatically take over.
- **Observation** = what you saw/heard, not what you think.
- **Confidential information** = protect it.
- **Medication / safety / IEP / procedure** = don't guess; follow the authorized procedure.
- **DRDP** = developmental progress.
- **CLASS** = classroom interactions.
- **ASQ** = developmental screening.
- **ASQ-SE** = social-emotional screening.
- **Screening is not diagnosis.**
""")

with study:
    st.header("📚 High-Yield Study Guide")
    guides={
    "1. California PTKLF":"Current California preschool/TK foundations describe learning and development for roughly ages 3–5½ across nine domains. Focus on developmentally appropriate, inclusive, play- and inquiry-based learning; language/literacy; math; science; social-emotional development; physical development; health; history-social science; arts; and approaches to learning.",
    "2. DRDP (2025)":"Know that DRDP is a developmental continuum used to assess progress and inform curriculum/program planning. The 2025 revision is aligned to PTKLF and is more inclusive of children with disabilities and dual language learners. Objective evidence matters.",
    "3. CLASS":"Know the basic idea: observation of classroom interaction quality. For practice questions, favor warm, responsive, organized, language-rich interactions and meaningful feedback rather than punitive or disengaged interaction.",
    "4. ASQ / ASQ-SE":"Treat these as screening tools, not diagnoses. ASQ concerns development broadly; ASQ-SE focuses on social-emotional development. Follow program procedures when a screening raises a concern.",
    "5. Guidance & Behavior":"Use calm redirection, positive reinforcement, emotion coaching, limited choices, replacement skills, and consistent expectations. Avoid shaming, threats, labels, and unnecessary exclusion.",
    "6. Safety & Supervision":"Immediate hazards come first. Use active supervision: position, scan, move, anticipate hazards, and follow site emergency/health/medication procedures.",
    "7. Observation & Confidentiality":"Write what you saw and heard, not what you assume. Protect student information. Follow IEPs/plans and teacher/authorized staff direction.",
    "8. Reading/Writing/Math":"Expect practical high-school-level fundamentals: reading comprehension, sequence and main idea, grammar, spelling, professional writing, arithmetic, fractions, percentages, ratios, money, and elapsed time."
    }
    for title,text in guides.items():
        with st.expander(title):
            st.write(text)

with tests:
    st.header("📝 Mock Exams")
    c1,c2,c3=st.columns(3)
    if c1.button("Mock Exam 1 — 40 Questions",type="primary"): start(QUESTIONS,"Mock Exam 1",40); st.rerun()
    if c2.button("Mock Exam 2 — 40 New Random Questions"): start(QUESTIONS,"Mock Exam 2",40); st.rerun()
    if c3.button("Final Warm-Up — 20 Questions"): start(QUESTIONS,"Final Warm-Up",20); st.rerun()

    if st.session_state.run:
        qs=st.session_state.run; i=st.session_state.i
        if i<len(qs):
            q=qs[i]
            st.progress(i/len(qs))
            st.write(f"**{st.session_state.label} • Question {i+1} of {len(qs)} • {q['section']}**")
            st.caption({"mc":"Multiple Choice","multi":"Select All That Apply","tf":"True / False"}[q["type"]])
            st.subheader(q["question"])
            selected=widget(q,i)
            if not st.session_state.answered:
                if st.button("Submit",type="primary"):
                    if not selected: st.warning("Choose an answer first.")
                    else:
                        st.session_state.selected=selected
                        if set(selected)==set(q["answers"]): st.session_state.score+=1
                        else: st.session_state.wrong.append(q)
                        st.session_state.answered=True; st.rerun()
            else:
                if set(st.session_state.selected)==set(q["answers"]): st.success("✅ Correct")
                else:
                    st.error("❌ Review this one")
                    st.write("**Correct answer(s):** "+", ".join(q["answers"]))
                st.info(q["why"])
                if st.button("Next",type="primary"):
                    st.session_state.i+=1; st.session_state.answered=False; st.session_state.selected=[]; st.rerun()
        else:
            total=len(qs); pct=round(st.session_state.score/total*100)
            st.success(f"Score: {st.session_state.score}/{total} — {pct}%")
            if pct>=90: st.balloons(); st.success("Excellent.")
            elif pct>=80: st.success("Strong. Review missed topics.")
            else: st.warning("Use Topic Practice on your weakest areas, then retest.")
            if st.session_state.wrong:
                counts={}
                for q in st.session_state.wrong: counts[q["section"]]=counts.get(q["section"],0)+1
                st.subheader("Weak-area summary")
                for k,v in sorted(counts.items(),key=lambda x:-x[1]): st.write(f"• **{k}:** {v} missed")

with topics:
    st.header("🧠 Topic Practice")
    section=st.selectbox("Choose a topic",SECTIONS)
    pool=[q for q in QUESTIONS if q["section"]==section]
    st.write(f"Questions available: **{len(pool)}**")
    if st.button("Start Topic Practice",type="primary"): start(pool,section); st.rerun()

with scenario:
    st.header("🎯 Scenario Challenge")
    st.info("Use this pattern: **Immediate safety → calm/professional response → protect dignity → teach/support → follow authorized plan/procedure → document objectively when needed.**")
    pool=[q for q in QUESTIONS if q["section"]=="Scenario Challenge"]
    for q in pool:
        with st.expander(q["question"]):
            st.write("**Best answer:** "+q["answers"][0])
            st.write(q["why"])

with academic:
    st.header("➗ Reading, Writing & Mathematics")
    st.write("The current IUSD posting specifically states proficiency in reading, writing, and mathematics up to or above the level required for high-school seniors.")
    for sec in ["Reading","Writing & Grammar","Mathematics"]:
        pool=[q for q in QUESTIONS if q["section"]==sec]
        st.subheader(sec)
        st.write(f"Practice questions available: **{len(pool)}**")
        if st.button(f"Practice {sec}",key="btn_"+sec):
            start(pool,sec); st.rerun()

with final:
    st.header("✅ Final Review")
    st.markdown("""
### When the question says FIRST
Choose the immediate priority — especially **safety**.

### When it says BEST or MOST appropriate
Choose the response that is most **developmentally appropriate, respectful, inclusive, professional, and supportive of learning/independence**.

### Assessment reminders
- **DRDP** → developmental progress + observation/evidence + curriculum planning.
- **CLASS** → quality of classroom interactions.
- **ASQ** → developmental screening.
- **ASQ-SE** → social-emotional screening.
- **Screening is not diagnosis.**

### Professional reminders
- Follow teacher direction and authorized plans/procedures.
- Protect confidentiality.
- Document observable facts, not motives.
- Use positive guidance and teach replacement skills.
- Support home language, culture, disability access, and independence.
- For medication, health, emergencies, or procedures: **do not guess**.
""")
    st.success("Before the exam: do the 20-question warm-up, review only missed concepts, then stop cramming.")

st.divider()
st.caption("Independent study aid. Original practice content only; not affiliated with or endorsed by IUSD, eSkill, CDE, CLASS, or ASQ publishers.")
