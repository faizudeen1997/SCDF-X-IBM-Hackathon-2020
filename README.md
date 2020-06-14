# SCDF X IBM Lifesavers’ Innovation Challenge: Call for Code 2020

## Table of Contents
### 1. [About Us](#about-us)
### 2. [Problem Statement](#problem-statement)
### 3. [Pitch Video](#pitch-video)
### 4. [Project Architecture](#project-architecture)
### 5. [Detailed Solutions](#detailed-solutions)
### 6. [Tools Used](#tools-used)

## About Us 
We are the **circodeBreakers**! We are a team of NUS undergradutaes from various disciplines. 
Let us introduce ourselves!

**Amir Azhar** *Year 3 Computer Engineering Major*
</br>
**Md Faizudeen** *Year 3 Chemical Engineering Major*
</br>
**Nur Aisyah Lyana** *Year 3 Double Major in Global Studies and Malay Studies*

So as you can probably tell from our team name, we were a bunch of bored kids stuck at home during the Circuit-Breaker and thought that it was a good idea to try something new, that is the SCDF-X-IBM Hackathon. 

A very good idea indeed.

Within 48 hours, we've come up with a project solution called ohChute! that tackles the large rubbish chute fires that consistently make up the bulk of the reported residential fires in Singapore for many years. Please read on!

## Problem Statement 
This is the problem statement that our group aims to tackle:

##### INTEGRATING WITH A SMART ENVIRONMENT

Infrastructure is getting “smart”, with sensors and Internet of things (IoT) increasingly embedded in the built environment (e.g. Punggol Digital District). How might we leverage a network of smart infrastructure in the built environment to make better and more timely sense of emergency incidents (e.g. detection of fires developing, building collapses, falls, road traffic accidents etc.) and to trigger early intervention measures, without the need to activate precious emergency resources?

##### The Problem at a Glance

According to the available fire statistics from the National Fire and Civil Emergency Preparedness Council (NFEC), rubbish chute fires have consistently formed the bulk of all fires (more than 50%) received by the SCDF from 2004 to 2015. Even in a recent news article reported by The Straits Times (Dec 12, 2018), rubbish chute fires still constitute 1 in 2 of residential fires.

Rubbish chute fires are considered minor cases by the SCDF since the fires have a small risk of spreading and can be easily contained by members of the public.

Yet, 

##### 1. SCDF still receives many calls from the public on the 995 emergency hotline, which is already often busy due to medical emergencies, and
##### 2. SCDF continues to activate its precious emergency resources by physically dispatching a fire vehicle (typically the Red Rhino) and a team of 4 firefighters to assess the situation on-the-ground as well as to record details of such events to identify hotspots of rubbish chute fire cases. 

As seen from the above, rubbish chute fires cause a strain on precious emergency resources such as the available call operators and firefighting vehicles which could be better used for more serious emergencies. Furthermore, with an increasingly aging population, the number of available firefighters in the future will be significantly reduced. Thus, it is even more crucial to delegate limited manpower resources to respond to critical emergencies.

Before we address the above mentioned problems, we first analyse the current existing solutions and leverage on the existing smart environment infrastructures before proposing solutions.

##### Analysing existing solutions
We have also identified SCDF’s existing solutions (using the datasets on NFEC’s website) and their areas for improvement:

1. In 2006, automatic sprinklers were installed within some rubbish chutes in some blocks in Jurong West. Problems with this existing solution: 
- High installation costs 
- The moist environment within the chutes corroded the heat detectors, rendering them ineffective
- Promotes bacterial growth 
- The discarded water makes the rubbish heavy and inconvenient for the garbage collectors

2. In 2011, buttons to activate the chute flushing system were installed in the common areas of some blocks in Tanjong Pagar GRC, so residents could press them to release water down the chute if a fire broke out. Problems with this existing solution: 
- High false alarms
- High water wastage due to misuse of pressed buttons despite no rubbish chute fires
- Promotes Bacterial growth
 
## Pitch Video

## Project Architecture
The following image demonstrates the architecture used in this project

![Architecture](images/projectarchitecture.jpg)

## Detailed Solutions
The detailed solution can be found [here](Detailed-Solution.md).

## Tools Used 
In the development of *ohChute!*, we have made use of the following services from IBM:

1. Node-RED
2. Cloud Foundry
3. Watson Visual Recognition
