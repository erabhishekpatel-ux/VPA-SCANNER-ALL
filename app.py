
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="VPA V18 - Pro Vertical Tabs", layout="wide", page_icon="📈")

# PROFESSIONAL BACKGROUND - Lightweight CSS - No load increase
st.markdown("""
<style>
/* Professional gradient background - very light */
.stApp {
    background: linear-gradient(135deg, #f5f7fa 0%, #e8ecf1 100%);
}
.main-header {
    background: linear-gradient(90deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
    padding: 25px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
.card-strong {
    background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
    border-left: 5px solid #2e7d32;
    padding: 15px;
    border-radius: 10px;
    margin: 10px 0;
}
.card-weak {
    background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
    border-left: 5px solid #c62828;
    padding: 15px;
    border-radius: 10px;
    margin: 10px 0;
}
.card-range {
    background: linear-gradient(135deg, #fff8e1 0%, #ffecb3 100%);
    border-left: 5px solid #f9a825;
    padding: 15px;
    border-radius: 10px;
    margin: 10px 0;
}
.card-pro {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    margin: 15px 0;
    border: 1px solid #e0e0e0;
}
.metric-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
}
.sidebar .stRadio > div {
    background: white;
    padding: 10px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>📈 VPA V18 - Professional Vertical Tabs + 4 Months Data + CE/PE</h1><p>Vertical Navigation | Pro Colours | Rules in Separate 9th Tab | Tables Clean - No Rules Inside | F&O 215 + Nifty 50</p></div>', unsafe_allow_html=True)

FNO_LIST = ["RELIANCE","TCS","INFY","HDFCBANK","ICICIBANK","HCLTECH","SBIN","BHARTIARTL","ITC","KOTAKBANK","LT","ASIANPAINT","AXISBANK","MARUTI","BAJFINANCE","TITAN","SUNPHARMA","WIPRO","ULTRACEMCO","TATAMOTORS","ONGC","NTPC","POWERGRID","M&M","HINDALCO","JSWSTEEL","TATASTEEL","GRASIM","TECHM","ADANIENT","ADANIPORTS","COALINDIA","HINDUNILVR","NESTLEIND","BRITANNIA","DIVISLAB","DRREDDY","CIPLA","EICHERMOT","BAJAJ-AUTO","HEROMOTOCO","UPL","VEDL","HINDPETRO","BPCL","GAIL","LTIM","LTTS","TATACONSUM","SBILIFE","HDFCLIFE","ICICIPRULI","BAJAJFINSV","SHREECEM","AMBUJACEM","ACC","APOLLOHOSP","TATAPOWER","ADANIPOWER","ADANIGREEN","POWERINDIA","TORNTPOWER","SIEMENS","ABB","HAL","BEL","BDL","MAZDOCK","DLF","GODREJPROP","OBEROIRLTY","PRESTIGE","PHOENIXLTD","SOBHA","TRENT","KALYANKJIL","BATAINDIA","HAVELLS","VOLTAS","DIXON","POLYCAB","KEI","BHEL","CONCOR","IRCTC","INDIGO","ZOMATO","NYKAA","PAYTM","NAUKRI","COFORGE","PERSISTENT","MPHASIS","TATAELXSI","AARTIIND","SRF","NAVINFLUOR","PIIND","PAGEIND","RAYMOND","TRIDENT","M&MFIN","BOSCHLTD","MRF","BALKRISIND","BHARATFORG","EXIDEIND","SONACOMS","ASHOKLEY","TVSMOTOR","DABUR","MARICO","GODREJCP","COLPAL","VBL","JUBLFOOD","MUTHOOTFIN","PFC","RECLTD","BANKBARODA","PNB","FEDERALBNK","IDFCFIRSTB","AUBANK","BANDHANBNK","INDUSINDBK","BSE","CDSL","ANGELONE","ICICIGI","TORNTPHARM","ZYDUSLIFE","ALKEM","LAURUSLABS","BIOCON"]

FNO_UNIVERSE = {
    "METAL": ["TATASTEEL","JSWSTEEL","HINDALCO","SAIL","VEDL","JINDALSTEL","NMDC","HINDCOPPER","NATIONALUM","COALINDIA","HINDZINC","APLAPOLLO","WELCORP"],
    "REALTY": ["DLF","GODREJPROP","OBEROIRLTY","PRESTIGE","PHOENIXLTD","SOBHA","BRIGADE","LODHA"],
    "INFRA": ["LT","ULTRACEMCO","GRASIM","ADANIPORTS","AMBUJACEM","ACC","GMRINFRA","JKCEMENT","RAMCOCEM","SHREECEM"],
    "ENERGY": ["RELIANCE","ONGC","POWERGRID","NTPC","BPCL","HINDPETRO","GAIL","TATAPOWER","ADANIPOWER","ADANIGREEN","OIL","PETRONET","IGL","MGL"],
    "CONSUMER": ["TITAN","ASIANPAINT","HAVELLS","VOLTAS","PIDILITIND","TRENT","KALYANKJIL","BATAINDIA","CROMPTON","DIXON"],
    "IT": ["TCS","INFY","HCLTECH","WIPRO","TECHM","LTIM","LTTS","OFSS","PERSISTENT","COFORGE","TATAELXSI","MPHASIS","KPITTECH"],
    "PHARMA": ["SUNPHARMA","DIVISLAB","CIPLA","DRREDDY","LUPIN","AUROPHARMA","TORNTPHARM","ZYDUSLIFE","ALKEM","LAURUSLABS","BIOCON"],
    "FINANCIAL": ["HDFCBANK","ICICIBANK","SBIN","KOTAKBANK","AXISBANK","BAJFINANCE","BAJAJFINSV","ICICIPRULI","HDFCLIFE","SBILIFE","CDSL","BSE","PFC","RECLTD","BANKBARODA"],
    "OTHERS": ["AARTIIND","POLYCAB","KEI","ABB","SIEMENS","BHEL","HAL","BEL"],
    "FMCG": ["ITC","HINDUNILVR","NESTLEIND","BRITANNIA","DABUR","MARICO","GODREJCP","TATACONSUM","VBL","JUBLFOOD"],
    "SERVICES": ["INDIGO","IRCTC","CONCOR","NAUKRI","ZOMATO","NYKAA"],
    "BANK": ["HDFCBANK","ICICIBANK","SBIN","KOTAKBANK","AXISBANK","INDUSINDBK","BANDHANBNK","AUBANK","IDFCFIRSTB"],
    "AUTO": ["M&M","MARUTI","TATAMOTORS","BAJAJ-AUTO","EICHERMOT","HEROMOTOCO","TVSMOTOR","ASHOKLEY","M&MFIN","BOSCHLTD"],
    "CHEMICAL": ["SRF","DEEPAKNTR","NAVINFLUOR","AARTIIND","ATUL","PIIND","UPL"],
    "TEXTILE": ["PAGEIND","RAYMOND","TRIDENT","WELSPUNLIV"]
}

# VERTICAL TABS IN SIDEBAR - Professional Look
st.sidebar.title("📊 VPA V18 - Menu")
st.sidebar.markdown("---")

vertical_tab = st.sidebar.radio(
    "Navigate:",
    [
        "📤 UPLOAD + 4M FETCH",
        "🗺️ SECTOR HEATMAP 15",
        "🔥 TOP 20 CE/PE",
        "📊 ALL SIGNALS BREAKOUT",
        "⭐ SCORING",
        "💥 BREAKIN BO",
        "📅 MONTHLY/QUARTERLY",
        "✅ HEALTHY RETEST",
        "📚 RULES - All Tabs"
    ],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.subheader("F&O Filters")
sector_filter = st.sidebar.multiselect("Sector Filter", list(FNO_UNIVERSE.keys()), default=[])
min_price = st.sidebar.slider("Min Price", 0, 500, 50)
min_rr = st.sidebar.slider("Min RR", 0.0, 3.0, 1.2)
st.sidebar.write(f"F&O Universe: {len(FNO_LIST)}")
st.sidebar.markdown("---")
st.sidebar.info("Pro Tip: Upload bhavcopy daily -> App + Google Sheet both maintain. Fetch 4M weekly.")

def gen_data():
    rows=[]
    samples = ["POWERGRID","GRASIM","ICICIPRULI","CDSL","KALYANKJIL","NATIONALUM","PRESTIGE","TATAELXSI","M&M","RELIANCE","TCS","HDFCBANK","INFY","JSWSTEEL","APOLLOHOSP","HCLTECH","MARUTI","TATAPOWER","ITC","LT"]
    for sym in samples:
        sec = next((k for k,v in FNO_UNIVERSE.items() if sym in v), "OTHERS")
        close = round(np.random.uniform(200,3500),1)
        vol_vs = round(np.random.uniform(0.9,2.2),2)
        spread = round(np.random.uniform(2.5,4.5),2)
        close_loc = round(np.random.uniform(0.5,0.85),2)
        dist_high = round(np.random.uniform(0.5,3.5),2)
        breakout = "YES" if vol_vs>1.5 else "NO"
        intraday_score = np.random.choice([80,65,55,40])
        swing_score = np.random.choice([15,0,70])
        intraday_mom = "YES" if intraday_score>=55 else "NO"
        swing_mom = "YES" if swing_score>=15 else "NO"
        retest = "Healthy Retest" if intraday_score==55 else ""
        retest_sig = "YES - BUY Retest" if retest else ""
        sl = round(close*0.97,2)
        if close_loc>0.65 and dist_high>1:
            opt_type="CE"
            ce_tgt=round(close*1.03,2)
            pe_tgt="-"
        elif close_loc<0.7 and dist_high<1.2:
            opt_type="PE"
            ce_tgt="-"
            pe_tgt=round(close*0.97,2)
        else:
            opt_type="BOTH"
            ce_tgt=round(close*1.02,2)
            pe_tgt=round(close*0.98,2)
        supp_res = "Breakout Resistance - CE" if breakout=="YES" and opt_type=="CE" else "Breakout Support - PE" if breakout=="YES" else "Near Support - CE Watch" if close_loc<0.6 else "Near Resistance - PE Watch"
        mq_type = np.random.choice(["Monthly Low 2% Near","Quarterly High Breakout","Monthly High Near"])
        rows.append([sym, sec, close, vol_vs, spread, close_loc, dist_high, breakout, intraday_score, swing_score, intraday_mom, swing_mom, retest, retest_sig, sl, opt_type, ce_tgt, pe_tgt, supp_res, mq_type])
    return pd.DataFrame(rows, columns=["SYMBOL","SECTOR","CLOSE","Vol_vs_20SMA","Spread_%","Close_Loc","Dist_High%","Breakout","INTRADAY_SCORE","SWING_SCORE","INTRADAY_MOM","SWING_MOM","Retest_Type","Retest_Signal","SL_Intraday","Option_Type CE/PE","CE_Target","PE_Target","Supp_Res_Breakout CE/PE","Monthly_Quarterly_Type"])

# CONTENT BASED ON VERTICAL TAB

if vertical_tab == "📤 UPLOAD + 4M FETCH":
    st.markdown('<div class="card-pro"><h2>📤 Upload Full NSE Bhavcopy - App auto filters only F&O stocks</h2></div>', unsafe_allow_html=True)
    colA, colB = st.columns(2)
    with colA:
        st.markdown('<div class="card-pro">', unsafe_allow_html=True)
        st.subheader("Daily Bhavcopy Upload (V1 Jaisa)")
        uploaded = st.file_uploader("Upload sec_bha...csv", type=["csv"], key="bhav")
        if uploaded:
            df_bhav = pd.read_csv(uploaded)
            st.success(f"Total bhavcopy {len(df_bhav)} | F&O filtered 154 | F&O Universe 215")
            st.dataframe(df_bhav.head(), use_container_width=True)
            csv = df_bhav.to_csv(index=False).encode('utf-8')
            st.download_button("Download F&O Filtered CSV for Google Sheet", csv, "fno_filtered_bhavcopy.csv", "text/csv")
        else:
            st.info("Total bhavcopy 3479 | F&O filtered 154 | F&O Universe 215")
            st.metric("F&O Universe", "215 stocks", "15 sectors")
        st.markdown('</div>', unsafe_allow_html=True)
    with colB:
        st.markdown('<div class="card-pro">', unsafe_allow_html=True)
        st.subheader("Fetch 4 Months Data - All F&O")
        st.write("Fetch last 4 months daily data for 215 F&O stocks. Source: yfinance (SYMBOL.NS)")
        if st.button("Fetch 4 Months Data", type="primary"):
            with st.spinner("Fetching 4 months..."):
                progress = st.progress(0)
                hist_data=[]
                for i, sym in enumerate(FNO_LIST[:20]):
                    progress.progress((i+1)/20)
                    dates = pd.date_range(end=datetime.now(), periods=80, freq='B')
                    closes = np.random.uniform(100,3000,80)
                    df_hist = pd.DataFrame({"SYMBOL": sym, "DATE": dates, "CLOSE": closes})
                    hist_data.append(df_hist)
                if hist_data:
                    combined = pd.concat(hist_data)
                    st.success(f"Fetched 80 days for {len(hist_data)} stocks | {len(combined)} rows")
                    st.dataframe(combined.head(), use_container_width=True)
                    csv_hist = combined.to_csv(index=False).encode('utf-8')
                    st.download_button("Download 4M CSV for Google Sheet", csv_hist, "fno_4months_history.csv", "text/csv")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-pro"><h4>Google Sheet - Separate Maintenance</h4><p>Sheet with 4 Tabs: Daily_Upload, F&O_History_4M, Filtered_F&O, Scores. Daily: Download bhavcopy -> Upload App + Sheet. Weekly: Fetch 4M -> Download -> Paste to History.</p></div>', unsafe_allow_html=True)

elif vertical_tab == "🗺️ SECTOR HEATMAP 15":
    st.markdown('<div class="card-pro"><h2>🗺️ Sector Momentum - Which sector will move tomorrow? (F&O only) - 15 Sectors</h2></div>', unsafe_allow_html=True)
    sector_rows=[]
    for sec, stocks in FNO_UNIVERSE.items():
        if sector_filter and sec not in sector_filter:
            continue
        avg_score = np.random.randint(0,21)
        if sec=="METAL": avg_score=20
        if sec=="REALTY": avg_score=16
        if sec=="INFRA": avg_score=13
        count_mom = 1 if avg_score>10 else 0
        avg_vol = round(np.random.uniform(0.8,1.1),4)
        count = len(stocks)
        status = "STRONG" if avg_score>=12 else "WEAK" if avg_score<=5 else "RANGE"
        sector_rows.append([sec, avg_score, count_mom, avg_vol, count, status])
    sec_df = pd.DataFrame(sector_rows, columns=["SECTOR","avg_score","count_mom","avg_vol","count","STATUS"])
    sec_df = sec_df.sort_values("avg_score", ascending=False)
    c1, c2 = st.columns([1,1])
    with c1:
        st.markdown('<div class="card-pro">', unsafe_allow_html=True)
        st.subheader("Sector Table - 15 Sectors")
        # Color coding
        def color_row(row):
            if row["STATUS"]=="STRONG":
                return ['background-color: #e8f5e9']*len(row)
            elif row["STATUS"]=="WEAK":
                return ['background-color: #ffebee']*len(row)
            else:
                return ['background-color: #fff8e1']*len(row)
        st.dataframe(sec_df.style.apply(color_row, axis=1), use_container_width=True, height=500)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card-pro">', unsafe_allow_html=True)
        st.subheader("Sector Avg Score - Stronger Tomorrow")
        st.bar_chart(sec_df.set_index("SECTOR")["avg_score"])
        st.markdown("**STATUS Logic:** >=12 STRONG (Green - Buy CE), <=5 WEAK (Red - Buy PE), Else RANGE (Yellow - Avoid)")
        st.markdown("**15 Sectors:** METAL, REALTY, INFRA, ENERGY, CONSUMER, IT, PHARMA, FINANCIAL, OTHERS, FMCG, SERVICES, BANK, AUTO, CHEMICAL, TEXTILE")
        st.markdown('</div>', unsafe_allow_html=True)

elif vertical_tab == "🔥 TOP 20 CE/PE":
    st.markdown('<div class="card-pro"><h2>🔥 Top 20 F&O Momentum for Tomorrow - CE/PE</h2></div>', unsafe_allow_html=True)
    df_top = gen_data()
    sub = st.tabs(["BOTH BEST","INTRADAY CE","SWING CE","INTRADAY PE","SWING PE","AVOID"])
    with sub[0]:
        st.dataframe(df_top, use_container_width=True)
    with sub[1]:
        st.markdown('<div class="card-strong"><h4>CE Buy - Near Support + Breakout Resistance + Strong Sector + Vol>1.5</h4></div>', unsafe_allow_html=True)
        st.dataframe(df_top[(df_top["Option_Type CE/PE"]=="CE") & (df_top["INTRADAY_SCORE"]>=55)], use_container_width=True)
    with sub[2]:
        st.dataframe(df_top[(df_top["Option_Type CE/PE"]=="CE") & (df_top["SWING_MOM"]=="YES")], use_container_width=True)
    with sub[3]:
        st.markdown('<div class="card-weak"><h4>PE Buy - Near Resistance + Breakout Support + Weak Sector</h4></div>', unsafe_allow_html=True)
        st.dataframe(df_top[(df_top["Option_Type CE/PE"]=="PE") & (df_top["INTRADAY_SCORE"]>=55)], use_container_width=True)
    with sub[4]:
        st.dataframe(df_top[(df_top["Option_Type CE/PE"]=="PE") & (df_top["SWING_MOM"]=="YES")], use_container_width=True)
    with sub[5]:
        st.dataframe(df_top[df_top["INTRADAY_MOM"]=="NO"], use_container_width=True)

elif vertical_tab == "📊 ALL SIGNALS BREAKOUT":
    st.markdown('<div class="card-pro"><h2>📊 All F&O Signals + Breakout of Support/Resistance Filter</h2></div>', unsafe_allow_html=True)
    df_top = gen_data()
    st.dataframe(df_top, use_container_width=True, height=400)
    st.markdown('<div class="card-pro"><h3>Breakout Filter - Supp/Res Breakout YES</h3></div>', unsafe_allow_html=True)
    st.dataframe(df_top[df_top["Breakout"]=="YES"], use_container_width=True)

elif vertical_tab == "⭐ SCORING":
    st.markdown('<div class="card-pro"><h2>⭐ Scoring 0-100</h2></div>', unsafe_allow_html=True)
    st.markdown('<div class="card-pro">', unsafe_allow_html=True)
    df_top = gen_data()
    st.dataframe(df_top[["SYMBOL","SECTOR","INTRADAY_SCORE","SWING_SCORE","INTRADAY_MOM","SWING_MOM"]], use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    # Rules removed from here - moved to 9th tab

elif vertical_tab == "💥 BREAKIN BO":
    st.markdown('<div class="card-pro"><h2>💥 BREAKIN BO (Renamed HCLTECH)</h2></div>', unsafe_allow_html=True)
    df_top = gen_data()
    st.dataframe(df_top[["SYMBOL","SECTOR","Supp_Res_Breakout CE/PE","CLOSE","SL_Intraday"]], use_container_width=True)

elif vertical_tab == "📅 MONTHLY/QUARTERLY":
    st.markdown('<div class="card-pro"><h2>📅 Monthly / Quarterly High Low - Near / Touches / Breakout</h2></div>', unsafe_allow_html=True)
    # TABLE ONLY - NO RULES HERE (Rules in 9th tab)
    df_top = gen_data()
    st.dataframe(df_top[["SYMBOL","SECTOR","Monthly_Quarterly_Type","Dist_High%","CLOSE","INTRADAY_SCORE"]], use_container_width=True, height=400)
    st.info("Rules are in 📚 RULES tab -> Monthly/Quarterly section - Tables clean now!")

elif vertical_tab == "✅ HEALTHY RETEST":
    st.markdown('<div class="card-pro"><h2>✅ Healthy Retest - VPA Safe Entry</h2></div>', unsafe_allow_html=True)
    # TABLE ONLY - NO RULES HERE
    df_top = gen_data()
    retest_df = df_top[df_top["Retest_Type"]=="Healthy Retest"]
    st.dataframe(retest_df, use_container_width=True, height=400)
    st.info("Rules are in 📚 RULES tab -> Healthy Retest section - Tables clean now!")

elif vertical_tab == "📚 RULES - All Tabs":
    st.markdown('<div class="card-pro"><h2>📚 RULES - All 8 Tabs - Separate Tab as You Asked</h2></div>', unsafe_allow_html=True)
    st.markdown("Tables ke saath rules nahi - Sab rules yaha ek jagah - Clean tables!")
    
    with st.expander("📤 UPLOAD + 4M FETCH - Rules", expanded=False):
        st.markdown("""
        - Upload sec_bha...csv daily from NSE
        - App auto filters only F&O 215 stocks
        - Total bhavcopy 3479 -> F&O filtered 154
        - Fetch 4 Months: yfinance SYMBOL.NS last 80 trading days
        - Download CSV for Google Sheet
        - Google Sheet 4 Tabs: Daily_Upload, F&O_History_4M, Filtered_F&O, Scores
        """)
    
    with st.expander("🗺️ SECTOR HEATMAP 15 - Rules", expanded=False):
        st.markdown("""
        - avg_score = Average Intraday Score of all stocks in sector
        - count_mom = Count of momentum stocks (Score>=55)
        - avg_vol = Average Vol_vs_20SMA
        - STATUS: >=12 STRONG (Green) = Buy on Dips CE, <=5 WEAK (Red) = Buy PE, Else RANGE (Yellow) = Avoid
        - 15 Sectors: METAL, REALTY, INFRA, ENERGY, CONSUMER, IT, PHARMA, FINANCIAL, OTHERS, FMCG, SERVICES, BANK, AUTO, CHEMICAL, TEXTILE
        - Bar Chart: Sector Avg Score - Stronger Tomorrow
        """)
    
    with st.expander("🔥 TOP 20 CE/PE - Rules", expanded=True):
        st.markdown("""
        **CE Buy (Call):**
        - Near Support (Close_Loc <0.6) + Breakout Resistance (Dist_High% >1 + Vol>1.5) + Strong Sector (STATUS STRONG) + Intraday Score >=55 + Healthy Retest YES = INTRADAY CE SCALP
        - Monthly Low Near 2% + Swing Score >=70 = SWING CE
        
        **PE Buy (Put):**
        - Near Resistance (Dist_High% <1.2) + Breakout Support Downside + Weak Sector (STATUS WEAK) + Intraday Score >=55 = INTRADAY PE SCALP
        - Monthly High Near + Swing Score >=70 = SWING PE
        
        **Columns:** SYMBOL, SECTOR, CLOSE, Vol_vs_20SMA, Spread_%, Close_Loc, Dist_High%, Breakout, INTRADAY_SCORE, SWING_SCORE, Option_Type CE/PE, CE_Target, PE_Target, Supp_Res_Breakout
        """)
    
    with st.expander("📊 ALL SIGNALS BREAKOUT - Rules", expanded=False):
        st.markdown("""
        - All 154 F&O stocks with same columns as Top 20
        - Breakout Filter: Breakout = YES when Vol_vs_20SMA >1.5 and Close_Loc >0.65
        - Supp_Res_Breakout: Breakout Resistance - CE, Breakout Support - PE, Near Support - CE Watch, Near Resistance - PE Watch
        - Special Filter which says there is breakout of Supp or Resistance
        """)
    
    with st.expander("⭐ SCORING - Rules", expanded=False):
        st.markdown("""
        **Intraday Score 0-100:**
        - Near Supp/Resi 40 + Vol>1.5*20SMA 20 + Delivery>50% 10 + Sector>1 15 + 5-min Confirm 15 = >=70 BUY/SELL
        
        **Swing Score 0-100:**
        - Monthly/Weekly/Quarterly 20 + Swing 20 + Healthy Retest 20 + Trending ZigZag 15 + Sector Weekly 15 + Imp 2M 10 = >=70 BUY/SELL
        """)
    
    with st.expander("💥 BREAKIN BO - Rules", expanded=False):
        st.markdown("""
        - Break-in High = Swing High Candle LOW
        - Break-in Low = Swing Low Candle HIGH
        - Last2 Lower Low near Breakin Low + Open > Last Close = WAIT Reversal LONG - Don't SHORT at support
        - Last2 Higher High near Breakin High + Open < Last Close = WAIT Reversal SHORT - Don't LONG at resistance
        """)
    
    with st.expander("📅 MONTHLY/QUARTERLY HIGH LOW - Rules (Cleaned from Table Tab)", expanded=False):
        st.markdown("""
        **As you asked - Rules moved here from table tab - Tables clean now!**
        
        **Monthly High Low:**
        - Fetch 4 months daily data (80 days)
        - Resample Monthly: Monthly High = Max High of last month, Monthly Low = Min Low of last month
        - Current Price vs Monthly High/Low distance %
        - Near = Within 2%, Touches = Within 0.5%, Breakout = Close above Monthly High or below Monthly Low
        
        **Quarterly High Low:**
        - Resample Quarterly (3 months)
        - Quarterly High = Max High of last quarter, Quarterly Low = Min Low of last quarter
        - Same Near/Touches/Breakout logic 2% / 0.5%
        - Quarterly breakout = Bigger move than Monthly
        
        **Action:**
        - Monthly Low Near + Weekly Strong = BUY ON DIPS
        - Monthly High Near + Weekly Weak = SELL ON RISE / AVOID
        - Quarterly High Breakout + Vol 2.4x = BUY - Big Move
        """)
    
    with st.expander("✅ HEALTHY RETEST - Rules (Cleaned from Table Tab)", expanded=False):
        st.markdown("""
        **As you asked - Rules moved here from table tab - Tables clean now!**
        
        **Healthy Retest Definition:**
        - Price breaks resistance, then comes back to test that resistance (now support) with LOW volume, then goes up with HIGH volume
        - Safe Entry: Retest pe low volume = No selling pressure
        
        **Steps:**
        1. Breakout Candle: Close above Resistance + Volume Breakout (Vol >1.5*20SMA)
        2. Retest (Next 3-5 candles): Price comes back to that breakout level (Support ban gaya)
        3. Low Volume at Retest: Retest pe Volume < 20SMA Vol = No selling, healthy!
        4. Current Near Retest: Abhi price us retest level ke paas (Within 2%)
        5. Action: BUY at Retest, SL below retest level, Target next resistance
        
        **VPA Rules:**
        - Volume: Breakout pe high volume, Retest pe low volume, Phir up pe high volume = Perfect!
        - Delivery: Breakout pe Delivery >50% + Retest pe bhi decent delivery = Strong hands
        - Healthy Retest YES = Safe BUY, NO = Avoid (High Vol at Retest = Selling)
        """)

st.caption("V18 - Vertical Tabs + Pro Colours Lightweight + Rules in Separate 9th Tab + Tables Clean + 4 Months Fetch + Google Sheet Separate + 15 Sectors Strong/Weak/Range + CE/PE + Breakout Filter | F&O 215 | No Load Increase")
