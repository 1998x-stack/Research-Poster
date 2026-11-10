from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN, MSO_AUTO_SIZE
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.oxml.xmlchemy import OxmlElement
from pptx.oxml.ns import qn
import qrcode, os, math

from pathlib import Path
OUT=str(Path(__file__).resolve().parent)
prs=Presentation()
prs.slide_width=Inches(48)
prs.slide_height=Inches(36)
slide=prs.slides.add_slide(prs.slide_layouts[6])

# Inspired by research posters in ICLR/ICML/NeurIPS proceedings and modern editorial layout.
NAVY='112B3C'; NAVY2='17384B'; INK='173044'; BG='F6F8F7'; WHITE='FFFFFF'
TEAL='0F968E'; TEAL2='E3F4F1'; CORAL='FF815C'; CORAL2='FEF0E8'
SKY='E5EFF8'; BLUE='2C6282'; MUTED='536A76'; SOFT='CAD8DB'; PALE='EEF3F4'
LAV='EBE9FA'; VIOLET='655EB0'; YELLOW='FFF1D2'; GOLD='DB9C39'; LINE='D5E0E1'
FONT='Inter'; DISPLAY='Inter Display'

def C(h):return RGBColor.from_string(h.lstrip('#'))
def rect(x,y,w,h,fill=None,line=None,lw=1, radius=0):
    sh=slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE, Inches(x),Inches(y),Inches(w),Inches(h))
    if radius:
        try: sh.adjustments[0]=min(0.40, radius)
        except: pass
    if fill is None: sh.fill.background()
    else: sh.fill.solid(); sh.fill.fore_color.rgb=C(fill)
    if line: sh.line.color.rgb=C(line);sh.line.width=Pt(lw)
    else:sh.line.fill.background()
    return sh

def circ(x,y,d,fill,line=None,lw=1):
    sh=slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x),Inches(y), Inches(d), Inches(d))
    if fill: sh.fill.solid();sh.fill.fore_color.rgb=C(fill)
    else:sh.fill.background()
    if line:sh.line.color.rgb=C(line);sh.line.width=Pt(lw)
    else:sh.line.fill.background()
    return sh

def text(s,x,y,w,h,sz=27,color=INK,bold=False,font=FONT,align='left',valign='mid',margin=0,spacing=None,italic=False):
    sh=slide.shapes.add_textbox(Inches(x),Inches(y), Inches(w), Inches(h))
    tf=sh.text_frame; tf.clear(); tf.word_wrap=True;tf.auto_size=MSO_AUTO_SIZE.NONE
    tf.margin_left=tf.margin_right=Inches(margin);tf.margin_top=tf.margin_bottom=Inches(0)
    tf.vertical_anchor={'top':MSO_ANCHOR.TOP,'mid':MSO_ANCHOR.MIDDLE,'bottom':MSO_ANCHOR.BOTTOM}[valign]
    p=tf.paragraphs[0]
    p.alignment={'left':PP_ALIGN.LEFT,'center':PP_ALIGN.CENTER,'right':PP_ALIGN.RIGHT}[align]
    if spacing is not None:p.space_after=Pt(spacing)
    run=p.add_run();run.text=s
    run.font.name=font;run.font.size=Pt(sz);run.font.bold=bold;run.font.italic=italic;run.font.color.rgb=C(color)
    return sh

def line(x1,y1,x2,y2,color=SOFT,width=2,dash=None):
    sh=slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    sh.line.color.rgb=C(color);sh.line.width=Pt(width)
    if dash:
        from pptx.enum.dml import MSO_LINE_DASH_STYLE
        sh.line.dash_style=MSO_LINE_DASH_STYLE.DASH
    return sh

def arrow(x1,y1,x2,y2,color=BLUE,width=3,tip=.16):
    line(x1,y1,x2,y2,color,width)
    a=math.atan2(y2-y1,x2-x1)
    pts=[]
    for theta in [a,a+2.5,a-2.5]:
        pass
    # lightweight editable triangle; rotated toward target
    sh=slide.shapes.add_shape(MSO_SHAPE.ISOSCELES_TRIANGLE, Inches(x2-tip/2), Inches(y2-tip/2), Inches(tip), Inches(tip))
    sh.fill.solid();sh.fill.fore_color.rgb=C(color);sh.line.fill.background()
    sh.rotation=math.degrees(a)+90
    return sh

def label(num,title,x,y,w):
    rect(x,y+.14,.10,.47,TEAL)
    text(f'{num}  /  {title.upper()}',x+.27,y,w-.3,.78,30,INK,True,font=DISPLAY)

def small_tag(s,x,y,w,fc=TEAL2,txt=TEAL,h=.56,sz=20):
    rect(x,y,w,h,fc,radius=.3)
    text(s,x+.1,y+.01,w-.2,h-.01,sz,txt,True,align='center')

def block(x,y,w,h,heading,bg,accent,fontsize=25):
    rect(x,y,w,h,bg,radius=.13)
    rect(x,y,.08,h,accent)
    text(heading,x+.20,y+.01,w-.4,h-.02,fontsize,INK,True,align='center')

def metric(x,y,w,h,lead,num,trail,note,color=TEAL):
    rect(x,y,w,h,WHITE,line=LINE,lw=1.4,radius=.16)
    rect(x,y,.13,h,color)
    text(lead,x+.30,y+.24,w-.5,.55,25,MUTED,True)
    text(num,x+.27,y+.79,w-.6,1.35,79,color,True,DISPLAY)
    text(trail,x+.36,y+2.20,w-.7,.43,24,INK,True)
    text(note,x+.34,y+2.79,w-.65,.6,17,MUTED)

# ---------- BACKGROUND + HEADER ----------
rect(0,0,48,36,BG)
rect(0,0,48,7.65,NAVY)
rect(0,7.61,48,.09,TEAL)
rect(1.12,1.0,.11,5.62,CORAL)
text('RESEARCH POSTER  /  FOUNDATIONAL MACHINE LEARNING  /  2017',1.55,.77,30,.47,22,'9DC6C8',True)
text('ATTENTION IS',1.48,1.58,30,1.85,104,WHITE,True,DISPLAY)
text('ALL YOU NEED',1.48,3.45,31,1.84,104,WHITE,True,DISPLAY)
text('Ashish Vaswani  ·  Noam Shazeer  ·  Niki Parmar  ·  Jakob Uszkoreit  ·  Llion Jones',1.55,5.48,32,.47,21,'D9E8EC')
text('Aidan N. Gomez  ·  Łukasz Kaiser  ·  Illia Polosukhin    |    NeurIPS (NIPS) 2017',1.55,6.05,32,.42,21,'D9E8EC')
rect(33.97,1.02,12.63,5.55,NAVY2,line='42637B',lw=1.3,radius=.14)
small_tag('THE CENTRAL IDEA',34.46,1.50,4.65,fc='2E6368',txt='CCF6EE',sz=19)
text('NO RECURRENCE.',34.46,2.33,11.55,.81,49,WHITE,True,DISPLAY)
text('ALL ATTENTION.',34.46,3.27,11.55,.81,49,'59D7C5',True,DISPLAY)
text('Model global token interactions directly,\nwhile training positions in parallel.',34.51,4.52,11.39,1.14,26,'D5E8E7')
# hero detail token motif
for i in range(6):
    circ(45.27+i*.16,1.56+i*.12,.10, CORAL if i%2 else TEAL)

# ---------- LEFT COLUMN ----------
LX=1.12; LW=11.67
label('01','Why replace recurrence?',LX,8.24,LW)
text('The old bottleneck: each recurrent step waits for the previous one.',LX+.02,9.12,LW-.2,1.25,31,INK,True)

# RNN row
rect(LX,10.70,LW,4.08,WHITE,line=LINE,lw=1.0,radius=.12)
text('RECURRENT / SEQUENTIAL',LX+.3,10.93,LW-.6,.55,22,MUTED,True)
node_x=[LX+.6,LX+2.76,LX+4.92,LX+7.08,LX+9.24]
for i,x in enumerate(node_x):
    rect(x,12.0,1.75,1.25,CORAL2,line='EDBBA6',lw=1,radius=.22)
    text(f't{i+1}',x,12.02,1.75,.54,25,'B95D41',True,align='center')
    text('state',x,12.57,1.75,.37,17,MUTED,align='center')
    if i<4:arrow(x+1.81,12.63,x+2.13,12.63,CORAL,2.4,.17)
text('Sequence depth grows with length n',LX+.34,13.64,LW-.68,.55,21,'A05F48')

rect(LX,15.02,LW,5.95,WHITE,line=LINE,lw=1.0,radius=.12)
text('SELF-ATTENTION / PARALLEL',LX+.3,15.24,LW-.6,.55,22,TEAL,True)
# parallel nodes and mixing interaction curves as thin lines
xs=[LX+.9+i*2.13 for i in range(5)]
for i,x in enumerate(xs):
    circ(x,16.33,.75, TEAL if i==2 else SKY)
    text(f'x{i+1}',x,16.42,.75,.35,20,WHITE if i==2 else INK,True,align='center')
for i,x in enumerate(xs):
    for j,z in enumerate(xs):
        if i==j:continue
        if (i+j)%2==0:
            line(x+.37,17.14,z+.37,18.55,'B6DCD8',1.4)
for i,x in enumerate(xs):
    rect(x,18.53,.75,.67,TEAL2,line='B9DEDA',lw=.7,radius=.21)
    text(f'z{i+1}',x,18.63,.75,.31,18,TEAL,True,align='center')
text('Each position can attend to other positions in one layer.',LX+.35,19.57,LW-.8,.89,22,MUTED)

label('02','The attention operation',LX,21.27,LW)
rect(LX,22.40,LW,4.60,NAVY,radius=.11)
text('Scaled dot-product attention',LX+.44,22.72,LW-.88,.56,25,'C2DAE0',True)
text('softmax(QKᵀ / √dₖ) V',LX+.44,23.52,LW-.9,1.0,39,WHITE,True,DISPLAY,align='center')
line(LX+.48,24.74,LX+LW-.48,24.74,'537183',1.3)
for i,(abbr,dsc) in enumerate([('Q','queries'),('K','keys'),('V','values')]):
    x=LX+.55+i*3.66
    circ(x,25.16,.63,TEAL if i==0 else BLUE if i==1 else CORAL)
    text(abbr,x,25.23,.63,.37,22,WHITE,True,align='center')
    text(dsc,x+.76,25.25,2.55,.38,21,'E2ECF1')

label('03','Multi-head attention',LX,27.30,LW)
text('Multiple learned projections capture different relationships.',LX+.02,28.15,LW-.2,.86,24,MUTED)
for i in range(4):
    x=LX+.30+i*2.78
    rect(x,29.40,2.42,.94, LAV if i%2==0 else TEAL2,line='CDDDDF',lw=1,radius=.12)
    text('HEAD '+str(i+1),x,29.60,2.42,.47,22,VIOLET if i%2==0 else TEAL,True,align='center')
    arrow(x+1.21,30.38,LX+LW/2,31.02,BLUE,1.8,.12)
rect(LX+3.60,31.05,4.47,.91,SKY,radius=.16)
text('Concat + linear',LX+3.65,31.24,4.37,.48,22,BLUE,True,align='center')
text('Schematic: 4 heads shown; base model uses 8.',LX+.28,32.29,LW-.7,.56,19,MUTED)

# ---------- CENTER: ARCHITECTURE ----------
CX=13.32; CW=21.34
label('04','The Transformer, in one view',CX,8.24,CW)
text('Two 6-layer stacks. Context flows through attention, not recurrence.',CX+.03,9.12,CW-.2,.75,26,MUTED)
rect(CX,10.06,CW,20.31,WHITE,line=LINE,lw=1.2,radius=.12)
# central backgrounds
rect(14.10,11.16,9.22,17.67,'F3F7FB',radius=.12)
rect(24.59,11.16,9.22,17.67,'EFF9F6',radius=.12)
small_tag('ENCODER  × 6',15.25,11.55,6.95,fc='DCEAF7',txt=BLUE,h=.76,sz=27)
small_tag('DECODER  × 6',25.73,11.55,6.95,fc='D7F0E9',txt=TEAL,h=.76,sz=27)
# graphic arrows label top to bottom
text('Context representations',14.66,12.75,8.2,.49,23,BLUE,True,align='center')
text('Autoregressive predictions',25.11,12.75,8.2,.49,23,TEAL,True,align='center')
# encoder, top down
block(15.24,14.50,7.02,1.53,'Feed-forward network',SKY,BLUE,26)
block(15.24,16.63,7.02,1.57,'Multi-head self-attention',LAV,VIOLET,25)
# Residual + LayerNorm is noted in the architectural takeaway strip
arrow(18.76,21.25,18.76,18.98,BLUE,3,.22)
arrow(18.76,16.61,18.76,16.13,BLUE,3,.20)
arrow(18.76,14.46,18.76,13.48,BLUE,3,.20)
# encoder bottom
block(15.74,21.28,6.02,1.25,'+ Positional encoding',YELLOW,GOLD,23)
arrow(18.76,23.62,18.76,22.62,BLUE,3,.2)
rect(15.73,23.65,6.04,.87,WHITE,line='B4C7D6',lw=1.2,radius=.19)
text('Input embeddings',15.81,23.82,5.88,.48,22,INK,True,align='center')
arrow(18.76,25.60,18.76,24.62,BLUE,3,.2)
rect(15.74,25.65,6.02,1.23,WHITE,line='B4C7D6',lw=1.3,radius=.17)
text('Source tokens',15.80,25.94,5.9,.57,25,INK,True,align='center')
text('The encoder sees the whole source sequence.',14.61,27.48,8.23,.65,20,MUTED,align='center')
# Decoder top to bottom
block(25.54,14.01,7.26,1.27,'Linear + softmax',SKY,BLUE,24)
block(25.54,16.03,7.26,1.39,'Feed-forward network',SKY,BLUE,25)
block(25.54,18.20,7.26,1.55,'Encoder–decoder attention',TEAL2,TEAL,24)
block(25.54,20.52,7.26,1.59,'Masked self-attention',LAV,VIOLET,25)
small_tag('+ Positional encoding',25.65,22.51,7.08,fc=YELLOW,txt='947024',h=.66,sz=19)
arrow(29.19,22.51,29.19,22.12,TEAL,3,.2)
arrow(29.19,20.49,29.19,19.82,TEAL,3,.2)
arrow(29.19,18.16,29.19,17.45,TEAL,3,.2)
arrow(29.19,15.99,29.19,15.33,TEAL,3,.2)
arrow(29.19,13.98,29.19,13.45,TEAL,3,.2)
# Cross attention line, from upper encoder to decoder block
line(22.30,13.58,23.90,13.58,TEAL,2.5)
line(23.90,13.58,23.90,18.96,TEAL,2.5)
arrow(23.90,18.96,25.48,18.96,TEAL,2.8,.2)
# Cross-attention arrow from encoder to decoder
# Decoder lower sections to bottom
arrow(29.19,23.86,29.19,23.26,TEAL,2.8,.21)
rect(26.12,23.91,6.13,.92,WHITE,line='BDD9D2',lw=1.2,radius=.17)
text('Output embeddings',26.18,24.09,5.95,.46,21,INK,True,align='center')
arrow(29.19,25.62,29.19,24.90,TEAL,2.8,.18)
rect(26.13,25.65,6.12,1.23,WHITE,line='BDD9D2',lw=1.3,radius=.17)
text('Shifted target tokens',26.18,25.94,6.02,.56,24,INK,True,align='center')
text('Causal mask blocks future-token access.',25.17,27.48,8.12,.65,20,MUTED,align='center')

# Callout under architectural illustration, gap reserved
rect(CX+.72,29.12,CW-1.44,.82,NAVY,radius=.18)
text('Core principle: attention replaces recurrence; residual normalization stabilizes the blocks.',CX+.98,29.30,CW-1.96,.47,24,WHITE,True,align='center')

# Positional encoding strip y30.6-33.4
label('05','How order is represented',CX,30.63,CW)
text('Sinusoidal position signals are added to token embeddings.',CX+.03,31.50,CW-.2,.57,23,MUTED)
# clean mini-wave, 2 editable sinusoids
xmin=CX+.6; xmax=CX+CW-.6; ymid=33.07
line(xmin,ymid,xmax,ymid,'A8C0C8',1.2)
for wave,color,phase in [(3.6,TEAL,0),(1.9,CORAL,math.pi/2)]:
    points=[]
    for k in range(80):
        x=xmin+(xmax-xmin)*k/79
        y=ymid-.53*math.sin((x-xmin)/(xmax-xmin)*math.pi*2*wave+phase)
        points.append((x,y))
    for a,b in zip(points[:-1],points[1:]):line(a[0],a[1],b[0],b[1],color,1.7)

# ---------- RIGHT COLUMN ----------
RX=35.39; RW=11.48
label('06','Evidence from translation',RX,8.24,RW)
metric(RX,9.31,RW,3.63,'WMT14  ·  EN → DE','28.4','BLEU  ·  Transformer (big)','vs 26.36  ·  ConvS2S ensemble',BLUE)
metric(RX,13.16,RW,3.63,'WMT14  ·  EN → FR','41.0','BLEU  ·  Transformer (big)','vs 40.56 MoE (single)  ·  3.5 days / 8 P100 GPUs',TEAL)
# Differentiated data table rather than big text
label('07','Base-model blueprint',RX,17.20,RW)
rect(RX,18.22,RW,6.21,WHITE,line=LINE,lw=1,radius=.13)
for i,(head,num,unit,col) in enumerate([
    ('ENCODER / DECODER','6 / 6','layers',BLUE),
    ('ATTENTION','8','heads',TEAL),
    ('MODEL WIDTH','512','d_model',VIOLET),
    ('FEED-FORWARD','2,048','d_ff',GOLD),
    ('PARAMETERS','≈65M','base',BLUE),
    ('ATTENTION KEY','64','d_k',TEAL),
]):
    c=i%2;r=i//2
    x=RX+.32+c*5.62;y=18.48+r*1.86
    if c==1:line(RX+RW/2,18.57+r*1.82,RX+RW/2,20.12+r*1.82,LINE,1.1)
    text(head,x,y,5.2,.38,16,MUTED,True)
    text(num,x,y+.44,3.31,.83,41,col,True,DISPLAY)
    text(unit,x+3.35,y+.82,1.7,.33,17,MUTED)

label('08','What actually improves?',RX,24.79,RW)
rect(RX,25.80,RW,3.57,TEAL2,radius=.14)
text('GLOBAL CONTEXT.\nPARALLEL TRAINING.',RX+.40,26.19,RW-.80,1.86,38,TEAL,True,DISPLAY)
text('Short attention paths between positions.',RX+.43,28.37,RW-.86,.45,21,MUTED)
# brief limitation caution
rect(RX,29.68,RW,3.68,CORAL2,radius=.13)
text('IMPORTANT LIMITATION',RX+.34,29.99,RW-.68,.51,22,'AD5F40',True)
text('Full self-attention scales quadratically with sequence length. The autoregressive decoder still produces tokens sequentially.',RX+.35,30.76,RW-.70,1.86,24,INK)

# ---------- FOOTER ----------
rect(0,34.22,48,1.78,NAVY)
rect(1.15,34.62,.09,.91,CORAL)
text('SOURCE  /  Vaswani et al. (2017), Attention Is All You Need. NeurIPS 2017, Table 2.',1.54,34.40,36.9,.45,20,WHITE,True)
text('Research poster reinterpretation  ·  Architecture redrawn schematically  ·  EN–FR 41.0 uses the 2017 proceedings version (later arXiv v7 reports 41.8).',1.54,34.97,41.7,.48,16,'B8D0D6')
# QR link
qr=qrcode.QRCode(version=2,box_size=10,border=1,error_correction=qrcode.constants.ERROR_CORRECT_M)
qr.add_data('https://papers.nips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf')
qr.make(fit=True)
qrpath=os.path.join(OUT,'paper_qr.png')
qr.make_image(fill_color='black',back_color='white').save(qrpath)
rect(45.20,34.34,1.48,1.48,WHITE,radius=.04)
slide.shapes.add_picture(qrpath,Inches(45.27),Inches(34.41),Inches(1.34), Inches(1.34))
text('PAPER',43.78,34.84,1.19,.4,17,'CFE4E7',True,align='right')

pptx=os.path.join(OUT,'poster.pptx')
prs.save(pptx)
print(pptx)
print('slide shapes:',len(slide.shapes))