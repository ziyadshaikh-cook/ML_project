import os
import sys
import pandas as pd
import numpy as np
from scipy.stats import ks_2samp
from src.ML_project.logger import logging
from src.ML_project.exception import CustomException


class ModelMonitoring:
    def __init__(self, reference_data_path: str, threshold: float = 0.05):
        """
        reference_data_path : path to the training data (used as baseline)
        threshold           : p-value cutoff for drift detection (default 0.05)
        """
        try:
            self.threshold = threshold
            self.reference_data = pd.read_csv(reference_data_path)
            logging.info(f"Reference data loaded from {reference_data_path}")
        except Exception as e:
            raise CustomException(e, sys)

    def detect_drift(self, new_data: pd.DataFrame) -> dict:
        """
        Compares new_data against reference_data column by column.
        Uses the Kolmogorov-Smirnov test for numerical columns.
        Returns a dict with drift status for each column.
        """
        try:
            logging.info("Starting data drift detection")
            drift_report = {}

            numerical_columns = ["reading score", "writing score", "math score"]

            for column in numerical_columns:
                if column not in self.reference_data.columns:
                    continue
                if column not in new_data.columns:
                    continue

                reference_col = self.reference_data[column].dropna()
                new_col = new_data[column].dropna()

                # KS test: if p-value < threshold, distributions are different = drift
                ks_stat, p_value = ks_2samp(reference_col, new_col)

                drift_detected = p_value < self.threshold

                drift_report[column] = {
                    "ks_statistic": round(ks_stat, 4),
                    "p_value": round(p_value, 4),
                    "drift_detected": drift_detected
                }

                if drift_detected:
                    logging.warning(
                        f"DRIFT DETECTED in '{column}': "
                        f"KS={ks_stat:.4f}, p={p_value:.4f}"
                    )
                else:
                    logging.info(
                        f"No drift in '{column}': "
                        f"KS={ks_stat:.4f}, p={p_value:.4f}"
                    )

            logging.info("Drift detection complete")
            return drift_report

        except Exception as e:
            raise CustomException(e, sys)

    def print_report(self, drift_report: dict):
        """Prints a clean summary of the drift report to the console."""
        print("\n========== DATA DRIFT REPORT ==========")
        for column, stats in drift_report.items():
            status = "⚠️  DRIFT DETECTED" if stats["drift_detected"] else "✅ No Drift"
            print(f"  {column:20s} | KS: {stats['ks_statistic']:.4f} | "
                  f"p-value: {stats['p_value']:.4f} | {status}")
        print("=======================================\n")