from src.preprocessing import main as preprocess_main
from src.outlier_detection import detect_and_plot_outliers

def main():
    # 1️⃣ Préprocessing
    print("✅ Préprocessing des données...")
    preprocess_main()  # Télécharge, filtre et sauvegarde processed.csv

    # 2️⃣ Détection des outliers et génération du graphique
    print("✅ Détection d'outliers et génération du graphique...")
    ts_pred, ts_global, ts1 = detect_and_plot_outliers(
        csv_path="data/processed.csv",
        year=2019,
        wind_length=60,
        shift_step=40,
        tau=8,
        output_path="docs/outliers.png"
    )

    print("🎉 Tout est terminé ! Le graphique est sauvegardé dans docs/outliers.png")

if __name__ == "__main__":
    main()
