from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pmdarima.arima import auto_arima
from statsmodels.tsa.stattools import adfuller

def detect_and_plot_outliers(csv_path="data/processed.csv",
                             year=2019,
                             wind_length=60,
                             shift_step=40,
                             tau=8,
                             output_path="docs/outliers.png"):
    """Détecte les outliers par fenêtres glissantes vs ARIMA global et sauvegarde un plot."""
    
    # Lecture CSV et filtrage année 2019
    w = pd.read_csv(csv_path)
    w1 = w[w['year'] == year].copy()
    ts1 = w1[['MEAN_TEMPERATURE_MONTREAL', 'date']].copy()
    ts1['date'] = pd.to_datetime(ts1['date'])
    ts1.set_index('date', inplace=True)

    # Fenêtres glissantes
    windows = [ts1[start:start + wind_length] for start in range(0, len(ts1) - wind_length + 1, shift_step)]
    ts_pred = ts1.copy()
    for i in range(len(windows)):
        ts_pred[f'predicted_window_{i}'] = np.nan
        ts_pred[f'outlier_{i}'] = False

    for i, window in enumerate(windows):
        window_copy = window.copy()
        d = 0
        result = adfuller(window_copy['MEAN_TEMPERATURE_MONTREAL'])
        while result[1] > 0.05:
            window_copy = window_copy.diff().dropna()
            result = adfuller(window_copy['MEAN_TEMPERATURE_MONTREAL'])
            d += 1
        model = auto_arima(window, d=d, seasonal=False, stepwise=True, trace=False)
        predicted_in_sample = pd.Series(model.predict_in_sample(), index=window.index)
        ts_pred.loc[window.index, f'predicted_window_{i}'] = predicted_in_sample
        ts_pred.loc[window.index, f'outlier_{i}'] = np.abs(window['MEAN_TEMPERATURE_MONTREAL'] - predicted_in_sample) > tau

    outlier_cols = [c for c in ts_pred.columns if c.startswith('outlier_')]
    ts_pred['is_outlier'] = ts_pred[outlier_cols].any(axis=1)

    # ARIMA global
    ts_global = ts1.copy()
    model_global = auto_arima(ts_global['MEAN_TEMPERATURE_MONTREAL'], seasonal=False, stepwise=True, trace=False)
    pred_global = pd.Series(model_global.predict_in_sample(), index=ts_global.index)
    ts_global['predicted'] = pred_global
    ts_global['outlier'] = np.abs(ts_global['MEAN_TEMPERATURE_MONTREAL'] - pred_global) > tau

    # Plot
    plt.figure(figsize=(14, 6))
    plt.plot(ts1.index, ts1['MEAN_TEMPERATURE_MONTREAL'], color='grey', label='Température moyenne')
    out_windows = ts_pred[ts_pred['is_outlier']]
    plt.scatter(out_windows.index, out_windows['MEAN_TEMPERATURE_MONTREAL'], color='red',
                label='Outliers fenêtres glissantes', marker='o', s=50, alpha=0.7)
    out_global = ts_global[ts_global['outlier']]
    plt.scatter(out_global.index, out_global['MEAN_TEMPERATURE_MONTREAL'], color='purple',
                label='Outliers ARIMA global', marker='x', s=50, alpha=0.7)
    common_idx = out_windows.index.intersection(out_global.index)
    plt.scatter(common_idx, ts1.loc[common_idx, 'MEAN_TEMPERATURE_MONTREAL'],
                color='orange', label='Outliers communs', marker='D', s=60, alpha=0.9)
    plt.title('Outliers détectés : Fenêtres glissantes vs ARIMA global')
    plt.xlabel('Date')
    plt.ylabel('Température moyenne quotidienne (°C)')
    plt.legend()
    plt.tight_layout()

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_file)
    print(f"Graphique sauvegardé dans {output_file}")

    return ts_pred, ts_global, ts1


# --------------------------
# CLI minimale
# --------------------------
if __name__ == "__main__":
    print(f"Détection d'outliers pour l'année en cours...")
    detect_and_plot_outliers(csv_path="data/processed.csv",
                             year=2019,
                             wind_length=60,
                             shift_step=40,
                             tau=6,
                             output_path="docs/outliers.png")
    print("Graphique généré et sauvegardé avec succès !")
