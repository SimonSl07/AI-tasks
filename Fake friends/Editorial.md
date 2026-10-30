**Dataset Authors**:
 * Mix of AG News Dataset (https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset) and Large Movie Review Dataset (https://ai.stanford.edu/~amaas/data/sentiment/)

**Task Author**: 
 * Slănină Simon - TU Delft, Olanda

**Statement Author**: 
 * Slănină Simon - TU Delft, Olanda

**Translators**:
* Ionescu Clara - Universitatea Babeș-Bolyai, Cluj-Napoca
 * Slănină Simon - TU Delft, Olanda

**Testers**:
 * Miron Radu - Universitatea Alexandru-Ioan Cuza, Iași
 * Șuchea Rareș-Andrei - Universitatea Babeș-Bolyai, Cluj-Napoca

### About the Dataset

The dataset consists of samples of data from the AG News Dataset, mixed with some movie reviews from the Large Movie Review Dataset.

### About the Task

The task is meant to test the student's ability to solve unsupervised learning tasks by analysing the data, performing dimensionality reduction and clustering.

#### Intended solution

One of the first ideas that might come to mind when reading the task is embedding the texts using the provided model, doing dimensionality reduction with a tool like UMAP or PCA on these embeddings and then using HDBSCAN to solve both subtasks at the same time. While this solution does get some points, the provided model is not smart enough to provide embeddings of the quality needed for this task.

### Subtask 1

By looking at the data we can observe that the noise seems to only consist of movie reviews. This sparks the idea that we can find the noise using a simple heuristic: 
1. Compute embeddings for the texts in the dataset
2. Create two simple embeddings that encompass the concept of news (**news_concept**), and the noise respectively  (**movie_concept**)
3. Use cosine similarity to check for each text what concept it is more similar to
4. Mark texts that are more similar to the concept of movies as noise
For example:
```py

model = SentenceTransformer('BAAI/bge-small-en-v1.5')
embeddings = model.encode(texts, show_progress_bar=True,normalize_embeddings=True)

movie_concept = model.encode(["movie review film acting director cinema plot"])
news_concept = model.encode(["breaking news politics world finance sports technology business local events"])

is_noise_mask = sim_movie > sim_news + 0.06 # 0.06 is a margin that was chosen by testing multiple values, and choosing the one that performed best on the given data
is_news_mask = ~is_noise_mask  # Everything else is news
```

### Subtask 2
New for subtask 2 we must:
5. Perform **dimensionality reduction** on the embeddings that we classified as news in subtask 1
6. Either perform **HDBSCAN** to group the data into clusters, and either mark the noise found by HDBSCAN as noise, or as another cluster
Or for a better score, use **KMeans** and attempt to find the amount of clusters yourself  (which is 4). 
On the given data, KMeans performs better than HDBSCAN, and the **n_clusters** parameter of KMeans is easier to tweak than the **min_cluster_size , min_samples** parameters of HDBCAN

```py
news_embeddings = embeddings[is_news_mask]

#Reduce embeddings
pca = PCA(n_components=7, random_state=42)
reduced_news = pca.fit_transform(news_embeddings)

#Perform clustering
clusterer = KMeans(4)
news_labels = clusterer.fit_predict(reduced_news) 
```


This solution provides a MCC score of 0.87 and a AMI score of 0.6.

#### A simpler solution is to use the concepts "movie reviews" and "news article" as prompts. This way, the 0.06 margin is no longer needed for the first task and PCA is no longer needed for the second task as well.