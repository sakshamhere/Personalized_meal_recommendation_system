# A Personalized Meal Recommendation System 

### - **Abstract** 
_On the Internet, where the number of choices is overwhelming, there is need to filter, prioritize and efficiently deliver relevant information in order to alleviate the problem of information overload, which has created a potential problem to many Internet users. Recommender systems solve this problem by searching through large volume of dynamically generated information to provide users with personalized content and services._


### - **Objective**
_The goal of application is to provide a platform where users find their Nutritious food according to their  personal health preferences and build a behavior of living healthy life._

Hi , This is my college mini project based on python for **learning purpose**, the system recommends meal on the basis of user's preference of following :

1. Nutrient (Protien,fiber,carbohydrates,calcium etc ..)
2. Diet (Vegan diet,Paleo diet,high - fiber,gluten-free,low-fat diet etc ..)
3. Disease or medical condition, if user have any (pregnancy ,diabetes , obesity etc ..)

### flow of project: 

1. Data collection - data is collected by web scraping (projects works on demo data).
2. Data processing - data is processed and required attributes are added to make demo datasets.
3. User's profile generation by taking input from them .
4. Initial recommendation on the basis of user's profile (Content-based,implemented by k-nearest neighbors).
5. Recommendation based on similar profiles to users.
5. Recommendation on the basis of users past/recent activity (Collaborative Memory based approach,implemented by K-nearest neighbors).

### - Technology used - 

1. **Python and its libraries**
- For Web scraping - **Beautifulsoup**, **requests**
- For Maintaing/handeling data and Data processing- **Pandas**,**numpy**,**time**,**datetime**,**random**,**nltk**
- For Recommendation - **sklearn**


### Future Scope - 
Matrix factorisation methods of collaborative filtering can be applied,
further Single Value Decomposition can be applied 

### Some Articles to Refer:
[Kaggle](https://www.kaggle.com/ibtesama/getting-started-with-a-movie-recommendation-system)
[kaggle](https://www.kaggle.com/rounakbanik/movie-recommender-systems)
[Article](https://hackernoon.com/introduction-to-recommender-system-part-1-collaborative-filtering-singular-value-decomposition-44c9659c5e75)
[Article](https://towardsdatascience.com/introduction-to-recommender-systems-6c66cf15ada)
[Article](https://towardsdatascience.com/various-implementations-of-collaborative-filtering-100385c6dfe0)
[Article](https://towardsdatascience.com/prototyping-a-recommender-system-step-by-step-part-1-knn-item-based-collaborative-filtering-637969614ea)

