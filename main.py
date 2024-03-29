from pdf2image import convert_from_path

# Path to the pdf file
pdf_path = 'example_pdf_4.pdf'

# Converting PDF to images
images = convert_from_path(pdf_path)

# Saving each image to a file
for i, image in enumerate(images):
    image_path = f'page_{i + 1}.jpg'
    image.save(image_path, 'JPEG')
    print(f'Saved page {i + 1} as {image_path}')
