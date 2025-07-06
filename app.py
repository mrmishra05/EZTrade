import streamlit as st
import pandas as pd
import numpy as np
import random
import time

# --- Simulate GenAI Functions (In a real app, these would call actual LLMs) ---

# --- Placeholder for a real financial data API key ---
# In a real application, you would get this from a service like Alpha Vantage, Finnhub, etc.
# API_KEY = st.secrets["financial_api_key"] # Recommended for security in Streamlit Cloud

# Dummy data for demonstration (will be replaced by simulated API calls or real data)
# For 5000+ stocks, you'd fetch this dynamically from a financial data API.
# This mock data is just to keep the app runnable for demonstration purposes.
def fetch_mock_watchlist_data():
    """Simulates fetching data for a few watchlist stocks."""
    return {
        "Reliance Industries": {"price": 2900, "change": "+1.2%", "sentiment": "positive", "sector": "Diversified"},
        "Infosys": {"price": 1500, "change": "-0.5%", "sentiment": "neutral", "sector": "IT"},
        "Tata Motors": {"price": 950, "change": "+2.1%", "sentiment": "bullish", "sector": "Automobile"},
        "HDFC Bank": {"price": 1650, "change": "+0.1%", "sentiment": "neutral", "sector": "Finance"},
        "Bitcoin (BTC)": {"price": 70000, "change": "+3.5%", "sentiment": "bullish", "sector": "Crypto"}
    }

# --- Simulated LLM Call for Hot Stories ---
def generate_hot_story_with_ai(market_context):
    """
    Simulates an API call to a Generative AI model (e.g., Gemini 2.0 Flash)
    to generate a "Hot Market Story" based on given market context.
    In a real app, you would use a library like `requests` to call the LLM API.
    """
    # This is the prompt that would be sent to the LLM
    prompt = (
        f"Based on the following market context, generate a concise, engaging headline "
        f"and a brief impact summary for a 'Hot Market Story' for retail traders. "
        f"Focus on the 'why' behind the movement and affected assets. "
        f"Context: {market_context}"
        f"\n\nFormat your response as: 'Headline: [Your Headline]\nImpact: [Your Impact]'"
    )

    # --- SIMULATED LLM RESPONSE ---
    # In a real application, this would be a fetch/requests call to a Gemini API endpoint.
    # Example (conceptual, as actual fetch is JS-based, and requests is Python-based):
    # import requests
    # headers = {'Content-Type': 'application/json'}
    # payload = {"contents": [{"role": "user", "parts": [{"text": prompt}]}]}
    # response = requests.post(f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}", json=payload)
    # result = response.json()
    # generated_text = result['candidates'][0]['content']['parts'][0]['text']

    # For this demo, we return a hardcoded but dynamic-looking response
    simulated_responses = {
        "IT Sector": "Headline: IT Sector Jumps as Global Tech Spending Outlook Improves\nImpact: Positive for IT stocks like Infosys, TCS, and Wipro due to renewed client confidence.",
        "Automobile Sector": "Headline: Automobile Sector Revs Up on Strong Festive Season Sales Forecasts\nImpact: Bullish for auto manufacturers like Tata Motors and Maruti Suzuki as consumer demand rises.",
        "Commodity Prices": "Headline: Unexpected Global Commodity Price Surge – Impact on Metal & Energy Stocks\nImpact: Mixed, watch for specific company exposure. Potential cost pressures for some, gains for others like Reliance Industries and Tata Steel.",
        "RBI Rates": "Headline: RBI Holds Rates Steady: What it Means for Banking & Finance\nImpact: Neutral to slightly positive for banks like HDFC Bank and ICICI Bank, ensuring stable lending environment.",
        "Crypto Market": "Headline: Bitcoin & Crypto Market Rally on ETF Approvals\nImpact: Strong bullish sentiment across digital assets. High volatility expected around regulatory news."
    }
    # Randomly pick one for demonstration
    chosen_context = random.choice(list(simulated_responses.keys()))
    return simulated_responses[chosen_context]

def get_hot_stories_from_ai():
    """Fetches AI-generated hot stories."""
    hot_stories = []
    # In a real app, you'd have more sophisticated data inputs for the AI
    # For demo, we'll simulate a few calls with different contexts
    contexts = [
        "Recent positive earnings reports from major IT companies and optimistic global tech forecasts.",
        "Anticipated surge in vehicle sales during upcoming festivals and government incentives for EVs.",
        "Sudden increase in global crude oil and metal prices due to geopolitical tensions.",
        "Reserve Bank of India's latest monetary policy announcement, keeping key interest rates unchanged.",
        "Recent approvals of Bitcoin ETFs in major markets and increasing institutional adoption."
    ]
    for _ in range(3): # Generate 3 hot stories for the demo
        context = random.choice(contexts)
        ai_response = generate_hot_story_with_ai(context)
        parts = ai_response.split('\nImpact: ')
        if len(parts) == 2:
            title = parts[0].replace('Headline: ', '')
            impact = parts[1]
            hot_stories.append({"title": title, "impact": impact})
        else:
            hot_stories.append({"title": "AI Story Generation Error", "impact": "Could not parse AI response."})
    return hot_stories

# --- Simulated Premium Interests Data (for "Stories Just For You") ---
PREMIUM_INTERESTS_DATA = {
    "AI & Tech": [
        {"title": "Mid-Cap AI Firm 'TechGen' Secures Major Government Contract", "asset": "TechGen Solutions", "signal": "Unusual insider buying detected."},
        {"title": "Semiconductor Demand Soars Amidst AI Boom: Focus on 'ChipInnovate'", "asset": "ChipInnovate Ltd.", "signal": "Early analyst upgrades."},
    ],
    "Renewable Energy": [
        {"title": "Solar Panel Manufacturing Booms: 'SunPower India' Expands Capacity", "asset": "SunPower India", "signal": "Positive regulatory news overlooked by market."},
        {"title": "Green Hydrogen Policy Boosts 'GreenFuel Corp' Prospects", "asset": "GreenFuel Corp", "signal": "Increased institutional interest."},
    ],
    "Healthcare Innovation": [
        {"title": "Biotech Startup 'GeneCure' Announces Breakthrough Drug Trial Results", "asset": "GeneCure Pharma", "signal": "Strong pre-market buzz."},
        {"title": "Hospital Chain 'MediCare' Adopts AI for Patient Management", "asset": "MediCare Hospitals", "signal": "Partnership with leading tech firm."},
    ]
}

def get_personalized_alerts(is_premium, user_interests=None):
    """Simulates GenAI generating personalized trend alerts."""
    alerts = []
    if is_premium and user_interests:
        for interest in user_interests:
            if interest in PREMIUM_INTERESTS_DATA:
                for item in PREMIUM_INTERESTS_DATA[interest]:
                    alerts.append(f"💡 **New Opportunity in {interest}:** {item['title']} ({item['asset']}). Signal: {item['signal']}")
    return alerts

def generate_asset_story(asset_name, data):
    """Simulates GenAI generating a concise asset story."""
    price_change = data.get('change', 'N/A')
    sentiment = data.get('sentiment', 'neutral')
    sector = data.get('sector', 'General')

    # In a real app, this would be an LLM call with detailed asset-specific data
    # For now, we use the mock data
    if asset_name == "Reliance Industries":
        return (
            f"**Reliance Industries ({price_change}):** Positive buzz on new energy ventures and strong analyst upgrades for Q2 results. "
            f"Overall sentiment for the {sector} giant is currently **{sentiment}**. "
            f"Watch for updates on their green hydrogen projects."
        )
    elif asset_name == "Infosys":
        return (
            f"**Infosys ({price_change}):** Concerns about global tech spending slowing, leading to a minor dip. "
            f"Sentiment for the {sector} leader is **{sentiment}**. "
            f"Keep an eye on their upcoming client deal announcements."
        )
    elif asset_name == "Tata Motors":
        return (
            f"**Tata Motors ({price_change}):** Strong performance driven by robust festive season sales forecasts for their EV segment. "
            f"Market sentiment for the {sector} stock is highly **{sentiment}**. "
            f"Potential for further upside if sales targets are met."
        )
    elif asset_name == "HDFC Bank":
        return (
            f"**HDFC Bank ({price_change}):** RBI's decision to hold interest rates steady has kept sentiment **{sentiment}** for the banking sector. "
            f"Focus remains on loan book growth and asset quality."
        )
    elif asset_name == "Bitcoin (BTC)":
        return (
            f"**Bitcoin ({price_change}):** Crypto market rallying on positive ETF news and high social media excitement. "
            f"Sentiment is strongly **{sentiment}**. "
            f"Volatility expected around upcoming regulatory discussions."
        )
    else:
        return f"**{asset_name}:** Price {price_change}. Sentiment: {sentiment}. No specific story available yet."

def analyze_trade(trade_details):
    """Simulates GenAI analyzing a past trade."""
    st.write(f"### Debrief for your trade on {trade_details['asset']}:")
    st.write(f"**Trade Type:** {trade_details['type']} | **Outcome:** {trade_details['outcome']}")
    st.write(f"**Entry Price:** {trade_details['entry_price']} | **Exit Price:** {trade_details['exit_price']}")
    st.write(f"**Date:** {trade_details['date']}")

    # Simulate AI analysis based on outcome
    if trade_details['outcome'] == 'Profit':
        st.success("🎉 **Great Job!** Your trade was profitable.")
        st.write("The AI notes that your entry aligned with a strong positive sentiment shift driven by **[simulated news/event related to profitability]**. Your quick exit captured the peak momentum.")
        st.write("Consider: How did you identify this opportunity? Can you replicate this process?")
    else:
        st.error("📉 **Learning Opportunity:** Your trade resulted in a loss.")
        st.write("The AI observes that while there was initial positive news, broader market sentiment for the sector was turning negative due to **[simulated macro factor or unexpected event]**. Your exit might have been delayed, missing an earlier chance to minimize losses.")
        st.write("Consider: Did you account for wider market trends? How could you have managed risk better in this scenario?")

    st.write("\n---")
    st.write("#### Personalized Learning Suggestions:")
    st.write("- Review modules on 'Sentiment Analysis in Volatile Markets'.")
    st.write("- Explore strategies for 'Early Exit Signals' to protect profits/limit losses.")
    st.write("- Understand 'Sectoral Correlations' to anticipate broader market impact.")

# --- User Authentication (Simplified for demo) ---
def authenticate_user():
    # In a real app, this would involve a login system (e.g., Firebase Auth)
    # For demo, we use a simple checkbox to switch between free/premium
    st.sidebar.header("User Status")
    is_premium = st.sidebar.checkbox("Enable Premium Features (Simulated)", value=False)
    return is_premium

# --- Main Streamlit App Layout ---
def main():
    st.set_page_config(layout="wide", page_title="EZTrade AI")

    st.title("EZTrade AI: Your AI Co-Pilot for Smarter Trades")
    st.write("Transforming market noise into clear, actionable narratives.")

    is_premium = authenticate_user()

    st.markdown("---")

    # 1. My Watchlist First
    st.header("My Watchlist Stories")
    st.write("Quick insights for the assets you care about most.")

    # Fetch mock data for watchlist (in real app, this would be from API)
    watchlist_data = fetch_mock_watchlist_data()

    cols = st.columns(len(watchlist_data))
    for i, (asset, data) in enumerate(watchlist_data.items()):
        with cols[i]:
            card_title = f"{asset} ({data['change']})"
            if data['sentiment'] == 'positive' or data['sentiment'] == 'bullish':
                st.markdown(f"**<p style='color:green;'>{card_title} ↑</p>**", unsafe_allow_html=True)
            elif data['sentiment'] == 'negative' or data['sentiment'] == 'bearish':
                st.markdown(f"**<p style='color:red;'>{card_title} ↓</p>**", unsafe_allow_html=True)
            else:
                st.markdown(f"**<p style='color:orange;'>{card_title} ↔</p>**", unsafe_allow_html=True)

            if st.button(f"View Story for {asset}", key=f"watchlist_btn_{asset}"):
                with st.expander(f"**{asset} - The Full Story**", expanded=True):
                    st.write(generate_asset_story(asset, data))
                    st.write(f"**Sector:** {data['sector']}")
                    st.write("*(In a real app, this would be a detailed AI-generated narrative based on live data.)*")
            st.markdown("---") # Separator for cards

    st.markdown("---")

    # 2. Hot Stories of the Day (Now AI-Generated)
    st.header("🔥 Hot Market Stories Today (AI-Generated)")
    st.write("The biggest narratives moving the overall market, synthesized by AI.")

    hot_stories_ai = get_hot_stories_from_ai()
    for story in hot_stories_ai:
        st.subheader(f"Headline: {story['title']}")
        st.write(f"**Impact:** {story['impact']}")
        st.write("*(These stories are dynamically generated by AI based on simulated market context.)*")
        st.markdown("---")

    st.markdown("---")

    # 3. My Interests, My Stories (Premium Feature)
    st.header("💡 Stories Just For You (Premium Feature)")
    if is_premium:
        st.write("AI-powered insights tailored to your specific trading interests, helping you spot unique opportunities.")
        user_selected_interests = st.multiselect(
            "Select your interests to see personalized stories:",
            list(PREMIUM_INTERESTS_DATA.keys()),
            default=["AI & Tech"] # Default selection for demo
        )
        if user_selected_interests:
            personalized_alerts = get_personalized_alerts(is_premium, user_selected_interests)
            if personalized_alerts:
                for alert in personalized_alerts:
                    st.markdown(alert)
                    st.write("*(These are early signals and nuanced insights, often missed by the general market.)*")
                    st.markdown("---")
            else:
                st.info("No personalized stories found for your selected interests today. Try different interests!")
        else:
            st.info("Select interests above to see personalized stories.")
    else:
        st.warning("Unlock 'Stories Just For You' and other advanced features with EZTrade AI Premium!")
        if st.button("Learn More about Premium"):
            st.write("*(Imagine a link to your pricing page here)*")

    st.markdown("---")

    # 4. Trade Debrief & Learn (Premium Feature)
    st.header("📈 Trade Debrief & Learn (Premium Feature)")
    if is_premium:
        st.write("Get personalized feedback on your past trades to refine your strategy and avoid common pitfalls.")
        st.info("*(In a real app, you would connect your brokerage account securely for automated debriefs.)*")

        # Simulate a manual trade entry for debrief
        st.subheader("Simulate a Trade Debrief:")
        sim_asset = st.selectbox("Select Asset for Debrief:", list(watchlist_data.keys()), key="sim_asset")
        sim_trade_type = st.radio("Trade Type:", ["Buy", "Sell"], key="sim_trade_type")
        sim_entry_price = st.number_input("Entry Price:", value=100.0, key="sim_entry_price")
        sim_exit_price = st.number_input("Exit Price:", value=105.0, key="sim_exit_price")
        sim_date = st.date_input("Trade Date:", pd.to_datetime('today'), key="sim_date")

        sim_outcome = "Profit" if sim_exit_price > sim_entry_price else "Loss"

        if st.button("Analyze This Trade", key="analyze_trade_btn"):
            trade_details = {
                "asset": sim_asset,
                "type": sim_trade_type,
                "entry_price": sim_entry_price,
                "exit_price": sim_exit_price,
                "date": sim_date.strftime("%Y-%m-%d"),
                "outcome": sim_outcome
            }
            analyze_trade(trade_details)
    else:
        st.warning("Unlock 'Trade Debrief & Learn' to get personalized feedback on your trading performance with EZTrade AI Premium!")

    st.markdown("---")
    st.sidebar.markdown("---")
    st.sidebar.info("EZTrade AI: Your intelligent co-pilot for the Indian stock market. Built for clarity, powered by AI.")

if __name__ == "__main__":
    main()
