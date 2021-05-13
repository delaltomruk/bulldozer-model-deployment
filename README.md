# bulldozer-model-deployment

This was one my first projects in ML and I forgot about it until recently. I've realized this would be a good project to learn model deployment, so here we are.

Going back to this beginner project also made me realize I made a lot of mistakes as a beginner, so here is my blog post about it:

# Models and Data

I followed a tutorial on Udemy for this project when I first did it, however I tweaked the solution a bit now since I've realized there can be some improvements such as scaling, feature selection and hyperparameter tuning.

Dataset: https://www.kaggle.com/c/bluebook-for-bulldozers

Initial Tutorial: https://github.com/mrdbourke/zero-to-mastery-ml/blob/master/section-3-structured-data-projects/end-to-end-bluebook-bulldozer-price-regression-video.ipynb

# Deployment

For deployment, I chose 4 features based on feature importance:

<img width="400" alt="Screen Shot 2021-05-13 at 6 11 21 PM" src="https://user-images.githubusercontent.com/66208179/118194034-608aec80-b451-11eb-8b60-e5023d194a37.png">

I used Flask to host the website on my local machine.

<p float="left">
  
<img width="400" alt="Screen Shot 2021-05-13 at 6 16 32 PM" src="https://user-images.githubusercontent.com/66208179/118194454-135b4a80-b452-11eb-9470-ecf9271404da.png">

<img width="400" alt="Screen Shot 2021-05-13 at 6 16 41 PM" src="https://user-images.githubusercontent.com/66208179/118194472-16563b00-b452-11eb-9ecb-75b46880edfa.png">



</p>


# To Do:

- Heroku
