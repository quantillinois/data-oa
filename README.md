# Data Science: Exploratory Data Analysis on a Consumer Finance Dataset

Exploratory data analysis plays a huge part in quantitative finance. Often, in a variety of scenarios, consumer interests, expectations and beliefs play a huge role in deciding major moves for organisations.

_Imagine the following scenario:_ We are an up and coming bank with limited resources. We want to start generating alpha as soon as possible and are elated to do so. Unfortunately, we are unable to hire a large legal team that handles disputes effectively, and seek to minimise the number of consumer complaints that we deal with, as well as deal with only general categories whose disputes are easy to resolve.

On the bright side, we have a dataset with a large number of submitted complaints for many credit based products. Based on these complaints, can you generate insights and a summary of credit products that our company can sell safely? Are there optimizations that we can make in our product offering? (from a legal and PR perspective, assume that another team handles actual credit-default risk.)

Your task, then, is to write a Jupyter Notebook detailing an exploration into the data that you have. Here are a few ideas that you can explore: 

- What states are these disputes most prevalent in? (Can you also maybe get in your own dataset about populations of these states to measure percentages?)
- Could you figure out the most common products and sub-products with these complaints? Could you find out which of the banks were most likely to have which issues?
- Could you find out what the most common language / keywords that companies used in their personal statements are? 
- Can you build a quick and dirty model to take in a bunch of relevant features and figure out how the compnay is going to approach the issue?
   - You cannot take in the consumer complaint as text itself in most models, that would be unwise, is there any way you can quantify this text using some basic NLP, and use those instead as features.
- In the same way, taking more relevant features, can you build out a model that takes in relevant features and the company's closure method, and predict if the consumer is going to dispute it or not?

Remember, this is a non comprehensive list, and any new ideas that you have can and should be implemented. If you have the opportunity to use any other public datasets to amplify the insights from this dataset, you're encouraged to import them in!

Your code should be highly modular, customizable, and absent of technical debt. Your exploration must contain lots of your hanging ideas, explanations based on your choices you make with the data. Remember to work with only the essential data, and drop all irrelevant columns, remove outliers, etc.

This criteria is the same in our codebase and will be a good indicator if you can generate data science based insights. Imagine that you're showing the insights from this dataset to an executive, and retain only visual and simple to understand correlations that you find. Good luck!

## Instructions for working with the dataset:

The dataset is on Google Drive. Our advice for you is to download the dataset, work on it, and add it to the gitignore in your private forks, so that you don't commit it. **Always print out outputs of operations within your notebook, but do not include the dataset itself as part of your submission.**

Link to dataset: https://drive.google.com/file/d/1Vnny6HVGBgF_mdDtIo2ddOTtOiGF5jxK/view?usp=sharing

Log in with your GApps@Illinois account to access this dataset.

