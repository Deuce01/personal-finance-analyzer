import streamlit as st
import pandas as pd
from cluster_model import cluster_transactions
from utils import preprocess_data, plot_category_distribution
import PyPDF2

class PersonalFinanceAnalyzer:
    def __init__(self):
        self.uploaded_file = None
        self.df = None
        self.cleaned_df = None
        self.clustered_df = None

    def load_file(self):
        """Handles file upload and identifies file type (CSV or PDF)"""
        self.uploaded_file = st.file_uploader("📤 Upload your M-Pesa or Bank CSV/PDF Statement", type=["csv", "pdf"])

    def process_csv(self):
        """Process the uploaded CSV file"""
        if self.uploaded_file.type == "text/csv":
            self.df = pd.read_csv(self.uploaded_file)
            st.subheader("🔍 Raw Data Preview")
            st.dataframe(self.df.head())

            self.cleaned_df = preprocess_data(self.df)
            self.clustered_df = cluster_transactions(self.cleaned_df)

            st.subheader("🧠 Clustered Transactions")
            st.dataframe(self.clustered_df.head())

            st.subheader("📊 Spending Distribution by Category")
            fig = plot_category_distribution(self.clustered_df)
            st.pyplot(fig)

            csv = self.clustered_df.to_csv(index=False).encode('utf-8')
            st.download_button("⬇️ Download Clustered Data", csv, "clustered_spending.csv", "text/csv")

    def process_pdf(self):
        """Handle PDF extraction and data display"""
        if self.uploaded_file.type == "application/pdf":
            pdf_reader = PyPDF2.PdfReader(self.uploaded_file)
            pdf_text = ""
            for page in pdf_reader.pages:
                pdf_text += page.extract_text()

            st.subheader("📄 Extracted Text from PDF")
            st.write(pdf_text)

            st.info("🔧 PDF support is basic. For best results, upload a clean CSV file of your transactions.")

    def run(self):
        """Run the app: load the file, process it, and display results"""
        st.set_page_config(page_title="Smart Personal Finance Analyzer", page_icon="💰", layout="centered")

        st.title("💰 Smart Personal Finance Analyzer")
        st.subheader("Track. Cluster. Visualize. — Understand your spending habits with AI insights")
        st.markdown("""
Welcome to your intelligent finance assistant! 📈  
Upload your **M-Pesa** or **bank statement** in CSV or PDF format, and this tool will:
- Automatically **cluster** transactions into categories like Food, Transport, Utilities
- Generate **insightful visualizations** to help you track where your money goes
- Use **machine learning** to understand your financial patterns

---
""")

        self.load_file()

        if self.uploaded_file is not None:
            if self.uploaded_file.type == "text/csv":
                self.process_csv()
            elif self.uploaded_file.type == "application/pdf":
                self.process_pdf()
            else:
                st.error("❌ Unsupported file type. Please upload a CSV or PDF.")

if __name__ == "__main__":
    app = PersonalFinanceAnalyzer()
    app.run()
