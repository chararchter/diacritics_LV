from pandas.core.frame import DataFrame
import pandas as pd
import regex


def read_csv(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath, encoding="utf-8")

def has_letters(value: str) -> bool:
    """Return True if the value contains at least one Unicode letter."""
    return bool(regex.search(r"\p{L}", str(value)))

def has_diacritics(value: str) -> bool:
    """Return True if the value contains any Latvian diacritic character."""
    latvian_diacritics = "ĀāĒēĪīŪūČčĢģĶķĻļŅņŠšŽžŖŗ"
    return any(char in latvian_diacritics for char in str(value))

def clean_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows with missing or letter-free names.
    Returns the cleaned DataFrame with additional has_letters column (TODO: remove has_letters)
    """

    # Drop NA
    df: DataFrame = df.dropna(subset=["Vardi"])

    # Drop rows that don't have letters, e.g. "-"
    df["has_letters"] = df["Vardi"].apply(has_letters)

    return df[df["has_letters"]]


def compute_diacritics_percentage(filepath: str) -> float:
    df = read_csv(filepath)
    df = clean_names(df)
    df["has_diacritics"] = df["Vardi"].apply(has_diacritics)

    with_diacritics = df.loc[df["has_diacritics"], "Skaits"].sum()
    total = df["Skaits"].sum()

    return with_diacritics/total*100


def main():
    x = compute_diacritics_percentage("vardi-20260101.csv")
    print(x)


if __name__ == "__main__":
    main()
 