import pandas as pd


def main_loop(df):
    emails = []
    for index, row in df.iterrows():
        # first last
        emails.append(
            "".join([row["first_name"], row["last_name"], "@", row["company"], ".com"])
        )
        # first.last
        emails.append(
            "".join(
                [row["first_name"], ".", row["last_name"], "@", row["company"], ".com"]
            )
        )
        # firstletter last
        emails.append(
            "".join(
                [
                    row["first_name"][0],
                    row["last_name"],
                    "@",
                    row["company"],
                    ".com",
                ]
            )
        )
        # firstletter.last
        emails.append(
            "".join(
                [
                    row["first_name"][0],
                    ".",
                    row["last_name"],
                    "@",
                    row["company"],
                    ".com",
                ]
            )
        )
    return emails


def main():
    print("*   " * 5 + "reading in linkedin.csv..." + "   *" * 5)
    df = pd.read_csv("linkedin.csv")

    print("*   " * 5 + "cleaning the data..." + "   *" * 6)
    df[["first_name", "last_name"]] = (
        df["full_name"]
        .loc[df["full_name"].str.split().str.len() == 2]
        .str.split(expand=True)
    )
    df["company"] = df["company"].str.replace(" ", "")

    # iterate over dataframe, construct email list
    email_list = main_loop(df=df)
    print("*   " * 5 + "creating email list..." + "   *" * 6)

    # output emails to text file
    output_file = open("output.txt", "w")
    for email in email_list:
        print(email)
        output_file.write(email)
        output_file.write("\n")
    output_file.close()


if __name__ == "__main__":
    main()
