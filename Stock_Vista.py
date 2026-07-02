import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
    layout="wide",

    page_icon="📈"
)

# ---------------- Sidebar ----------------
with st.sidebar:

    st.markdown("""
    # 📈 StockVista
    ### A Real-Time Market Dashboard
    """)

    st.markdown("## 👩‍💻 Developer")
    st.write("Aradhya Bharti")

    st.markdown("---")

    st.markdown("## ⚙️ Technologies")
    st.write("🐍 Python")
    st.write("📊 Streamlit")
    st.write("📈 Plotly")
    st.write("💹 yFinance")

    st.markdown("---")

    st.success("🟢 Live Market Data")

# ---------------- Main Page ----------------

st.markdown("""
<h1 style="
font-size:58px;
font-weight:800;
margin-bottom:0;
background:linear-gradient(90deg,#C026D3,#EC4899);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
">
📈 StockVista
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style="color:#E9D5FF;margin-top:-15px;">
Real-Time Stock Market Dashboard
</h3>
""", unsafe_allow_html=True)

st.caption("Track live stock prices, financial ratios and company financial statements.")

st.markdown("---")

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return info, stock

def get_stock_history(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="5y")
    return hist

def get_nasdaq_history():
    nasdaq = yf.Ticker("^IXIC")
    hist = nasdaq.history(period="5y")
    return hist

# Custom CSS to improve app appearance
st.markdown("""
<style>
   
/* Background */
.stApp{
    background: #0E081A;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background: linear-gradient(
        180deg,
        #1B102E 0%,
        #24113D 100%
    );
}

/* Sidebar text */
[data-testid="stSidebar"] *{
    color:white;
}

/* Cards */
div[data-testid="stVerticalBlock"]>div{
    border-radius:20px;
}

/* Buttons */

.stButton>button{
    background:linear-gradient(
        90deg,
        #A855F7,
        #EC4899
    );

    color:white;
    border:none;

    border-radius:14px;

    font-weight:bold;

    height:50px;

    transition:.3s;
}

.stButton>button:hover{

    background:linear-gradient(
        90deg,
        #C084FC,
        #F472B6
    );

    box-shadow:
    0 0 18px #EC4899;

}

/* Text Input */

.stTextInput input{

    background:#1E1532;

    color:white;

    border:2px solid #A855F7;

    border-radius:12px;

}

/* Metric Cards */

[data-testid="metric-container"]{
    background: linear-gradient(
        135deg,
        rgba(110,30,170,.35),
        rgba(236,72,153,.18)
    );

    border:1px solid rgba(236,72,153,.25);

    border-radius:18px;

    padding:18px;

    box-shadow:0 0 20px rgba(192,38,211,.18);

    transition:all .25s ease;
}

[data-testid="metric-container"]:hover{
    transform:translateY(-6px);
    box-shadow:0 0 30px rgba(236,72,153,.35);
}

/* Horizontal line */

hr{

    border-color:#C026D3;

}

/* Tabs */

button[data-baseweb="tab"]{

    background:#24143A;

    color:white;

    border-radius:12px;

    margin-right:8px;

}

button[data-baseweb="tab"][aria-selected="true"]{

    background:#EC4899;

    color:white;

}

/* Headers */

h1,h2,h3{

    color:white;

}

/* Links */

a{

    color:#F472B6;

}

/* Success Box */

.stSuccess{

    background:#26163F;

    color:white;

    border-radius:14px;

}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div style="
background: linear-gradient(135deg,#211136,#31184F);
padding:30px;
border-radius:22px;
border:1px solid #C026D3;
box-shadow:0 0 25px rgba(236,72,153,.18);
margin-bottom:25px;
">

<h2 style="
color:white;
margin-top:0;
font-size:32px;
">
📊 About StockVista
</h2>

<p style="
color:#D8B4FE;
font-size:17px;
line-height:1.8;
">
StockVista is a real-time financial dashboard that provides
live stock prices, historical performance, financial ratios,
interactive visualizations, and company financial statements
using Yahoo Finance.
</p>

<hr style="
border:0;
height:1px;
background:#7E22CE;
margin:20px 0;
">

<h3 style="
color:#F472B6;
">
✨ Features
</h3>

<div style="
display:grid;
grid-template-columns:1fr 1fr;
gap:12px;
color:white;
font-size:16px;
">

<div>📈 Live Stock Prices</div>
<div>📊 Interactive Charts</div>
<div>💰 Financial Ratios</div>
<div>📚 Financial Statements</div>
<div>📥 CSV Export</div>
<div>📊 Stock Comparison</div>

</div>

</div>
""", unsafe_allow_html=True)
st.markdown("---")
st.caption("👩‍💻 Developed by Aradhya | B.Tech CSE Internship Project | 2026")

# Input for stock ticker
ticker = st.text_input('🔎 Search Stock Symbol :', 'AAPL', placeholder='NVDA, PLTR, TSLA...')
compare_ticker = st.text_input(
    "📊 Compare With",
    "MSFT"
)
st.caption("Examples: AAPL • MSFT • NVDA • TSLA • GOOGL • RELIANCE.NS")

# main section
if st.button('Get Stock Info', use_container_width=True):
    # Get stock info
    info, stock = get_stock_info(ticker)
    compare_info, compare_stock = get_stock_info(compare_ticker)
    st.divider()
    st.markdown("## 📊 Stock Comparison")

    left, middle, right = st.columns([5,1,5])

    with left:
     with st.container(border=True):
      st.image(
        f"https://logos.stockanalysis.com/{ticker.lower()}.svg",
        width=70
)
      st.subheader(info.get("longName", ticker.upper()))

      st.metric(
      "💲 Current Price",
      f"${info.get('currentPrice', 'N/A')}"
    )

      st.metric(
        "💰 Market Cap",
        f"{info.get('marketCap', 0)/1e9:.2f} B"
    )

      st.metric(
        "📈 P/E Ratio",
        info.get("trailingPE", "N/A")
    )

    with middle:
     st.markdown("""
        <div style="
            display:lex;
            justify-content:center;
            align-items:center;
            height:100%;
            margin-top:180px;
        ">
            <h1 style="
                color:#EC4899;
                font-size:55px;
                font-weight:800;
            ">
                VS
            </h1>
        </div>
    """, unsafe_allow_html=True)  

    with right:
      with st.container(border=True):
        st.image(
         f"https://logos.stockanalysis.com/{compare_ticker.lower()}.svg",
        width=70
)
        st.subheader(compare_info.get("longName", compare_ticker.upper()))

        st.metric(
        "💲 Current Price",
        f"${compare_info.get('currentPrice', 'N/A')}"
    )

        st.metric(
        "💰 Market Cap" ,
        f"{compare_info.get('marketCap', 0)/1e9:.2f} B"
    )
        st.metric(
        "📈 P/E Ratio",
        compare_info.get("trailingPE", "N/A")
    )

    st.divider()
    tab1, tab2, tab3 = st.tabs([f"💧 {ticker} Info", "📊 Financial Ratios", "📚 Financial Statements"])


    

    # Tab 1: Info
    with tab1:

     st.subheader(
         f"🏷️ {info.get('longName', 'N/A')} :orange-background[{ticker}]",
         divider="violet"
        )

    # Current price and day change
    current_price = info.get("currentPrice", "N/A")
    previous_close = info.get("previousClose", "N/A")

    if current_price != "N/A" and previous_close != "N/A":
        day_change = current_price - previous_close
        day_change_percent = (day_change / previous_close) * 100

        col0, col1, col2, col3, col4 = st.columns([2,2,2,3,4])

        with col0:
            st.image(
                f"https://logos.stockanalysis.com/{ticker.lower()}.svg",
                width=100
            )

        with col1:
            st.metric(
                f"📈 {ticker}",
                f"$ {current_price:.2f}",
                f"{day_change_percent:.2f}%"
            )

        with col2:
            st.metric(
                "💰 Market Cap",
                f"{info.get('marketCap', 0) / 1e9:.2f} B$"
            )

        with col3:
            st.metric(
                "🏭 Sector",
                info.get("sector", "N/A")
            )

        with col4:
            st.metric(
                "🔧 Industry",
                info.get("industry", "N/A")
            )
        # Display company description    
        st.markdown("### 📖 Company Description")

        with st.expander("Read More"):
            st.write(info.get("longBusinessSummary", "N/A"))    
           
            # Display financial ratios in cards
            st.subheader('📊 Financial Ratios', divider='grey')
            col1, col2, col3, col4 = st.columns(4)
            ratios = [
                ('P/S Ratio', 'priceToSalesTrailing12Months', '💹'),
                ('P/E Ratio', 'trailingPE', '📊'),
                ('Forward P/E', 'forwardPE', '🔮'),
                ('1Q Earnings Growth', 'earningsQuarterlyGrowth', '🌱'),
                ('Recommendation', 'recommendationKey', '🎯'),
                ('Target Price', 'targetMedianPrice', '💲'),
                ('Short Ratio', 'shortRatio', '📉'),
                ('Profit Margin', 'profitMargins', '📈'),
            ]   
    
        for i, (label, key, emoji) in enumerate(ratios):
            with [col1, col2, col3, col4][i % 4]:
                value = info.get(key, 'N/A')
                if isinstance(value, float):
                    value = f"{value:.2f}"
                st.metric(f"{emoji} {label}", value)
    
        #st.markdown('---')

    
        # Get historical data and create an interactive chart
        hist = get_stock_history(ticker)
        nasdaq_hist = get_nasdaq_history()
    
        #st.subheader('📉 Interactive Stock Chart', divider='violet')
    
        fig = make_subplots(specs=[[{"secondary_y": True}]])
    
        fig.add_trace(go.Scatter(x=hist.index, y=hist['Close'], name='Close'), secondary_y=False)
        fig.add_trace(go.Bar(x=hist.index, y=hist['Volume'], name='Volume', marker_color='grey', width=0.1), secondary_y=True)
    
        # Calculate the 20-day moving average
        hist['MA100'] = hist['Close'].rolling(window=100).mean()
        fig.add_trace(go.Scatter(x=hist.index, y=hist['MA100'], name='MA100'), secondary_y=False)
    
        fig.update_layout(title=f'📉 {ticker} Price Chart', xaxis_title='Date', yaxis_title='Price')
        fig.update_yaxes(title_text="Volume", secondary_y=True, range=[0, hist['Volume'].max() * 5])
        st.plotly_chart(fig, use_container_width=True)
        # Download historical data
        csv = hist.to_csv().encode("utf-8")

        st.download_button(
        label="📥 Download Historical Data (CSV)",
        data=csv,
        file_name=f"{ticker.upper()}_history.csv",
        mime="text/csv",)

        st.divider()


    # Tab 2: Financial Ratios
    with tab2:
        
        # Display financial ratios in cards
        st.subheader('📊 Financial Ratios', divider='violet')
        col1, col2, col3, col4 = st.columns(4)
        ratios = [
            ('P/S Ratio', 'priceToSalesTrailing12Months', '💹'),
            ('P/E Ratio', 'trailingPE', '📊'),
            ('Forward P/E', 'forwardPE', '🔮'),
            ('PEG Ratio', 'pegRatio', '🌱'),
            ('Price to Book', 'priceToBook', '📚'),
            ('Dividend Yield', 'dividendYield', '💵'),
            ('Profit Margin', 'profitMargins', '📈'),
            ('EV/EBITDA', 'enterpriseToEbitda', '🏦')
        ]
    
        for i, (label, key, emoji) in enumerate(ratios):
            with [col1, col2, col3, col4][i % 4]:
                value = info.get(key, 'N/A')
                if isinstance(value, float):
                    value = f"{value:.2f}"
                st.metric(f"{emoji} {label}", value)
    
        st.markdown('---')
    
    
        # Cards for Growth Metrics
        st.subheader('📈 Growth Metrics', divider='violet')
        growth_metrics = [
            ('Earnings Quarterly Growth', 'earningsQuarterlyGrowth', '📊'),
            ('Revenue Quarterly Growth', 'revenueQuarterlyGrowth', '📈'),
            ('Earnings Growth', 'earningsGrowth', '💹'),
            ('Revenue Growth', 'revenueGrowth', '💵'),
            ('Gross Margins', 'grossMargins', '📊'),
            ('EBITDA Margins', 'ebitdaMargins', '📈'),
            ('Operating Margins', 'operatingMargins', '💹'),
            ('Profit Margins', 'profitMargins', '💵')
        ]
    
        cols = st.columns(4)
        for i, (label, key, emoji) in enumerate(growth_metrics):
            with cols[i % 4]:
                value = info.get(key, 'N/A')
                if isinstance(value, (int, float)):
                    value = f"{value:.2f}"
                st.metric(f"{emoji} {label}", value)
    
        # Display Rsik cards
        st.divider()
    
        # Risk Metrics
        st.subheader('🎢 Risk Metrics', divider='violet')
        risk_metrics = [
            ('Total Debt', 'totalDebt', '💳'),
            ('Quick Ratio', 'quickRatio', '⚡'),
            ('Current Ratio', 'currentRatio', '💧'),
            ('Debt to Equity', 'debtToEquity', '📊'),
            ('Short Ratio', 'shortRatio', '📉'),
            ('Short Percent of Float', 'shortPercentOfFloat', '📈'),
            ('Audit Risk', 'auditRisk', '🔍'),
            ('Overall Risk', 'overallRisk', '⚠️')
        ]
    
        cols = st.columns(4)
        for i, (label, key, emoji) in enumerate(risk_metrics):
            with cols[i % 4]:
                value = info.get(key, 'N/A')
                if isinstance(value, (int, float)):
                    value = f"{value:.2f}"
                st.metric(f"{emoji} {label}", value)
    
        st.divider()
    
        # Recommendations
        st.subheader('🕵️‍♂️ Analyst Recommendations', divider='violet')
        risk_metrics = [
            ('Recommendation', 'recommendationKey', '🎯'),
            ('Target Price', 'targetMedianPrice', '💲'),
            ('Recommendation Mead', 'recommendationMean', '🔍'),
            ('Target Mean Price', 'targetMeanPrice', '💧'),
            ('Target High Price', 'targetHighPrice', '📈'),
            ('Target Low Price', 'targetLowPrice', '📉'),
        ]
    
        cols = st.columns(3)
        for i, (label, key, emoji) in enumerate(risk_metrics):
            with cols[i % 3]:
                value = info.get(key, 'N/A')
                if isinstance(value, (int, float)):
                    value = f"{value:.2f}"
                st.metric(f"{emoji} {label}", value)
    
        st.divider()
    

    # tab 3: Financial Statements
    with tab3:
        
        # Financial Statements
        st.subheader('📑 Financial Statements')
    
        # Income Statement
        income_stmt = stock.income_stmt
        if not income_stmt.empty:
            st.write("💰 Income Statement")
            income_stmt_metrics = ['Total Revenue', 'Operating Revenue','Net Income', 'Gross Profit', 'Operating Income', 'EBITDA' , 'EBIT', ]
            fig = go.Figure()
            for metric in income_stmt_metrics:
                if metric in income_stmt.index:
                    fig.add_trace(go.Bar(x=income_stmt.columns, y=income_stmt.loc[metric], name=metric))
            fig.update_layout(title='Income Statement Metrics', barmode='group')
            st.plotly_chart(fig, use_container_width=True)
    
        # Balance Sheet
        balance_sheet = stock.balance_sheet
        if not balance_sheet.empty:
            st.write("📊 Balance Sheet")
            balance_sheet_metrics = ['Total Assets', 'Total Debt', 'Current Liabilities', 'Long Term Debt', 'Cash And Cash Equiv']
            fig = go.Figure()
            for metric in balance_sheet_metrics:
                if metric in balance_sheet.index:
                    fig.add_trace(go.Bar(x=balance_sheet.columns, y=balance_sheet.loc[metric], name=metric))
            fig.update_layout(title='Balance Sheet Metrics', barmode='group')
            st.plotly_chart(fig, use_container_width=True)
    
        # Cash Flow
        cash_flow = stock.cashflow
        if not cash_flow.empty:
            st.write("💸 Cash Flow")
            cash_flow_metrics = ['Free Cash Flow', 'Operating Cash Flow', 'Financing Cash Flow', 'Investing Cash Flow','Capital Expenditures', 'Long Term Debt Payments']
            fig = go.Figure()
            for metric in cash_flow_metrics:
                if metric in cash_flow.index:
                    fig.add_trace(go.Bar(x=cash_flow.columns, y=cash_flow.loc[metric], name=metric))
            fig.update_layout(title='Cash Flow Metrics', barmode='group')
            st.plotly_chart(fig, use_container_width=True)
    
        st.markdown('---')
        st.caption("👩‍💻 Developed by Aradhya Bharti | B.Tech CSE Internship Project | 2026")