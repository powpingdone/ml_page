# An overview of Machine Learning from a relatively inexperienced student.

This document/blogpost/markdown sheet/assignment should not be a document about what machine learning is. The writing here should not be used as factual information, but as an expression of my opinions.

To obtain a pdf of this page, [click here.](mlovrvw.pdf) Please note that this is not a 1 to 1 representation of this page and is rendered using `pandoc` and `texlive`. 

---
### Machine Learning, A Basis

Machine Learning is a process where a computational entity uses some form of "learning" in order to create some program that will mimic a very complex system which is impossible to represent within the realm of code. This process uses a large amount of data points in order to create a generalized understanding of the data interpreted. A quantification of "large amount of data" would be dependent on the type of data itself, accuracy required by the model, and the pattern that the user wants to recognize. The accuracy in the model and the pattern recognition is tuned via modifying weights in the model itself using the "large amount of data." This weight system allows for unparalleled accuracy and complex pattern recognition in machine learning for use in data analysis, prediction, or even some primitive artificial intelligence by choosing actions. 

Some examples of modern machine learning models are Deep Style and Image Generators like DALL-E and Stable Diffusion. These are impossible to create with just programming alone due to the fact that it requires an algorithmic system of gargantuan scales tuned with many magic numbers. 

Deep Style is a style transfer system that takes two images and puts the "style" of one image onto another. (Figure 1)

![An example of a Deep Style combination.](imgs/deepstyle.jpg)

Image Generators take a prompt and turn them into actual images. (Figure 2)

![An example of a Image Generation using the prompt "Dumb red panda eats a keyboard while laughing at a computer, paintin" generated using DALL-E.](imgs/imgen.png)

Some other terms used with machine learning data that are needed to process data properly are observation, feature, quantitative data, and qualitative data. Observations and features are the X and Y axis of a data set, where X is an observation and Y are the features from that observation. Each of the features can be quantitative (numerically qualified, i.e the weight of a bird) or qualitative (categorically identified, i.e the color pattern of a bird). This relates back to machine learning by having observations being those "data points" I mentioned earlier, and the features being the parts fed into the machine learning model in a certain way. Quantitative data can typically just be fed directly into the model while qualitative data must be preprocessed.

### My Interest in Machine Learning

The personal interest I hold in machine learning is mostly for creative endeavors, as I personally suck at the creative arts of art itself and music. I also want to create a model for automatic organization of music for my own purposes in my software. Professionally, I don't know for what purposes I would use machine learning, but I can imagine that generic internal datasets would be trained on in order to do recommendations. My learning would probably be on how to properly represent data as I have had major trouble in the past doing so.