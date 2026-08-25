import streamlit as st
import pandas as pd

st.set_page_config(page_title="VPA V15.3 - 8 Tabs", layout="wide", page_icon="📈")

st.markdown("""
<style>
.main-header {background: linear-gradient(90deg, #0f2027 0%, #203a43 50%, #2c5364 100%); padding: 20px; border-radius: 15px; color: white; text-align: center; margin-bottom: 20px;}
.retest-box {background: #e8f5e9; border-left: 5px solid #00c853; padding: 15px; border-radius: 10px; margin: 10px 0;}
.mq-box {background: #fff3e0; border-left: 5px solid #ff9800; padding: 15px; border-radius: 10px; margin: 10px 0;}
.confirm-box {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 15px; margin: 10px 0; text-align: center;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>📈 VPA V15.3 - 8 Tabs - Monthly/Quarterly + Healthy Retest</h1><p>Scanner = Shortlist 200+ Stocks -> Watchlist | Repetition = Confirmation | 10-15 Min Scanner + Hours Chart = Action List</p></div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["CLEAN SCANNER","HEATMAP","DROPDOWN","INVESTING","SCORING","BREAKIN BO","MONTHLY/QUARTERLY","HEALTHY RETEST"])

with tab1:
    st.subheader("Clean Scanner - Shortlist from 200+")
    data = [
        ["M&M","Auto","Swing Low 2%","2.1x","62%","1.6 Strong",85,"BUY","Tab 2,6,7,8 me bhi - HIGH POTENTIAL!"],
        ["JSWSTEEL","Metal","Monthly Low 2%","1.8x","58%","1.4 Strong",78,"BUY","Tab 7 me bhi - Monthly Low"],
        ["APOLLOHOSP","Healthcare","Imp Candle 1%","2.3x","65%","1.7 Strong",90,"BUY","Tab 2 Strong Sector"],
        ["HCLTECH","IT","Breakin Low 0.8%","2.2x","61%","1.5 Strong",88,"WAIT BREAKIN BO","Tab 6 BREAKIN BO"],
    ]
    df = pd.DataFrame(data, columns=["Stock","Sector","Near Level","Vol 20SMA","Delivery","Sector Ratio","Score","Action","Repetition = Confirmation"])
    st.dataframe(df, use_container_width=True)
    st.markdown('<div class="confirm-box"><h3>Same Stock in Multiple Tabs = High Potential Confirmation!</h3><p>M&M = Tab1 + Tab2 + Tab6 + Tab7 + Tab8 = TOP Watchlist!</p></div>', unsafe_allow_html=True)

with tab2:
    st.subheader("Sector Heatmap - Strong/Weak/Range Ratio")
    heatmap_data = [
        ["Auto",1.6,"STRONG","Buy on Dips"],
        ["Metal",0.8,"WEAK","Sell on Rise"],
        ["Banking",1.4,"STRONG","Buy on Dips"],
        ["IT",1.0,"RANGE","Avoid"],
        ["Pharma",1.5,"STRONG","Buy on Dips"],
        ["Healthcare",1.7,"STRONG","Buy on Dips"],
    ]
    st.dataframe(pd.DataFrame(heatmap_data, columns=["Sector","Ratio","Status","Strategy"]), use_container_width=True)

with tab3:
    st.subheader("Sector Dropdown - Filter Stocks")
    sel = st.selectbox("Choose Sector", ["Auto","Metal","Banking","IT"], index=0, key="dropdown")
    stocks = ["M&M","MARUTI","TATAMOTORS"] if sel=="Auto" else ["TATASTEEL","JSWSTEEL"]
    df = pd.DataFrame([[s, sel, "2% Near", "1.8x", 80] for s in stocks], columns=["Stock","Sector","Near Level","Vol","Score"])
    st.dataframe(df, use_container_width=True)

with tab4:
    st.subheader("Investing - Only Nifty 50 + F&O Filtered")
    investing = [["RELIANCE","Energy","Strong","2.5% Retest","Swing Low 2%","2.0x",88,"BUY SWING"],["M&MFIN","Auto","Strong","2% Breakout","Trending Up","2.2x",90,"BUY INVEST"]]
    st.dataframe(pd.DataFrame(investing, columns=["Stock","Sector","Weekly","Monthly","Swing","Vol","Score","Action"]), use_container_width=True)

with tab5:
    st.subheader("Scoring 0-100")
    st.markdown("Intraday: Near Supp/Resi 40 + Vol>1.5*20SMA 20 + Delivery>50% 10 + Sector>1 15 + 5-min Confirm 15 = >70 BUY/SELL")
    st.markdown("Swing: Monthly/Weekly/Quarterly 20 + Swing 20 + Healthy Retest 20 + Trending ZigZag 15 + Sector Weekly 15 + Imp 2M 10 = >70 BUY/SELL")

with tab6:
    st.subheader("BREAKIN BO (Renamed from HCLTECH)")
    st.markdown("Break-in High = Swing High Candle LOW, Break-in Low = Swing Low Candle HIGH")
    st.markdown("Last2 LL near Breakin Low = WAIT Reversal LONG if OPEN>last_close. Last2 HH near Breakin High = WAIT Reversal SHORT if OPEN<last_close")
    df = pd.DataFrame([["M&M","DOWNTREND","Near BREAKIN LOW 1245","Yes 2%","WAIT REVERSAL LONG","If OPEN>1255 LONG till 1280"],["APOLLOHOSP","UPTREND","Near BREAKIN HIGH 4560","Yes 1.5%","WAIT REVERSAL SHORT","If OPEN<4540 SHORT till 4450"]], columns=["Stock","Trend","Breakin Level","Near?","Action","Condition"])
    st.dataframe(df, use_container_width=True)

with tab7:
    st.subheader("MONTHLY / QUARTERLY HIGH LOW - Near / Touches / Breakout")
    st.markdown('<div class="mq-box"><h4>Monthly/Quarterly High Low Scanner - Criteria 1</h4><p>Monthly High = Last month High, Monthly Low = Last month Low<br>Quarterly High = Last 3 months High, Quarterly Low = Last 3 months Low<br>Near = Within 2%, Touches = Within 0.5%, Breakout = Close above/below</p></div>', unsafe_allow_html=True)
    
    st.write("Monthly High Low Logic:")
    st.write("Fetch 6 months daily data, Resample Monthly: Monthly High = Max High of last month, Monthly Low = Min Low of last month")
    st.write("Current Price vs Monthly High Low distance %")
    st.write("Near = Within 2%, Touches = 0.5%, Breakout = Close above Monthly High or below Monthly Low")
    
    st.write("Quarterly High Low Logic:")
    st.write("Resample Quarterly (3 months), Quarterly High = Max High of last quarter, Quarterly Low = Min Low of last quarter")
    st.write("Same Near/Touches/Breakout logic 2% / 0.5%")
    st.write("Stronger level than Monthly! Quarterly breakout = Big move")
    
    st.divider()
    mq_data = [
        ["M&M","Auto","Nifty50","Monthly Low 1240","Current 1265","1.9% Near Low","Near","Monthly Low Near + Weekly Strong","BUY ON DIPS","Tab1,6,8 me bhi - HIGH POTENTIAL"],
        ["RELIANCE","Energy","Nifty50","Monthly Low 2450","Current 2480","1.2% Near Low","Near","Monthly Low Near + Healthy Retest","BUY","Tab4 Investing me bhi"],
        ["TATAPOWER","Energy","F&O","Quarterly High 420","Current 425","1.1% Breakout","Breakout","Quarterly High Breakout + Vol 2.4x","BUY - Big Move","Quarterly breakout strong!"],
        ["TCS","IT","Nifty50","Monthly High 3450","Current 3420","0.8% Near High","Touches","Monthly High Near + Weekly Weak","SELL ON RISE / AVOID","Range"],
    ]
    df_mq = pd.DataFrame(mq_data, columns=["Stock","Sector","Market","Level","Current","Distance","Type","Strategy","Action","Repetition Check"])
    st.dataframe(df_mq, use_container_width=True, height=350)

with tab8:
    st.subheader("HEALTHY RETEST AS PER VPA RULES - Criteria 4")
    st.markdown('<div class="retest-box"><h4>Healthy Retest - VPA ka Sabse Safe Entry!</h4><p>Definition: Price breaks resistance, then comes back to test that resistance (now support) with LOW volume, then goes up with HIGH volume<br>Safe Entry: Retest pe low volume = No selling pressure</p></div>', unsafe_allow_html=True)
    
    st.write("Healthy Retest Steps (VPA Rules):")
    st.write("1. Breakout Candle: Close above Resistance + Volume Breakout (Vol >1.5*20SMA)")
    st.write("2. Retest (Next 3-5 candles): Price comes back to that breakout level (Support ban gaya)")
    st.write("3. Low Volume at Retest: Retest pe Volume < 20SMA Vol = No selling, healthy!")
    st.write("4. Current Near Retest: Abhi price us retest level ke paas (Within 2%)")
    st.write("5. Action: BUY at Retest, SL below retest level, Target next resistance")
    
    st.write("VPA Rules for Healthy Retest:")
    st.write("Volume: Breakout pe high volume, Retest pe low volume, Phir up pe high volume = Perfect!")
    st.write("Delivery: Breakout pe Delivery >50% + Retest pe bhi decent delivery = Strong hands")
    
    st.divider()
    retest_data = [
        ["M&M","Auto","Nifty50","Swing High 1250 Breakout Oct 10","Vol 2.2x","Retest Oct 11-13","Vol 0.8x Low","Current 1265 Near 1250","1.2%","Healthy Retest YES","BUY at 1265 SL 1235 Target 1300","Tab1,6,7 me bhi - TOP PRIORITY"],
        ["RELIANCE","Energy","Nifty50","PDL 2480 Breakout","Vol 2.0x","Retest 2475","Vol 0.7x Low","Current 2480 Near 2480","0%","Healthy Retest YES","BUY at 2480 SL 2450","Tab4,7 me bhi"],
        ["TCS","IT","Nifty50","Monthly High 3400 Breakout","Vol 1.1x Low","Retest 3390","Vol 1.3x High","Current 3420","0.8%","Healthy Retest NO - High Vol at Retest","AVOID - Selling at retest","Weak retest"],
    ]
    df_retest = pd.DataFrame(retest_data, columns=["Stock","Sector","Market","Breakout Level","Breakout Vol","Retest Level","Retest Vol","Current","Distance","Healthy?","Action","Repetition"])
    st.dataframe(df_retest, use_container_width=True, height=350)
    
    st.markdown('<div class="confirm-box"><h3>Repetition = Confirmation</h3><p>M&M = Tab1 Clean + Tab6 Breakin BO + Tab7 Monthly Low + Tab8 Healthy Retest = 4 Tabs = TOP Watchlist!</p><p>No Magic Scanner! Scanner = Shortlist 200+ -> Watchlist -> Chart Analysis -> Action List!</p></div>', unsafe_allow_html=True)

st.caption("V15.3 Fixed Syntax - 8 Tabs - No Error - Monthly/Quarterly + Healthy Retest + BREAKIN BO + Heatmap + Dropdown + Only Nifty50+F&O")
