"""This module will have code to call jenkins job
"""

import os
import time
import requests


# get the value of Jenkins from environmental variable or set to default
JENKINS_URL = os.getenv("JENKINS_URL", "http://13.233.147.163:8080")
JENKINS_JOB = os.getenv("JENKINS_JOB", "deploy_app")
JENKINS_TOKEN = os.getenv("JENKINS_TOKEN", "11bf9a3647ab419e3b3a5998cca75dee60")
JENKINS_USER = os.getenv("JENKINS_USER", "qtdevops")


def trigger_jenkins_job():
    """This function will trigger jenkins job"""
    job_url = f"{JENKINS_URL}/job/{JENKINS_JOB}/build"
    response = requests.post(job_url, auth=(JENKINS_USER, JENKINS_TOKEN), timeout=30)
    if response.status_code == 201:
        print("Jenkins job triggered successfully")
    else:
        print(f"Failed to trigger Jenkins job {response.text}")


def get_last_build_number():
    """This function will get the last build number"""
    job_url = f"{JENKINS_URL}/job/{JENKINS_JOB}/lastBuild/api/json"
    response = requests.get(job_url, auth=(JENKINS_USER, JENKINS_TOKEN), timeout=30)
    if response.status_code == 200:
        return response.json()["number"]
    else:
        print(f"Failed to get last build number {response.text}")


def get_build_status(build_number):
    """This function will get the build status"""
    job_url = f"{JENKINS_URL}/job/{JENKINS_JOB}/{build_number}/api/json"
    response = requests.get(job_url, auth=(JENKINS_USER, JENKINS_TOKEN), timeout=30)
    if response.status_code == 200:
        return response.json()["result"]
    else:
        print(f"Failed to get build status {response.text}")


if __name__ == "__main__":
    trigger_jenkins_job()
    time.sleep(10)
    build_id = get_last_build_number()
    status = get_build_status(build_id)
    print(f"build id: {build_id} build_status: {status}")
