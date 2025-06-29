import streamlit as st
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt


st.set_page_config(page_title="Learn how to invest")
st.title("Learn how to invest with a bot!")

st.write("Ask me anything about stocks, ETFs, or how to get started with investing! \n Also you can ask me to show you a stocks graph.")
# ticker = st.text_input("Enter a stock ticker symbol (e.g., NVDA, MSFT):")

# def stocksshow(ticker):
#     stock = yf.Ticker(ticker.upper())
#     data = stock.history(period="6mo")
#     plt.grid(True)
#     plt.show()
#     if not data.empty:
#         st.line_chart(data["Close"])
#     else:
#         st.warning("No data found for that ticker. Double-check the symbol!")
#this is for the user input
user_input = st.text_input("Enter here...")

def chatbot_response(query):
    query = query.lower()

    if "stock" in query:
        return "A stock is a share of ownership in a company. When you own one, you're a partial owner!"
    
    elif "etf" in query:
        return "An ETF (Exchange-Traded Fund) is a basket of investments you can buy like a stock."

    elif "bond" in query:
        return "A bond is a loan you give to a company or government, which pays you back with interest."

    elif "dividend" in query:
        return "A dividend is a portion of a company's profit paid to its shareholders, often quarterly."

    elif "mutual fund" in query:
        return "A mutual fund pools money from many investors to buy a diversified portfolio of assets."

    elif "index fund" in query:
        return "An index fund tracks the performance of a market index like the S&P 500—low cost and diversified."

    elif "roth ira" in query or "ira" in query:
        return "A Roth IRA is a retirement account where your investments grow tax-free, and you can withdraw later without paying taxes."

    elif "risk tolerance" in query:
        return "Risk tolerance is how much volatility you're comfortable with. It depends on your goals, age, and personality."

    elif "diversification" in query:
        return "Diversification means spreading your investments across different assets to reduce overall risk."

    elif "compound interest" in query:
        return "Compound interest is when your investments earn returns on both the original amount and the past returns. It’s like interest earning interest."

    elif "brokerage" in query:
        return "A brokerage is a platform (like Fidelity, E*TRADE, or Robinhood) where you buy and sell investments."

    elif "how to start" in query or "begin investing" in query:
        return "Start by opening a brokerage account, decide how much to invest regularly, and stick to diversified, long-term strategies."

    elif "bull market" in query:
        return "A bull market is when prices are rising and investors are optimistic. It's the opposite of a bear market."

    elif "bear market" in query:
        return "A bear market is when prices fall 20% or more from recent highs—usually due to negative investor sentiment or economic downturns."

    elif "inflation" in query:
        return "Inflation is the rise in prices over time. It erodes the purchasing power of your money if not outpaced by your investment returns."

    # elif ticker in query:
    #     stocksshow(ticker)
    else:
        return "Hmm, I'm still learning that topic. Try asking about stocks, ETFs, or portfolio basics."
    

# Display chatbot reply
if user_input:
    response = chatbot_response(user_input)
    st.write("🤖: " + response)