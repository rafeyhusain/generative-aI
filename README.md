# Introduction
Write a solution using Generative AI technologies.

## Problem

Create a page where users can upload a text file and email address.

The system will run the following 2 Generative AI Prompts, and the response from the prompts will be sent to the user's email.

## Prompts:

1. **Prompt:** Based on the meeting transcription, please provide a 100-word summary of the meeting.

2. **Prompt:** Based on the meeting transcription, please provide the action item table, with the action owner and deadlines.

## Solution

To achieve this task, you can use the Flask web framework for the web application and the OpenAI GPT-3.5 for the generative prompts. Additionally, you'll need to use an email library to send emails. In this repo you will find code using Flask, OpenAI GPT-3.5, and the `smtplib` library for sending emails. Please note that you'll need to replace 'YOUR_OPENAI_API_KEY' and fill in the email configuration with your own details.

### Get Started

Remember to install the required packages before running the script by executing:

```bash
pip install Flask openai
```

Replace the placeholder values with your actual OpenAI API key, email credentials, and secret key.
