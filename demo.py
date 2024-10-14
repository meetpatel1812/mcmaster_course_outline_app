import streamlit as st
from pdf_data import pdfs  # Import the PDF data

# Set Page Configuration
st.set_page_config(page_title="PDF Library", layout="wide")

# Main Page Filters
st.header("MEST Course outlines (McMaster University)")

# Layout for filters in a single row
col1, col2, col3, col4, col5 = st.columns([3, 3, 3, 4, 1])

with col1:
    # First Filter: Stream
    stream_options = [
        "Automotive Stream",
        "Automation and Smart Systems",
        "Digital Manufacturing",
        "Process Systems Stream",
        "All stream course"
    ]
    selected_streams = st.multiselect("Select Stream(s)", stream_options)

with col2:
    # Second Filter: Course Type
    course_type_options = [
        "Required core courses",
        "Professional Development course",
        "Core course",
        "Recommended Technical electives",
        "Cross-Disciplinary Elective Course",
        "Other elective course"
    ]
    selected_course_types = st.multiselect("Select Course Type(s)", course_type_options)

with col3:
    # Third Filter: Semester
    semester_options = ["Fall", "Winter", "Summer"]
    selected_semesters = st.multiselect("Select Semester(s)", semester_options)

# Search Bar and Button in a single row with placeholder
with col4:  
    search_query = st.text_input("", placeholder="Search for a course")

with col5:
    st.write("")  # Add some spacing
    search_button = st.button("Search")

st.markdown("---")

# Function to filter PDFs based on selections and search
def filter_pdfs(pdfs, streams, course_types, semesters, search):
    filtered = pdfs

    # Filter by Stream
    if streams:
        # Map stream options to subcategories
        stream_map = {
            "Automotive Stream": "Automotive Stream",
            "Automation and Smart Systems": "Automation and Smart Systems",
            "Digital Manufacturing": "Digital Manufacturing",
            "Process Systems Stream": "Process Systems Stream",
            "All stream course":"All stream course"
        }
        selected_subcategories = [stream_map[stream] for stream in streams if stream in stream_map]
        filtered = [pdf for pdf in filtered if pdf["subcategory"] in selected_subcategories]

    # Filter by Course Type
    if course_types:
        filtered = [pdf for pdf in filtered if pdf["category"] in course_types]

    # Filter by Semester
    if semesters:
        filtered = [pdf for pdf in filtered if any(semester in pdf["semesters"] for semester in semesters)]

    # Filter by Search Query (only when search button is pressed)
    if search and search_button:
        search_lower = search.lower()
        filtered = [
            pdf for pdf in filtered
            if search_lower in pdf["name"].lower() or search_lower in pdf["label"].lower()
        ]

    return filtered

# Apply Filters
filtered_pdfs = filter_pdfs(pdfs, selected_streams, selected_course_types, selected_semesters, search_query)

# Display PDFs as Cards
st.subheader("MEST Course Outline PDFs")

if not filtered_pdfs:
    st.info("No PDFs match the selected filters.")
else:
    # Define the number of columns per row
    cols_per_row = 6
    for i in range(0, len(filtered_pdfs), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, pdf in enumerate(filtered_pdfs[i:i + cols_per_row]):
            with cols[j]:
                # Render the card with HTML and CSS for styling
                st.markdown(f"""
                    <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); margin-bottom: 20px;">
                        <h3 style="color: #007bff; font-size: 20px;">{pdf['icon']} {pdf['name']}</h3>
                        <p style="font-weight: bold; font-size: 16px;">{pdf['label']}</p>
                        <p><strong>Category:</strong> {pdf['category']}</p>
                        <p><strong>Subcategory:</strong> {pdf['subcategory']}</p>
                        <p><strong>Semesters:</strong> {', '.join(pdf['semesters'])}</p>
                        """, unsafe_allow_html=True)

                try:
                    with open(pdf['file_path'], "rb") as f:
                        pdf_data = f.read()
                    st.download_button(
                        label="Download PDF",
                        data=pdf_data,
                        file_name=f"{pdf['name']}.pdf",
                        mime="application/pdf"
                    )
                except FileNotFoundError:
                    st.error("File not found.")
                st.markdown("</div>", unsafe_allow_html=True)
