import csv

def save_to_file(word):
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for index, char in enumerate(word):
        print("char, index: ", char, index)
        writer.writerow([index, char, 0, 0])
        # writer.writerow(list(job.values()))

    return 