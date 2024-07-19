import spacy
from sklearn import svm
import streamlit as st
import spacy.cli

def load_spacy_model():
    model_name = "en_core_web_md"
    try:
        # Check if the model is available
        nlp = spacy.load(model_name)
        st.write("Model loaded successfully!")
    except OSError:
        # Download the model if not available
        st.write("Model not found. Downloading...")
        try:
            spacy.cli.download(model_name)
            nlp = spacy.load(model_name)
            st.write("Model downloaded and loaded successfully!")
        except Exception as e:
            st.error(f"Failed to download spaCy model: {e}")
            nlp = None
    return nlp

report_nlp = load_spacy_model()

class report_type:
    SALES_REPORT = "SALES_REPORT"
    FINANCIAL_REPORT = "FINANCIAL_REPORT"
    INVENTORY_REPORT = "INVENTORY_REPORT"
    PRODUCT_REPORT = "PRODUCT_REPORT"
    

training_text_2 = [ "Generate a sales report for the last quarter",
                    "show me the weekly sales performance report",
                    "i need a sales report comparing this month to the previous month",
                    "get me a sales report for q2",

                    "Can you provide a financial summary for the past year?",
                    "Generate a profit and loss statement for Q2.",
                    "I need a detailed expense report for the last month.",
                    "generate a financial report for the last quarter,"
                 ]
training_report_type = [report_type.SALES_REPORT,
                        report_type.SALES_REPORT,
                        report_type.SALES_REPORT,
                        report_type.SALES_REPORT,

                        report_type.FINANCIAL_REPORT,
                        report_type.FINANCIAL_REPORT,
                        report_type.FINANCIAL_REPORT,
                        report_type.FINANCIAL_REPORT,
                        ]

docs = [report_nlp(text) for text in training_text_2]
training_vectors = [x.vector for x in docs]
report_classify_svm = svm.SVC(kernel="linear")

report_classify_svm.fit(training_vectors,training_report_type)