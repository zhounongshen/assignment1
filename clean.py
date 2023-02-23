import pandas as pd


def clean(contact_info_file,other_info_file):
    df1 = pd.read_csv(contact_info_file)
    df2 = pd.read_csv(other_info_file)
    df1.rename(columns={'respondent_id': 'id'}, inplace=True)
    df = pd.merge(df1, df2, on='id')  # same as pd.merge(df1, df2)
    df.dropna(inplace=True)
    df.drop(df[df['job'].str.contains('insurance')].index, inplace=True)
    df.drop(df[df['job'].str.contains('Insurance')].index, inplace=True)
    return df


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('contact_info_file', help='The path to the respondent_contact.csv file')
    parser.add_argument('other_info_file', help='The path to the respondent_other.csv file')
    parser.add_argument('output_file', help='The path to the output file')
    # contact_info_file(The path to the respondent_contact.csv file)
    # other_info_file(The path to the respondent_other.csv file)
    # output_file(The path to the output file)
    # python3 clean.py respondent_contact.csv respondent_other.csv cleaned.csv
    args = parser.parse_args()

    cleaned = clean(args.contact_info_file,args.other_info_file)
    cleaned.to_csv(args.output_file, index=False)
