#!/usr/bin/env python3
"""Editable vector PowerPoint recreation of Attention Is All You Need Research Poster V2.
Reconstructed from the original poster design; paper metrics follow NeurIPS 2017 Table 2.
"""
from pathlib import Path
import math
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE

OUT=Path(__file__).resolve().parent
NAVY="112B3C";NAVY2="1E4355";INK="173044";BG="F6F8F7";WHITE="FFFFFF"
TEAL="0F968E";MINT="62DDCA";CORAL="FF815C";BLUE="2C6282";MUTED="617782"
SKY="E5EFF8";LAV="EBE9FA";TEAL2="E3F4F1";CORAL2="FEEFE9";LINE="D3DFE0";YELLOW="FFF1D2"
prs=Presentation();prs.slide_width=Inches(48);prs.slide_height=Inches(36)
s=prs.slides.add_slide(prs.slide_layouts[6])
def rgb(hexcolor):return RGBColor.from_string(hexcolor)
def rect(x,y,w,h,fill=WHITE,stroke=None,r=0):
    shape=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if r else MSO_SHAPE.RECTANGLE,Inches(x),Inches(y),Inches(w),Inches(h))
    shape.fill.solid();shape.fill.fore_color.rgb=rgb(fill)
    if stroke:shape.line.color.rgb=rgb(stroke);shape.line.width=Pt(1.6)
    else:shape.line.fill.background()
    return shape
def text(value,x,y,w,h,size=25,color=INK,bold=False,align=None):
    shape=s.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h))
    f=shape.text_frame;f.clear();f.word_wrap=True;f.auto_size=MSO_AUTO_SIZE.NONE
    f.margin_left=f.margin_right=Inches(.02);f.margin_top=f.margin_bottom=0
    f.vertical_anchor=MSO_ANCHOR.MIDDLE
    p=f.paragraphs[0];p.alignment={"center":PP_ALIGN.CENTER,"right":PP_ALIGN.RIGHT}.get(align,PP_ALIGN.LEFT)
    run=p.add_run();run.text=str(value);run.font.name="Arial";run.font.size=Pt(size);run.font.bold=bold;run.font.color.rgb=rgb(color)
    return shape
def seg(x1,y1,x2,y2,color=BLUE,width=3):
    sh=s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,Inches(x1),Inches(y1),Inches(x2),Inches(y2))
    sh.line.color.rgb=rgb(color);sh.line.width=Pt(width)
def badge(t,x,y,w,fill=TEAL2,fg=TEAL):
    rect(x,y,w,.62,fill,r=.12);text(t,x+.1,y+.02,w-.2,.56,21,fg,True,align="center")
def box(t,x,y,w,h,fill,edge=TEAL,size=24):
    rect(x,y,w,h,fill,r=.10);rect(x,y,.08,h,edge);text(t,x+.13,y+.08,w-.24,h-.16,size,INK,True,align="center")
def header(num,title,x,y,w):
    rect(x,y+.16,.1,.48,TEAL);text(f"{num}  /  {title.upper()}",x+.29,y,w-.3,.82,30,INK,True)
def circ(x,y,d,fill):
    sh=s.shapes.add_shape(MSO_SHAPE.OVAL,Inches(x),Inches(y),Inches(d),Inches(d));sh.fill.solid();sh.fill.fore_color.rgb=rgb(fill);sh.line.fill.background()
# HEADER
rect(0,0,48,36,BG);rect(0,0,48,7.65,NAVY);rect(0,7.6,48,.08,TEAL)
rect(1.12,1.0,.12,5.55,CORAL)
text("RESEARCH POSTER  /  FOUNDATIONAL MACHINE LEARNING  /  2017",1.55,.75,32,.49,23,"A7CBCD",True)
text("ATTENTION IS",1.5,1.55,31,1.9,106,WHITE,True)
text("ALL YOU NEED",1.5,3.43,31,1.9,106,WHITE,True)
text("Ashish Vaswani · Noam Shazeer · Niki Parmar · Jakob Uszkoreit · Llion Jones",1.55,5.44,32,.5,21,"DBE9EA")
text("Aidan N. Gomez · Łukasz Kaiser · Illia Polosukhin   |   NeurIPS 2017",1.55,6.02,32,.46,21,"DBE9EA")
rect(34,1.06,12.55,5.5,NAVY2,r=.12);badge("THE CENTRAL IDEA",34.49,1.49,4.8,"315F69","C7FAEA")
text("NO RECURRENCE.",34.48,2.33,11.65,.82,51,WHITE,True)
text("ALL ATTENTION.",34.48,3.29,11.65,.82,51,MINT,True)
text("Model global token interactions directly,\nwhile training positions in parallel.",34.51,4.48,11.35,1.23,26,"D8E8EA")
# LEFT CONTEXT
LX=1.12;LW=11.65
header("01","Why replace recurrence?",LX,8.24,LW)
text("Recurrent computation requires sequential state updates.",LX+.04,9.17,LW-.3,1.1,29,INK,True)
rect(LX,10.55,LW,4.35,WHITE,LINE,.12);text("RECURRENT / SEQUENTIAL",LX+.32,10.82,LW-.6,.5,23,MUTED,True)
for i in range(5):
    x=LX+.6+i*2.17;rect(x,12.13,1.8,1.13,CORAL2,"E9BBA5",.09)
    text(f"t{i+1} state",x,12.32,1.8,.72,22,"A86148",True,align="center")
    if i<4:seg(x+1.81,12.69,x+2.14,12.69,CORAL,3)
text("Dependency depth grows with sequence length n",LX+.39,13.73,LW-.6,.59,22,"A15E48")
rect(LX,15.13,LW,5.65,WHITE,LINE,.12);text("SELF-ATTENTION / PARALLEL",LX+.35,15.38,LW-.7,.45,23,TEAL,True)
for i in range(5):
    x=LX+1.03+2.12*i;circ(x,16.55,.74,TEAL if i==2 else BLUE)
    text(f"x{i+1}",x,16.69,.74,.41,20,WHITE,True,align="center")
    rect(x,18.64,.76,.69,TEAL2,"C0DEDB",.09);text(f"z{i+1}",x,18.77,.76,.37,19,TEAL,True,align="center")
for i in range(5):
    for j in (0,2,4):
        if i!=j:seg(LX+1.39+2.12*i,17.40,LX+1.39+2.12*j,18.62,"B2DCD6",1.6)
text("Every position can attend to other positions in one layer.",LX+.36,19.65,LW-.7,.77,22,MUTED)
header("02","The attention operation",LX,21.17,LW)
rect(LX,22.31,LW,4.7,NAVY,r=.12)
text("Scaled dot-product attention",LX+.42,22.67,LW-.8,.58,25,"C9DCE0",True)
text("softmax(QKᵀ / √dₖ) V",LX+.45,23.53,LW-.9,1.0,39,WHITE,True,align="center")
seg(LX+.45,24.8,LX+LW-.45,24.8,"547687",1.8)
text("Q = queries    ·    K = keys    ·    V = values",LX+.45,25.23,LW-.9,.78,23,"DEEFF0",True,align="center")
header("03","Multi-head attention",LX,27.30,LW)
text("Independent learned projections capture varied relationships.",LX+.08,28.19,LW-.4,.89,24,MUTED)
for i in range(4):badge("HEAD "+str(i+1),LX+.19+i*2.8,29.41,2.56,LAV if i%2==0 else TEAL2,BLUE if i%2==0 else TEAL)
for i in range(4):seg(LX+1.45+i*2.8,30.09,LX+5.8,31.09,BLUE,2)
badge("Concat + output projection",LX+2.9,31.17,5.75,SKY,BLUE)
text("Four heads illustrated; the base model has eight.",LX+.17,32.14,LW-.3,.64,21,MUTED)
# CENTER ARCHITECTURE
CX=13.3;CW=21.36
header("04","The Transformer, in one view",CX,8.24,CW)
text("Six encoder layers and six decoder layers.",CX+.05,9.11,CW-.2,.67,26,MUTED)
rect(CX,10.02,CW,20.4,WHITE,LINE,.15)
rect(14.03,11.0,9.28,17.76,"F1F6FB",r=.10);rect(24.57,11.0,9.28,17.76,"F0F9F6",r=.10)
badge("ENCODER × 6",15.18,11.36,7,"D8E9F6",BLUE)
badge("DECODER × 6",25.67,11.36,7,"D7F1E8",TEAL)
text("Context representations",14.42,12.43,8.5,.75,24,BLUE,True,align="center")
text("Autoregressive predictions",24.92,12.43,8.5,.75,24,TEAL,True,align="center")
box("Feed-forward network",15.17,14.32,7.08,1.47,SKY,BLUE,25)
box("Multi-head self-attention",15.17,16.51,7.08,1.57,LAV,"645EB0",25)
box("Linear + softmax",25.55,13.97,7.21,1.23,SKY,BLUE,24)
box("Feed-forward network",25.55,15.88,7.21,1.32,SKY,BLUE,24)
box("Encoder–decoder attention",25.55,17.99,7.21,1.44,TEAL2,TEAL,24)
box("Masked self-attention",25.55,20.16,7.21,1.53,LAV,"645EB0",25)
seg(18.68,20.89,18.68,18.11,BLUE,4);seg(18.68,16.5,18.68,15.8,BLUE,4)
seg(18.68,14.32,18.68,13.37,BLUE,4)
seg(29.16,22.38,29.16,21.7,TEAL,4);seg(29.16,20.15,29.16,19.45,TEAL,4)
seg(29.16,17.97,29.16,17.22,TEAL,4);seg(29.16,15.85,29.16,15.23,TEAL,4)
seg(22.34,13.57,23.85,13.57,TEAL,3);seg(23.85,13.57,23.85,18.72,TEAL,3);seg(23.85,18.72,25.49,18.72,TEAL,3)
badge("+ Positional encoding",15.75,21.28,5.91,YELLOW,"8A6E22")
badge("+ Positional encoding",26.03,22.20,6.31,YELLOW,"8A6E22")
box("Input embeddings",15.74,23.65,5.96,.91,WHITE,BLUE,22)
box("Source tokens",15.74,25.65,5.96,1.13,WHITE,BLUE,24)
seg(18.68,25.61,18.68,24.56,BLUE,3);seg(18.68,23.62,18.68,21.93,BLUE,3)
box("Output embeddings",25.99,23.65,6.31,.91,WHITE,TEAL,22)
box("Shifted target tokens",25.99,25.65,6.31,1.13,WHITE,TEAL,23)
seg(29.15,25.60,29.15,24.56,TEAL,3);seg(29.15,23.63,29.15,22.83,TEAL,3)
text("Source sequence is fully visible.",14.6,27.65,8.1,.6,20,MUTED,align="center")
text("Causal mask hides future tokens.",25.1,27.65,8.15,.6,20,MUTED,align="center")
rect(CX+.70,29.24,CW-1.4,.75,NAVY,r=.10)
text("Self-attention replaces recurrence; residual + normalization stabilize each stack.",CX+.98,29.35,CW-1.96,.53,22,WHITE,True,align="center")
header("05","Positional encoding",CX,30.71,CW)
text("Sinusoidal position signals are added to token embeddings.",CX+.09,31.58,CW-.3,.57,24,MUTED)
for k in range(78):
    x1=CX+.6+k*(CW-1.2)/78;x2=CX+.6+(k+1)*(CW-1.2)/78
    for wave,color,phase in ((3.5,TEAL,0),(1.8,CORAL,math.pi/2)):
        y1=33.11-.45*math.sin(k/78*2*math.pi*wave+phase)
        y2=33.11-.45*math.sin((k+1)/78*2*math.pi*wave+phase)
        seg(x1,y1,x2,y2,color,1.9)
# RIGHT METRICS
RX=35.35;RW=11.5
header("06","Evidence from translation",RX,8.24,RW)
def metric(y,task,number,note,color):
    rect(RX,y,RW,3.60,WHITE,LINE,.13);rect(RX,y,.14,3.60,color)
    text(task,RX+.34,y+.26,RW-.7,.52,26,MUTED,True)
    text(number,RX+.30,y+.79,7,1.42,83,color,True)
    text("BLEU / Transformer (big)",RX+.35,y+2.18,RW-.6,.56,24,INK,True)
    text(note,RX+.35,y+2.91,RW-.6,.48,18,MUTED)
metric(9.26,"WMT14  ·  EN → DE","28.4","2017 NeurIPS proceedings · Table 2",BLUE)
metric(13.10,"WMT14  ·  EN → FR","41.0","2017 NeurIPS proceedings · Table 2",TEAL)
header("07","Base-model blueprint",RX,17.14,RW)
rect(RX,18.14,RW,6.14,WHITE,LINE,.13)
rows=[("ENCODER / DECODER","6 / 6"),("ATTENTION HEADS","8"),("MODEL WIDTH","512"),("FEED-FORWARD","2,048"),("PARAMETERS","≈65M"),("KEY WIDTH","64")]
for i,(label,value) in enumerate(rows):
    col=i%2;row=i//2;x=RX+.28+5.54*col;y=18.42+1.83*row
    text(label,x,y,5.15,.45,18,MUTED,True)
    text(value,x,y+.42,5.05,1.12,39,TEAL if col else BLUE,True)
header("08","What actually improves?",RX,24.7,RW)
rect(RX,25.72,RW,3.57,TEAL2,r=.14)
text("GLOBAL CONTEXT.",RX+.42,26.15,RW-.7,.86,41,TEAL,True)
text("PARALLEL TRAINING.",RX+.42,27.02,RW-.7,.86,41,TEAL,True)
text("Short attention paths across sequence positions.",RX+.42,28.43,RW-.8,.50,22,MUTED)
rect(RX,29.61,RW,3.65,CORAL2,r=.14)
text("IMPORTANT LIMITATION",RX+.36,29.99,RW-.7,.60,24,"A35F45",True)
text("Dense self-attention has quadratic pairwise token interactions. The decoder still emits output tokens autoregressively.",RX+.38,30.75,RW-.7,1.91,24,INK)
# FOOTER
rect(0,34.20,48,1.8,NAVY);rect(1.15,34.59,.10,.99,CORAL)
text("SOURCE / Vaswani et al. (2017), Attention Is All You Need. NeurIPS 30, Table 2.",1.52,34.41,43,.51,21,WHITE,True)
text("Educational architecture redraw · NeurIPS EN–FR 41.0 differs from later arXiv revisions · https://arxiv.org/abs/1706.03762",1.52,35.00,44,.47,18,"C2D7DC")
target=OUT/"poster.pptx";prs.save(target)
print("Generated",target,"shapes:",len(s.shapes))
