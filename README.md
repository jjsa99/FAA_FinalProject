# FAA_FinalProject
### Fundamentos de Aprendizagem automática final project
The development of a COVID-19 and pneumonia detection from
chest X-ray images with Deep Learning.

**Abstract**
The goal of this work was to develop a deep learning model to classify X-Ray images of
healthy patients, patients with Covid-19 and patients with pneumonia. This task can be hard due to the fact
that if the disease is caught in an early stage, it’s unlikely that anything substantial will appear on the X-Ray.
We have used a dataset with 4725 samples, whose classes were balanced.
The models proposed in the literature to solve this problem fit one of the following groups: create a CNN
from scratch, do transfer learning for feature extraction or do transfer learning with fine-tuning. All models
that were reviewed registered accuracies above 90%.
We have implemented two models, one based on transfer learning for feature extraction and another based
on transfer learning with fine tuning. In the first model, five pre-trained CNNs were used to extract features
from the images in our dataset. Then, after feature reduction was applied, several linear classifiers were
trained with these features. The results were disapointing. We couldn’t determine the source of the problem,
as it was shown that the features contained relevant information about the data.
In the second model the last layer of five pre-trained CNNs was substituted by a simpler layer containing
just three neurons. An ensemble classifier based on hard voting was obtained from the CNNs. The results
achieved were satisfactory. The CNN RestNet and the CNN DenseNet had the best performances. The
accuracy of the modified ResNet, which was the model with the best performance, was 87.1%. This value
is inferior to most values present in literature, but is is still very satisfactory.
