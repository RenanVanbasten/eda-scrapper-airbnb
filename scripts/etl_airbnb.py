import pandas as pd

def extract(path='data/airbnb_listings.csv'):
    return pd.read_csv(path)

def transform(df):
    df = df.copy()

    df['nota_avaliacao'] = df['avaliacao'].str.split(' ').str[0].str.replace(',', '.').astype(float)
    df['qtd_avaliacao'] = df['avaliacao'].str.split(' ').str[1].astype(int)

    df['preco_noite'] = (
        df['preco_noite']
        .str.replace('R$', '', regex=False)
        .str.replace('.', '_', regex=False)
        .astype(float)
    )

    return df

def load(df, path='data/airbnb_listings_limpas.csv'):
    df.to_csv(path, index=False)

def main():
    df_raw = extract()
    df_clean = transform(df_raw)
    load(df_clean)

if __name__ == '__main__':
    main()
