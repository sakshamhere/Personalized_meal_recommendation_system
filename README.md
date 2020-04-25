# A Personalized Meal Recommendation System 

### - **Abstract** 
_On the Internet, where the number of choices is overwhelming, there is need to filter, prioritize and efficiently deliver relevant information in order to alleviate the problem of information overload, which has created a potential problem to many Internet users. Recommender systems solve this problem by searching through large volume of dynamically generated information to provide users with personalized content and services._


### - **Objective**
_The goal of application is to provide a platform where users find their Nutritious food according to their  personal health preferences and build a behavior of living healthy life._

Hi , This is my college mini project based on python for **learning purpose**, the system recommends meal on the basis of user's preference of following :

1. Nutrient (Protien,fiber,carbohydrates,calcium etc ..)
2. Diet (Vegan diet,Paleo diet,high - fiber,gluten-free,low-fat diet etc ..)
3. Disease or medical condition, if user have any (pregnancy ,diabetes , obesity etc ..)

### - Types of methods for Recommendation systems 

1. **Content based method** - _A Content-based recommendation system tries to recommend items to users based on their profile. In this recommender system the content of the Meal (can be ingredient description , keywords , users review etc..) is used to find its similarity with other Meal. Then the Meal that are most likely to be similar are recommended._

2. **Collaborative method** -  _ Uses user’s past behaviors (items previously purchased or selected and/or numerical ratings given to those items) as well as similar decisions made by other users. This model is then used to predict items (or ratings for items) that the user may have an interest in.The collaborative method is based on user-item interactions The class of collaborative filtering algorithms is divided into two sub-categories that are generally called memory based and model based approaches. Memory based approaches (**approach in this project**) directly works with values of recorded interactions, assuming no model, and are essentially based on nearest neighbours search (for example, find the closest users from a user of interest and suggest the most popular items among these neighbours)._  

_The other model based method uses Matrix factorisation, decomposing the huge and sparse user-item interaction matrix into a product of two smaller and dense matrices: a user-factor matrix (containing users representations) that multiplies a factor-item matrix (containing items representations)._

3. **hybrid** - _this is combination of both approaches_

***************************************************************************************************************************************

### flow of project: 

1. Data collection - data is collected by web scraping (projects works on demo data).
2. Data processing - data is processed and required attributes are added to make demo datasets.
3. User's profile generation by taking input from them .
4. Initial recommendation on the basis of user's profile (Content-based,implemented by k-nearest neighbors).
5. Recommendation based on similar profiles to users.
5. Recommendation on the basis of users past/recent activity (Collaborative Memory based approach,implemented by K-nearest neighbors).

***************************************************************************************************************************************

- The project above is a very small implementation by k-nearest neigbor algorithm,
- what more should be done ?

The profile should get updated everytime on user's activity
Matrix factorisation methods of collaborative filtering can be applied
further Single Value Decomposition can be applied 

### one should read:
[Kaggle](https://www.kaggle.com/ibtesama/getting-started-with-a-movie-recommendation-system)
[kaggle](https://www.kaggle.com/rounakbanik/movie-recommender-systems)
[Article](https://hackernoon.com/introduction-to-recommender-system-part-1-collaborative-filtering-singular-value-decomposition-44c9659c5e75)
[Article](https://towardsdatascience.com/introduction-to-recommender-systems-6c66cf15ada)
[Article](https://towardsdatascience.com/various-implementations-of-collaborative-filtering-100385c6dfe0)
[Article](https://towardsdatascience.com/prototyping-a-recommender-system-step-by-step-part-1-knn-item-based-collaborative-filtering-637969614ea)