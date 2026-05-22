from pandas.core.frame import DataFrame
import pandas as pd
import regex


def read_csv(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath, encoding="utf-8")

def has_letters(value):
    return bool(regex.search(r"\p{L}", str(value)))

def has_diacritics(value):
    latvian_diacritics = "ĀāĒēĪīŪūČčĢģĶķĻļŅņŠšŽžŖŗ"
    return any(char in latvian_diacritics for char in str(value))

def clean_names(df: pd.DataFrame) -> pd.DataFrame:
    na_rows = df[df["Vardi"].isna()]
    print("Rows with missing names:")
    print(na_rows)
    # Drop NA
    df: DataFrame = df.dropna(subset=["Vardi"])

    # Drop rows that don't have letters, e.g. "-"
    df["has_letters"] = df["Vardi"].apply(has_letters)

    print("Rows with no letters:")
    print(df[~df["has_letters"]])

    return df[df["has_letters"]]


def main():
    df = read_csv("vardi-20260101.csv")
    df = clean_names(df)
    df["has_diacritics"] = df["Vardi"].apply(has_diacritics)
    print(df[df["has_diacritics"]])
    print(df[~df["has_diacritics"]])

    with_diacritics = df.loc[df["has_diacritics"], "Skaits"].sum()
    without_diacritics = df.loc[~df["has_diacritics"], "Skaits"].sum()

    print(f"With diacritics: {with_diacritics}")
    print(f"Without diacritics: {without_diacritics}")

    total = df["Skaits"].sum()
    print(total)
    print(with_diacritics + without_diacritics)

    diacritics_percentage = with_diacritics/total*100
    print(diacritics_percentage)


if __name__ == "__main__":
    main()
 