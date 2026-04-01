import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_chart(csv_file="benchmark_stats.csv"):
    try:
        df = pd.read_csv(csv_file)
        
        avg_results = df.groupby('script').mean().reset_index()
        
        avg_results = avg_results.sort_values('elapsed_time', ascending=False)

        scripts = avg_results['script']
        times = avg_results['elapsed_time']
        
        plt.style.use('seaborn-v0_8-muted')
        fig, ax1 = plt.subplots(figsize=(12, 7))

        bars = ax1.bar(scripts, times, color='skyblue', alpha=0.7, label='Elapsed Time (s)')
        ax1.set_ylabel('seconds', color='blue', fontsize=12)
        ax1.set_title('perf', fontsize=14)
        plt.xticks(rotation=15)

        for bar in bars:
            height = bar.get_height()
            ax1.annotate(f'{height:.3f}s',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3), 
                        textcoords="offset points",
                        ha='center', va='bottom')

        if 'page_faults' in avg_results.columns and avg_results['page_faults'].sum() > 0:
            ax2 = ax1.twinx()
            ax2.plot(scripts, avg_results['page_faults'], color='red', marker='o', label='Page Faults')
            ax2.set_ylabel('Page Faults Count', color='red', fontsize=12)
            ax2.legend(loc='upper right')

        fig.tight_layout()
        
        output_file = 'performance_chart.png'
        plt.savefig(output_file, dpi=300)
        plt.show() 

    except Exception as e:
        print(f"err: {e}")

if __name__ == "__main__":
    generate_chart()