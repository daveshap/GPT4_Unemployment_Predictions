# Job Displacement Risk Due to AI

This repository contains data and scripts used to forecast job displacement risk due to the rise of AI. The data was
generated by a Python script that reads YAML files containing job statistics and uses an AI model to estimate the
percentage of work activities that can be automated and the intrinsic technological vulnerability of each job.

## Data Description

The data is stored in YAML files, one for each job. Each file contains the following fields:

- `OCC_CODE`: The occupation code.
- `OCC_TITLE`: The job title.
- `TOT_EMP`: The total employment for the job in 2022.
- `dexterity`: The estimated mean percentage of work activities that require high dexterity physical contact.
- `solo`: The estimated mean percentage of work activities that can be done solo in front of a computer.
- `group`: The estimated mean percentage of work activities that require group collaboration and communication.
- `vulnerability`: The estimated risk of job displacement due to no intrinsic need for humans.
- `explanation`: A natural language explanation of the above numbers and forecast.
- `Jobs Lost`: The estimated number of jobs that could be lost due to automation.
- `Jobs Remaining`: The estimated number of jobs that would remain after automation.

## Methodology

The Python script reads each YAML file and uses the `TOT_EMP` field to convert it to a float. It then uses an AI model
to estimate the `dexterity`, `solo`, and `group` fields, which represent the mean percentage of work activities broken
down into several categories. The `vulnerability` field is estimated based on the intrinsic need for humans in the job.
The `Jobs Lost` and `Jobs Remaining` fields are calculated based on these estimates.

## Interpreting the Data

The `dexterity`, `solo`, and `group` fields represent the estimated mean percentage of work activities that fall into
each category. A higher value in the `dexterity` field means that a larger percentage of the job's activities require
high dexterity physical contact, which is difficult to automate. A higher value in the `solo` field means that a larger
percentage of the job's activities can be done solo in front of a computer, which is easy to automate. A higher value inthe `group` field means that a larger percentage of the job's activities require group collaboration and communication,
which is also difficult to automate.

The `vulnerability` field represents the estimated risk of job displacement due to no intrinsic need for humans. A
higher value means that a larger percentage of the job's activities could be automated, leading to job displacement.

The `Jobs Lost` and `Jobs Remaining` fields represent the estimated number of jobs that could be lost or would remain
after automation, respectively. These fields are calculated based on the `TOT_EMP`, `solo`, and `vulnerability` fields.

The `explanation` field provides a natural language explanation of the above numbers and forecast. This field can be
used to understand the reasoning behind the estimates and the potential impact of automation on the job.