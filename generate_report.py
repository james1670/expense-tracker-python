"""
Expense Tracker Analysis Report Generator
Professional report for Qrate interview submission
Author: James Bright Das
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import numpy as np
from datetime import datetime
import base64
from io import BytesIO
import warnings
warnings.filterwarnings('ignore')

# Clean, professional styling
plt.style.use('seaborn-v0_8-whitegrid')

def chart_to_base64(fig):
    """Convert matplotlib figure to base64 for HTML embedding"""
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=120, bbox_inches='tight', facecolor='white')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return img_base64

def load_data(filename='Expenses.csv'):
    """Load expense data from CSV"""
    df = pd.read_csv(filename)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def calculate_statistics(df):
    """Calculate key statistics"""
    stats = {
        'total_expenses': df['Amount'].sum(),
        'num_transactions': len(df),
        'avg_expense': df['Amount'].mean(),
        'median_expense': df['Amount'].median(),
        'max_expense': df['Amount'].max(),
        'min_expense': df['Amount'].min(),
        'date_range_start': df['Date'].min().strftime('%B %d, %Y'),
        'date_range_end': df['Date'].max().strftime('%B %d, %Y'),
        'num_days': (df['Date'].max() - df['Date'].min()).days + 1,
        'avg_daily': df['Amount'].sum() / ((df['Date'].max() - df['Date'].min()).days + 1),
        'top_category': df.groupby('Category')['Amount'].sum().idxmax(),
        'top_category_amount': df.groupby('Category')['Amount'].sum().max(),
        'top_category_pct': (df.groupby('Category')['Amount'].sum().max() / df['Amount'].sum() * 100)
    }
    return stats

def generate_visualizations(df):
    """Generate clean, professional visualizations"""
    charts = {}
    
    # Color scheme - professional and clean
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']
    
    # Chart 1: Category Distribution (Pie Chart)
    fig, ax = plt.subplots(figsize=(9, 6))
    category_totals = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    
    wedges, texts, autotexts = ax.pie(
        category_totals.values, 
        labels=category_totals.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        textprops={'fontsize': 11}
    )
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax.set_title('Expense Distribution by Category', fontsize=14, fontweight='bold', pad=20)
    charts['pie'] = chart_to_base64(fig)
    
    # Chart 2: Category Totals (Bar Chart)
    fig, ax = plt.subplots(figsize=(10, 6))
    category_sorted = category_totals.sort_values(ascending=True)
    
    bars = ax.barh(range(len(category_sorted)), category_sorted.values, color='#3498db', height=0.6)
    ax.set_yticks(range(len(category_sorted)))
    ax.set_yticklabels(category_sorted.index, fontsize=11)
    ax.set_xlabel('Total Amount (₹)', fontsize=11, fontweight='bold')
    ax.set_title('Total Expenditure by Category', fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Add value labels on bars
    for i, (bar, value) in enumerate(zip(bars, category_sorted.values)):
        ax.text(value + 200, i, f'₹{value:,.0f}', va='center', fontsize=10)
    
    charts['bar'] = chart_to_base64(fig)
    
    # Chart 3: Daily Spending Trend
    fig, ax = plt.subplots(figsize=(12, 5))
    daily_expenses = df.groupby('Date')['Amount'].sum()
    
    ax.plot(daily_expenses.index, daily_expenses.values, 
            color='#3498db', linewidth=2, marker='o', markersize=4, alpha=0.8)
    ax.fill_between(daily_expenses.index, daily_expenses.values, alpha=0.2, color='#3498db')
    
    ax.set_xlabel('Date', fontsize=11, fontweight='bold')
    ax.set_ylabel('Daily Expense (₹)', fontsize=11, fontweight='bold')
    ax.set_title('Daily Spending Trend', fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3, linestyle='--')
    plt.xticks(rotation=45, ha='right')
    
    charts['trend'] = chart_to_base64(fig)
    
    # Chart 4: Category Transaction Count
    fig, ax = plt.subplots(figsize=(10, 6))
    category_counts = df['Category'].value_counts().sort_values(ascending=True)
    
    bars = ax.barh(range(len(category_counts)), category_counts.values, 
                   color='#2ecc71', height=0.6)
    ax.set_yticks(range(len(category_counts)))
    ax.set_yticklabels(category_counts.index, fontsize=11)
    ax.set_xlabel('Number of Transactions', fontsize=11, fontweight='bold')
    ax.set_title('Transaction Frequency by Category', fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    
    for i, (bar, value) in enumerate(zip(bars, category_counts.values)):
        ax.text(value + 0.5, i, f'{int(value)}', va='center', fontsize=10)
    
    charts['count'] = chart_to_base64(fig)
    
    # Chart 5: Average Expense by Category
    fig, ax = plt.subplots(figsize=(10, 6))
    category_avg = df.groupby('Category')['Amount'].mean().sort_values(ascending=True)
    
    bars = ax.barh(range(len(category_avg)), category_avg.values, 
                   color='#f39c12', height=0.6)
    ax.set_yticks(range(len(category_avg)))
    ax.set_yticklabels(category_avg.index, fontsize=11)
    ax.set_xlabel('Average Amount (₹)', fontsize=11, fontweight='bold')
    ax.set_title('Average Expense per Transaction by Category', fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    
    for i, (bar, value) in enumerate(zip(bars, category_avg.values)):
        ax.text(value + 10, i, f'₹{value:,.0f}', va='center', fontsize=10)
    
    charts['avg'] = chart_to_base64(fig)
    
    return charts

def generate_html_report(df, charts, stats):
    """Generate clean, minimalistic HTML report"""
    
    # Category summary table
    category_summary = df.groupby('Category').agg({
        'Amount': ['sum', 'count', 'mean', 'min', 'max']
    }).round(0)
    category_summary.columns = ['Total', 'Count', 'Average', 'Min', 'Max']
    category_summary['% of Total'] = (category_summary['Total'] / category_summary['Total'].sum() * 100).round(1)
    category_summary = category_summary.sort_values('Total', ascending=False)
    
    category_rows = ""
    for cat, row in category_summary.iterrows():
        category_rows += f"""
        <tr>
            <td>{cat}</td>
            <td>₹{row['Total']:,.0f}</td>
            <td>{row['% of Total']:.1f}%</td>
            <td>{int(row['Count'])}</td>
            <td>₹{row['Average']:,.0f}</td>
        </tr>
        """
    
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expense Tracker Analysis Report</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.7;
            color: #2c3e50;
            background: #ffffff;
            padding: 0;
        }}
        
        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 50px 40px;
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 50px;
            padding-bottom: 30px;
            border-bottom: 2px solid #e0e0e0;
        }}
        
        h1 {{
            font-size: 28px;
            color: #1a1a1a;
            margin-bottom: 8px;
            font-weight: 600;
            letter-spacing: -0.5px;
        }}
        
        .subtitle {{
            font-size: 16px;
            color: #7f8c8d;
            font-weight: 400;
        }}
        
        .meta {{
            margin-top: 20px;
            font-size: 14px;
            color: #95a5a6;
        }}
        
        h2 {{
            font-size: 20px;
            color: #2c3e50;
            margin-top: 50px;
            margin-bottom: 20px;
            font-weight: 600;
            border-left: 4px solid #3498db;
            padding-left: 12px;
        }}
        
        h3 {{
            font-size: 17px;
            color: #34495e;
            margin-top: 35px;
            margin-bottom: 15px;
            font-weight: 600;
        }}
        
        p {{
            margin: 15px 0;
            color: #555;
            font-size: 15px;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 35px 0;
        }}
        
        .stat-card {{
            background: #f8f9fa;
            padding: 25px 20px;
            border-radius: 8px;
            border-left: 4px solid #3498db;
        }}
        
        .stat-label {{
            font-size: 13px;
            color: #7f8c8d;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 8px;
        }}
        
        .stat-value {{
            font-size: 26px;
            font-weight: 600;
            color: #2c3e50;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 14px;
        }}
        
        th {{
            background: #f8f9fa;
            padding: 14px 12px;
            text-align: left;
            font-weight: 600;
            color: #2c3e50;
            border-bottom: 2px solid #e0e0e0;
        }}
        
        td {{
            padding: 12px;
            border-bottom: 1px solid #f0f0f0;
        }}
        
        tr:hover {{
            background: #f8f9fa;
        }}
        
        .chart-container {{
            margin: 35px 0;
            text-align: center;
        }}
        
        .chart-container img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }}
        
        .insight-box {{
            background: #f8f9fa;
            border-left: 4px solid #3498db;
            padding: 20px;
            margin: 25px 0;
            border-radius: 4px;
        }}
        
        .insight-box strong {{
            color: #2c3e50;
        }}
        
        .key-findings {{
            background: #f8f9fa;
            padding: 25px;
            border-radius: 8px;
            margin: 30px 0;
        }}
        
        .key-findings ul {{
            margin-left: 20px;
            margin-top: 15px;
        }}
        
        .key-findings li {{
            margin: 12px 0;
            color: #555;
        }}
        
        .tech-section {{
            background: #f8f9fa;
            padding: 25px;
            border-radius: 8px;
            margin: 30px 0;
        }}
        
        .tech-section ul {{
            margin-left: 20px;
            margin-top: 10px;
        }}
        
        .tech-section li {{
            margin: 8px 0;
        }}
        
        .footer {{
            text-align: center;
            margin-top: 60px;
            padding-top: 30px;
            border-top: 1px solid #e0e0e0;
            color: #95a5a6;
            font-size: 13px;
        }}
        
        .page-break {{
            page-break-before: always;
        }}
        
        @media print {{
            body {{
                background: white;
            }}
            .container {{
                padding: 30px 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <div class="header">
            <h1>Expense Tracker Analysis Report</h1>
            <div class="subtitle">Personal Finance Management System</div>
            <div class="meta">
                James Bright Das | {datetime.now().strftime('%B %Y')}
            </div>
        </div>

        <!-- Executive Summary -->
        <section>
            <h2>Executive Summary</h2>
            <p>
                This report presents a comprehensive analysis of personal expense data tracked over a 
                {stats['num_days']}-day period from {stats['date_range_start']} to {stats['date_range_end']}. 
                The Expense Tracker application, built using Python and CSV-based data storage, captured 
                {stats['num_transactions']} transactions across five expense categories.
            </p>
            <p>
                Total expenses recorded amount to ₹{stats['total_expenses']:,.0f}, with {stats['top_category']} 
                representing the largest spending category at {stats['top_category_pct']:.1f}% of total expenditure. 
                The average daily expense stands at ₹{stats['avg_daily']:,.0f}, providing a clear baseline for 
                budget planning and financial management.
            </p>
        </section>

        <!-- Key Metrics -->
        <section>
            <h2>Key Financial Metrics</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-label">Total Expenses</div>
                    <div class="stat-value">₹{stats['total_expenses']:,.0f}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Transactions</div>
                    <div class="stat-value">{stats['num_transactions']}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Avg per Transaction</div>
                    <div class="stat-value">₹{stats['avg_expense']:,.0f}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Avg Daily Expense</div>
                    <div class="stat-value">₹{stats['avg_daily']:,.0f}</div>
                </div>
            </div>
        </section>

        <!-- Project Overview -->
        <section>
            <h2>Project Overview</h2>
            <h3>Objectives</h3>
            <p>The Expense Tracker application was developed to address the need for systematic personal finance management through:</p>
            <ul style="margin-left: 20px; margin-top: 10px;">
                <li>Real-time logging of daily expenses across multiple categories</li>
                <li>Data persistence using CSV format for portability and simplicity</li>
                <li>Interactive command-line interface for ease of use</li>
                <li>Visual analytics through charts and graphs</li>
                <li>Budget monitoring and expense summarization capabilities</li>
            </ul>
            
            <h3>Data Collection Methodology</h3>
            <p>
                Data collection was performed through a custom Python application featuring input validation, 
                category standardization, and date formatting. The system captures three primary data points 
                for each transaction:
            </p>
            <ul style="margin-left: 20px; margin-top: 10px;">
                <li><strong>Date:</strong> Transaction date in YYYY-MM-DD format</li>
                <li><strong>Category:</strong> Predefined categories (Food, Transport, Entertainment, Groceries, Clothing)</li>
                <li><strong>Amount:</strong> Transaction amount in Indian Rupees (₹)</li>
            </ul>
        </section>

        <!-- Category Analysis -->
        <section>
            <h2>Category-wise Expenditure Analysis</h2>
            <table>
                <thead>
                    <tr>
                        <th>Category</th>
                        <th>Total Amount</th>
                        <th>% of Total</th>
                        <th>Transactions</th>
                        <th>Avg per Transaction</th>
                    </tr>
                </thead>
                <tbody>
                    {category_rows}
                </tbody>
            </table>
        </section>

        <!-- Visualizations -->
        <div class="page-break"></div>
        <section>
            <h2>Visual Analysis</h2>
            
            <h3>Expense Distribution by Category</h3>
            <div class="chart-container">
                <img src="data:image/png;base64,{charts['pie']}" alt="Category Distribution">
            </div>
            <div class="insight-box">
                <strong>Key Insight:</strong> {stats['top_category']} accounts for {stats['top_category_pct']:.1f}% 
                of total spending (₹{stats['top_category_amount']:,.0f}), indicating this as the primary area 
                for potential budget optimization.
            </div>

            <h3>Total Expenditure by Category</h3>
            <div class="chart-container">
                <img src="data:image/png;base64,{charts['bar']}" alt="Category Totals">
            </div>

            <h3>Daily Spending Trend</h3>
            <div class="chart-container">
                <img src="data:image/png;base64,{charts['trend']}" alt="Daily Trend">
            </div>
            <div class="insight-box">
                <strong>Trend Analysis:</strong> The daily spending pattern reveals fluctuations that can inform 
                better budgeting decisions and highlight high-expenditure periods requiring additional attention.
            </div>

            <div class="page-break"></div>
            <h3>Transaction Frequency by Category</h3>
            <div class="chart-container">
                <img src="data:image/png;base64,{charts['count']}" alt="Transaction Count">
            </div>

            <h3>Average Expense per Transaction</h3>
            <div class="chart-container">
                <img src="data:image/png;base64,{charts['avg']}" alt="Average Expense">
            </div>
        </section>

        <!-- Key Findings -->
        <section>
            <h2>Key Findings</h2>
            <div class="key-findings">
                <ul>
                    <li><strong>Spending Distribution:</strong> {stats['top_category']} represents the highest 
                    expense category, suggesting targeted budget management in this area could yield significant savings.</li>
                    
                    <li><strong>Transaction Patterns:</strong> With {stats['num_transactions']} transactions over 
                    {stats['num_days']} days, the average transaction frequency is {stats['num_transactions']/stats['num_days']:.1f} 
                    per day, indicating regular spending habits.</li>
                    
                    <li><strong>Expense Range:</strong> Individual transactions range from ₹{stats['min_expense']:,.0f} 
                    to ₹{stats['max_expense']:,.0f}, with a median of ₹{stats['median_expense']:,.0f}, showing 
                    relatively consistent spending patterns.</li>
                    
                    <li><strong>Daily Average:</strong> The daily average expense of ₹{stats['avg_daily']:,.0f} 
                    provides a practical benchmark for daily budget planning and financial goal setting.</li>
                    
                    <li><strong>Category Behavior:</strong> Analysis reveals distinct spending patterns across 
                    categories, enabling targeted interventions for budget optimization.</li>
                </ul>
            </div>
        </section>

        <!-- Technical Implementation -->
        <section>
            <h2>Technical Implementation</h2>
            <div class="tech-section">
                <h3 style="margin-top: 0;">Technology Stack</h3>
                <ul>
                    <li><strong>Programming Language:</strong> Python 3.x</li>
                    <li><strong>Data Storage:</strong> CSV (Comma-Separated Values) format</li>
                    <li><strong>Data Processing:</strong> CSV module for file I/O operations</li>
                    <li><strong>Visualization:</strong> Matplotlib library for chart generation</li>
                    <li><strong>User Interface:</strong> Command-line interface with Tabulate for formatted output</li>
                    <li><strong>Testing:</strong> Pytest framework for unit testing</li>
                </ul>
                
                <h3>Key Features Implemented</h3>
                <ul>
                    <li><strong>Data Validation:</strong> Regex-based validation for dates, categories, and amounts</li>
                    <li><strong>CRUD Operations:</strong> Create, read, update, and delete expense entries</li>
                    <li><strong>Budget Monitoring:</strong> Real-time budget tracking with surplus/deficit calculation</li>
                    <li><strong>Visualization:</strong> Multiple chart types (bar, pie) for different analytical perspectives</li>
                    <li><strong>Data Integrity:</strong> File existence checks and error handling</li>
                    <li><strong>Sorting & Filtering:</strong> Date-based sorting and category-wise aggregation</li>
                </ul>
                
                <h3>Code Architecture</h3>
                <ul>
                    <li><strong>project.py:</strong> Main application logic and user interface</li>
                    <li><strong>data_handler.py:</strong> Data management operations (CRUD)</li>
                    <li><strong>visualize.py:</strong> Chart generation and visualization logic</li>
                    <li><strong>Modular Design:</strong> Separation of concerns for maintainability</li>
                </ul>
            </div>
        </section>

        <!-- Insights & Recommendations -->
        <section>
            <h2>Insights & Recommendations</h2>
            <p><strong>Budget Optimization Strategies:</strong></p>
            <ul style="margin-left: 20px; margin-top: 15px;">
                <li>Focus on high-spend categories for maximum savings impact</li>
                <li>Set category-specific monthly budgets based on historical averages</li>
                <li>Monitor daily spending to stay within the ₹{stats['avg_daily']:,.0f} average</li>
                <li>Review high-value transactions (above ₹{stats['median_expense']*2:,.0f}) before purchase</li>
                <li>Conduct weekly expense reviews using the tracker's visualization features</li>
            </ul>
            
            <p style="margin-top: 25px;"><strong>Application Enhancements:</strong></p>
            <ul style="margin-left: 20px; margin-top: 15px;">
                <li>Implement monthly/weekly summaries for trend analysis</li>
                <li>Add category-wise budget limits with alert notifications</li>
                <li>Integrate database support for scalability</li>
                <li>Develop web-based interface for multi-device access</li>
            </ul>
        </section>

        <!-- Conclusion -->
        <section>
            <h2>Conclusion</h2>
            <p>
                This Expense Tracker project demonstrates practical application of data management principles, 
                including data collection, validation, storage, analysis, and visualization. The system successfully 
                tracked {stats['num_transactions']} transactions over {stats['num_days']} days, providing actionable 
                insights into spending patterns.
            </p>
            <p>
                The technical implementation showcases proficiency in Python programming, file I/O operations, 
                data validation, and visualization techniques—skills directly applicable to project data analysis 
                roles. The modular code architecture and comprehensive feature set demonstrate both technical 
                capability and understanding of user requirements.
            </p>
            <p>
                The analysis reveals clear patterns and opportunities for financial optimization, proving the value 
                of systematic data tracking and analysis in personal finance management. This project serves as 
                a foundation for understanding how data-driven approaches can inform better decision-making across 
                various domains.
            </p>
        </section>

        <!-- Footer -->
        <div class="footer">
            <p>Report Generated: {datetime.now().strftime('%B %d, %Y')}</p>
            <p>Author: James Bright Das</p>
            <p>GitHub: <a href="https://github.com/james1669/ExpensesTracker" style="color: #3498db; text-decoration: none;">github.com/james1669/ExpensesTracker</a></p>
        </div>
    </div>
</body>
</html>
"""
    
    return html

def main():
    print("=" * 70)
    print("EXPENSE TRACKER ANALYSIS REPORT GENERATOR".center(70))
    print("=" * 70)
    
    try:
        # Load data
        print("\n[1/4] Loading expense data from Expenses.csv...")
        df = load_data('Expenses.csv')
        print(f"      ✓ Loaded {len(df)} transactions successfully")
        
        # Calculate statistics
        print("\n[2/4] Calculating statistics...")
        stats = calculate_statistics(df)
        print(f"      ✓ Total Expenses: ₹{stats['total_expenses']:,.0f}")
        print(f"      ✓ Date Range: {stats['date_range_start']} to {stats['date_range_end']}")
        print(f"      ✓ Top Category: {stats['top_category']} ({stats['top_category_pct']:.1f}%)")
        
        # Generate visualizations
        print("\n[3/4] Creating visualizations...")
        charts = generate_visualizations(df)
        print(f"      ✓ Generated {len(charts)} professional charts")
        
        # Generate HTML report
        print("\n[4/4] Generating HTML report...")
        html_report = generate_html_report(df, charts, stats)
        
        # Save report
        filename = f"Expense_Tracker_Analysis_Report_James_Das.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_report)
        
        print(f"\n{'=' * 70}")
        print(f"SUCCESS!".center(70))
        print(f"{'=' * 70}")
        print(f"\n✓ Report saved as: {filename}")
        print(f"\n📋 NEXT STEPS:")
        print(f"   1. Open {filename} in your browser")
        print(f"   2. Press Ctrl+P (or Cmd+P on Mac)")
        print(f"   3. Select 'Save as PDF'")
        print(f"   4. Send PDF to employer")
        print(f"\n{'=' * 70}\n")
        
    except FileNotFoundError:
        print("\n❌ ERROR: Expenses.csv not found in current directory")
        print("   Make sure Expenses.csv is in the same folder as this script")
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")

if __name__ == "__main__":
    main()