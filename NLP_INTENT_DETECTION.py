import spacy
from sklearn import svm
import streamlit as st
def load_spacy_model():
    model_name = "en_core_web_sm"  # Changed to a smaller model
    try:
        nlp = spacy.load(model_name)
        st.write("Model loaded successfully!")
    except OSError:
        st.write("Model not found. Downloading...")
        try:
            spacy.cli.download(model_name)
            nlp = spacy.load(model_name)
            st.write("Model downloaded and loaded successfully!")
        except Exception as e:
            st.error(f"Failed to download or load spaCy model: {e}")
            nlp = None
    return nlp

# Call the function to load the model
nlp = load_spacy_model()

class Search_Type:
    COST_PRICE = "COST_PRICE"
    QTY = "QUANTITY"
    SELLING_PRICE = "SELLING_PRICE"
    HISTORICAL_SALES = "HISTORICAL_SALES"
    RANKING = "RANKING"
    LISTING = "LISTING"
    

training_text = ["what is the cost price of Alvaro", 
                 "how much does Guiness malt cost?",
                 "what is the cost price of fanta?",
                 "what is the cost price of this item?",
                 "can you tell me the cost price?",
                 "how much is the cost price?",
                 "what's the cost price?",
                 "I need to know the cost price",
                 "how much does this product cost?",
                 "what is the wholesale price?",
                 "how much does it cost to get this?",
                 "what is the cost price for this?",
                 "tell me the cost price of this product",
                 "what is the cost price of this?",
                 "how much does this cost?",
                 "what's the cost price for this?",
                 "how much does this item cost?",
                 "what is the acquisition cost?",
                 "how much does it cost to buy this?",
                 "what is the price to obtain this?",
                 "how much is the wholesale cost?",
                 "can you tell me the cost price of this?",
                 "what is the procurement cost?",
                 "how much is the base price?",
                 "what's the expense for this?",
                 "how much does this item cost wholesale?",
                 "what is the initial cost?",
                 "how much does it cost to acquire this?",
                 "tell me the cost price",
                 "what's the cost price of this item?",
                 "how much is this item?",
                 "what's the cost price for bel malt chocolate?",
                 "cost price of",
                 "Can i get the cost price of ?",
                 "item cost price?",


                 "what is the selling price of ?", 
                 "what is the price of ?",
                 "what is the selling price of ",
                 "what is the price for",
                 "what is the selling price of awake?",
                 "at what price do we sell cheese balls?",
                 "how much is awake 500ml?",
                 "can you tell me the selling price of this product?",
                 "how much does it sell for?",
                 "what's the selling price?",
                 "how much do we sell this?",
                 "what is the retail price?",
                 "how much is this product?",
                 "what's the price tag on this?",
                 "what is the current selling price?",
                 "what's the price for this item?",
                 "how much do we charge for this?",
                 "what is the market price?",
                 "what is the sale price of this?",
                 "how much is this item being sold for?",
                 "what's the going rate for this?",
                 "how much do we sell this product for?",
                 "can you tell me the price for this?",
                 "how much is the selling price?",
                 "what is the price we are selling this for?",
                 "what's the price of this item?",
                 "what is the listed price?",
                 "how much is this product listed for?",
                 "what is the price at which we sell this?",
                 "how much does this product sell for?",
                 "what is the asking price for this?",
                 "how much should I pay for this?",
                 "what is the set price for this?",
                 "what's the selling price for this item?",
                 "what price is this being sold at?",
                 "what is the selling price of this product?",

                 "how many bottles of water do we have?",
                 "how many bottles of bel cola do we have in stock?",
                 "what is the total qty of malt we have in stock",
                 "what is the quantity of Alvaro",
                 "what is the quantity of sprite",

                 "how much did we make on ",
                 "how much did we make on the 5th of may 2024",
                 "what was our revenue on ",
                 "what was the profit for ",
                 "what was our revenue for January 1st 2024?",
                 "what were our sales for ",
                 "how much money did we make ",
                 "how much have we made since we started?",
                 "how much did we make on 10/01/2024 ? ",
       
                 "show me the top 10 products by quantity",
                 "Which products sold the most last month?",
                 "Show the most popular products by sales volume.",
                 "What are the top 5 items by number of units sold?",
                 "Give me the highest-ranked products by quantity sold.",
                 "Display the top-performing products by quantity.",
                 "What are our top sellers by units?",
                 "Which items are leading in sales volume?",
                 "Rank the products by quantity sold.",
                 "Show the products with the highest sales numbers.",
                 "List the items with the most units sold.",
                 "What are the top 10 products by quantity sold this year?",
                 "Give me a list of the best-selling products by volume.",
                 "Which products had the highest sales figures?",
                 "Show the top-ranked items by the number of units sold.",
                 "What are the best-performing products by quantity sold?",
                 "Which products have the highest sales volumes?",
                 "List the top products in terms of sales volume.",
                 "What are the top 5 products by the number of units sold?",
                 "Display the most popular products by sales quantity.",

                 "Give me a list of the products provided by thakar",
                 "give me a list of all the delta products",
                 "give me a list of all guiness products", 

                 ]

training_search_type = [Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,
                        Search_Type.COST_PRICE,

                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        Search_Type.SELLING_PRICE,
                        
                        Search_Type.QTY,
                        Search_Type.QTY,
                        Search_Type.QTY,
                        Search_Type.QTY,
                        Search_Type.QTY,

                        Search_Type.HISTORICAL_SALES,
                        Search_Type.HISTORICAL_SALES,
                        Search_Type.HISTORICAL_SALES,
                        Search_Type.HISTORICAL_SALES,
                        Search_Type.HISTORICAL_SALES,
                        Search_Type.HISTORICAL_SALES,
                        Search_Type.HISTORICAL_SALES,
                        Search_Type.HISTORICAL_SALES,
                        Search_Type.HISTORICAL_SALES,
                       
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,
                        Search_Type.RANKING,

                        Search_Type.LISTING,
                        Search_Type.LISTING,
                        Search_Type.LISTING,

                        ]

docs = [nlp(text) for text in training_text]
training_vectors = [x.vector for x in docs]
classify_svm = svm.SVC(kernel="linear")

classify_svm.fit(training_vectors,training_search_type)