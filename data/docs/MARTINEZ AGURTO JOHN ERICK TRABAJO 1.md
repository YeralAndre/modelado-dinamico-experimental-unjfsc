# you asked

transcribeme todo en MD para Codex

---

# gemini response

# Experimental Identification of Dynamic Parameters in a Free Vibration SDOF System Using FFT and RDT

**John Erick Martínez Agurto**  
*Universidad Nacional de Ingeniería*  
*Master's Program in Civil Engineering Sciences with Specialization in Structures*  
*Course: Structural Dynamics*  
*Lima - Perú, 2026*

---

## Abstract
This study presents the experimental identification of dynamic parameters of a simple structural system through free vibration testing. For this purpose, five experimental tests were conducted using an accelerometer integrated into a mobile device, recording the dynamic response of the specimen in the time domain. Based on the acquired records, signal processing was performed primarily considering the acceleration component along the vertical axis (Z-axis), selecting the representative free-vibration interval for the dynamic analysis.

Subsequently, the main system parameters, such as the natural period, natural frequency, and structural damping ratio, were determined using experimental methods including logarithmic decrement and successive peak analysis. In addition, the Fast Fourier Transform (FFT) was applied to identify the dominant frequency of the system in the frequency domain, while the Random Decrement Technique (RDT) was employed to obtain an equivalent free-vibration signal by reducing the influence of experimental noise.

The obtained results exhibit the characteristic behavior of an underdamped system, evidenced by the progressive decrease in vibration amplitude over time and the presence of a dominant frequency close to the experimentally calculated natural frequency. Finally, the experimental response was compared with the theoretical mathematical model of a Single Degree of Freedom (SDOF) system, showing good agreement between both approaches.

**Keywords:** Free vibration, Fast Fourier Transform (FFT), Random Decrement Technique (RDT), damping, natural frequency, SDOF system, structural dynamic

---

## 1. Introduction
Structural dynamics enables the analysis of the behavior of systems subjected to time-varying loads, such as mechanical vibrations, seismic actions, and external dynamic excitations. Among the principal parameters governing the vibratory response of a structure are the natural period, natural frequency, and damping ratio, which allow the dynamic behavior of the system to be characterized.

In the experimental field, the identification of these parameters generally requires specialized instrumentation. However, recent technological advances in mobile devices have enabled the use of accelerometers embedded in smartphones as accessible tools for the recording and preliminary analysis of structural vibrations.

In the present study, an experimental free-vibration test was carried out using a metallic ruler configured as a cantilever beam and a smartphone functioning as an acceleration sensor. The system was excited through an initial displacement followed by sudden release, while the dynamic response in the time domain was recorded using a mobile accelerometer application.

Based on the acquired signals, dynamic signal processing was performed mainly considering the vertical acceleration component (Z-axis). Subsequently, the natural period, natural frequency, and structural damping ratio were experimentally determined through time-domain analysis, logarithmic decrement, and Fast Fourier Transform (FFT). In addition, the Random Decrement Technique (RDT) was applied to obtain equivalent free-vibration signals with reduced experimental noise.

Finally, the dynamic behavior of the system was represented through a simplified Single Degree of Freedom (SDOF) mathematical model, comparing the experimentally obtained response with the corresponding theoretical response of an underdamped system.

---

## 2. Theoretical Framework

### 2.1 Free Vibration and SDOF System
Free vibration corresponds to the oscillatory motion experienced by a structural system after being displaced from its equilibrium position and subsequently released without the continuous action of external forces. In this type of motion, the dynamic response depends primarily on the physical properties of the system, such as mass, stiffness, and damping.

In real systems, the vibration amplitude progressively decreases due to energy dissipation caused by internal material friction, air resistance, and mechanical losses, resulting in a damped behavior characteristic of most civil and mechanical structures.

For simplified dynamic analysis, the experimental system can be idealized using a Single Degree of Freedom (SDOF) model, represented by an equivalent mass connected to an elastic element and a damping element. This model adequately describes the dominant behavior of simple vibrating systems through a single displacement coordinate.

> **Figure 1.** Conceptual SDOF system model. *(Composed of fixed support, spring $k$, damper $c$, mass $m$, and dynamic displacement coordinate $x(t)$)*.

The dynamic behavior of the damped system is represented by the following differential equation:

$$m\dot{x}(t)+c\dot{x}(t)+kx(t)=0$$

Where:
* $m$: equivalent mass of the system.
* $c$: damping coefficient.
* $k$: equivalent stiffness.
* $x(t)$: dynamic displacement.

When the damping ratio satisfies the condition:
$$0 < \zeta < 1$$

The system exhibits underdamped behavior, characterized by oscillations that gradually decay over time. The corresponding dynamic response is expressed as:
$$x(t)=Ae^{-\zeta\omega_{n}t}\sin(\omega_{d}t)$$

Where $A$ represents the initial amplitude, $\zeta$ is the damping ratio, $\omega_{n}$ the natural frequency, and $\omega_{d}$ the damped frequency of the system.

> **Figure 2.** Typical underdamped free vibration response. *(Showing progressive exponential decay envelope governed by $Ae^{-\zeta\omega_n t}$ and period $T_d$)*.

### 2.2 Dynamic Parameters and Damping
The principal parameters used to describe the dynamic behavior of a vibrating system are the natural period, natural frequency, and damping ratio. These parameters make it possible to characterize both the oscillation rate and the energy dissipation capacity of the structural system.

The natural period ($T_{n}$) represents the time required to complete one cycle of free vibration, whereas the natural frequency ($f_{n}$) corresponds to the number of oscillations occurring per unit time. Both quantities are related by:
$$f_{n}=\frac{1}{T_{n}}$$

Likewise, the natural angular frequency ($\omega_n$) of the system is expressed as:
$$\omega_{n}=2\pi f_{n}$$

Damping represents the ability of the system to dissipate energy during vibratory motion, causing a progressive reduction in oscillation amplitude. Experimentally, damping can be estimated using the logarithmic decrement method, which relates successive amplitudes recorded during free vibration.

The logarithmic decrement ($\delta$) is calculated as:
$$\delta = \ln\left(\frac{x_i}{x_{i+1}}\right)$$

Where $x_i$ and $x_{i+1}$ represent consecutive vibration amplitudes.

Subsequently, the equivalent damping ratio ($\zeta$) of the system is determined by:
$$\zeta=\frac{\delta}{\sqrt{4\pi^{2}+\delta^{2}}}$$

Depending on the value of $\zeta$, dynamic systems may be classified as undamped, underdamped, critically damped, or overdamped. In real structures, systems generally exhibit underdamped behavior with low levels of energy dissipation.

**Table 1.** Classification of dynamic systems according to damping ratio.
| Damping ratio | Classification |
| :--- | :--- |
| $\zeta=0$ | Undamped |
| $0<\zeta<1$ | Underdamped |
| $\zeta=1$ | Critically damped |
| $\zeta>1$ | Overdamped |

### 2.3 Signal Processing Techniques (FFT and RDT)
In order to identify the dynamic properties of the experimental system, the signals recorded by the accelerometer were processed in both the time domain and the frequency domain using dynamic signal analysis techniques.

The Fast Fourier Transform (FFT) is a mathematical tool used to transform signals from the time domain into the frequency domain, allowing the identification of the dominant frequencies present in the vibratory response of the system. In the FFT spectrum, the amplitude peaks represent the frequencies with the highest energy content, enabling the experimental estimation of the dominant natural frequency of the structural system.

On the other hand, the Random Decrement Technique (RDT) was employed to obtain equivalent free-vibration signals by reducing the experimental noise present in the original records. The procedure consists of selecting multiple signal segments activated by a trigger condition, temporally aligning them, and subsequently obtaining an averaged response representative of the dominant dynamic behavior.

As a result, the random components tend to cancel out during the averaging process, while the coherent vibratory response of the system remains, yielding more stable signals that are better suited for dynamic identification. The combined application of FFT and RDT enabled the experimental validation of the dominant frequency of the system and improved the interpretation of the dynamic response recorded during the free-vibration tests.

---

## 3. Experimental Methodology

### 3.1 Experimental Setup
The experimental system consisted of a metallic ruler arranged in a cantilever configuration, rigidly fixed at one end in order to allow the development of free vibrations at the opposite end. A smartphone was attached to the free end using adhesive tape, functioning simultaneously as an additional mass and as an acceleration acquisition sensor through the accelerometer integrated into the device.

> **Figure 3.** Experimental setup of the free vibration system. *(Photographic depiction of the cantilever configuration fixed to the support block)*.

Data acquisition was performed using a mobile accelerometer application, recording accelerations along the X, $Y$, and Z axes. For the present study, the component corresponding to the Z-axis was primarily considered, since it represented the dominant vibration direction of the system during the experimental tests.

The system excitation was generated by applying a manual initial displacement at the free end of the ruler and subsequently releasing it without imposing additional forces, thereby producing a characteristic damped free-vibration response.

In order to evaluate experimental repeatability, **5** independent tests were conducted under similar configuration and initial excitation conditions. The obtained records were exported in CSV format for subsequent processing and dynamic analysis in Python using Visual Studio Code (VS Code).

**Table 2.** Characteristics of the experimental setup.
| Parameter | Description |
| :--- | :--- |
| Structural specimen | Metallic ruler |
| Configuration | Cantilever |
| Sensor | Smartphone accelerometer |
| Acquisition type | Free vibration |
| Number of tests | **5** |
| Export format | CSV |
| Processing tool | Python + VS Code |

### 3.2 Signal Processing
The experimental records obtained from the smartphone accelerometer were exported in CSV format for subsequent processing and dynamic analysis using Python in the Visual Studio Code (VS Code) environment.

Initially, the signals were represented in the time domain in order to identify the interval corresponding to the useful free-vibration response. For this purpose, the initial and final portions of the signal associated with external disturbances and manual manipulation of the system were removed, selecting only the segment representative of the dominant dynamic behavior.

Subsequently, the successive positive acceleration peaks were identified in order to experimentally calculate the natural period of the system through the time differences between consecutive peaks. Based on these values, the experimental natural frequency was determined.

The structural damping ratio was estimated using the logarithmic decrement method, considering the progressive reduction of amplitudes recorded during free vibration. In addition, the signals were transformed into the frequency domain through the Fast Fourier Transform (FFT), allowing the identification of the dominant frequency present in the dynamic response.

Additionally, the Random Decrement Technique (RDT) was applied to obtain equivalent free-vibration signals through the alignment and averaging of segments activated by a trigger condition, significantly reducing the experimental noise present in the original records. Finally, the experimentally obtained dynamic parameters were compared with the theoretical response corresponding to an underdamped SDOF system.

**Table 3.** Signal processing stages.
| Stage | Objective |
| :--- | :--- |
| Selection of useful interval | Eliminate external disturbances |
| Peak identification | Calculate natural period |
| Logarithmic decrement | Estimate damping |
| FFT | Identify dominant frequency |
| RDT | Reduce experimental noise |

---

## 4. Results

### 4.1 Experimental Signals
**Five** experimental free-vibration tests were conducted using a metallic ruler in a cantilever configuration and a smartphone as an acceleration sensor. The recorded signals exhibited a damped oscillatory behavior characteristic of underdamped systems, showing a progressive decrease in amplitude over time. For the dynamic processing, the acceleration component corresponding to the Z-axis was primarily considered, selecting the representative free-vibration interval for each test.

> **Figure 4.** Representative experimental free-vibration signal. *(Plotting Acceleration Z $(\text{m/s}^2)$ versus Time $(\text{s})$ from **0** to **14** seconds)*.

### 4.2 Experimental Dynamic Parameters
Based on the identification of successive positive acceleration peaks, the natural period of the system was experimentally calculated through the time differences between consecutive peaks. Subsequently, the natural frequency was determined using the inverse relationship between frequency and period.

**Table 4.** Experimental dynamic parameters obtained.
| Test | $T_n \text{ (s)}$ | $f_n \text{ (Hz)}$ | $\delta$ | $\zeta$ |
| :---: | :---: | :---: | :---: | :---: |
| **1** | **0.4** | **2.5** | **0.14** | **0.022** |
| **2** | **0.39** | **2.56** | **0.13** | **0.021** |
| **3** | **0.4** | **2.52** | **0.15** | **0.024** |
| **4** | **0.41** | **2.44** | **0.14** | **0.022** |
| **5** | **0.39** | **2.55** | **0.13** | **0.021** |

The structural damping ratio was estimated using the logarithmic decrement method, obtaining characteristic values of an underdamped system with low energy dissipation.

<h3>4.3 FFT and RDT Analysis</h3>
The experimental signals were transformed into the frequency domain through the Fast Fourier Transform (FFT), identifying a dominant frequency close to the experimentally calculated natural frequency.

> **Figure 5.** FFT spectrum corresponding to the experimental test. *(Showing a sharp magnitude peak centered at **2.52 Hz**)*.

Furthermore, the application of the Random Decrement Technique (RDT) made it possible to obtain equivalent free-vibration signals with a significant reduction in experimental noise, while preserving the periodicity and damped behavior of the system.

> **Figure 6.** Equivalent signal obtained using RDT. *(Averaged stable harmonic decay signal across time)*.

### 4.4 Global Results
The results obtained showed adequate consistency among the **five** experimental tests, with low dispersion observed in the natural frequency and damping values. The agreement between time-domain analysis, FFT analysis, and the signals obtained using RDT validates the experimental stability of the system and the applicability of the proposed SDOF model.

**Table 5.** Global summary of dynamic parameters.
| Parameter | Value / Test Matrix |
| :--- | :--- |
| FFT Test **1** | **2.49 Hz** |
| FFT Test **2** | **2.53 Hz** |
| FFT Test **3** | **2.52 Hz** |
| FFT Test **4** | **2.5 Hz** |
| FFT Test **5** | **2.55 Hz** |
| **Average $T_n \text{ (s)}$** | **0.398** |
| **Average $f_n \text{ (Hz)}$** | **2.514** |
| **Average FFT (Hz)** | **2.518** |
| **Average $\zeta$** | **0.022** |

---

## 5. Discussion
The results obtained during the **five** experimental tests allowed an adequate identification of the main dynamic properties of the analyzed structural system. The recorded signals exhibited a characteristic damped free vibration behavior, evidenced by the progressive decrease in amplitude and the presence of clearly defined periodic oscillations.

The time-domain analysis performed through the identification of successive peaks allowed the experimental calculation of the natural period and natural frequency of the system. The obtained values presented low dispersion among tests, indicating adequate experimental repeatability and a sufficiently stable structural configuration during the development of the experiments.

Likewise, the damping values obtained through the logarithmic decrement method evidenced an underdamped behavior of the experimental system, showing relatively low damping ratios. This behavior is consistent with the physical nature of the specimen used, since metallic rulers generally exhibit low energy losses and reduced dissipation during small-amplitude free vibrations.

The spectra obtained through Fast Fourier Transform (FFT) showed a clearly identifiable dominant frequency close to the natural frequency calculated through time-domain analysis. The agreement between both methods validates the consistency of the experimental processing and confirms the presence of a dominant vibration mode associated with the main dynamic behavior of the system.

Regarding the Random Decrement Technique (RDT), the processed signals showed a significant reduction of experimental noise compared to the original signals recorded by the accelerometer. The alignment and averaging procedure of multiple segments allowed obtaining smoother and more stable dynamic responses while adequately preserving the periodicity and damped behavior of the system.

The similarity observed between the RDT signals and the theoretical response expected for an underdamped SDOF system demonstrates that the experimental specimen can be reasonably represented through a simplified single-degree-of-freedom model. This approximation is valid because the dynamic behavior was mainly dominated by a single vibration mode, which is typical in simple low-complexity structural systems.

On the other hand, certain sources of experimental uncertainty were identified, mainly associated with the use of low-cost sensors integrated into mobile devices. These include inherent accelerometer noise, slight variations in the manually applied excitation during each test, possible relative movements between the smartphone and the specimen, and limitations related to the device sampling frequency. However, despite these limitations, the obtained results showed adequate coherence and stability among tests.

In general terms, the developed work demonstrates that smartphone-integrated sensors can be successfully used for educational and preliminary experimental applications in structural dynamics, allowing the estimation of representative dynamic parameters through accessible methodologies and freely available computational tools.

---

## 6. Conclusions
1. The dynamic behavior of a metallic ruler in cantilever configuration was successfully identified experimentally through free vibration tests using a smartphone as an acceleration sensor.
2. The experimental system exhibited a characteristic underdamped behavior, evidenced by progressively decreasing oscillations and low damping ratios obtained during signal processing.
3. Fast Fourier Transform (FFT) allowed the clear identification of the dominant frequency present in the recorded signals, obtaining values close to the natural frequencies calculated through time-domain analysis, thereby validating the experimental consistency of the results.
4. The Random Decrement Technique (RDT) allowed obtaining equivalent free vibration signals with significant reduction of experimental noise, facilitating the interpretation of the dominant dynamic behavior of the system.
5. The simplified single-degree-of-freedom (SDOF) mathematical model adequately represented the dynamic response of the experimental specimen, showing agreement between the theoretical response and the processed experimental signals.

---

## References
* Chopra, A. K. (2017). *Dynamics of structures: Theory and applications to earthquake engineering* (5th ed.). Pearson Education.
* Clough, R. W., & Penzien, J. (2003). *Dynamics of structures* (3rd ed.). Computers & Structures, Inc.
* Craig, R. R., & Kurdila, A. J. (2006). *Fundamentals of structural dynamics* (2nd ed.). John Wiley & Sons.
* Ewins, D. J. (2000). *Modal testing: Theory, practice and application* (2nd ed.). Research Studies Press.
* Inman, D. J. (2014). *Engineering vibration* (4th ed.). Pearson Education.
* Matplotlib Development Team. (2025). *Matplotlib documentation*. [https://matplotlib.org/](https://matplotlib.org/).
* NumPy Developers. (2025). *NumPy documentation*. [https://numpy.org/](https://numpy.org/).
* Oppenheim, A. V., & Schafer, R. W. (2010). *Discrete-time signal processing* (3rd ed.). Pearson.
* Pandas Development Team. (2025). *Pandas documentation*. [https://pandas.pydata.org/](https://pandas.pydata.org/).
* Python Software Foundation. (2025). *Python language reference*. [https://www.python.org/](https://www.python.org/).
* Randall, R. B. (2011). *Vibration-based condition monitoring: Industrial, aerospace and automotive applications*. John Wiley & Sons.
* SciPy Community. (2025). *SciPy documentation*. [https://scipy.org/](https://scipy.org/).
* Smith, S. W. (1997). *The scientist and engineer's guide to digital signal processing*. California Technical Publishing.
* Tamura, Y., Suganuma, S., & Hibi, K. (1999). Random decrement technique for damping evaluation of structures. *Journal of Wind Engineering and Industrial Aerodynamics*, **83(1-3)**, **137-146**. [https://doi.org/10.1016/S0167-6105(99)00068-5](https://doi.org/10.1016/S0167-6105(99)00068-5)

---

## Appendix

### A. Experimental setup of the specimen
This appendix presents the photographic evidence corresponding to the experimental setup used during the free vibration tests.

> **Figure A1.** Experimental setup used during the free vibration tests. *(Shows the device secured to the rule projecting a measurement indicator scale)*.

### B. Experimental records
This appendix includes the original records obtained during the **five** experimental tests, corresponding to the acceleration signals exported in CSV format.

> **Figure B1.** Experimental records UI. *(Mobile application display showing logs from May 25, such as **20:46**, **20:45**, **20:44** and exported CSV listings)*.

### C. Signal processing
This appendix presents the main stages of the computational processing performed on the experimental signals using Python and Visual Studio Code.

```python
# COMPUTATIONAL PROCESSING OF EXPERIMENTAL SIGNALS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# ARCHIVO CSV
archivo = "Accelerometer(1).csv"
df = pd.read_csv(archivo)

# EXTRAER COLUMNAS
tiempo = df["seconds_elapsed"]
z = df["z"]

# RECORTAR
mask = (tiempo >= 1.5) & (tiempo <= 15)
tiempo = tiempo[mask]
z = z[mask]
```
> **Figure C1.** Computational processing script layout.

> **Figure C2.** Terminal execution plots interface. *(Displaying the stacked outputs of: Signal Experimental - Vibración Libre, Random Decrement Technique (RDT), and FFT - Espectro de Frecuencias)*.

### D. Experimental Code and Calculations
The calculations developed for the determination of the dynamic parameters of the experimental system are presented below.

#### D.1 Natural Period Calculation
The experimental natural period was determined through the time differences between successive positive acceleration peaks recorded during free vibration.
* Peak **1**: **2.10 s**
* Peak **2**: **2.49 s**

$$T_n = t_2 - t_1$$
$$T_n = 2.49 - 2.10 = 0.39 \text{ s}$$

#### D.2 Natural Frequency Calculation
The natural frequency was obtained using the inverse relationship between frequency and period.
$$f_{n}=\frac{1}{T_{n}}$$
$$f_{n}=\frac{1}{0.39}=2.56 \text{ Hz}$$

#### D.3 Logarithmic Decrement Calculation
The logarithmic decrement was calculated using successive amplitudes recorded during free vibration.
$$\delta=\ln\left(\frac{x_{1}}{x_{2}}\right)$$
$$\delta=\ln\left(\frac{0.82}{0.71}\right)=0.144$$

#### D.4 Damping Ratio Calculation
The equivalent damping ratio was determined using the relationship between logarithmic decrement and damped frequency.
$$\zeta=\frac{\delta}{\sqrt{4\pi^{2}+\delta^{2}}}$$
$$\zeta=\frac{0.144}{\sqrt{4\pi^{2}+0.144^{2}}}=0.0229$$

#### Python Code Snippet Mapping
```python
Tn = t2 - t1
fn = 1 / Tn
delta = np.log(x1 / x2)
zeta = delta / np.sqrt(4 * np.pi**2 + delta**2)
```