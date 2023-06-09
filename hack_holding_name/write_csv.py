import csv
import sys
from time import sleep

import get_ideas


def main():
    """gpt-3.5-turboからアイデアをもらってcsvに書き込む"""
    count = int(sys.argv[1]) if len(sys.argv) == 2 else 1

    for _ in range(count):
        try:
            company_name, origin_of_the_company_name = get_ideas.run()
            write_to_file(company_name, origin_of_the_company_name)
        except Exception as e:
            print(e)
            continue
        # 分間3リクエストまで
        sleep(22)


def write_to_file(company_name, origin_of_the_company_name):
    """csvに書き込む"""
    with open("company-store.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([company_name, origin_of_the_company_name])


if __name__ == "__main__":
    main()
