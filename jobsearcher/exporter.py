import csv

def save_to_file(jobs):
    print("execute method save_to_file(), len: ", len(jobs))
    file = open("jobs.csv", mode="w", encoding="utf-8-sig", newline="")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])

    for index, job in enumerate(jobs):
        writer.writerow(list(job.values()))