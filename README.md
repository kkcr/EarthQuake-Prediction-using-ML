# Earthquake Prediction Using Machine Learning

## Abstract

Earthquake prediction is one of the most focused areas in disaster management, especially with the emergence of more advanced machine learning. In a world highly based on data collection, visualization, and modelling massive seismic data can be pivotal to enabling accurate, reliable, and precise earthquake prediction. This paper introduces a decision tree-based earthquake prediction model that uses Random Forest, XGBoost, LightGBM. Four critical phases are involved in this system: data collection, preprocessing, model training, and predictive analytics application. The features of historical seismic data are analysed to determine the patterns that support probabilistic predictions-including magnitude, depth, and location. Advanced visualization techniques also help to represent seismic trends more clearly, making it possible to make informed decisions in disaster preparedness. This study underlines the potential of machine learning in disaster management by aiding in early warnings that can save lives and reduce damage. However, there are still open challenges, such as the quality of the data, the integration of diverse data sources, and the possibility of deploying the prediction system in real time. The areas mentioned thus far represent avenues for further development, making systems more resilient and responsive to fighting against earthquake-related disasters.

## Introduction: 

Natural disaster management, such as earthquake, is still a global challenge that needs effective management. Earthquakes are the most unpredictable and destructive of natural phenomena. The threat to communities worldwide has resulted in the loss of life, severe infrastructural damage, economic disruption, and long-term societal impacts. Earthquake disasters can be broadly categorized into two main types: tectonic earthquakes, which are caused by the sudden movement of Earth’s tectonic plates, and volcanic earthquakes, which are associated with volcanic activity.  Both types create cascading effects, including aftershocks, landslides, and tsunamis, compounding the challenges of disaster response. A systematic approach toward disaster management has the goal of minimizing such impacts through preparedness, early warning systems, and mechanisms for rapid responses. Modern technological advances in the fields of data analytics and machine learning are used primarily in such a process. Machine learning will extract actionable insights from massive seismic information data sets, which can then be used to identify and predict patterns related to earthquakes with high precision.
This project introduces the earthquake prediction system using machine learning techniques, particularly Decision trees, Random Forest, XGBoost, LightGBM. Following a structured methodology through data collection and preprocessing, followed by model training and predictive analytics, ensures good pattern recognition accuracy critical for inputs toward early warning systems and aiding decisions in response formulating strategies to be implemented for effective responses.
The integration of machine learning in disaster management goes beyond enhancing situational awareness but also empowers authorities to make informed decisions and mitigate risks with regard to protecting societal infrastructure. By improving the accuracy and reliability of earthquake prediction, this project contributes to the advancement of global disaster management capabilities.

## Existing System

- Even with the improvement in seismology, no scientist or organization, including the USGS, has been able to predict a major earthquake, and the scientific community does not anticipate being able to make accurate earthquake predictions in the near future.
- Rather, scientists estimate the probabilities of significant earthquakes happening in a particular area within a time frame, which is expressed through hazard mapping.
- An actual earthquake prediction should give the date and time, place, and magnitude. Most earthquake predictions are spurious because they lack scientific proof, usually a result of unrelated events such as cloud formation, animal movements, or physical feelings.
- They do not define all three necessary conditions or employ imprecise wording which is always capable of fitting an earthquake somewhere, like anticipating a M4 in the U.S. within 30 days. Moreover, in cases where an earthquake coincidentally occurs to match a prediction, claimants tend to distort their success.
- Social media and non-technical sources tend to misinterpret possible precursors like swarms of minor earthquakes, increased radon contents in groundwater, strange behaviour by animals, and trends in moderate-magnitude earthquakes.
- Although these in some cases precede massive earthquakes, they happen relatively often without leading to large events, rendering accurate predictions futile. Rather, probabilistic prediction is employed to predict the chances of future earthquakes.
- Past instances, like the Chinese earthquake prediction based on minor earthquakes and animal migration, have been mixed. While some lives were saved, there were subsequent killer earthquakes without warning, resulting in heavy casualties.
- With these uncertainties in mind, the USGS and other science institutions focus more on long-term hazard mitigation rather than short-term forecasting by promoting earthquake-resistant buildings, creating early warning systems, performing seismic hazard analysis, and initiating public education and preparedness programs.
- In this way, a proactive system of disaster response and recovery is maintained, lowering earthquake hazards through science-based resilience efforts instead of uncertain predictions.


## Existing systems

The USGS nor any other scientists have ever predicted a major earthquake. We do not know how, and we do not expect to know how anytime in the foreseeable future. USGS scientists can only calculate the probability that a significant earthquake will occur (shown on our hazard mapping) in a specific area within a certain number of years.

An earthquake prediction must define 3 elements:
1. The date and time
2. The location
3. The magnitude

Yes, some people say they can predict earthquakes, but here are the reasons why their statements are false:

- They are not based on scientific evidence, and earthquakes are part of a scientific process. For example, earthquakes have nothing to do with clouds, bodily aches and pains, or slugs.
- They do not define all three of the elements required for a prediction.
- Their predictions are so general that there will always be an earthquake that fits; such as:
  - (a) There will be a M4 earthquake somewhere in the U.S. in the next 30 days.
  - (b) There will be a M2 earthquake on the west coast of the U.S. today.
- If an earthquake happens to occur that remotely fits their prediction, they claim success even though one or more of their predicted elements is wildly different from what actually occurred, making it a failed prediction.

## System architecture

### Rough flowchart
![Proposed system](https://github.com/user-attachments/assets/4bbaf94c-bbd5-4e10-a81b-d5fdb6446375)

The picture above is a flowchart of the process of an earthquake prediction system. It begins with the user opening the application by registering or signing in. The system proceeds to find out where the user is located through the Reverse Geolocation OpenCage API and fetches elevation information through the Open Topo Data API, in addition to the date and time of the moment.  
The data collected is processed to predict earthquakes through a pre-trained model saved in a Pickle file. The predicted outcome is shown on a dashboard and also emailed through the Google Gmail API. The process terminates when the email alert is sent successfully.  
The above flowchart gives a systematic description of how various elements of the system work in conjunction to predict and alert users regarding possible earthquakes.

### APIs Used:
- **Google API** for Gmail
- **OpenCage API** for reverse geolocation
- **opentopodata.org** for elevation



## Datasets
- Due to large set, dataset files were uploaded to GDrive. Link:
  - https://drive.google.com/drive/folders/1h3hW_RKqBf0fGPP9_IUlzPTfsRWRBGMz?usp=sharing

- Data was handpicked from websites like:
  - https://www.earthscope.org/
  - https://www.usgs.gov/programs/earthquake-hazards
  - https://earthquaketrack.com/

## Results
| Model                           | Accuracies |
|----------------------------------|------------|
| Light GBM                        | 93.36      |
| Random Forest Regressor          | 93.27      |
| XGBoost                          | 93.03      |
| Multi-Layer Perceptron (MLP)     | 92.71      |
| Support Vector Machine           | 92.13      |
| K-Nearest Neighbour              | 91.68      |
| Gated Recurrent Unit             | 91.26      |
| Recurrent Neural Networks        | 91.15      |
| LSTM                             | 90.79      |
| Decision Trees Regressor         | 90.73      |
| Transformer                      | 86.53      |


## Top 3 Models Results
- ### Light GBM
![Light GBM SP result](https://github.com/user-attachments/assets/c74d7578-3677-4430-95a7-b819e7f4fe20)

- ### Random Forest Regressor
![Random Forest SP result](https://github.com/user-attachments/assets/c7acdd8c-604d-42ac-9e4e-ac900c97d35d)

- ### XGBoost
![XGBoost SP result](https://github.com/user-attachments/assets/ae58ff45-1509-4651-8aad-6281167daa86)

  
## Top 3 Models Feature Importance
![Top 3 Feature importances](https://github.com/user-attachments/assets/9fb42440-25f1-48dd-889c-c69f61cc78e9)


## Alert Result
![Email](https://github.com/user-attachments/assets/ecec82d0-ce04-4e38-a9cb-d425907bc102)

## References
- Literature Reviews
  -  **Improving earthquake prediction accuracy in Los Angeles with machine learning** :- *Cemil Emre Yavas, Lei Chen, Christopher Kadlec, Yiming Ji*  used sophisticated machine learning methods, specifically the Random Forest algorithm, to forecast peak earthquake magnitudes in Los Angeles over a 30-day time frame. Their model had an impressive accuracy of 97.97%, greatly improving seismic risk management and preparedness planning.
  -  **Earthquake magnitude prediction in Hindukush region using machine learning techniques** :- *K. M. Asim, F. Martínez-Álvarez, A. Basit, T. Iqbal*.  The research delves into machine learning methods for earthquake magnitude prediction in the Hindukush area. Based on seismic data from the past, the authors implement different models to find patterns and enhance forecast accuracy. The research points towards the capability of AI-based methodologies for early warning systems to support preparedness for disasters & reducing risks.
  -  **Major earthquake event prediction using various machine learning algorithms** :- *Roxane Mallouhy, Chady Abou Jaoude, Christophe Guyeux, Abdallah Makhoul*. The research paper "Major earthquake event prediction using different machine learning algorithms" by Roxane Mallouhy, Chady Abou Jaoude, Christophe Guyeux, and Abdallah Makhoul examines the performance of eight machine learning algorithms for the task of categorizing seismic events into major and minor earthquakes. The work assesses each of the models in terms of a number of metrics to conclude that Random Forest and K-Nearest Neighbours are the most precise classifiers.
  -  **Earthquake magnitude prediction in Turkey** :-*Hatice Öncel Çekim, Hatice Nur Karakavak, Gamze Ozel, Senem Tekin*.A  comparative study of deep learning methods, ARIMA and singular spectrum analysis. This research compares deep learning approaches used in forecasting earthquake magnitudes in Turkey. It combines ARIMA and SSA for earthquake response and recovery modeling. The study analyzes forecasting precision, stating the superiority of hybrid models in the depiction of seismic patterns and enhancing disaster preparedness and mitigation measures.
 

- Links & Websites
  - **IRIS Browser**  
    [https://ds.iris.edu/ieb/index.html](https://ds.iris.edu/ieb/index.html?format=text&nodata=404&src=usgs&limit=200&maxlat=56.000&minlat=22.000&maxlon=159.000&minlon=127.000&sbl=1&pbl=1&caller=self&name=Japan%20Region&zm=4)
  
  - **Google API for Gmail**  
    [https://console.cloud.google.com/apis/dashboard](https://console.cloud.google.com/apis/library)
  
  - **OpenCage API for Reverse Geolocation**  
    [https://opencagedata.com/dashboard#geocoding](https://opencagedata.com/dashboard#geocoding)
  
  - **OpenTopData API for Elevation**  
    [https://www.opentopodata.org](https://www.opentopodata.org)
