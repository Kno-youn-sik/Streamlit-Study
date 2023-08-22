import streamlit as st
import pandas as pd 
import FinanceDataReader as fdr
import datetime 

st.title('사전 학습 2강 대전9기- 노윤식')
st.header('주가 데이터 시각화')
st.text('*[사전 학습 1강] - [과제]*')
st.header('')

st.divider()
st.subheader('상위 100개 기업')
st.title('')

df_krx = fdr.StockListing('KRX')

st.dataframe(df_krx.head(100))

# 이름으로 코드를 찾기위한 단순한 함수
def codeFromName(name):
    row = df_krx[df_krx['Name'] == name]
    if not row.empty:
        return row['Symbol'].values[0]
    return None 

stock_code=st.text_input('종목 코드 입력 :','005380')
st.subheader('')
data_range=st.date_input("조회일 설정:",[datetime.date(2023,1,1),datetime.date(2024,1,1)])

st.divider()
st.subheader('데이터차트')
st.title('')
start_date=data_range[0].strftime("%Y-%m-%d")
end_date=data_range[1].strftime("%Y-%m-%d")
#Convert dates to string 

df = fdr.DataReader(stock_code,start_date,end_date)

ma5 = pd.DataFrame(  df['Close'].rolling(window=5).mean())
ma20 = pd.DataFrame( df['Close'].rolling(window=20).mean())
ma60 = pd.DataFrame( df['Close'].rolling(window=60).mean())
ma120 = pd.DataFrame(df['Close'].rolling(window=120).mean())
ma240 = pd.DataFrame(df['Close'].rolling(window=240).mean())

df.insert(len(df.columns), '5일', ma5)
df.insert(len(df.columns), '20일', ma20)
df.insert(len(df.columns), '60일', ma60)
df.insert(len(df.columns), '120일', ma120)
df.insert(len(df.columns), '240일', ma240)

st.dataframe(df)

st.divider()
st.subheader('데이터 시각화')
st.title('')

st.line_chart(df[['5일','20일','60일','120일','240일']])
st.header('')
st.bar_chart(df['Volume'])
