import kagglehub
import pandas as pd

def main():
    # Download dataset
    path = kagglehub.dataset_download("aturner374/eighty-years-of-canadian-climate-data")
    data = pd.read_csv(path + "/Canadian_climate_history.csv")
    
    # Montreal temperatures
    w = data.loc[7305:, ['LOCAL_DATE', 'MEAN_TEMPERATURE_MONTREAL']].copy()
    w['date'] = pd.to_datetime(w['LOCAL_DATE'])
    w['year'] = w['date'].dt.year
    w['month'] = w['date'].dt.month
    w['day'] = w['date'].dt.day
    
    # Keep 2000-2019
    w = w[(w['year'] >= 2000) & (w['year'] <= 2020)]
    
    # Fill missing values
    w['MEAN_TEMPERATURE_MONTREAL'] = w['MEAN_TEMPERATURE_MONTREAL'].interpolate(method='linear')
    
    # Save processed data
    w.to_csv("data/processed.csv", index=False)
    print("Processed data saved to data/processed.csv")

if __name__ == "__main__":
    main()
