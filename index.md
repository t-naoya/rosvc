# ROBUST ONE-SHOT SINGING VOICE CONVERSION

## Abstruct
Many existing works on singing voice conversion (SVC) require clean recordings of target singer’s voice for training. However, it is often difficult to collect them in advance and singing voices are often distorted with reverb and accompaniment music. In this work, we propose a robust one-shot SVC (ROSVC) that performs any-to-any SVC robustly even on such distorted singing voice using only less than 10s of a reference voice. 
To this end, we propose a two-stage training method called **Robustify**. In the first stage, a novel one-shot SVC model based on a generative adversarial network is trained on clean data to ensure the high-quality conversion. In the second stage, enhancement modules are introduced to encoders of the model to improve the robustness against distortions in the feature space. Experimental results show that the proposed method outperforms one-shot SVC baselines for both seen and unseen singers and greatly improves the robustness against the distortions.

---
## One-shot Singing Voice conversion on distorted data
In this section, we show the robustness of our model against distortion. We perform one-shot SVC on samples that have reberb and accompaniment music.  
**All singers are unseen during the model training.**  


### MUSDB18
The source and reference singers are from the MUSDB18 dataset. Singing voices are extracted by the music source separation model called <a href="https://github.com/sony/ai-research-code/tree/master/d3net">D3Net</a>.
Note that the models are trained uging NHSS and NUS48E datasets, so this is samples from **unseen domain data**.

|              | Sample 1<BR>AM Contra → Carlos Gonzalez | Sample 2<BR> Mu → AM Contra | Sample 3<BR>Cristina Vane → Mu |
|:------------:|:-------:|:-------:|:-------:|
|    **Source**    |    <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/mixture/AM Contra - Heart Peripheral_0.wav"></source> </audio>   |    <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/mixture/Mu - Too Bright_0.wav"></source> </audio>  |    <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/mixture/Cristina Vane - So Easy_0.wav"></source> </audio>  |
|    **Target**    |     <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/mixture/Carlos Gonzalez - A Place For Us_0.wav"></source> </audio>   |     <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/mixture/AM Contra - Heart Peripheral_0.wav"></source> </audio> |     <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/mixture/Mu - Too Bright_0.wav"></source> </audio> |
|    **Separated Source**    |    <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/separation/origi_AM Contra - Heart Peripheral_0_sep.wav"></source> </audio>   |    <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/separation/origi_Mu - Too Bright_0_sep.wav"></source> </audio>  |    <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/separation/origi_Cristina Vane - So Easy_0_sep.wav"></source> </audio>  |
|    **Separated Target**    |     <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/separation/origi_Carlos Gonzalez - A Place For Us_0_sep.wav"></source> </audio>   |     <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/separation/origi_AM Contra - Heart Peripheral_0_sep.wav"></source> </audio> |     <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/separation/origi_Mu - Too Bright_0_sep.wav"></source> </audio> |
|    **w/o Robustify**   |     <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/SRC_sep_TRG_sep/SRC_AM Contra - Heart Peripheral_0_TRG_Carlos Gonzalez - A Place For Us_0.wav"></source> </audio>    |     <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/SRC_sep_TRG_sep/SRC_Mu - Too Bright_0_TRG_AM Contra - Heart Peripheral_0.wav"></source> </audio>     |     <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/SRC_sep_TRG_sep/SRC_Cristina Vane - So Easy_0_TRG_Mu - Too Bright_0.wav"></source> </audio>     |
| **ROSVC (Ours)** |    <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/SRC_sepEnh_TRG_sepEnh/SRC_AM Contra - Heart Peripheral_0_TRG_Carlos Gonzalez - A Place For Us_0.wav"></source> </audio>     |    <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/SRC_sepEnh_TRG_sepEnh/SRC_Mu - Too Bright_0_TRG_AM Contra - Heart Peripheral_0.wav"></source> </audio>      |    <audio  controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/MUSDB18/SRC_sepEnh_TRG_sepEnh/SRC_Cristina Vane - So Easy_0_TRG_Mu - Too Bright_0.wav"></source> </audio>      |


### Synthetic Distortion on Reference
The source and reference singers are unseen singers from the NHSS and NUS48E datasets. We syntheticaly distort *reference* singing voices by applying reverb and mixing music.  

|              | Sample 1 <BR>M05(NHSS) → F05(NHSS) | Sample 2<BR> F05(NHSS) → M05(NHSS) | Sample 3<BR> F05(NHSS) → PMAR(NUS48E)|
|:------------:|:-------:|:-------:|:-------:|
|    **Source**    |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="CroppedSources/M05_98.wav"></source> </audio>   |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="CroppedSources/F05_48.wav"></source> </audio>  |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="CroppedSources/F05_48.wav"></source> </audio>  |
|    **Target**    |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/mix/F05_48_mix.wav"></source> </audio>   |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/mix/M05_98_mix.wav"></source> </audio> |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/mix/PMAR_1_mix.wav"></source> </audio> |
|    **Separated Target**    |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/sep/origi_F05_48_sep.wav"></source> </audio>   |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/sep/origi_M05_98_sep.wav"></source> </audio> |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/sep/origi_F05_48_sep.wav"></source> </audio> |
|    **W/O Robustify**   |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_clean_TRG_sep/SRC_M05_98_TRG_F05_48.wav"></source> </audio>    |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_clean_TRG_sep/SRC_F05_48_TRG_M05_98.wav"></source> </audio>     |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_clean_TRG_sep/SRC_F05_48_TRG_PMAR_1.wav"></source> </audio>     |
| **ROSVC (Ours)** |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_clean_TRG_sepEnh/SRC_M05_98_TRG_F05_48.wav"></source> </audio>     |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_clean_TRG_sepEnh/SRC_F05_48_TRG_M05_98.wav"></source> </audio>      |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_clean_TRG_sepEnh/SRC_F05_48_TRG_PMAR_1.wav"></source> </audio>      |
  

### Synthetic Distortion on Source
The source and reference singers are unseen singers from the NHSS and NUS48E datasets. We syntheticaly distort *source* singing voices by applying reverb and mixing music.

|              | Sample 1 <BR>F05(NHSS) → PMAR(NUS48E) | Sample 2<BR>ZHIY(NUS48E) → PMAR(NUS48E) | Sample 2<BR>PMAR(NUS48E) → ZHIY(NUS48E) |
|:------------:|:-------:|:-------:|:-------:|
|    **Source**    |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/mix/F05_48_mix.wav"></source> </audio>   |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/mix/ZHIY_1_mix.wav"></source> </audio>   |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/mix/PMAR_1_mix.wav"></source> </audio>  |
|    **Target**    |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="CroppedSources/PMAR_1.wav"></source> </audio>   |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="CroppedSources/PMAR_1.wav"></source> </audio>   |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="CroppedSources/ZHIY_1.wav"></source> </audio> |
|    **Separated Source**    |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/sep/origi_F05_48_sep.wav"></source> </audio>   |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/sep/origi_ZHIY_1_sep.wav"></source> </audio>   |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/sep/origi_PMAR_1_sep.wav"></source> </audio>  |
|    **W/O Robustify**   |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_sep_TRG_clean/SRC_F05_48_TRG_PMAR_1.wav"></source> </audio>    |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_sep_TRG_clean/SRC_ZHIY_1_TRG_PMAR_1.wav"></source> </audio>    |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_sep_TRG_clean/SRC_PMAR_1_TRG_ZHIY_1.wav"></source> </audio>     |
| **ROSVC (Ours)** |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_sepEnh_TRG_clean/SRC_F05_48_TRG_PMAR_1.wav"></source> </audio>     |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_sepEnh_TRG_clean/SRC_ZHIY_1_TRG_PMAR_1.wav"></source> </audio>     |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_sepEnh_TRG_clean/SRC_PMAR_1_TRG_ZHIY_1.wav"></source> </audio>      |


### Synthetic Distortion on Source and Reference
The source and reference singers are unseen singers from the NHSS and NUS48E datasets. We syntheticaly distort *source and reference* singing voices by applying reverb and mixing music.

|              | Sample 1<BR> M05(NHSS) → F05(NHSS) | Sample 2<BR> F05(NHSS) → M05(NHSS) |Sample 3<BR> PMAR(NUS48E) → M05(NHSS) |
|:------------:|:-------:|:-------:|:-------:|
|    **Source**    |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/mix/M05_98_mix.wav"></source> </audio>   |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/mix/F05_48_mix.wav"></source> </audio>  |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/mix/PMAR_1_mix.wav"></source> </audio>  |
|    **Target**    |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/mix/F05_48_mix.wav"></source> </audio>   |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/mix/M05_98_mix.wav"></source> </audio> |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/mix/M05_98_mix.wav"></source> </audio> |
|    **Separated Source**    |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/sep/origi_M05_98_sep.wav"></source> </audio>   |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/sep/origi_F05_48_sep.wav"></source> </audio>  |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/sep/origi_PMAR_1_sep.wav"></source> </audio>  |
|    **Separated Target**    |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/sep/origi_F05_48_sep.wav"></source> </audio>   |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/sep/origi_M05_98_sep.wav"></source> </audio> |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/sep/origi_M05_98_sep.wav"></source> </audio> |
|    **W/O Robustify**   |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_sep_TRG_sep/SRC_M05_98_TRG_F05_48.wav"></source> </audio>    |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_sep_TRG_sep/SRC_F05_48_TRG_M05_98.wav"></source> </audio>     |     <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_sep_TRG_sep/SRC_PMAR_1_TRG_M05_98.wav"></source> </audio>     |
| **ROSVC (Ours)** |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_sepEnh_TRG_sepEnh/SRC_M05_98_TRG_F05_48.wav"></source> </audio>     |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_sepEnh_TRG_sepEnh/SRC_F05_48_TRG_M05_98.wav"></source> </audio>      |    <audio controls="controls" style="width:200px;">  <source type="audio/wav" src="Samples/Distorted/SRC_sepEnh_TRG_sepEnh/SRC_PMAR_1_TRG_M05_98.wav"></source> </audio>      |


---
## Comparision against baselines

In this section, we compare our proposed model ROSVC with the baseline, an extention of <a href="https://arxiv.org/pdf/2008.02830.pdf">UCDSVC</a> [1]. We use clean singing voices of unseen singers from the NHSS and NUS48E datasets. 


### Female to Female 

|              | Sample 1 (F05(NHSS) → PMAR(NUS48E)) | Sample 2 (PMAR(NUS48E) → F05(NHSS)) |
|:------------:|:-------:|:-------:|
|    **Source**    |    <audio controls="controls">  <source type="audio/wav" src="CroppedSources/F05_48.wav"></source> </audio>   |    <audio controls="controls">  <source type="audio/wav" src="CroppedSources/PMAR_43.wav"></source> </audio>  |
|    **Target**    |     <audio controls="controls">  <source type="audio/wav" src="CroppedSources/PMAR_1.wav"></source> </audio>   |     <audio controls="controls">  <source type="audio/wav" src="CroppedSources/F05_118.wav"></source> </audio> |
|    **UCDSVC**   |     <audio controls="controls">  <source type="audio/wav" src="Samples/Comparision/UCDSVC/F2F/SRC_F05_48_TRG_PMAR_1.wav"></source> </audio>    |     <audio controls="controls">  <source type="audio/wav" src="Samples/Comparision/UCDSVC/F2F/SRC_PMAR_43_TRG_F05_118.wav"></source> </audio>     |
| **ROSVC** |    <audio controls="controls">  <source type="audio/wav" src="Samples/Comparision/ROSVC/F2F/SRC_F05_48_TRG_PMAR_1.wav"></source> </audio>     |    <audio controls="controls">  <source type="audio/wav" src="Samples/Comparision/ROSVC/F2F/SRC_PMAR_43_TRG_F05_118.wav"></source> </audio>      |

### Female to Male 

|              | Sample 1 (F05(NHSS) → ZHIY(NUS48E)) | Sample 2 (PMAR(NUS48E) → M05(NHSS)) |
|:------------:|:-------:|:-------:|
|    **Source**    |    <audio controls="controls">  <source type="audio/wav" src="CroppedSources/F05_48.wav"></source> </audio>   |    <audio controls="controls">  <source type="audio/wav" src="CroppedSources/PMAR_1.wav"></source> </audio>  |
|    **Target**    |     <audio controls="controls">  <source type="audio/wav" src="CroppedSources/ZHIY_14.wav"></source> </audio>   |     <audio controls="controls">  <source type="audio/wav" src="CroppedSources/M05_98.wav"></source> </audio> |
|    **UCDSVC**   |     <audio controls="controls">  <source type="audio/wav" src="Samples/Comparision/UCDSVC/F2M/SRC_F05_48_TRG_ZHIY_14.wav"></source> </audio>    |     <audio controls="controls">  <source type="audio/wav" src="Samples/Comparision/UCDSVC/F2M/SRC_PMAR_1_TRG_M05_98.wav"></source> </audio>     |
| **ROSVC** |    <audio controls="controls">  <source type="audio/wav" src="Samples/Comparision/ROSVC/F2M/SRC_F05_48_TRG_ZHIY_14.wav"></source> </audio>     |    <audio controls="controls">  <source type="audio/wav" src="Samples/Comparision/ROSVC/F2M/SRC_PMAR_1_TRG_M05_98.wav"></source> </audio>      |

### Male to Female 

|              | Sample 1 (M05(NHSS) → F05(NHSS)) | Sample 2 (ZHIY(NUS48E) → PMAR(NUS48E)) |
|:------------:|:-------:|:-------:|
|    **Source**    |    <audio controls="controls">  <source type="audio/wav" src="CroppedSources/M05_118.wav"></source> </audio>   |    <audio controls="controls">  <source type="audio/wav" src="CroppedSources/ZHIY_14.wav"></source> </audio>  |
|    **Target**    |     <audio controls="controls">  <source type="audio/wav" src="CroppedSources/F05_48.wav"></source> </audio>   |     <audio controls="controls">  <source type="audio/wav" src="CroppedSources/PMAR_1.wav"></source> </audio> |
|    **UCDSVC**   |     <audio controls="controls">  <source type="audio/wav" src="Samples/Comparision/UCDSVC/M2F/SRC_M05_118_TRG_F05_48.wav"></source> </audio>    |     <audio controls="controls">  <source type="audio/wav" src="Samples/Comparision/UCDSVC/M2F/SRC_ZHIY_14_TRG_PMAR_1.wav"></source> </audio>     |
| **ROSVC** |    <audio controls="controls">  <source type="audio/wav" src="Samples/Comparision/ROSVC/M2F/SRC_M05_118_TRG_F05_48.wav"></source> </audio>     |    <audio controls="controls">  <source type="audio/wav" src="Samples/Comparision/ROSVC/M2F/SRC_ZHIY_14_TRG_PMAR_1.wav"></source> </audio>      |

### Male to Male

|              | Sample 1 (M05(NHSS) → ZHIY(NUS48E)) | Sample 2 (ZHIY(NUS48E) → M05(NHSS)) |
|:------------:|:-------:|:-------:|
|    **Source**    |    <audio controls="controls">  <source type="audio/wav" src="CroppedSources/M05_98.wav"></source> </audio>   |    <audio controls="controls">  <source type="audio/wav" src="CroppedSources/ZHIY_14.wav"></source> </audio>  |
|    **Target**    |     <audio controls="controls">  <source type="audio/wav" src="CroppedSources/ZHIY_14.wav"></source> </audio>   |     <audio controls="controls">  <source type="audio/wav" src="CroppedSources/M05_98.wav"></source> </audio> |
|    **UCDSVC**   |     <audio controls="controls">  <source type="audio/wav" src="Samples/Comparision/UCDSVC/M2M/SRC_M05_98_TRG_ZHIY_14.wav"></source> </audio>    |     <audio controls="controls">  <source type="audio/wav" src="Samples/Comparision/UCDSVC/M2M/SRC_ZHIY_14_TRG_M05_98.wav"></source> </audio>     |
| **ROSVC** |    <audio controls="controls">  <source type="audio/wav" src="Samples/Comparision/ROSVC/M2M/SRC_M05_98_TRG_ZHIY_14.wav"></source> </audio>     |    <audio controls="controls">  <source type="audio/wav" src="Samples/Comparision/ROSVC/M2M/SRC_ZHIY_14_TRG_M05_98.wav"></source> </audio>      |

## Reference
[1] A. Polyak, L. Wolf, Y. Adi, and Y. Taigman, “Unsupervised cross-domain singing voice conversion,” in Proc. ICASSP, 2020.
