import pandas as pd
import matplotlib.pyplot as plt
import os
from PyQt5.QtWidgets import QMessageBox

def find_closest_value(series, value):
    #Find the value in series closest to 'value'.
    return min(series, key=lambda x: abs(x - value))

def extract_and_plot_data(video_path, frame_index, frame_rate, selected_columns, csv_files):

    timestamp = frame_index / frame_rate
    extracted_data = pd.DataFrame()
    directory = os.path.dirname(video_path)

    output_folder = "output_data"
    os.makedirs(output_folder, exist_ok=True)  # Ensure output folder exists if not it will create

    for file_path in csv_files:
        try:
            df = pd.read_csv(file_path)
            first_ts = df.loc[0, 'timestamp[s]']
            df['adjusted_timestamp'] = df['timestamp[s]'] - first_ts

            if timestamp in df['adjusted_timestamp'].values:
                out_df = df.loc[df['adjusted_timestamp'] == timestamp, selected_columns]
            else:
                closest = find_closest_value(df['adjusted_timestamp'], timestamp)
                out_df = df.loc[df['adjusted_timestamp'] == closest, selected_columns]

            if not out_df.empty:
                out_df.insert(0, 'filename', os.path.basename(file_path))
                extracted_data = pd.concat([extracted_data, out_df], ignore_index=True)

        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    if not extracted_data.empty:
        excel_path = os.path.join(output_folder, 'data.xlsx')
        plot_path = os.path.join(output_folder, 'plot_image.jpg')

        extracted_data.to_excel(excel_path, index=False)

        plt.clf()
        for col in selected_columns:
            plt.scatter(extracted_data['filename'], extracted_data[col], label=col)

        plt.xlabel('Filename')
        plt.ylabel('Value')
        plt.title('Scatter Plot')
        plt.xticks(rotation=90)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(plot_path, bbox_inches='tight')
        show_success(f"✅ Data saved successfully to:\n{os.path.abspath(output_folder)}")

def show_warning(message="No video file chosen."):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(message)
    msg.setWindowTitle("Error")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

def show_success(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(message)
    msg.setWindowTitle("Success")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()
