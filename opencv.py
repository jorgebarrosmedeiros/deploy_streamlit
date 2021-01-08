#importando bibliotecas
import streamlit as st
import numpy as np
import cv2
from PIL import Image, ImageEnhance

OUTPUT_WIDTH = 700

def main():
    st.title("Web Application: OpenCV and Filters")
    st.text("Author: Jorge Barros - Data Scientist")
    st.sidebar.title("Filters")
    
    #page options
    menu_options = ['Filters', 'About']
    choice = st.sidebar.selectbox("Choose a Option", menu_options)
  

    #initial image
    #upload image and show image
    image_file = st.file_uploader("Upload a photo and apply a filter on the side menu",type=['jpg','jpeg','png','PNG'])
    our_image = Image.open("/home/jorge/jorge/Linkedin/upload.jpg")
    

    if choice == 'Filters':

        if image_file is not None:
            our_image = Image.open(image_file)
            st.sidebar.text("Original Image")
            st.sidebar.image(our_image, width = 150)

        #filters to by applied
        filters = st.sidebar.radio("Filters",['Original Image','Grayscale','Sketch','Sepia','Blur','Canny',"Contrast"])

        if filters == 'Original Image':
            st.image(our_image, width = OUTPUT_WIDTH)

        elif filters == 'Grayscale':
            converted_image = np.array(our_image.convert("RGB"))
            gray_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2GRAY)
            st.image(gray_image, width = OUTPUT_WIDTH)

        elif filters == 'Sketch':
            converted_image = np.array(our_image.convert("RGB"))
            gray_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2GRAY)
            inv_gray_image = 255 - gray_image
            blur_image = cv2.GaussianBlur(inv_gray_image, (21,21), 0,0)
            sketch_image = cv2.divide(gray_image, 255 - blur_image, scale = 256)
            st.image(sketch_image, width = OUTPUT_WIDTH)

        elif filters == 'Sepia':
            converted_image = np.array(our_image.convert("RGB"))
            converted_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2BGR)
            #criando filtro de sépia
            kernel = np.array([[0.272,0.534,0.131],[0.349, 0.686, 0.168],[0.393,0.769, 0.189]])
            sepia_image = cv2.filter2D(converted_image, -1, kernel)
            st.image(sepia_image, width = OUTPUT_WIDTH)

        elif filters == 'Blur':
            b_amount = st.sidebar.slider('Kernel (n x n)',3,81,9, step = 2)
            converted_image = np.array(our_image.convert("RGB"))
            converted_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2BGR)
            blur_image = cv2.GaussianBlur(converted_image, (b_amount,b_amount), 0,0)
            st.image(blur_image, width = OUTPUT_WIDTH)

        elif filters == 'Canny':
            converted_image = np.array(our_image.convert("RGB"))
            converted_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2BGR)
            blur_image = cv2.GaussianBlur(converted_image, (7,7), 0,0)
            canny = cv2.Canny(blur_image, 100,150)
            st.image(canny, width = OUTPUT_WIDTH)

        elif filters == 'Contrast':
            c_amount = st.sidebar.slider("Contrast", 0.0,2.0,1.0)
            enhancer = ImageEnhance.Contrast(our_image)
            contrast_image = enhancer.enhance(c_amount)
            st.image(contrast_image, width = OUTPUT_WIDTH)

    else:
        st.subheader("Author: Jorge Barros")
        st.text("For more projects, follow me on [Linkedin](https://www.linkedin.com/in/jorge-barros-medeiros/)")
        st.text("Instagram: @jorge.barros.35")

if __name__ == '__main__':
    main()