from fpdf import FPDF

pdf = FPDF()
WIDTH = 210
HEIGHT = 297
X = 0
Y = 0

def set_letterhead(pdf: FPDF = pdf):
    pdf.image("./resources/letterhead.png", -1, 0, WIDTH*1.1, HEIGHT*1.18)
    pass

def set_title_font(pdf: FPDF = pdf):
    pdf.set_font('Arial', 'B', 22)

def set_heading_1_font(pdf: FPDF = pdf):
    pdf.set_font('Arial', 'B', 18)

def set_heading_2_font(pdf: FPDF = pdf):
    pdf.set_font('Arial', 'I', 14)

def set_p_font(pdf: FPDF = pdf):
    pdf.set_font('Arial', '', 11)

def set_p_i_font(pdf: FPDF = pdf):
    pdf.set_font('Arial', 'I', 11)

def lb(size: float = 10):
    global Y
    Y += size
    pdf.ln(size)


### PAGE 1
pdf.add_page()

# Letterhead
set_letterhead()

# Title of report
set_title_font()
lb(12)
pdf.write(5, f"Consumer Financial Complaints Report")
lb(8)

set_heading_2_font()
pdf.write(5, "Anuj Singla")
lb(7)

set_p_font()
pdf.write(5, "September 28th, 2022")
lb(15)

# Introduction
set_heading_1_font()
pdf.write(10, "Introduction")
lb()

set_p_font()
pdf.write(5, ("As a new financial institution entering alpha, our mission is to optimize "
              "the efficiency of every facet of our operations. Consumer complaints are "
              "inevitable, but handling disputed resolutions can often become a costly and "
              "time-consuming process. It is in our best interest to examine our clients' "
              "backgrounds and prevent them from disputing claims by offering them sufficient "
              "initial resolutions."))
lb(15)

# Data
set_heading_1_font()
pdf.write(10, "Data")
lb()

# Data visualization 1
set_heading_2_font()
pdf.write(10, "1) How does product affect dispute rate?")
lb(35)

image_width = WIDTH / 1.1 # Make image fit comfortbly on the page
image_height = WIDTH / (1.1 * 1132 / 525) # Set height proportional to width and original pixel dimensions
pdf.image("./resources/visualizations/product-disputes.png", 7, Y, image_width, image_height)
lb(image_height / 1.4)

set_p_font()
pdf.write(5,"Mortgages are the most frequent complaint product and have the highest rate of disputes. "
             "On the other hand, although credit reporting has a fairly large amount of complaints "
             "(~15,000), it has a lower rate of disputes compared to the rest of the products.")
lb(6)
set_p_i_font()
pdf.write(6, "    -   Why are mortgages disputed so frequently?\n"
             "    -   Why is credit reporting disputed so rarely?\n"
             "    -   Why do mortgages have over twice the amount of complaints as any other product?")


### PAGE 2
pdf.add_page()
Y = 0

# Letterhead
set_letterhead()

# Data visualization 2
set_heading_2_font()
pdf.write(10, "2) How does location affect dispute rate?")
lb(20)

pdf.image("./resources/visualizations/state-disputes.png", 7, Y, image_width, image_height)
lb(image_height / 1.3)

set_p_font()
pdf.write(5, "Consumers in the west coast seem to be more likely to dispute their "
             "complaint resolutions compared to the rest of the country, followed "
             "by the east coast. The middle region of the country, highlighted by "
             "New Mexico and South Dakota, have much lower dispute rates.")
lb(6)
set_p_i_font()
pdf.write(6, "    -   Why does the west coast dispute their complaints so frequently?\n"
             "    -   Why does the plains region generally have such low dispute rates?")
lb(15)

# Data visualization 3
set_heading_2_font()
pdf.write(10, "3) How does complaint submission method affect dispute rate?")
lb(35)

pdf.image("./resources/visualizations/submission-disputes.png", 7, Y, image_width, image_height)
lb(image_height / 1.5)

set_p_font()
pdf.write(5, "Web submissions, which also happen to be the most common form of complaint "
             "submission, have the highest dispute rate. On the other hand, postal mail "
             "submissions, which are one of the least common methods for complaint submissions, "
             "have the lowest dispute rates. Most notably, instant and non-verbal forms "
             "of communication (web, fax, email) have higher dispute rates than slower, "
             "non-anonymous methods of submission (referral, phone, postal mail).")
lb(6)
set_p_i_font()
pdf.write(6, "    -   Do time-consuming submission methods create a barrier for consumers to dispute?")


### PAGE 3
pdf.add_page()
Y = 0

# Letterhead
set_letterhead()

# Data visualization 3
set_heading_2_font()
pdf.write(10, "4) Sentiment analysis on the most common issues")
lb(25)

image_width /= 2.15
image_height /= 2.15

pdf.image("./resources/visualizations/all-complaints-wc.png", 10, Y, image_width, image_height)
pdf.image("./resources/visualizations/disputed-complaints-wc.png", 20+image_width, Y, image_width, image_height)
lb(image_height / 1.4)

set_p_i_font()
pdf.cell(w=image_width, h=6, txt='WordCloud of All Issues', align='C')
pdf.cell(w=image_width/9, h=6, txt='', align='C')
pdf.cell(w=image_width, h=6, txt='WordCloud of Disputed Issues Only', align='C')
lb(10)

set_p_font()
pdf.write(5, "A form of modification (loan, collection) is the most common issue found "
"in sentiment analysis. Credit reports seem to be less common among disputes than all "
"issues. However, servicing payments seems to be an issue that leads to greater disputes.")
lb(6)

set_p_i_font()
pdf.write(6, "    -   Why is servicing payments more common among disputed issues?\n"
             "    -   Why are credit reports less common among disputed issues?\n"
             "    -   What makes loan and collection modification such common issues?")
lb(15)

# Introduction
set_heading_1_font()
pdf.write(10, "Conclusion")
lb()

set_p_font()
pdf.write(5, "Further research and exploration is required to make any concrete conclusions. "
             "However, these current data insights can orient us in the right direction."
             "We must gather more data to answer the questions generated from such visualiaitons, "
             "and in doing so, generate quality financial complaint resolutions for our consumers.")
lb()

set_p_i_font()
pdf.write(5, "Note: Future hypotheses are located in the GitHub LaTeX file.")


### EXPORT REPORT AS PDF
pdf.output('report.pdf')