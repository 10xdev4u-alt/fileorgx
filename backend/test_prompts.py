from ai.prompts import FILE_ANALYSIS_PROMPT_TEMPLATE

# Test template rendering
rendered = FILE_ANALYSIS_PROMPT_TEMPLATE.format(
    name="invoice_123.pdf",
    file_type="application/pdf",
    size=1024,
    path="/home/user/Downloads/invoice_123.pdf",
    content_snippet="Invoice for AWS services - total $50"
)
print("Rendered Prompt Sample:\n", rendered)
