Experimental Identification of Dynamic Parameters in a Free Vibration SDOF
System Using FFT and RDT
John Erick Martínez Agurto
Universidad Nacional de Ingeniería
Master’s Program in Civil Engineering Sciences with Specialization in Structures
Course: Structural Dynamics
Lima – Perú
2026
Abstract
This study presents the experimental identification of dynamic parameters of a simple structural system through
free vibration testing. For this purpose, five experimental tests were conducted using an accelerometer integrated
into a mobile device, recording the dynamic response of the specimen in the time domain. Based on the acquired
records, signal processing was performed primarily considering the acceleration component along the vertical
axis (Z-axis), selecting the representative free-vibration interval for the dynamic analysis.
Subsequently, the main system parameters, such as the natural period, natural frequency, and structural damping
ratio, were determined using experimental methods including logarithmic decrement and successive peak
analysis. In addition, the Fast Fourier Transform (FFT) was applied to identify the dominant frequency of the
system in the frequency domain, while the Random Decrement Technique (RDT) was employed to obtain an
equivalent free-vibration signal by reducing the influence of experimental noise.
The obtained results exhibit the characteristic behavior of an underdamped system, evidenced by the progressive
decrease in vibration amplitude over time and the presence of a dominant frequency close to the experimentally
calculated natural frequency. Finally, the experimental response was compared with the theoretical
mathematical model of a Single Degree of Freedom (SDOF) system, showing good agreement between both
approaches.
Keywords
Free vibration, Fast Fourier Transform (FFT), Random Decrement Technique (RDT), damping, natural
frequency, SDOF system, structural dynamic
1. Introduction the dynamic behavior of the system to be
characterized.
Structural dynamics enables the analysis of the
behavior of systems subjected to time-varying In the experimental field, the identification of these
loads, such as mechanical vibrations, seismic parameters generally requires specialized
actions, and external dynamic excitations. Among instrumentation. However, recent technological
the principal parameters governing the vibratory advances in mobile devices have enabled the use of
response of a structure are the natural period, accelerometers embedded in smartphones as
natural frequency, and damping ratio, which allow accessible tools for the recording and preliminary
analysis of structural vibrations.

In the present study, an experimental free-vibration  For simplified dynamic analysis, the experimental
test  was  carried  out  using  a  metallic  ruler  system can be idealized using a Single Degree of
configured as a cantilever beam and a smartphone  Freedom  (SDOF)  model,  represented  by  an
functioning as an acceleration sensor. The system  equivalent mass connected to an elastic element and
was  excited  through  an  initial  displacement  a  damping  element.  This  model  adequately
followed  by  sudden  release,  while  the  dynamic  describes the dominant behavior of simple vibrating
response in the time domain was recorded using a  systems through a single displacement coordinate.
mobile accelerometer application.
| Based  | on  the  | acquired  |     | signals,  | dynamic  | signal  |     |     |     |     |     |
| ------ | -------- | --------- | --- | --------- | -------- | ------- | --- | --- | --- | --- | --- |
processing was performed mainly considering the
| vertical  | acceleration  |     |     | component  |     | (Z-axis).  |     |     |     |     |     |
| --------- | ------------- | --- | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- |
Subsequently, the natural period, natural frequency,
and structural damping ratio were experimentally
| determined  |     | through  |     | time-domain  |     | analysis,  |     |     |     |     |     |
| ----------- | --- | -------- | --- | ------------ | --- | ---------- | --- | --- | --- | --- | --- |
logarithmic decrement, and Fast Fourier Transform
| (FFT).  | In  | addition,  | the  | Random  |     | Decrement  |     |     |     |     |     |
| ------- | --- | ---------- | ---- | ------- | --- | ---------- | --- | --- | --- | --- | --- |

Technique (RDT) was applied to obtain equivalent
Figure 1. Conceptual SDOF system model.
| free-vibration  |     | signals  | with  | reduced  |     | experimental  |              |           |         |                |     |
| --------------- | --- | -------- | ----- | -------- | --- | ------------- | ------------ | --------- | ------- | -------------- | --- |
| noise.          |     |          |       |          |     |               | The dynamic  | behavior  | of the  | damped system  | is  |
represented by the following differential equation:
Finally, the dynamic behavior of the system was
|     |     |     |     |     |     |     |     | ???(?)+???(?)+??(?)= |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- |
represented through a simplified Single Degree of
| Freedom (SDOF) mathematical model, comparing  |     |     |           |     |           |            | where:  |     |     |     |     |
| --------------------------------------------- | --- | --- | --------- | --- | --------- | ---------- | ------- | --- | --- | --- | --- |
| the  experimentally                           |     |     | obtained  |     | response  | with  the  |         |     |     |     |     |
•  ?: equivalent mass of the system.
| corresponding        |     | theoretical  |     |     | response  | of  an  |                           |     |     |     |     |
| -------------------- | --- | ------------ | --- | --- | --------- | ------- | ------------------------- | --- | --- | --- | --- |
| underdamped system.  |     |              |     |     |           |         | ?: damping coefficient.   |     |     |     |     |
•
| 2. Theoretical Framework  |     |     |     |     |     |     | •  ?: equivalent stiffness.   |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- |
2.1 Free Vibration and SDOF System
•  ?(?): dynamic displacement.
Free vibration corresponds to the oscillatory motion  When the damping ratio satisfies the condition:
| experienced  |       | by  a  | structural        |     | system  | after  being   |     |     |         |     |     |
| ------------ | ----- | ------ | ----------------- | --- | ------- | -------------- | --- | --- | ------- | --- | --- |
|              |       |        |                   |     |         |                |     |     | 0 < ? < | 1   |     |
| displaced    | from  |        | its  equilibrium  |     |         | position  and  |     |     |         |     |     |

| subsequently  |     | released  |     | without  | the  | continuous  |     |     |     |     |     |
| ------------- | --- | --------- | --- | -------- | ---- | ----------- | --- | --- | --- | --- | --- |
action of external forces. In this type of motion, the  the  system  exhibits  underdamped  behavior,
dynamic  response  depends  primarily  on  the  characterized by oscillations that gradually decay
physical properties  of the system, such as mass,  over time. The corresponding dynamic response is
stiffness, and damping.
expressed as:
| In  real  | systems,  |     | the  | vibration  |     | amplitude  |     |      |                 |     |     |
| --------- | --------- | --- | ---- | ---------- | --- | ---------- | --- | ---- | --------------- | --- | --- |
|           |           |     |      |            |     |            |     | ?(?) | = ???????sin?(? | ?)  |     |
?
progressively decreases due to energy dissipation

caused by internal material friction, air resistance,
|                                                       |     |          |     |            |     |                | where  ?represents  |     | the  initial                    | amplitude,  | ?is  the  |
| ----------------------------------------------------- | --- | -------- | --- | ---------- | --- | -------------- | ------------------- | --- | ------------------------------- | ----------- | --------- |
| and  mechanical                                       |     | losses,  |     | resulting  |     | in  a  damped  |                     |     |                                 |             |           |
|                                                       |     |          |     |            |     |                | damping ratio, ?    |     | is the natural frequency, and ? |             | is        |
| behavior characteristic of most civil and mechanical  |     |          |     |            |     |                |                     |     | ?                               |             | ?         |
the damped frequency of the system.
structures.

|     |     |     |     |     |     | where  | ? and  ? represent  |     | consecutive  | vibration  |     |
| --- | --- | --- | --- | --- | --- | ------ | ------------------- | --- | ------------ | ---------- | --- |
|     |     |     |     |     |     |        | ? ?+1               |     |              |            |     |
amplitudes.
Subsequently, the equivalent damping ratio of the
system is determined by:
?
|     |     |     |     |     |     |     | ? = |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
?4?2 +?2

Depending on the value of ?, dynamic systems may
|     |     |     |     |     |     | be classified as undamped, underdamped, critically  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- |
damped, or overdamped. In real structures, systems
Figure 2. Typical underdamped free vibration response.
generally exhibit underdamped behavior with low
levels of energy dissipation.
2.2 Dynamic Parameters and Damping
The  principal  parameters  used  to  describe  the  Table 1. Classification of dynamic systems according to
damping ratio.
| dynamic           | behavior    | of a vibrating  |             | system  are the  |     |                |     |     |                 |     |     |
| ----------------- | ----------- | --------------- | ----------- | ---------------- | --- | -------------- | --- | --- | --------------- | --- | --- |
| natural  period,  |             | natural         | frequency,  | and  damping     |     |                |     |     |                 |     |     |
|                   |             |                 |             |                  |     | Damping ratio  |     |     | Classification  |     |     |
| ratio.  These     | parameters  |                 | make        | it  possible     | to  |                |     |     |                 |     |     |
characterize both the oscillation rate and the energy  ? = 0  Undamped
dissipation capacity of the structural system.  0 < ? < 1  Underdamped
| The natural period (? |     | ) represents the time required  |     |     |     |     |        |                    |     |     |     |
| --------------------- | --- | ------------------------------- | --- | --- | --- | --- | ------ | ------------------ | --- | --- | --- |
|                       |     | ?                               |     |     |     |     | ? = 1  | Critically damped  |     |     |     |
to complete one cycle of free vibration, whereas the
|                      |     |                                 |     |     |     |     | ? > 1  |     | Overdamped  |     |     |
| -------------------- | --- | ------------------------------- | --- | --- | --- | --- | ------ | --- | ----------- | --- | --- |
| natural frequency (? |     | ) corresponds to the number of  |     |     |     |     |        |     |             |     |     |
?
oscillations occurring per unit time. Both quantities
|     |     |     |     |     |     | 2.3  Signal  | Processing  | Techniques  |     | (FFT  | and  |
| --- | --- | --- | --- | --- | --- | ------------ | ----------- | ----------- | --- | ----- | ---- |
are related by:
RDT)
1
|     |     | ?   | =   |     |     | In order to identify the dynamic properties of the  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- |
? ?
?
|     |     |     |     |     |     | experimental  | system, the signals recorded by the  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | ------------------------------------ | --- | --- | --- | --- |

|     |     |     |     |     |     | accelerometer  | were  | processed  | in  | both  the  | time  |
| --- | --- | --- | --- | --- | --- | -------------- | ----- | ---------- | --- | ---------- | ----- |
Likewise,  the  natural  angular  frequency  of  the  domain and the frequency domain using dynamic
| system is expressed as:  |     |     |     |     |     | signal analysis techniques.  |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
? = 2??   The Fast Fourier Transform (FFT) is a mathematical
|          |             | ?            | ?   |                |     |                                                      |            |          |     |           |      |
| -------- | ----------- | ------------ | --- | -------------- | --- | ---------------------------------------------------- | ---------- | -------- | --- | --------- | ---- |
|          |             |              |     |                |     | tool used to transform signals from the time domain  |            |          |     |           |      |
|          |             |              |     |                |     | into  the                                            | frequency  | domain,  |     | allowing  | the  |
| Damping  | represents  | the ability  |     | of the system  | to  |                                                      |            |          |     |           |      |
identification of the dominant frequencies present
dissipate energy during vibratory motion, causing a
in the vibratory response of the system.
| progressive  | reduction  |     | in  oscillation  | amplitude.  |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | ---------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Experimentally, damping can be estimated using the  In the FFT spectrum, the amplitude peaks represent
logarithmic  decrement  method,  which  relates  the frequencies  with the  highest energy  content,
successive  amplitudes  recorded  during  free  enabling  the  experimental  estimation  of  the
vibration.  dominant natural frequency of the structural system.
The logarithmic decrement is calculated as:  On  the  other  hand,  the  Random  Decrement
|     |     |     |     |     |     | Technique  | (RDT)  | was  employed  |     | to  | obtain  |
| --- | --- | --- | --- | --- | --- | ---------- | ------ | -------------- | --- | --- | ------- |
?
|     |     |     | ln?( 1 )  |     |     |             |                 |                      |     |     |      |
| --- | --- | --- | --------- | --- | --- | ----------- | --------------- | -------------------- | --- | --- | ---- |
|     |     | ? = |           |     |     | equivalent  | free-vibration  | signals by reducing  |     |     | the  |
?
2
experimental noise present in the original records.

The procedure consists of selecting multiple signal

segments  activated  by  a  trigger  condition,  primarily  considered,  since  it  represented  the
dominant vibration direction of the system during
| temporally  | aligning  |     | them,  | and  subsequently  |     |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ------ | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
the experimental tests.
| obtaining  | an averaged  |     | response representative  |     | of  |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the dominant dynamic behavior.
The system excitation was generated by applying a
As a result, the random components tend to cancel  manual initial displacement at the free end of the
|     |     |     |     |     |     | ruler  and  | subsequently  |     | releasing  |     | it  without  |     |
| --- | --- | --- | --- | --- | --- | ----------- | ------------- | --- | ---------- | --- | ------------ | --- |
out during the averaging process, while the coherent
|     |     |     |     |     |     | imposing additional forces,  |     |     |     | thereby producing  |     | a   |
| --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | ------------------ | --- | --- |
vibratory response of the system remains, yielding
characteristic damped free-vibration response.
| more  stable  | signals  | that  | are  | better  suited  | for  |     |     |     |     |     |     |     |
| ------------- | -------- | ----- | ---- | --------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
dynamic identification.
In order to evaluate experimental repeatability, five
|     |     |     |     |     |     | independent tests were  |     |     | conducted under similar  |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | ------------------------ | --- | --- | --- |
The combined application of FFT and RDT enabled
configuration and initial excitation conditions. The
| the  experimental  |     | validation  |     | of  the  dominant  |     |     |     |     |     |     |     |     |
| ------------------ | --- | ----------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
obtained records were exported in CSV format for
| frequency  | of  | the  system  |     | and  improved  | the  |                        |     |     |      |                   |     |     |
| ---------- | --- | ------------ | --- | -------------- | ---- | ---------------------- | --- | --- | ---- | ----------------- | --- | --- |
|            |     |              |     |                |      | subsequent processing  |     |     | and  | dynamic analysis  |     | in  |
interpretation  of  the  dynamic  response  recorded  Python using Visual Studio Code (VS Code).
during the free-vibration tests.
Table 2. Characteristics of the experimental setup.

|     |     |     |     |     |     |     | Parameter  |     |     | Description  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | ------------ | --- | --- |
3. EXPERIMENTAL METHODOLOGY
Structural
Metallic ruler
specimen
3.1 Experimental Setup
|                   |     |                   |     |                |     | Configuration  |     |     |     | Cantilever  |     |     |
| ----------------- | --- | ----------------- | --- | -------------- | --- | -------------- | --- | --- | --- | ----------- | --- | --- |
| The experimental  |     | system consisted  |     | of a metallic  |     |                |     |     |     |             |     |     |
Smartphone
Sensor
ruler arranged in a cantilever configuration, rigidly  accelerometer
fixed at one end in order to allow the development  Acquisition type  Free vibration
of free vibrations at the opposite end. A smartphone  Number of tests  5
was attached to the free end using adhesive tape,  Export format  CSV
| functioning simultaneously  |     |     | as an additional mass  |     |     |                  |     |     |                   |     |     |     |
| --------------------------- | --- | --- | ---------------------- | --- | --- | ---------------- | --- | --- | ----------------- | --- | --- | --- |
|                             |     |     |                        |     |     | Processing tool  |     |     | Python + VS Code  |     |     |     |
and as an acceleration acquisition sensor through
the accelerometer integrated into the device.
3.2 Signal Processing

|     |     |     |     |     |     | The  experimental  |     | records  |     | obtained  | from  | the  |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | -------- | --- | --------- | ----- | ---- |
smartphone accelerometer were exported in CSV
|     |     |     |     |     |     | format  | for  subsequent processing  |     |     |     | and  dynamic  |     |
| --- | --- | --- | --- | --- | --- | ------- | --------------------------- | --- | --- | --- | ------------- | --- |
analysis using Python in the Visual Studio Code
(VS Code) environment.
Initially, the signals were represented in the time
|     |     |     |     |     |     | domain  | in  order  | to  | identify  |     | the  interval  |     |
| --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | --------- | --- | -------------- | --- |
corresponding to the useful free-vibration response.
For this purpose, the initial and final portions of the
|     |     |     |     |     |     | signal associated  |     | with external disturbances and  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | ------------------------------- | --- | --- | --- | --- |

manual manipulation of the system were removed,
selecting only the segment representative of the
| Figure 3.  | Experimental setup of  |     |     | the free vibration  |     |     |     |     |     |     |     |     |
| ---------- | ---------------------- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
dominant dynamic behavior.
system.
Subsequently, the successive positive acceleration
| Data acquisition was  |     | performed  |     | using a  | mobile  |             |                      |     |     |                    |     |     |
| --------------------- | --- | ---------- | --- | -------- | ------- | ----------- | -------------------- | --- | --- | ------------------ | --- | --- |
|                       |     |            |     |          |         | peaks were  | identified in order  |     |     | to experimentally  |     |     |
accelerometer application, recording accelerations
calculate the natural period of the system through
along the X, Y, and Z axes. For the present study,
|                              |     |     |     |                |      | the time differences  |     | between consecutive peaks.  |     |     |     |     |
| ---------------------------- | --- | --- | --- | -------------- | ---- | --------------------- | --- | --------------------------- | --- | --- | --- | --- |
| the component corresponding  |     |     |     | to the Z-axis  | was  |                       |     |                             |     |     |     |     |

Based  on these values, the experimental natural  primarily considered, selecting the representative
frequency was determined.  free-vibration interval for each test.
The structural damping ratio was estimated using
the logarithmic decrement method, considering the
| progressive  |     | reduction  |     | of  | amplitudes  |     | recorded  |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | --- | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
during free vibration. In addition, the signals were
transformed into the frequency domain through the
| Fast  | Fourier  |     | Transform  |     | (FFT),  | allowing  | the  |     |     |     |     |     |     |     |
| ----- | -------- | --- | ---------- | --- | ------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
identification of the dominant frequency present in

the dynamic response.
Figure 4. Representative experimental free-vibration
| Additionally, the Random Decrement Technique  |      |          |          |             |             |            |       |     |     |     | signal.  |     |     |     |
| --------------------------------------------- | ---- | -------- | -------- | ----------- | ----------- | ---------- | ----- | --- | --- | --- | -------- | --- | --- | --- |
| (RDT)                                         | was  | applied  |          | to  obtain  | equivalent  |            | free- |     |     |     |          |     |     |     |
| vibration                                     |      | signals  | through  |             | the         | alignment  | and   |     |     |     |          |     |     |     |
4.2 Experimental Dynamic Parameters
| averaging  |     | of  segments  |     | activated  |     | by  a  | trigger  |     |     |     |     |     |     |     |
| ---------- | --- | ------------- | --- | ---------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
condition, significantly reducing the experimental
Based on the identification of successive positive
noise present in the original records.
acceleration peaks, the natural period of the system
|     |     |     |     |     |     |     |     | was  | experimentally calculated  |     |     | through the time  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------------------------- | --- | --- | ----------------- | --- | --- |
Finally,  the  experimentally  obtained  dynamic  differences  between  consecutive  peaks.
| parameters  |     | were  | compared  |     | with  | the theoretical  |     |                |     |      |          |            |     |      |
| ----------- | --- | ----- | --------- | --- | ----- | ---------------- | --- | -------------- | --- | ---- | -------- | ---------- | --- | ---- |
|             |     |       |           |     |       |                  |     | Subsequently,  |     | the  | natural  | frequency  |     | was  |
response corresponding to an underdamped SDOF
determined using the inverse relationship between
system.
frequency and period.
Table 3. Signal processing stages.  Table 4. Experimental dynamic parameters obtained.
|     |     | Stage  |     |     | Objective  |     |     |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fn
|     |                  |       |     |                     |               |     |     |     | Ensayo  | Tn (s)  |       | ?     | ?      |     |
| --- | ---------------- | ----- | --- | ------------------- | ------------- | --- | --- | --- | ------- | ------- | ----- | ----- | ------ | --- |
|     | Selection of     |       |     | Eliminate external  |               |     |     |     |         |         | (Hz)  |       |        |     |
|     | useful interval  |       |     |                     | disturbances  |     |     |     | 1       | 0.4     | 2.5   | 0.14  | 0.022  |     |
|     |                  | Peak  |     | Calculate natural   |               |     |     |     | 2       | 0.39    | 2.56  | 0.13  | 0.021  |     |
|     | identification   |       |     |                     | period        |     |     |     |         |         |       |       |        |     |
|     |                  |       |     |                     |               |     |     |     | 3       | 0.4     | 2.52  | 0.15  | 0.024  |     |
Logarithmic
Estimate damping
|     |     | decrement  |     |                    |     |     |     |     | 4   | 0.41  | 2.44  | 0.14  | 0.022  |     |
| --- | --- | ---------- | --- | ------------------ | --- | --- | --- | --- | --- | ----- | ----- | ----- | ------ | --- |
|     |     |            |     | Identify dominant  |     |     |     |     | 5   | 0.39  | 2.55  | 0.13  | 0.021  |     |
FFT
frequency
Reduce experimental  The structural damping ratio was estimated using
RDT
|     |     |     |     |     | noise  |     |     | the                    | logarithmic  |     | decrement                  | method,  | obtaining  |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | ---------------------- | ------------ | --- | -------------------------- | -------- | ---------- | --- |
|     |     |     |     |     |        |     |     | characteristic values  |              |     | of  an underdamped system  |          |            |     |
with low energy dissipation.
4. RESULTS
| 4.1 Experimental Signals  |     |     |     |     |     |     |     | 4.3 FFT and RDT Analysis  |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
The experimental signals were transformed into the
| Five  | experimental  |     |     | free-vibration  |     | tests  | were  |            |     |         |          |      |       |          |
| ----- | ------------- | --- | --- | --------------- | --- | ------ | ----- | ---------- | --- | ------- | -------- | ---- | ----- | -------- |
|       |               |     |     |                 |     |        |       | frequency  |     | domain  | through  | the  | Fast  | Fourier  |
conducted using a metallic ruler in a cantilever
Transform (FFT), identifying a dominant frequency
configuration and a smartphone as an acceleration
|     |     |     |     |     |     |     |     | close  | to  the  | experimentally  |     | calculated  |     | natural  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --------------- | --- | ----------- | --- | -------- |
sensor. The recorded signals exhibited a damped
frequency.
oscillatory behavior characteristic of underdamped
| systems,  |     | showing  | a   | progressive  |     | decrease  | in  |     |     |     |     |     |     |     |
| --------- | --- | -------- | --- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
amplitude over time.
| For        | the  | dynamic        | processing,  |     | the      | acceleration  |      |     |     |     |     |     |     |     |
| ---------- | ---- | -------------- | ------------ | --- | -------- | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| component  |      | corresponding  |              |     | to  the  | Z-axis        | was  |     |     |     |     |     |     |     |

5. DISCUSSION
The results obtained during the five experimental
tests allowed an adequate identification of the main
|     |     |     |     | dynamic         | properties  |           | of  | the  analyzed    | structural  |     |
| --- | --- | --- | --- | --------------- | ----------- | --------- | --- | ---------------- | ----------- | --- |
|     |     |     |     | system.         | The         | recorded  |     | signals          | exhibited   | a   |
|     |     |     |     | characteristic  |             | damped    |     | free  vibration  | behavior,   |     |

evidenced by the progressive decrease in amplitude
|     |     |     |     | and  the  | presence  |     | of  | clearly  defined  | periodic  |     |
| --- | --- | --- | --- | --------- | --------- | --- | --- | ----------------- | --------- | --- |
Figure 5. FFT spectrum corresponding to the
oscillations.
experimental test.
The time-domain analysis performed through the
Furthermore, the application of the Random Decrement
Technique (RDT) made it possible to obtain equivalent  identification  of  successive  peaks  allowed  the
free-vibration signals with a significant reduction in  experimental calculation of the natural period and
experimental noise, while preserving the periodicity and  natural frequency  of  the  system.  The  obtained
damped behavior of the system.  values  presented  low  dispersion  among  tests,
indicating adequate experimental repeatability and
a sufficiently stable structural configuration during
the development of the experiments.
Likewise, the damping values obtained through the
|     |     |     |     | logarithmic  |     | decrement  |     | method  | evidenced  | an  |
| --- | --- | --- | --- | ------------ | --- | ---------- | --- | ------- | ---------- | --- |
underdamped behavior of the experimental system,
|     |     |     |     | showing  | relatively  |     | low  | damping  | ratios.  | This  |
| --- | --- | --- | --- | -------- | ----------- | --- | ---- | -------- | -------- | ----- |
behavior is consistent with the physical nature of
Figure 6. Equivalent signal obtained using RDT.  the specimen used, since metallic rulers generally
exhibit low energy losses and reduced dissipation
| 4.4 Global Results  |     |     |     | during small-amplitude free vibrations.  |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
The results obtained showed adequate consistency  The  spectra  obtained  through  Fast  Fourier
among  the  five  experimental  tests,  with  low  Transform  (FFT)  showed  a  clearly  identifiable
dispersion observed in the natural frequency and  dominant frequency close to the natural frequency
damping  values.  The  agreement between  time- calculated  through  time-domain  analysis.  The
|                   |                 |                   |     | agreement  | between  |     | both  | methods  | validates  | the  |
| ----------------- | --------------- | ----------------- | --- | ---------- | -------- | --- | ----- | -------- | ---------- | ---- |
| domain analysis,  | FFT  analysis,  | and  the signals  |     |            |          |     |       |          |            |      |
obtained  using RDT  validates  the experimental  consistency of  the experimental processing  and
confirms the presence of a dominant vibration mode
stability of the system and the applicability of the
proposed SDOF model.  associated with the main dynamic behavior of the
system.
|     | Test  | FFT (Hz)  |     |            |     |              |     |            |            |     |
| --- | ----- | --------- | --- | ---------- | --- | ------------ | --- | ---------- | ---------- | --- |
|     |       |           |     | Regarding  |     | the  Random  |     | Decrement  | Technique  |     |
|     | 1     | 2.49      |     |            |     |              |     |            |            |     |
(RDT), the processed signals showed a significant
|     | 2   | 2.53  |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
reduction of experimental noise compared to the
3  2.52  original signals recorded by the accelerometer. The
|            | 4   | 2.5      |     | alignment and     |          | averaging  |                              | procedure  | of  multiple  |     |
| ---------- | --- | -------- | --- | ----------------- | -------- | ---------- | ---------------------------- | ---------- | ------------- | --- |
|            | 5   | 2.55     |     | segments allowed  |          |            | obtaining smoother and more  |            |               |     |
|            |     |          |     | stable            | dynamic  |            | responses                    | while      | adequately    |     |
| Parameter  |     | Average  |     |                   |          |            |                              |            |               |     |
preserving the periodicity and damped behavior of
|     | Tn (s)  | 0.398  |     |     |     |     |     |     |     |     |
| --- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
the system.
|     | fn (Hz)  | 2.514  |     |     |     |     |     |     |     |     |
| --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
FFT (Hz)  2.518  The similarity observed between the RDT signals
?  0.022  and  the  theoretical  response  expected  for  an
underdamped SDOF system demonstrates that the
Table 5. Global summary of dynamic parameters.  experimental  specimen  can  be  reasonably
represented through a simplified single-degree-of-

freedom  model.  This  approximation  is  valid  experimental  specimen,  showing  agreement
because  the  dynamic  behavior  was  mainly  between the theoretical response and the processed
dominated by a single vibration mode, which is  experimental signals.
| typical   | in  | simple  | low-complexity  |     | structural  |     |             |     |     |     |     |     |     |
| --------- | --- | ------- | --------------- | --- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
| systems.  |     |         |                 |     |             |     | REFERENCES  |     |     |     |     |     |     |
On the other hand, certain sources of experimental  Chopra,  A.  K.  (2017).  Dynamics of  structures:
uncertainty were identified, mainly associated with  Theory and applications to earthquake engineering
the use of low-cost sensors integrated into mobile
(5th ed.). Pearson Education.
| devices.                  | These  | include  |                          | inherent  | accelerometer  |     |     |     |     |     |     |     |     |
| ------------------------- | ------ | -------- | ------------------------ | --------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| noise, slight variations  |        |          | in the manually applied  |           |                |     |     |     |     |     |     |     |     |
Clough, R. W., & Penzien, J. (2003). Dynamics of
excitation  during  each  test,  possible  relative  structures (3rd ed.). Computers & Structures, Inc.
| movements      |     | between              | the  | smartphone  | and         | the  |     |     |     |     |     |     |     |
| -------------- | --- | -------------------- | ---- | ----------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| specimen, and  |     | limitations related  |      | to          | the device  |      |     |     |     |     |     |     |     |
Craig, R. R., & Kurdila, A. J. (2006). Fundamentals
| sampling  | frequency.  |     | However,  | despite  |     | these  |     |     |     |     |     |     |     |
| --------- | ----------- | --- | --------- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
of structural dynamics (2nd ed.). John Wiley &
limitations, the obtained results showed adequate
Sons.
coherence and stability among tests.
Ewins, D. J. (2000). Modal testing: Theory, practice
In general terms, the developed work demonstrates
and application (2nd ed.). Research Studies Press.
| that  smartphone-integrated  |     |     |     | sensors  | can  | be  |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
successfully used for educational and preliminary
Inman, D. J. (2014). Engineering vibration (4th ed.).
experimental applications in structural dynamics,
Pearson Education.
allowing the estimation of representative dynamic
parameters through accessible methodologies and
Matplotlib Development Team. (2025). Matplotlib
freely available computational tools.6.
documentation. https://matplotlib.org/
CONCLUSIONS
|     |     |     |     |     |     |     | NumPy  | Developers.  |     |     | (2025).  |     | NumPy  |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | --- | -------- | --- | ------ |
documentation. https://numpy.org/
| 1. The dynamic behavior of  |     |     |     | a  metallic ruler in  |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
cantilever configuration was successfully identified
|     |     |     |     |     |     |     | Oppenheim, A.  |     | V.,  | &  Schafer,  |     | R.  | W.  (2010).  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---- | ------------ | --- | --- | ------------ |
experimentally through free vibration tests using a
Discrete-time signal processing (3rd ed.). Pearson.
smartphone as an acceleration sensor.
|          |               |     |     |         |            |     | Pandas  | Development  |     | Team.  |     | (2025).  | Pandas  |
| -------- | ------------- | --- | --- | ------- | ---------- | --- | ------- | ------------ | --- | ------ | --- | -------- | ------- |
| 2.  The  | experimental  |     |     | system  | exhibited  | a   |         |              |     |        |     |          |         |
documentation. https://pandas.pydata.org/
characteristic underdamped behavior, evidenced by
| progressively  |     | decreasing  |     | oscillations  | and  | low  |         |           |     |              |     |          |         |
| -------------- | --- | ----------- | --- | ------------- | ---- | ---- | ------- | --------- | --- | ------------ | --- | -------- | ------- |
|                |     |             |     |               |      |      | Python  | Software  |     | Foundation.  |     | (2025).  | Python  |
damping ratios obtained during signal processing.
language reference. https://www.python.org/
3. Fast Fourier Transform (FFT) allowed the clear
Randall, R. B. (2011). Vibration-based condition
identification of the dominant frequency present in
|     |     |     |     |     |     |     | monitoring: Industrial, aerospace  |     |     |     |     | and automotive  |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --------------- | --- |
the recorded signals, obtaining values close to the
applications. John Wiley & Sons.
natural frequencies calculated through time-domain
| analysis,  | thereby  |     | validating  | the  | experimental  |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ----------- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
consistency of the results.  SciPy Community. (2025). SciPy documentation.
https://scipy.org/
| 4.  The  | Random  | Decrement  |     | Technique  |     | (RDT)  |     |     |     |     |     |     |     |
| -------- | ------- | ---------- | --- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
Smith, S. W. (1997). The scientist and engineer’s
allowed obtaining equivalent free vibration signals
|     |     |     |     |     |     |     | guide  | to  digital  |     | signal  | processing.  |     | California  |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | ------- | ------------ | --- | ----------- |
with significant reduction of experimental noise,
Technical Publishing.
| facilitating  | the  | interpretation  |     | of  the  | dominant  |     |     |     |     |     |     |     |     |
| ------------- | ---- | --------------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
dynamic behavior of the system.
|          |               |     |                           |        |             |     | Tamura, Y.,  |            | Suganuma, S.,  |            | &        | Hibi,  | K.  (1999).  |
| -------- | ------------- | --- | ------------------------- | ------ | ----------- | --- | ------------ | ---------- | -------------- | ---------- | -------- | ------ | ------------ |
|          |               |     |                           |        |             |     | Random       | decrement  |                | technique  |          | for    | damping      |
| 5.  The  | simplified    |     | single-degree-of-freedom  |        |             |     |              |            |                |            |          |        |              |
|          |               |     |                           |        |             |     | evaluation   | of         | structures.    |            | Journal  |        | of  Wind     |
| (SDOF)   | mathematical  |     |                           | model  | adequately  |     |              |            |                |            |          |        |              |
Engineering and Industrial Aerodynamics, 83(1–3),
| represented  |     | the  | dynamic  | response  | of  | the  |     |     |     |     |     |     |     |
| ------------ | --- | ---- | -------- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |

137–146. https://doi.org/10.1016/S0167- This appendix presents the main stages of the
6105(99)00068-5 computational processing performed on the
experimental signals using Python and Visual
Appendix Studio Code.
A. Experimental setup of the specimen
This appendix presents the photographic evidence
corresponding to the experimental setup used
during the free vibration tests.
Figure C1. Computational processing of experimental
signals using Python and Visual Studio Code.
Executed command: python analisis_fft.py
Figure A1. Experimental setup used during the free
vibration tests.
Appendix B. Experimental records
This appendix includes the original records
obtained during the five experimental tests,
corresponding to the acceleration signals exported
in CSV format.
Figure B1. Experimental records.
Appendix C. Signal processing
Figure C2. Terminal execution of python
analisis_fft.py for Test 3, taken as the reference case.

| Appendix  | D.  Experimental  |     | Code  and  |     |     | ?   |
| --------- | ----------------- | --- | ---------- | --- | --- | --- |
|           |                   |     |            |     | ? = |     |
Calculations
|     |     |     |     |     | ???? | +?? |
| --- | --- | --- | --- | --- | ---- | --- |
The calculations developed for the determination of

the dynamic parameters of the experimental system
?.???
| are presented below.  |     |     |     |     | ? =  |         |
| --------------------- | --- | --- | --- | --- | ---- | ------- |
|                       |     |     |     |     | ???? | +?.???? |
D.1 Natural Period Calculation

| The experimental natural period  |     |     | was determined  |     | ?=  | ?.????  |
| -------------------------------- | --- | --- | --------------- | --- | --- | ------- |
through the time differences between successive
| positive    | acceleration peaks  | recorded  | during free  |                       |     |     |
| ----------- | ------------------- | --------- | ------------ | --------------------- | --- | --- |
| vibration.  |                     |           |              | PYTHON CODE FRAGMENT  |     |     |
Tn = t2 - t1
|     | Peak  | Time (s)  |     |     |     |     |
| --- | ----- | --------- | --- | --- | --- | --- |
fn = 1 / Tn
|     | 1   | 2.10  |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- |
|     | 2   | 2.49  |     |     |     |     |
delta = np.log(x1/x2)
Tn = 2.49 - 2.10 = 0.39 s  zeta = delta / np.sqrt(4*np.pi**2 + delta**2)
| D.2 Natural Frequency Calculation  |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- | --- |

| The  natural                                        | frequency  | was  obtained  | using  the  |     |     |     |
| --------------------------------------------------- | ---------- | -------------- | ----------- | --- | --- | --- |
| inverse relationship between frequency and period.  |            |                |             |     |     |     |

?
|     |     | ? =   |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- |
? ?
|     |     | ?          |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- |
|     |     | ?          |     |     |     |     |
|     | ? = | = ?.?? Hz  |     |     |     |     |
?
?.??

D.3 Logarithmic Decrement Calculation

| The logarithmic decrement was  |             |           | calculated using  |     |     |     |
| ------------------------------ | ----------- | --------- | ----------------- | --- | --- | --- |
| successive                     | amplitudes  | recorded  | during  free      |     |     |     |
vibration.
?
???( ? )
? =
?
?

?.??
|     | ?= ???( | )= ?.???  |     |     |     |     |
| --- | ------- | --------- | --- | --- | --- | --- |
?.??

D.4 Damping Ratio Calculation
The equivalent damping ratio was determined using
the relationship between logarithmic decrement and
damped frequency.
