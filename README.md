## README

## Sustainability experiment tool

Aim of this project is to find out what kind of an impact an end-user can make on their energy and network consumption by selecting different resolution values for the streaming. During the experiment, a video-on-demand service will be streamed at a selected resolution for a certain period of time.

This application prompts the user basic settings of the experiment, and then records both energy and network data rate (tx) values on Linux before and after the experiment. The recorded values are used to calculate energy and network usage during the experiment.

### Background

Course project for DATA12004 Sustainability in Computer and Data Sciences II 2026 at University of Helsinki.

## System

Designed for Fuxiläppäri

    Linux Ubuntu 24.04.1 x86_64

# Running

## Prerequisites

Poetry version 2.0.0 or later installed

## Installation

Clone this repository

Run to install dependencies

    poetry install 

Enter virtual environment with 

    poetry env activate

Run to start

    python3 main.py

## Documentation
See the [documentation file](documentation.md).
