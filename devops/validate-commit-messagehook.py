#!/usr/bin/env python

import sys
import re

def validate_commit_message(commit_message):
    """This method validates the commit message

    Returns:
       True if valid and false otherwise
    """
    pattern = r'^(feature|defect)-\d{5}:'
    # fetch defect or feature id
    # send the request to azuredevops or jira with 
    # defect to verify if it actual defect or not
    return re.match(pattern,commit_message)



def main():
    """This function will read the file and call validate message

    exits with 0 if valid commit message otherwise exits with 1
    """
    commit_message_path = sys.argv[1]

    with open(commit_message_path, "r") as file:
        commit_message = file.read().strip()

    if validate_commit_message(commit_message):
        sys.exit(0)
    else:
        print(
            "commit message has to be in the form of <defect-id|feature-id>: <message>"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
