import argparse
import os
import sys
import openai

def main():
    if(os.environ.get('OPENAI_API_KEY') is None):
        sys.exit("Configure your OpenAI API Key. Export OPENAI_API_KEY environment variable your key to use Chai")

    parser = argparse.ArgumentParser(description='AI in your CLI')
    parser.add_argument('args', nargs='*', help="Query in natural language")
    args = parser.parse_args()
    response = queryGPT(args.args[0])
    print(response)


def queryGPT(userQuery):
    if(userQuery is None):
        sys.exit()

    prompt = "You are an expert in using command-line interfaces. Every time I ask you a question or share my problem when I'm stuck in the command line, you must respond with a Linux command. You're only allowed to respond with a command to help when I'm stuck. No formatting, just the command that one can copy-and-paste in the terminal"

#    client = OpenAI()
    completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": userQuery},
            ]
    )


    return completion["choices"][0]["message"]["content"]
