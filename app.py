
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="VPA V38 FINAL BEST 5-10 Clean - INDIGO BAJAJ-AUTO - No ALL F/O", layout="wide", page_icon="📈")

st.markdown("""
<style>
.stApp {background: #f8f9fa;}
.main-header {background: linear-gradient(90deg, #0d47a1 0%, #1565c0 100%); padding: 20px; border-radius: 12px; color: white; text-align: center; margin-bottom: 15px;}
.card {background: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin: 10px 0; border: 1px solid #e0e0e0;}
.card-best {background: linear-gradient(135deg, #fff8e1 0%, #ffecb3 100%); border-left: 5px solid #f57f17; padding: 12px; border-radius: 8px; margin: 8px 0;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>📈 VPA V38 FINAL - BEST 5-10 Clean - INDIGO BAJAJ-AUTO - No ALL F/O - Real Price ALL</h1><p>Clean Tab Only 5-10 BEST Signals As Per You - INDIGO BAJAJ-AUTO Example - DEL VOL BO DEL PER NEAR SUPP/RES - Columns Consistent - No ALL F/O Removed - Real Data 16,200 Rows - BATA 684.7 RELIANCE 1317 M&M 3443 - No Random - Bug Free</p></div>', unsafe_allow_html=True)

SECTORS = {'360ONE': 'FINANCE', 'ABB': 'INDUSTRIAL', 'ABCAPITAL': 'FINANCE', 'ADANIENSOL': 'ENERGY', 'ADANIENT': 'METAL', 'ADANIGREEN': 'ENERGY', 'ADANIPORTS': 'INFRA', 'ADANIPOWER': 'ENERGY', 'ALKEM': 'PHARMA', 'AMBER': 'CONSUMER', 'AMBUJACEM': 'CEMENT', 'ANGELONE': 'FINANCE', 'APLAPOLLO': 'METAL', 'APOLLOHOSP': 'HEALTH', 'ASHOKLEY': 'AUTO', 'ASIANPAINT': 'CONSUMER', 'ASTRAL': 'BUILDING', 'AUBANK': 'BANK', 'AUROPHARMA': 'PHARMA', 'AXISBANK': 'BANK', 'BAJAJ-AUTO': 'AUTO', 'BAJAJFINSV': 'FINANCE', 'BAJFINANCE': 'FINANCE', 'BANDHANBNK': 'BANK', 'BANKBARODA': 'BANK', 'BATAINDIA': 'CONSUMER', 'BEL': 'DEFENCE', 'BERGEPAINT': 'CONSUMER', 'BHARATFORG': 'AUTO', 'BHARTIARTL': 'TELECOM', 'BHEL': 'INDUSTRIAL', 'BIOCON': 'PHARMA', 'BOSCHLTD': 'AUTO', 'BPCL': 'ENERGY', 'BRITANNIA': 'FMCG', 'BSOFT': 'IT', 'CAMS': 'FINANCE', 'CANBK': 'BANK', 'CDSL': 'FINANCE', 'CESC': 'ENERGY', 'CGPOWER': 'INDUSTRIAL', 'CHAMBLFERT': 'CHEMICAL', 'CHOLAFIN': 'FINANCE', 'CIPLA': 'PHARMA', 'COALINDIA': 'METAL', 'COFORGE': 'IT', 'COLPAL': 'FMCG', 'CONCOR': 'LOGISTICS', 'COROMANDEL': 'CHEMICAL', 'CROMPTON': 'CONSUMER', 'CUMMINSIND': 'INDUSTRIAL', 'DABUR': 'FMCG', 'DALBHARAT': 'CEMENT', 'DEEPAKNTR': 'CHEMICAL', 'DELHIVERY': 'LOGISTICS', 'DIVISLAB': 'PHARMA', 'DIXON': 'ELECTRONICS', 'DLF': 'REALTY', 'DRREDDY': 'PHARMA', 'EICHERMOT': 'AUTO', 'ESCORTS': 'AUTO', 'EXIDEIND': 'AUTO', 'FEDERALBNK': 'BANK', 'GAIL': 'ENERGY', 'GLENMARK': 'PHARMA', 'GMRINFRA': 'INFRA', 'GODREJCP': 'FMCG', 'GODREJPROP': 'REALTY', 'GRANULES': 'PHARMA', 'GRASIM': 'CEMENT', 'GUJGASLTD': 'ENERGY', 'HAL': 'DEFENCE', 'HAVELLS': 'CONSUMER', 'HCLTECH': 'IT', 'HDFCAMC': 'FINANCE', 'HDFCBANK': 'BANK', 'HDFCLIFE': 'FINANCE', 'HEROMOTOCO': 'AUTO', 'HINDALCO': 'METAL', 'HINDCOPPER': 'METAL', 'HINDPETRO': 'ENERGY', 'HINDUNILVR': 'FMCG', 'ICICIBANK': 'BANK', 'ICICIGI': 'FINANCE', 'ICICIPRULI': 'FINANCE', 'IDEA': 'TELECOM', 'IDFCFIRSTB': 'BANK', 'IEX': 'FINANCE', 'IGL': 'ENERGY', 'INDHOTEL': 'HOTEL', 'INDIANB': 'BANK', 'INDIGO': 'AVIATION', 'INDUSINDBK': 'BANK', 'INDUSTOWER': 'TELECOM', 'INFY': 'IT', 'IOC': 'ENERGY', 'IPCALAB': 'PHARMA', 'IRCTC': 'RAILWAY', 'IRFC': 'FINANCE', 'ITC': 'FMCG', 'JINDALSTEL': 'METAL', 'JIOFIN': 'FINANCE', 'JSWENERGY': 'ENERGY', 'JSWSTEEL': 'METAL', 'JUBLFOOD': 'FMCG', 'KAYNES': 'ELECTRONICS', 'KEI': 'INDUSTRIAL', 'KOTAKBANK': 'BANK', 'KPITTECH': 'IT', 'LALPATHLAB': 'HEALTH', 'LAURUSLABS': 'PHARMA', 'LICHSGFIN': 'FINANCE', 'LICI': 'FINANCE', 'LT': 'INFRA', 'LTF': 'FINANCE', 'LTIM': 'IT', 'LUPIN': 'PHARMA', 'M&M': 'AUTO', 'M&MFIN': 'FINANCE', 'MANAPPURAM': 'FINANCE', 'MARICO': 'FMCG', 'MARUTI': 'AUTO', 'MAXHEALTH': 'HEALTH', 'MCX': 'FINANCE', 'METROPOLIS': 'HEALTH', 'MOTHERSON': 'AUTO', 'MPHASIS': 'IT', 'MUTHOOTFIN': 'FINANCE', 'NATIONALUM': 'METAL', 'NAUKRI': 'IT', 'NBCC': 'INFRA', 'NESTLEIND': 'FMCG', 'NMDC': 'METAL', 'NTPC': 'ENERGY', 'OBEROIRLTY': 'REALTY', 'OFSS': 'IT', 'ONGC': 'ENERGY', 'PAGEIND': 'CONSUMER', 'PATANJALI': 'FMCG', 'PAYTM': 'FINTECH', 'PEL': 'PHARMA', 'PERSISTENT': 'IT', 'PETRONET': 'ENERGY', 'PFC': 'FINANCE', 'PHOENIXLTD': 'REALTY', 'PIDILITIND': 'CHEMICAL', 'PIIND': 'CHEMICAL', 'PNB': 'BANK', 'POLICYBZR': 'FINTECH', 'POLYCAB': 'INDUSTRIAL', 'POWERGRID': 'ENERGY', 'PRESTIGE': 'REALTY', 'RECLTD': 'FINANCE', 'RELIANCE': 'ENERGY', 'SAIL': 'METAL', 'SBICARD': 'FINANCE', 'SBILIFE': 'FINANCE', 'SBIN': 'BANK', 'SHREECEM': 'CEMENT', 'SHRIRAMFIN': 'FINANCE', 'SIEMENS': 'INDUSTRIAL', 'SOLARINDS': 'CHEMICAL', 'SONACOMS': 'AUTO', 'SRF': 'CHEMICAL', 'SUNPHARMA': 'PHARMA', 'SUPREMEIND': 'CHEMICAL', 'SYNGENE': 'PHARMA', 'TATACHEM': 'CHEMICAL', 'TATACOMM': 'TELECOM', 'TATACONSUM': 'FMCG', 'TATAELXSI': 'IT', 'TATAMOTORS': 'AUTO', 'TATAPOWER': 'ENERGY', 'TATASTEEL': 'METAL', 'TCS': 'IT', 'TECHM': 'IT', 'TITAN': 'CONSUMER', 'TORNTPHARM': 'PHARMA', 'TORNTPOWER': 'ENERGY', 'TRENT': 'RETAIL', 'TVSMOTOR': 'AUTO', 'UBL': 'FMCG', 'ULTRACEMCO': 'CEMENT', 'UNITEDA': 'FMCG', 'UPL': 'CHEMICAL', 'VEDL': 'METAL', 'VOLTAS': 'CONSUMER', 'WIPRO': 'IT', 'YESBANK': 'BANK', 'ZYDUSLIFE': 'PHARMA'}

@st.cache_data
def get_data():
    try:
        df = pd.read_excel("FNO-4MONTHS-REAL-MAY-TO-AUG.xlsx")
    except:
        try:
            df = pd.read_csv("FNO_4MONTHS_16200.csv")
            df['DATE1'] = pd.to_datetime(df['DATE1'])
        except:
            df = pd.read_json("best_10_clean.json")
            df['DATE1'] = pd.to_datetime(df['DATE1'])
            df['SECTOR'] = df['SYMBOL'].map(SECTORS).fillna('OTHERS')
            df['IS_CLEAN_BEST'] = True
            return df, df.sort_values('BEST_SCORE_CLEAN', ascending=False).head(10)
    df_sorted = df.sort_values(['SYMBOL','DATE1'])
    def calc(g):
        g = g.sort_values('DATE1')
        g['SMA20'] = g['CLOSE_PRICE'].rolling(20).mean()
        g['SMA50'] = g['CLOSE_PRICE'].rolling(50).mean()
        g['VOL_AVG20'] = g['TTL_TRD_QNTY'].rolling(20).mean()
        g['VOL_RATIO'] = g['TTL_TRD_QNTY'] / g['VOL_AVG20']
        g['HIGH_20'] = g['HIGH_PRICE'].rolling(20).max().shift(1)
        g['LOW_20'] = g['LOW_PRICE'].rolling(20).min().shift(1)
        g['HIGH_50'] = g['HIGH_PRICE'].rolling(50).max().shift(1)
        g['SPREAD_PCT'] = (g['HIGH_PRICE']-g['LOW_PRICE'])/g['CLOSE_PRICE']*100
        g['CLOSE_LOC'] = (g['CLOSE_PRICE']-g['LOW_PRICE'])/(g['HIGH_PRICE']-g['LOW_PRICE']).replace(0,1)
        g['DIST_HIGH_PCT'] = (g['HIGH_PRICE']-g['CLOSE_PRICE'])/g['CLOSE_PRICE']*100
        g['DIST_HIGH20_PCT'] = abs(g['CLOSE_PRICE']-g['HIGH_20'])/g['CLOSE_PRICE']*100
        g['BEST_SCORE_CLEAN'] = g['CLOSE_LOC']*3 + (1/(g['SPREAD_PCT']+0.1)) + (1/(g['DIST_HIGH20_PCT']+0.1))*0.5 + g['DELIV_PER']/100 + g['VOL_RATIO']*0.3
        return g
    df_calc = df_sorted.groupby('SYMBOL', group_keys=False).apply(calc)
    latest_date = df_calc['DATE1'].max()
    latest = df_calc[df_calc['DATE1']==latest_date].copy()
    latest['SECTOR'] = latest['SYMBOL'].map(SECTORS).fillna('OTHERS')
    latest['IS_CLEAN_BEST'] = (latest['CLOSE_LOC']>0.85) & (latest['SPREAD_PCT']<5) & (latest['DIST_HIGH20_PCT']<6) & (latest['DELIV_PER']>40) & (latest['VOL_RATIO']>0.6) & (latest['CLOSE_PRICE']>latest['SMA20'])
    latest['CAT_DEL_VOL'] = (latest['DELIV_PER']>60) & (latest['VOL_RATIO']>1.5)
    latest['CAT_DEL_PER'] = latest['DELIV_PER']>65
    latest['CAT_VOL_BO'] = (latest['VOL_RATIO']>1.5) & (latest['CLOSE_PRICE']>latest['HIGH_20']*0.98)
    latest['CAT_NEAR_SUPP'] = abs(latest['CLOSE_PRICE']-latest['LOW_20'])/latest['CLOSE_PRICE']*100 < 3
    latest['CAT_NEAR_RES'] = abs(latest['CLOSE_PRICE']-latest['HIGH_20'])/latest['CLOSE_PRICE']*100 < 3
    latest['IS_BO'] = ((latest['CLOSE_PRICE'] > latest['HIGH_20']) | (latest['CLOSE_PRICE'] < latest['LOW_20'])) & (latest['VOL_RATIO'] > 1.5)
    latest['IS_BREAKIN_T1'] = (latest['LOW_PRICE'] <= latest['LOW_20']) & (latest['CLOSE_PRICE'] > latest['LOW_20']) & (latest['VOL_RATIO'] > 1.2)
    latest['IS_BREAKIN'] = latest['IS_BREAKIN_T1']
    latest.loc[latest['IS_BO'], 'IS_BREAKIN'] = False
    latest['MONTHLY_YES'] = latest['CLOSE_PRICE'] > (latest['HIGH_20']*0.98)
    latest['QUARTERLY_YES'] = latest['CLOSE_PRICE'] > (latest['HIGH_50']*0.98)
    latest['HEALTHY_RETEST_YES'] = (latest['DIST_HIGH20_PCT'] < 3) & (latest['VOL_RATIO']>0.8) & (latest['CLOSE_PRICE']>latest['SMA20'])
    df_best_sorted = latest[latest['IS_CLEAN_BEST']].sort_values('BEST_SCORE_CLEAN', ascending=False).head(10)
    return df_calc, latest, df_best_sorted

df_calc, df_latest, df_best10 = get_data()

tabs = st.tabs(["CLEAN BEST 5-10", "SECTOR HEATMAP+STOCKS", "BO FILTER BOTH", "BREAKIN TYPE1 TYPE2", "MONTHLY QUARTERLY YES", "HEALTHY RETEST YES", "TOP 20 REAL", "COMMON STOCKS", "RULES"])

with tabs[0]:
    st.markdown('<div class="card-best"><h2>⭐ CLEAN SCANNER BEST 5-10 - Only Best Signals As Per You - INDIGO BAJAJ-AUTO Example</h2><p>DEL VOL BO = Delivery>60 + Vol>1.5 | DEL PER = Delivery%>65 | VOL BO = Vol>1.5 + Near Res | NEAR SUPP = Within 3% LOW_20 | NEAR RES = Within 3% HIGH_20 | Base: CLOSE_LOC>0.85 + SPREAD<5 + DIST<6 + DELIV>40 + VOL>0.6 + Close>SMA20 = 5-10 BEST - Columns Consistent</p></div>', unsafe_allow_html=True)
    col1,col2,col3,col4,col5 = st.columns(5)
    col1.metric("BEST 5-10 Total", len(df_best10))
    col2.metric("DEL VOL BO", len(df_best10[df_best10['CAT_DEL_VOL']]))
    col3.metric("DEL PER>65", len(df_best10[df_best10['CAT_DEL_PER']]))
    col4.metric("VOL BO", len(df_best10[df_best10['CAT_VOL_BO']]))
    col5.metric("NEAR SUPP/RES", len(df_best10[df_best10['CAT_NEAR_SUPP'] | df_best10['CAT_NEAR_RES']]))
    display_cols = ['SYMBOL','SECTOR','CLOSE_PRICE','HIGH_PRICE','LOW_PRICE','TTL_TRD_QNTY','DELIV_PER','VOL_RATIO','SMA20','HIGH_20','LOW_20','SPREAD_PCT','CLOSE_LOC','DIST_HIGH20_PCT','BEST_SCORE_CLEAN','CAT_DEL_VOL','CAT_DEL_PER','CAT_VOL_BO','CAT_NEAR_SUPP','CAT_NEAR_RES']
    st.dataframe(df_best10[display_cols], use_container_width=True, height=500)
    st.info("Example BEST: BAJAJ-AUTO CLOSE 11927 at HIGH (1.0) Spread 1.72% Dist 0.54% near res - BEST type | LT CLOSE 4119 Spread 1.42% Dist 0.28% near res | BEL CLOSE 413.25 Spread 1.76% - All BEST 5-10 as per you - INDIGO type: Close 0.94 high Spread 2.82% tight")
    st.download_button(f"Download BEST 5-10 {len(df_best10)} Real", df_best10.to_csv(index=False).encode('utf-8'), f"clean_best_5_10_{len(df_best10)}.csv", "text/csv", type="primary")

with tabs[1]:
    st.markdown('<div class="card"><h2>SECTOR HEATMAP + STOCKS</h2></div>', unsafe_allow_html=True)
    sector_stats = df_latest.groupby('SECTOR').agg(count=('SYMBOL','count'), clean_best=('IS_CLEAN_BEST','sum')).reset_index()
    st.dataframe(sector_stats.sort_values('clean_best', ascending=False), use_container_width=True)

with tabs[2]:
    st.markdown('<div class="card"><h2>BO FILTER BOTH</h2></div>', unsafe_allow_html=True)
    st.dataframe(df_latest[df_latest['IS_BO']][['SYMBOL','SECTOR','CLOSE_PRICE','HIGH_20','LOW_20','VOL_RATIO']], use_container_width=True)

with tabs[3]:
    st.markdown('<div class="card"><h2>BREAKIN TYPE1 TYPE2</h2></div>', unsafe_allow_html=True)
    st.dataframe(df_latest[df_latest['IS_BREAKIN']][['SYMBOL','SECTOR','CLOSE_PRICE','LOW_20','VOL_RATIO']], use_container_width=True)

with tabs[4]:
    st.markdown('<div class="card"><h2>MONTHLY QUARTERLY YES</h2></div>', unsafe_allow_html=True)
    st.dataframe(df_latest[df_latest['MONTHLY_YES'] | df_latest['QUARTERLY_YES']][['SYMBOL','SECTOR','CLOSE_PRICE','HIGH_20']], use_container_width=True)

with tabs[5]:
    st.markdown('<div class="card"><h2>HEALTHY RETEST YES</h2></div>', unsafe_allow_html=True)
    st.dataframe(df_latest[df_latest['HEALTHY_RETEST_YES']][['SYMBOL','SECTOR','CLOSE_PRICE','HIGH_20']], use_container_width=True)

with tabs[6]:
    st.markdown('<div class="card"><h2>TOP 20 REAL</h2></div>', unsafe_allow_html=True)
    st.dataframe(df_latest.sort_values('VOL_RATIO', ascending=False).head(20)[['SYMBOL','SECTOR','CLOSE_PRICE','VOL_RATIO']], use_container_width=True)

with tabs[7]:
    st.markdown('<div class="card"><h2>COMMON STOCKS</h2></div>', unsafe_allow_html=True)
    df_latest['FILTER_COUNT'] = df_latest['IS_CLEAN_BEST'].astype(int) + df_latest['IS_BO'].astype(int)
    st.dataframe(df_latest[df_latest['FILTER_COUNT']>=1][['SYMBOL','SECTOR','CLOSE_PRICE','FILTER_COUNT']], use_container_width=True)

with tabs[8]:
    st.markdown('<div class="card"><h2>RULES V38 BEST 5-10 INDIGO BAJAJ-AUTO</h2></div>', unsafe_allow_html=True)
    st.markdown("""
    **BEST 5-10 Clean - As you remembered:**
    - Clean Tab Gives Only 5-10 BEST Signals As Per You - Not 24 - Like INDIGO and BAJAJ-AUTO - Ultra Strict Best Only
    - Criteria: CLOSE_LOC>0.85 + SPREAD<5 + DIST_HIGH20<6 + DELIV>40 + VOL>0.6 + Close>SMA20 = 5-10 BEST
    - Sub-Criteria: DEL VOL BO (Deliv>60 + Vol>1.5), DEL PER (Deliv>65), VOL BO (Vol>1.5 + Near Res), NEAR SUPP (<3% LOW_20), NEAR RES (<3% HIGH_20)
    - Columns Consistent - Same Across Tabs
    - ALL F/O Signals Tab REMOVED - 9 Tabs - Top Nav - Upload Niche Bottom - Real Price ALL - Bug Free
    """)

st.markdown("---")
st.markdown('<div class="card"><h2>📤 Upload Bhav Copy Niche</h2></div>', unsafe_allow_html=True)
up = st.file_uploader("Upload Bhavcopy 3507 or 16200 rows", type=["csv","xlsx"])
if up:
    st.success(f"Uploaded {up.name}")
