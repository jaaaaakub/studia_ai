import os
import pandas as pd
from pprint import pp


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def basic_report(df: pd.DataFrame) -> dict:
    return {
        'rows': len(df),
        'columns': len(df.columns),
        'missing_values': int(df.isna().sum().sum()),
        'target_distribution': df['target'].value_counts().to_dict() if 'target' in df.columns else {}
    }


def extended_report(df: pd.DataFrame) -> dict:
    numeric_cols = df.select_dtypes(include='number')
    categorical_cols = df.select_dtypes(exclude='number')

    report = {
        'rows': len(df),
        'columns': len(df.columns),
        'missing_values': int(df.isna().sum().sum()),
        'dtypes': df.dtypes.astype(str).to_dict(),
        'numeric_summary': {},
        'categorical_summary': {},
    }

    # statystyki numeryczne
    for col in numeric_cols.columns:
        report['numeric_summary'][col] = {
            'mean': float(df[col].mean()),
            'min': float(df[col].min()),
            'max': float(df[col].max()),
        }

    # kolumny kategoryczne
    for col in categorical_cols.columns:
        report['categorical_summary'][col] = {
            'unique_values': int(df[col].nunique())
        }

    # target
    if 'target' in df.columns:
        report['target_distribution'] = df['target'].value_counts().to_dict()

    return report

def safe_load_data(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f'File not found: {path}')

    df = pd.read_csv(path)

    if df.empty:
        raise ValueError('DataFrame is empty')

    return df


if __name__ == '__main__':
    url = 'data/heart.csv'
    data = safe_load_data(url)
    pp(extended_report(data))
