# image-labels-generator-using-Amazon-Rekognition-
In this project, we will be building an image labels generator, using Amazon Rekognition. This is going to be a fun one. Once built, it will be able to recognize and label images. For example, if you have a photo of a cat, Amazon Recognition will be able to identify what it is, and label the image as a cat.

Services Used 🛠

    Amazon S3: For storing the images in the process of generating labels.
    Amazon Rekognition: To analyse images and generate image labels.
    AWS CLI: Interacting with AWS services through command line interface(CLI).

➡️ Architectural Diagram

This it the architectural diagram for the project:

![image](https://github.com/ElMehdiiiii/image-labels-generator-using-Amazon-Rekognition-/assets/115099306/a9604fa4-4ee7-4647-96b0-e9cfc0db4c97)

➡️ Final Result

This is what your project will look like, once built:

![image](https://github.com/ElMehdiiiii/image-labels-generator-using-Amazon-Rekognition-/assets/115099306/44aa12e3-1ccf-4aa7-b409-0c92f044430f)


Let's import the necessary libraries. We need:

    boto3 for interacting with AWS services.
    matplotlib for visualization.
    PIL (Python Imaging Library) for handling image data.
    BytesIO from the io module to work with image data.
