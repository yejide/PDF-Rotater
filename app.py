import PyPDF2


def rotatePdf(filename, newfilename, rotation):
    file = open(filename, 'rb')
    reader = PyPDF2.PdfFileReader(file)
    writer = PyPDF2.PdfFileWriter()
    for page in range(reader.numPages):
        pageObj = reader.getPage(page)
        pageObj.rotateClockwise(rotation)
        writer.addPage(pageObj)

    output = open(newfilename, "wb")
    writer.write(output)

    file.close()
    output.close()


filename = "RESUME.pdf"
newfilename = "rotated.pdf"
rotation = 90
rotatePdf(filename, newfilename, rotation)
