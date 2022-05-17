import io
from turtle import width
from reportlab.lib.pagesizes import A2
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.lib.units import inch
import random
import string
import textwrap

from sqlalchemy import table



# coordinate_ls = [
#     (360, 376, 2, 10, 20,15, "Sans-Bold", 0, 'black'),
#     # (600, 800, 2, 30, 20, 15,"Sans-Bold", 0, 'black'),    
#     (326, 315, 3, 10, 13,28,"Sans-Regular", 0, 'black'),
#     (440, -120, 3, 10, 13,28, "Sans-Regular", 60, 'black'),
#     (-220, 633, 3, 10, 13, 28,"Sans-Regular", 300, 'black'),
#     (-507, -220, 2, 10, 20, 15,"Sans-Bold", 180, 'black'),
#     (-540, -303, 3, 10, 13, 28,"Sans-Regular", 180, 'black'),
#     (-130, -430, 3, 10, 13, 28,"Sans-Regular", 120, 'black'),
#     (-520, 324, 3, 10, 13, 28,"Sans-Regular", 240, 'black'),
#     (80, -442, 1.2, 5, 10, 10,"Sans-Bold", 90, 'white'),
#     (-193, -423, 1.1, 5, 10,10, "Sans-Bold", 150, 'white'),
#     (-636, 10, 1.1, 5, 10, 10,"Sans-Bold", 210, 'white'),
#     (503, 153, 2, 10, 20, 15,"Sans-Bold", 0, 'black'),
#     (455, 78, 3, 10, 13, 28,"Sans-Regular", 0, 'black'),
#     (302, -360, 3, 10, 13, 28,"Sans-Regular", 60, 'black'),
#     (100, 633, 3, 10, 13, 28,"Sans-Regular", 300, 'blue'),
#     (220, 153, 2, 10, 20, 15,"Sans-Bold", 0, 'black'),
#     (195, 78, 3, 10, 13,28, "Sans-Regular", 0, 'black'),
#     (178, -120, 3, 10, 13,28, "Sans-Regular", 60, 'black'),
#     (-94, 393, 3, 10, 13,28, "Sans-Regular", 300, 'black'),
# ]



# datals = ["mynameisprashantaryaprashantara", "mynamedfsfdsfisprashantsdfsdfaryaprashantarafgdfgdvdsdsfdsfdsfsfddsfsff","mynadsfsdfsdfsdfmeisprashantaryaprashantagfdsfgssdragfdsfsdfs","mynameisprasfsdfsdfsfhantaryapdsgsgsdgrashantarasdgsdfg","dsffefrefefeferfefefefrefadAASDFASD","dsffffffffffffffffrveeeeeeeeeee","vrrvvvvvvvvvvvveeeeeeeeeevvvvvvvvvv","sdsdsfsvvvvvvvvvvvvvvvvvvvvvvvsdgwsdfadfDadaDaSAFASFAF","dsadasfsfsdfskjdfgojvnsdijvgisjvbsdv","afakfgiasfjknkaufshakjsfnkagfuasf","afdkjbasfiubkanmf bkajfbkansf kajfsbakmfn aksfb","asdkhasfgausfkjboasudhanlsfnoaifhjlafn","afjhaksudhnkamf kausfhlamfnlajsgfa","asdfkjgiuafbaknfbkaugfbkamsfbkuasgf","asfkjhiasufbkmdnkasgflajsfjboaifyhkpanf","askfjbkuagsflkmknlafihlkasmfnljh"]



def editPDF(data_dict):
    print("----------------------------2")
    print(data_dict)
    # packet = io.BytesIO()
    packet = "abc.pdf"
    can = canvas.Canvas(packet, pagesize=A2)
    for key, value in data_dict.items():
        print(key,value)

        can.saveState()
        can.rotate(value[-2])
        # for char in data_dict.items(): 
            
             
        # for abc in coordinate_ls:
        

        threshold=value[5]
        ll = []  
        final=""
        count = 0
        for val in key:          
                 
            count=count+1
            final=final+val
            if count==threshold:
                    count=0
                    ll.append([final])
                    final=""
        print(ll)
        print("----------------------------------------new")
        if threshold==15:
            # can.setFont("Times Roman",41)
            table = Table(ll,rowHeights=None, colWidths=value[2] * inch)
        # elif threshold<=15:
        #     table = Table([[key[0:]]],rowHeights=None, colWidths=value[2] * inch)
        elif threshold==10:
            # can.setFont("Times Roman", 30)
            # can.setFont("Courier-Bold", 18)
            table = Table([[key[0:9]]],rowHeights= None, colWidths=value[2] * inch)
        else:
            # can.setFont("Times Roman", 20)
            table = Table([[key[0:28]]],rowHeights=None, colWidths=value[2] * inch)

        # table = Table([[key]], colWidths=value[2] * inch)
        # table = Table(ll, colWidths=value[2] * inch)
        print("-------------------------------------3")
        # print(key)
        # print(value)
        # print(table)
        c = colors.black
        if (value[-1] == "white"):
            c = colors.white
        print(table)
        print("-------------------------------------4")
        table.setStyle(
            TableStyle(
                [
                    ("ALIGN", (0, 0,), (-1, -1), "CENTER"),
                    # ("FONTSIZE", (0, 0), (-2, -2), value[-4]),
                    ("TEXTCOLOR", (0, 0,), (-1, -1), c),
                    ("TEXTFONT", (0, 0), (-1, -1), value[-3]),
                ]
            )
        )
        # print(table)

        print("-------------------------------------5")
        table.wrapOn(can, value[2]*inch,value[3]*inch)
        print("------------------------------------5.1")
        # table.drawOn(can, value[0], value[1])
        can.setFont("Courier-Bold", 100)
        table.drawOn(can,value[0],value[1] )
        print("------------------------------------5.2")
        # print(table)
        can.restoreState()
    print("-------------------------------------51")
    can.save()
    # print("-------------------------------------51")
    # packet.seek(0)
    content_pdf = PdfFileReader(packet)
    output_pdf = PdfFileWriter()
    reader = PdfFileReader("./static/pdf/stratahedron.pdf", "rb")
    page = reader.getPage(0)
    print("-------------------------------------6")
    # print(page)
    page.mergePage(content_pdf.getPage(0))
    output_pdf.addPage(page)
    letters = string.digits
    file_name_random = ''.join(random.choice(letters) for i in range(5))
    file_name = f"./static/pdf/digital_stratahedron_{file_name_random}.pdf"
    outputStream = open(file_name, "wb")
    output_pdf.write(outputStream)
    outputStream.close()
    return file_name



    
# editPDF(dict(zip(datals, coordinate_ls)))


