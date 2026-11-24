#!/usr/bin/env python3
"""SignalWild deck generator: one hero and one editable 10-slide story."""
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from PIL import Image
import io

ROOT=Path(__file__).resolve().parent
p=Presentation();p.slide_width=Inches(13.333);p.slide_height=Inches(7.5)
COL={'bg':'091611','panel':'173124','panel2':'294631','lime':'D3EF84','white':'F4F2E8','muted':'B0C2B8','dark':'10231A'}
def rgb(v):return RGBColor.from_string(COL.get(v,v))
def box(s,x,y,w,h,fill='panel'):
    z=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,Inches(x),Inches(y),Inches(w),Inches(h))
    z.fill.solid();z.fill.fore_color.rgb=rgb(fill);z.line.fill.background()
def txt(s,value,x,y,w,h,size=18,col='white',bold=False):
    z=s.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h));f=z.text_frame
    f.word_wrap=True;f.clear();f.margin_left=f.margin_right=Inches(.015)
    f.margin_top=f.margin_bottom=0
    for i,l in enumerate(value.split('\n')):
        q=f.paragraphs[0] if i==0 else f.add_paragraph();q.text=l
        q.font.name='Aptos';q.font.size=Pt(size);q.font.bold=bold;q.font.color.rgb=rgb(col)
    return z
def basic(num,label):
    s=p.slides.add_slide(p.slide_layouts[6]);s.background.fill.solid();s.background.fill.fore_color.rgb=rgb('bg')
    pts=[(.56,.36),(.73,.36),(.81,.17),(.97,.57),(1.08,.28),(1.17,.36),(1.31,.36)]
    for (a,b),(c,d) in zip(pts,pts[1:]):
        line=s.shapes.add_connector(1,Inches(a),Inches(b),Inches(c),Inches(d))
        line.line.color.rgb=rgb('lime');line.line.width=Pt(2.7)
    txt(s,'signalwild',1.56,.12,2.5,.51,27,'white',True)
    txt(s,'.',3.49,.11,.25,.47,30,'lime',True)
    txt(s,'SIGNALWILD  /  '+label.upper(),.67,7.11,10,.23,9,'muted')
    txt(s,f'{num:02d} / 10',11.95,7.11,.8,.23,9,'muted')
    return s
def intro(s,label,title,subtitle,sz=37):
    txt(s,label,.71,.85,12,.27,11,'lime',True)
    txt(s,title,.69,1.22,11.92,1.42,sz,'white',True)
    txt(s,subtitle,.71,2.69,11.9,.77,14,'muted')
def card(s,x,title,body,tag,y=3.65,w=3.91):
    box(s,x,y,w,2.83)
    txt(s,tag,x+.22,y+.23,w-.42,.25,10.3,'lime',True)
    txt(s,title,x+.22,y+.71,w-.45,.63,20,'white',True)
    txt(s,body,x+.22,y+1.48,w-.45,1.06,13,'muted')
def cards(s,items):
    for i,(tag,title,body) in enumerate(items):
        card(s,.69+4.08*i,title,body,tag)

s=basic(1,'The vision')
txt(s,'INTERSPECIES COMMUNICATION  /  PRE-SEED',.67,.95,5.2,.28,11,'lime',True)
txt(s,'Intelligence\nbeyond language.',.67,1.47,5.15,1.87,46,'white',True)
txt(s,'A communication layer\nbetween humans and animals.',.69,3.78,5.26,1.0,22,'lime',True)
txt(s,'Smart sensing devices meet personalised multimodal AI: interpret natural signals, test meaning against outcomes and help humans respond.',.69,5.29,5.1,1.12,14.3,'white')
box(s,6.13,1.31,6.55,4.92,'panel')
with Image.open(ROOT/'assets/signalwild-vision.webp') as im:
    buf=io.BytesIO();im.convert('RGB').save(buf,'PNG');buf.seek(0)
    s.shapes.add_picture(buf, Inches(6.23), Inches(1.47), width=Inches(6.36),height=Inches(3.59))
txt(s,'SIGNALWILD SIGHT  /  SENSE  /  HOME',6.32,5.44,6.12,.29,12,'lime',True)
txt(s,'Device ecosystem with illustrative live reading',6.32,5.78,6.1,.3,10.1,'muted')

s=basic(2,'The insight')
intro(s,'01 / THE OPPORTUNITY','Animal communication is individual.\nUnderstanding is hard to transfer.','Experienced owners recognise everyday cues. But unseen behaviour and unfamiliar caregivers create valuable gaps.',35)
cards(s,[('CARE TRANSITIONS','Make history portable','An evidence-linked individual communication profile for sitters, adopters and care organisations.'),
('UNSEEN BEHAVIOUR','See what owners miss','Observe changes in activity, sound, posture and response when animals are left alone.'),
('TWO-WAY INTERACTION','Respond with context','Identify which familiar human cues produce voluntary, consistent responses.')])

s=basic(3,'Hardware ecosystem')
intro(s,'02 / DEVICES','Three sensing interfaces.\nOne individual intelligence.','Start with existing phones and cameras, then develop hardware where added sensors improve understanding.',38)
cards(s,[('SIGNALWILD SIGHT','Smart glasses','Owner-view camera and microphone, with optional private spoken guidance.'),
('SIGNALWILD SENSE','Smart collar','Audio and motion sensing, with future validated heart rate, HRV and respiratory measurements.'),
('SIGNALWILD HOME','Vision hub','Room-wide audio and video for full-body posture, gaze, routines and unattended behaviour.')])

s=basic(4,'Technology architecture')
intro(s,'03 / MULTIMODAL AI','Connect signals to real outcomes.','Synchronise audio, body language, movement, physiological context and observations around meaningful events.',39)
for i,(tag,title,body) in enumerate([('01 / CAPTURE','Observe','Natural vocalisations, pose, motion and environmental context'),
('02 / ALIGN','Synchronise','Evidence before, during and after interactions'),
('03 / PERSONALISE','Adapt','Species knowledge plus individual communication history'),
('04 / INFER','Assist','Rank intentions, explain uncertainty and test familiar responses')]):
    x=.70+i*3.16;box(s,x,3.65,3.00,2.30,'panel2' if i==2 else 'panel')
    txt(s,tag,x+.18,3.89,2.7,.25,10,'lime',True)
    txt(s,title,x+.18,4.34,2.7,.37,21,'white',True)
    txt(s,body,x+.18,4.96,2.65,.81,12.5,'muted')
box(s,.71,6.20,11.93,.43,'panel2')
txt(s,'THE COMPOUNDING ASSET: OUTCOME-LINKED INDIVIDUAL MODELS',1.33,6.28,10.8,.23,12,'lime',True)

s=basic(5,'Communication loop')
intro(s,'04 / BIDIRECTIONAL INTELLIGENCE','Understand. Verify. Respond.','SignalWild aims to move from plausible descriptions to evidence-backed interactions between humans and animals.',40)
cards(s,[('01 / UNDERSTAND','Interpret natural cues','Combine sound, posture, movement, context and each animal’s history.'),
('02 / VERIFY','Test hypotheses','Evaluate new events against observed outcomes and alternative explanations.'),
('03 / RESPOND','Use familiar cues','Guide voluntary, non-aversive interactions and observe the animal’s response.')])

s=basic(6,'First application')
intro(s,'05 / COMMERCIAL WEDGE','The Animal Communication Passport.','The first application makes individual communication history useful to authorised caregivers.',40)
box(s,.73,3.62,6.09,2.78,'E6EFE2')
txt(s,'BRUNO  /  PERSONAL COMMUNICATION PROFILE',1.05,3.87,5.36,.33,11,'365C42',True)
txt(s,'Repeated looks toward the door',1.05,4.37,5.3,.65,22,'dark',True)
txt(s,'Observation: gaze alternation + approach\nFamiliar response: check door, then observe voluntary behaviour.',1.05,5.17,5.35,.86,13,'365C42')
box(s,7.10,3.62,5.48,2.78)
txt(s,'FIRST CUSTOMERS',7.40,3.92,4.7,.30,11,'lime',True)
txt(s,'Animal-care handovers',7.40,4.44,4.8,.48,23,'white',True)
txt(s,'Rescues, adoption, boarding, pet sitters and multi-caregiver homes. Future applications include cats and home-alone insights.',7.40,5.15,4.72,.92,13,'muted')

s=basic(7,'Scientific evaluation')
intro(s,'06 / EXPERIMENT 001','Prove utility beyond familiar knowledge.','Compare caregiver decisions and held-out behaviour predictions against conventional notes and generic animal AI.',37)
for i,(tag,description) in enumerate([('A','Caregiver without assistance'),('B','Caregiver with written pet-care notes'),('C','Caregiver with general-purpose animal AI'),('D','Caregiver with personalised SignalWild intelligence')]):
    y=3.62+.65*i;box(s,.75,y,11.82,.54,'panel2' if i==3 else 'panel')
    txt(s,tag,1.04,y+.11,.4,.3,16,'lime',True)
    txt(s,description,1.74,y+.11,10.2,.34,15,'white',i==3)
txt(s,'SUCCESS = HELD-OUT PREDICTION + USEFUL CAREGIVER DECISIONS + REPLICATION',.84,6.46,11.92,.30,10.7,'lime',True)

s=basic(8,'Defensibility')
intro(s,'07 / COMPOUNDING ADVANTAGE','Our moat is verified individual understanding.','Sensors and basic AI classifiers are widely available. Our advantage is created by individual evidence, evaluation and trust.',36)
cards(s,[('LONGITUDINAL DATA','Individual histories','Repeated observations and outcomes linked to each animal, household and caregiver.'),
('EVIDENCE','Independent benchmarks','Measure usefulness and performance against owners, care notes and generic models.'),
('DISTRIBUTION','Trusted care networks','Rescue, welfare, care and research partners provide adoption pathways and deep feedback.')])

s=basic(9,'Founder-market fit')
intro(s,'08 / TEAM','Engineered systems.\nScaled businesses. New interfaces.','Systems engineering and venture execution combined with targeted scientific capability building.',35)
box(s,.73,3.55,4.1,2.89,'panel2')
txt(s,'SCIENTIFIC TEAM TO BUILD',1.02,3.80,3.45,.30,11,'lime',True)
for i,item in enumerate(['Animal cognition / welfare','Bioacoustics + multimodal ML','Research evaluation lead','Care and shelter partners','Animal trainers']):
    txt(s,'+',1.01,4.22+.40*i,.26,.25,14,'lime',True)
    txt(s,item,1.39,4.22+.40*i,3.13,.31,12.5,'white')
box(s,5.08,3.55,7.52,2.89)
txt(s,'PRIYANK BAKSHI',5.35,3.78,6.7,.36,20,'lime',True)
txt(s,'Founder | SignalWild',5.35,4.13,6.62,.25,12.5,'white',True)
txt(s,'Mechanical engineer at Delhi College of Engineering; Defianz Racing suspension and electrical systems. Founded mHire, acquired by Aasaanjobs; scaled largest business unit across 72 cities, growing GMV from ~$5m to ~$34m.',5.35,4.47,6.64,1.04,12,'white')
txt(s,'Also exploring SilentTyping, a wearable silent-speech interface concept: a related ambition to interpret communication beyond audible language.',5.35,5.65,6.65,.65,11.3,'white')

s=basic(10,'Investment opportunity')
intro(s,'09 / PRE-SEED RESEARCH PROGRAMME','$750k to build interspecies intelligence.','Illustrative 12-month investment programme, from multimodal software to real-world studies and initial wearable integrations.',35)
for i,(name,cost) in enumerate([('ML and software','$315k'),('Animal science','$130k'),('Pilot and data','$100k'),('Devices and compute','$60k'),('Privacy and operations','$45k'),('Contingency','$100k')]):
    x=.72+(i%3)*4.17;y=3.63+(i//3)*.84
    box(s,x,y,3.94,.66)
    txt(s,name,x+.18,y+.20,2.52,.27,12.2,'white')
    txt(s,cost,x+2.97,y+.17,.87,.32,15,'lime',True)
box(s,.73,5.52,11.89,.99,'panel2')
txt(s,'12-MONTH DECISION GATE',1.05,5.69,5,.29,10.8,'lime',True)
txt(s,'Personalisation improves evidence-backed interpretation and caregiver decisions.',1.05,6.00,11.20,.34,15,'white',True)
p.save(ROOT/'SignalWild_Investor_Deck.pptx')
print(f'Wrote {len(p.slides)} slides')
